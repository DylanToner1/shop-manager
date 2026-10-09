from lib.customer_repo import CustomerRepo
from lib.models.customer import Customer

"""
When we call CustomerRepo#all
We get a list of Customer objects reflecting the seed data.
"""


def test_get_all_records(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/customers.sql")  # Seed our database with some test data
    repository = CustomerRepo(db_connection)  # Create a new CustomerRepo

    customers = repository.all()  # Get all customers

    print(customers)

    # Assert on the results
    assert customers == [
        Customer(1, "customer1", "customer1@example.com"),
        Customer(2, "customer2", "customer2@example.com"),
        Customer(3, "customer3", "customer3@example.com"),
    ]


"""
When we call CustomerRepo#find
We get a single Customer object reflecting the seed data.
"""


def test_get_single_record(db_connection):
    db_connection.seed("seeds/customers.sql")
    repository = CustomerRepo(db_connection)

    customer = repository.get(3)
    assert customer == Customer(3, "customer3", "customer3@example.com")


"""
When we call CustomerRepo#create
We get a new record in the database.
"""


def test_create_record(db_connection):
    db_connection.seed("seeds/customers.sql")
    repository = CustomerRepo(db_connection)

    repository.create(Customer(None, "customer4", "customer4@example.com"))

    result = repository.all()
    assert result == [
        Customer(1, "customer1", "customer1@example.com"),
        Customer(2, "customer2", "customer2@example.com"),
        Customer(3, "customer3", "customer3@example.com"),
        Customer(4, "customer4", "customer4@example.com"),
    ]


"""
When we call CustomerRepo#delete
We remove a record from the database.
"""


def test_delete_record(db_connection):
    db_connection.seed("seeds/customers.sql")
    repository = CustomerRepo(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Customer(1, "customer1", "customer1@example.com"),
        Customer(2, "customer2", "customer2@example.com"),
    ]
