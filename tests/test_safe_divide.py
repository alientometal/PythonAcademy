# pytest example tests
import pytest

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b

def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5

def test_safe_divide_raises_on_zero():
    with pytest.raises(ZeroDivisionError):
        safe_divide(10, 0)
