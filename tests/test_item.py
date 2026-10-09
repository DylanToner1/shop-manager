from lib.models.item import Item


def test_item():
    item = Item(id=1, name="item", price=3.99, stock_count=2)

    assert item.id == 1
    assert item.name == "item"
    assert item.price == 3.99
    assert item.stock_count == 2


def test_item_eq():
    item = Item(id=1, name="item", price=3.99, stock_count=2)
    item2 = Item(id=1, name="item", price=3.99, stock_count=2)

    assert item == item2
