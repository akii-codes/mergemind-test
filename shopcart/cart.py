"""Shopping cart."""

from shopcart.pricing import COUPONS, round_money


class Cart:
    def __init__(self):
        self.items = []
        self.coupon = None

    def add(self, name, price, qty=1):
        if qty < 1:
            raise ValueError("qty must be at least 1")
        self.items.append((name, price, qty))

    def subtotal(self):
        return round_money(sum(price * qty for _, price, qty in self.items))

    def apply_coupon(self, code):
        key = code.strip().upper()
        if key not in COUPONS:
            raise ValueError(f"unknown coupon: {code}")
        self.coupon = COUPONS[key]

    def total(self):
        amount = self.subtotal()
        if self.coupon:
            amount = amount * (1 - self.coupon)
        return round_money(amount)
