"""Tiny arithmetic helpers — fixture target for PR Sentinel testing."""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def divide(a, b):
    """Return a / b; raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def apply_discount(total, rate):
    """Return total after a `rate` (0-1) discount is applied."""
    if not 0 <= rate <= 1:
        raise ValueError("rate must be between 0 and 1")
    return total - rate
