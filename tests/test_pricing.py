# pytest example (place each of this examples inside tests/test_pricing.py)
import pytest

#from src.pricing import apply_discount

def apply_discount(price: float, discount: float) -> float:
    """
    discount in range [0, 1]
    """
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return round(price * (1 - discount), 2)

def test_apply_discount_happy_path():
    assert apply_discount(100, 0.2) == 80.0

def test_apply_discount_zero_discount():
    assert apply_discount(100, 0.0) == 100.0

def test_apply_discount_invalid_discount_raises():
    with pytest.raises(ValueError):
        apply_discount(100, 1.5)
