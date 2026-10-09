from lib.models.customer import Customer


def test_customer():
    customer = Customer(id=1, name="customer", email="hello@example.com")

    assert customer.id == 1
    assert customer.name == "customer"
    assert customer.email == "hello@example.com"


def test_customer_eq():
    customer = Customer(id=1, name="customer", email="hello@example.com")
    customer2 = Customer(id=1, name="customer", email="hello@example.com")

    assert customer == customer2
