"""Shipping fees."""

FREE_SHIPPING_FROM = 50.00  # orders of $50.00 or more ship free
FLAT_FEE = 4.99


def shipping_fee(order_amount: float) -> float:
    """Flat fee below the free-shipping threshold, free at or above it."""
    if order_amount >= FREE_SHIPPING_FROM:
        return 0.0
    return FLAT_FEE
