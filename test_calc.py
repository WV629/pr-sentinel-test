"""Tests for calc.py — the fixture PRs are judged against these."""

import pytest

from calc import add, apply_discount, divide, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_discount():
    assert apply_discount(100, 0.2) == 80


def test_discount_invalid_rate():
    with pytest.raises(ValueError):
        apply_discount(100, 1.5)
