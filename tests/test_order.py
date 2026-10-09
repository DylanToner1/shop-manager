from lib.models.order import Order
from datetime import datetime, timezone


def test_order():
    order = Order(
        id=1,
        item_id=1,
        customer_id=1,
        placed_on=datetime(2026, 10, 9, 15, 23, 30, tzinfo=timezone.utc),
    )

    assert order.id == 1
    assert order.item_id == 1
    assert order.customer_id == 1
    assert order.placed_on == datetime(2026, 10, 9, 15, 23, 30, tzinfo=timezone.utc)


def test_order_eq():
    order = Order(
        id=1,
        item_id=1,
        customer_id=1,
        placed_on=datetime(2026, 10, 9, 15, 23, 30, tzinfo=timezone.utc),
    )
    order2 = Order(
        id=1,
        item_id=1,
        customer_id=1,
        placed_on=datetime(2026, 10, 9, 15, 23, 30, tzinfo=timezone.utc),
    )

    assert order == order2
