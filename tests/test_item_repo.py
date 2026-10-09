from lib.item_repo import ItemRepo
from lib.models.item import Item
from decimal import Decimal

"""
When we call ItemRepo#all
We get a list of Item objects reflecting the seed data.
"""


def test_get_all_records(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/items.sql")  # Seed our database with some test data
    repository = ItemRepo(db_connection)  # Create a new ItemRepo

    items = repository.all()  # Get all items

    print(items)

    # Assert on the results
    assert items == [
        Item(1, "item1", Decimal("3.99"), 0),
        Item(2, "item2", Decimal("6.99"), 6),
        Item(3, "item3", Decimal("1.99"), 124),
        Item(4, "item4", Decimal("36.99"), 32),
        Item(5, "item5", Decimal("4.99"), 640),
        Item(6, "item6", Decimal("8.99"), 4),
    ]


"""
When we call ItemRepo#find
We get a single Item object reflecting the seed data.
"""


def test_get_single_record(db_connection):
    db_connection.seed("seeds/items.sql")
    repository = ItemRepo(db_connection)

    item = repository.get(3)
    assert item == Item(3, "item3", Decimal("1.99"), 124)


"""
When we call ItemRepo#create
We get a new record in the database.
"""


def test_create_record(db_connection):
    db_connection.seed("seeds/items.sql")
    repository = ItemRepo(db_connection)

    repository.create(Item(None, "item7", 12.99, 0))

    result = repository.all()
    assert result == [
        Item(1, "item1", Decimal("3.99"), 0),
        Item(2, "item2", Decimal("6.99"), 6),
        Item(3, "item3", Decimal("1.99"), 124),
        Item(4, "item4", Decimal("36.99"), 32),
        Item(5, "item5", Decimal("4.99"), 640),
        Item(6, "item6", Decimal("8.99"), 4),
        Item(7, "item7", Decimal("12.99"), 0),
    ]


"""
When we call ItemRepo#delete
We remove a record from the database.
"""


def test_delete_record(db_connection):
    db_connection.seed("seeds/items.sql")
    repository = ItemRepo(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Item(1, "item1", Decimal("3.99"), 0),
        Item(2, "item2", Decimal("6.99"), 6),
        Item(4, "item4", Decimal("36.99"), 32),
        Item(5, "item5", Decimal("4.99"), 640),
        Item(6, "item6", Decimal("8.99"), 4),
    ]
