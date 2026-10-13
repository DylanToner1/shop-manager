from lib.db_conn import DatabaseConnection
from lib.models.order import Order, OrderSummary


class OrderRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self) -> list[Order]:
        return self._conn.execute("SELECT * from orders", cls=Order)

    def get(self, id) -> Order | None:
        rows = self._conn.execute("SELECT * from orders WHERE id = %s", [id], cls=Order)

        return rows[0] if rows else None

    def create(self, order: Order) -> int:
        rows = self._conn.execute(
            "INSERT INTO orders (item_id, customer_id, placed_on) VALUES (%s, %s, %s) RETURNING id",
            [order.item_id, order.customer_id, order.placed_on],
        )

        # decrement ordered item's stock
        self._conn.execute(
            "UPDATE items SET stock_count = items.stock_count - 1 WHERE id = %s",
            [order.item_id],
        )

        return int(rows[0]["id"])

    def delete(self, id: int):
        self._conn.execute("DELETE FROM orders WHERE id = %s", [id])

    def get_summary(self, id: int) -> OrderSummary | None:
        rows = self._conn.execute(
            """SELECT orders.id, orders.placed_on, items.name AS item_name, customers.name AS customer_name from orders 
            JOIN items ON orders.item_id = items.id 
            JOIN customers ON orders.customer_id = customers.id 
            WHERE orders.id = %s""",
            [id],
            cls=OrderSummary,
        )
        return rows[0] if rows else None
