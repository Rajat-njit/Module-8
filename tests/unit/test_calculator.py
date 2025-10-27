import math
import pytest

from app.operations import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0.0),
        (2, 3, 5.0),
        (-2, 3, 1.0),
        (2.5, 3.5, 6.0),
        (1e9, 1e9, 2e9),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0.0),
        (5, 3, 2.0),
        (-2, -3, 1.0),
        (2.5, 3.5, -1.0),
        (1e9, 1e9, 0.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0.0),
        (5, 0, 0.0),
        (2, 3, 6.0),
        (-2, 3, -6.0),
        (2.5, 3.5, 8.75),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 1, 0.0),
        (6, 3, 2.0),
        (-6, 3, -2.0),
        (2.5, 0.5, 5.0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


@pytest.mark.parametrize("bad", ["abc", object(), None])
def test_type_coercion_errors(bad):
    # All ops will fail float(bad) inside; ensure they raise ValueError or TypeError
    with pytest.raises((ValueError, TypeError)):
        add(bad, 1)
    with pytest.raises((ValueError, TypeError)):
        subtract(1, bad)
    with pytest.raises((ValueError, TypeError)):
        multiply(bad, 2)
    with pytest.raises((ValueError, TypeError)):
        divide(10, bad)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1e-9, 1e-9, 2e-9),
        (-1e-9, -1e-9, -2e-9),
        (1e308, -1e308, 0.0),
    ],
)
def test_add_extreme_values(a, b, expected):
    assert add(a, b) == pytest.approx(expected)
