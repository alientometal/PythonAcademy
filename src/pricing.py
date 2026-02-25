def apply_discount(price: float, discount: float) -> float:
    """
    discount in range [0, 1]
    """
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return round(price * (1 - discount), 2)
