from shopcart.cart import Cart


def test_subtotal_and_total():
    cart = Cart()
    cart.add("book", 12.50, qty=2)
    cart.add("pen", 1.25)
    assert cart.subtotal() == 26.25
    assert cart.total() == 26.25


def test_coupon_discount():
    cart = Cart()
    cart.add("book", 100.0)
    cart.apply_coupon("SAVE10")
    assert cart.total() == 90.0



def test_coupon_code_is_case_insensitive():
    cart = Cart()
    cart.add("book", 100.0)
    cart.apply_coupon("save25")
    assert cart.total() == 75.0


def test_unknown_coupon_is_a_clear_error():
    import pytest

    cart = Cart()
    with pytest.raises(ValueError, match="unknown coupon"):
        cart.apply_coupon("NOPE")
