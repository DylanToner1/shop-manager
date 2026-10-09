from lib.models.order import Order
from lib.db_conn import DatabaseConnection


class OrderRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self):
        rows = self._conn.execute("SELECT * from orders")
        orders = []
        for row in rows:
            order = Order(
                row["id"], row["item_id"], row["customer_id"], row["placed_on"]
            )
            orders.append(order)
        return orders

    def get(self, id):
        rows = self._conn.execute("SELECT * from orders WHERE id = %s", [id])
        row = rows[0]
        return Order(row["id"], row["item_id"], row["customer_id"], row["placed_on"])

    def create(self, order: Order):
        self._conn.execute(
            "INSERT INTO orders (item_id, customer_id, placed_on) VALUES (%s, %s, %s)",
            [order.item_id, order.customer_id, order.placed_on],
        )

    def delete(self, id: int):
        self._conn.execute("DELETE FROM orders WHERE id = %s", [id])
