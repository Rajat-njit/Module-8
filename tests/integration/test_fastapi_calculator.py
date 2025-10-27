import pytest
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


@pytest.mark.parametrize(
    "endpoint,a,b,expected",
    [
        ("/add", 2, 3, 5.0),
        ("/subtract", 5, 3, 2.0),
        ("/multiply", 2, 3, 6.0),
        ("/divide", 6, 3, 2.0),
    ],
)
def test_happy_path_operations(endpoint, a, b, expected):
    resp = client.post(endpoint, json={"a": a, "b": b})
    assert resp.status_code == 200
    data = resp.json()
    assert "result" in data
    assert data["result"] == pytest.approx(expected)


def test_divide_by_zero_returns_400_with_error():
    resp = client.post("/divide", json={"a": 1, "b": 0})
    assert resp.status_code == 400
    data = resp.json()
    # Our app returns {"error": "..."} for handled errors
    assert "error" in data
    assert "divide by zero" in data["error"].lower()


@pytest.mark.parametrize(
    "endpoint,payload",
    [
        ("/add", {"a": "abc", "b": 1}),
        ("/subtract", {"a": 1, "b": "xyz"}),
        ("/multiply", {"a": None, "b": 2}),
        ("/divide", {"a": 10, "b": "oops"}),
    ],
)
def test_invalid_payloads_return_400_with_error(endpoint, payload):
    resp = client.post(endpoint, json=payload)
    assert resp.status_code == 400
    data = resp.json()
    assert "error" in data


def test_root_serves_html():
    resp = client.get("/")
    assert resp.status_code == 200
    # Should be HTML content (index.html rendered)
    assert "text/html" in resp.headers.get("content-type", "")

def test_missing_payload_fields():
    resp = client.post("/add", json={"a": 5})
    assert resp.status_code == 400
    data = resp.json()
    assert "error" in data or "detail" in data


def test_non_numeric_payload_values():
    resp = client.post("/multiply", json={"a": "foo", "b": "bar"})
    assert resp.status_code == 400
    data = resp.json()
    assert "error" in data


def test_large_number_operations():
    resp = client.post("/add", json={"a": 1e308, "b": 1e308})
    assert resp.status_code == 200
    # Expect 'inf' or a very large float
    assert "result" in resp.json()

def test_division_precision():
    resp = client.post("/divide", json={"a": 1, "b": 3})
    assert resp.status_code == 200
    result = resp.json()["result"]
    assert 0.333 < result < 0.334  # within tolerance
