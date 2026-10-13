from lib.models.order import Order
from lib.db_conn import DatabaseConnection


class OrderRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self) -> list[Order]:
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
        if not rows:
            return None
        row = rows[0]
        return Order(row["id"], row["item_id"], row["customer_id"], row["placed_on"])

    def create(self, order: Order):
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

    def format_order(self, id: int):
        rows = self._conn.execute(
            """SELECT orders.id, orders.placed_on, items.name AS item_name, customers.name AS customer_name from orders 
            JOIN items ON orders.item_id = items.id 
            JOIN customers ON orders.customer_id = customers.id 
            WHERE orders.id = %s""",
            [id],
        )
        row = rows[0]

        timestamp_format = row["placed_on"].strftime("%Y-%m-%d at %H:%M:%S")
        return f"Order #{row['id']} - {row['item_name']} for {row['customer_name']}, ordered on {timestamp_format}"
