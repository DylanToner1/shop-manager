from lib.db_conn import DatabaseConnection
from lib.models.customer import Customer


class CustomerRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self) -> list[Customer]:
        return self._conn.execute("SELECT * from customers", cls=Customer)

    def get(self, id) -> Customer | None:
        rows = self._conn.execute(
            "SELECT * from customers WHERE id = %s", [id], cls=Customer
        )
        return rows[0] if rows else None

    def create(self, customer: Customer) -> int:
        rows = self._conn.execute(
            "INSERT INTO customers (name, email) VALUES (%s, %s) RETURNING id",
            [customer.name, customer.email],
        )
        return int(rows[0]["id"])

    def delete(self, id: int):
        self._conn.execute("DELETE FROM customers WHERE id = %s", [id])
