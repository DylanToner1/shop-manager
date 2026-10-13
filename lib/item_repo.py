from lib.db_conn import DatabaseConnection
from lib.models.item import Item


class ItemRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self, in_stock=False) -> list[Item]:
        query = "SELECT * from items ORDER BY id"
        if in_stock:
            query = "SELECT * from items WHERE stock_count > 0 ORDER BY id"

        return self._conn.execute(query, cls=Item)

    def get(self, id) -> Item | None:
        rows = self._conn.execute("SELECT * from items WHERE id = %s", [id], cls=Item)

        return rows[0] if rows else None

    def create(self, item: Item) -> int:
        rows = self._conn.execute(
            "INSERT INTO items (name, price, stock_count) VALUES (%s, %s, %s) RETURNING id",
            [item.name, item.price, item.stock_count],
        )
        return int(rows[0]["id"])

    def update(self, item: Item):
        self._conn.execute(
            "UPDATE items SET name = %s, price = %s, stock_count = %s WHERE id = %s",
            [item.name, item.price, item.stock_count, item.id],
        )

    def delete(self, id: int):
        self._conn.execute("DELETE FROM items WHERE id = %s", [id])
