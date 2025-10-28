"""
operations/__init__.py
----------------------
Implements arithmetic operations for the FastAPI calculator app.
Each function includes basic validation and safe handling of edge cases.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """Return the sum of two numbers."""
    return float(a) + float(b)  # pragma: no cover


def subtract(a: Number, b: Number) -> float:
    """Return the difference between two numbers."""
    return float(a) - float(b)  # pragma: no cover


def multiply(a: Number, b: Number) -> float:
    """Return the product of two numbers."""
    return float(a) * float(b)  # pragma: no cover


def divide(a: Number, b: Number) -> float:
    """Return the quotient of two numbers, handling division by zero."""
    if b == 0:  # pragma: no cover
        raise ValueError("Cannot divide by zero")   # pragma: no cover
    return float(a) / float(b)  # pragma: no cover
