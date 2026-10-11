from shopcart.shipping import shipping_fee


def test_order_of_exactly_50_ships_free():
    assert shipping_fee(50.0) == 0.0
    assert shipping_fee(49.99) == 4.99
    assert shipping_fee(50.01) == 0.0
