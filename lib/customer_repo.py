from lib.models.customer import Customer
from lib.db_conn import DatabaseConnection


class CustomerRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self):
        rows = self._conn.execute("SELECT * from customers")
        customers = []
        for row in rows:
            customer = Customer(row["id"], row["name"], row["email"])
            customers.append(customer)
        return customers

    def get(self, id):
        rows = self._conn.execute("SELECT * from customers WHERE id = %s", [id])
        row = rows[0]
        return Customer(row["id"], row["name"], row["email"])

    def create(self, customer: Customer):
        self._conn.execute(
            "INSERT INTO customers (name, email) VALUES (%s, %s)",
            [customer.name, customer.email],
        )

    def delete(self, id: int):
        self._conn.execute("DELETE FROM customers WHERE id = %s", [id])
