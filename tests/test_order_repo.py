from lib.order_repo import OrderRepo
from lib.models.order import Order
from datetime import datetime

"""
When we call OrderRepo#all
We get a list of Order objects reflecting the seed data.
"""


def test_get_all_records(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/items.sql")
    db_connection.seed("seeds/customers.sql")
    db_connection.seed("seeds/orders.sql")  # Seed our database with some test data
    repository = OrderRepo(db_connection)  # Create a new OrderRepo

    orders = repository.all()  # Get all orders

    print(orders)

    # Assert on the results
    assert orders == [
        Order(1, 1, 1, datetime.fromisoformat("2026-10-09 15:30:00Z")),
        Order(2, 5, 2, datetime.fromisoformat("2026-10-09 15:35:00Z")),
        Order(3, 3, 3, datetime.fromisoformat("2026-10-09 15:40:00Z")),
    ]


"""
When we call OrderRepo#find
We get a single Order object reflecting the seed data.
"""


def test_get_single_record(db_connection):
    db_connection.seed("seeds/items.sql")
    db_connection.seed("seeds/customers.sql")
    db_connection.seed("seeds/orders.sql")  # Seed our database with some test data
    repository = OrderRepo(db_connection)

    order = repository.get(3)
    assert order == Order(3, 3, 3, datetime.fromisoformat("2026-10-09 15:40:00Z"))


"""
When we call OrderRepo#create
We get a new record in the database.
"""


def test_create_record(db_connection):
    db_connection.seed("seeds/items.sql")
    db_connection.seed("seeds/customers.sql")
    db_connection.seed("seeds/orders.sql")  # Seed our database with some test data
    repository = OrderRepo(db_connection)

    repository.create(Order(None, 6, 2, datetime.fromisoformat("2026-10-09 15:45:00Z")))

    result = repository.all()
    assert result == [
        Order(1, 1, 1, datetime.fromisoformat("2026-10-09 15:30:00Z")),
        Order(2, 5, 2, datetime.fromisoformat("2026-10-09 15:35:00Z")),
        Order(3, 3, 3, datetime.fromisoformat("2026-10-09 15:40:00Z")),
        Order(4, 6, 2, datetime.fromisoformat("2026-10-09 15:45:00Z")),
    ]


"""
When we call OrderRepo#delete
We remove a record from the database.
"""


def test_delete_record(db_connection):
    db_connection.seed("seeds/items.sql")
    db_connection.seed("seeds/customers.sql")
    db_connection.seed("seeds/orders.sql")  # Seed our database with some test data
    repository = OrderRepo(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Order(1, 1, 1, datetime.fromisoformat("2026-10-09 15:30:00Z")),
        Order(2, 5, 2, datetime.fromisoformat("2026-10-09 15:35:00Z")),
    ]
