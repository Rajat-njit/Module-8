"""
tests/e2e/test_e2e.py
---------------------
End-to-end (E2E) tests for the FastAPI Calculator using Playwright.

✅ Starts FastAPI app automatically for CI/CD
✅ Tests UI-based arithmetic operations
✅ Works both locally and in GitHub Actions
"""

import subprocess
import time
import pytest
from playwright.sync_api import Page, expect

# URL where FastAPI runs
BASE_URL = "http://127.0.0.1:8000"


# -------------------------------------------------------
# Global fixture: start FastAPI server before all tests
# -------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def start_fastapi_server():
    """
    Launch FastAPI server before running Playwright tests.
    This ensures CI/CD (GitHub Actions) can connect to localhost:8000.
    """
    process = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(3)  # give server time to start
    yield
    process.terminate()


# -------------------------------------------------------
# Test 1: Verify calculator arithmetic operations via UI
# -------------------------------------------------------
@pytest.mark.parametrize(
    "button_text,a,b,expected",
    [
        ("Add", 2, 3, "5"),
        ("Subtract", 5, 3, "2"),
        ("Multiply", 2, 3, "6"),
        ("Divide", 6, 3, "2"),
    ],
)
def test_calculator_operations_ui(page: Page, button_text, a, b, expected):
    """Check each arithmetic operation works correctly via browser UI."""
    page.goto(BASE_URL)
    page.fill("#a", str(a))
    page.fill("#b", str(b))
    page.click(f"text={button_text}")
    expect(page.locator("#result")).to_contain_text(expected)


# -------------------------------------------------------
# Test 2: Division by zero should show an error
# -------------------------------------------------------
@pytest.mark.xfail(reason="Browser blocks non-numeric input for type=number fields")
def test_ui_invalid_input_error_message(page: Page):
    page.goto(BASE_URL)
    page.fill("#a", "abc")
    page.fill("#b", "5")
    page.click("text=Add")
    expect(page.locator("#result")).to_contain_text("invalid")


# -------------------------------------------------------
# Test 3: Empty inputs should not crash UI
# -------------------------------------------------------
def test_ui_handles_empty_inputs(page: Page):
    page.goto(BASE_URL)
    page.click("text=Add")
    expect(page.locator("#result")).not_to_have_text("Internal Server Error")


# -------------------------------------------------------
# Test 4: Invalid inputs (non-numeric)
# -------------------------------------------------------
@pytest.mark.xfail(reason="Browser prevents non-numeric input for type=number fields")
def test_ui_invalid_input_error_message(page: Page):
    page.goto(BASE_URL)
    page.fill("#a", "abc")
    page.fill("#b", "5")
    page.click("text=Add")
    expect(page.locator("#result")).to_contain_text("invalid")


# -------------------------------------------------------
# Test 5: Chained operations simulate real user flow
# -------------------------------------------------------
def test_ui_chained_operations(page: Page):
    page.goto(BASE_URL)
    page.fill("#a", "10")
    page.fill("#b", "2")
    page.click("text=Divide")
    page.fill("#a", "5")
    page.fill("#b", "3")
    page.click("text=Add")
    expect(page.locator("#result")).not_to_have_text("Error")
