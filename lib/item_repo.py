from lib.models.item import Item
from lib.db_conn import DatabaseConnection


class ItemRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self):
        rows = self._conn.execute("SELECT * from items")
        items = []
        for row in rows:
            item = Item(row["id"], row["name"], row["price"], row["stock_count"])
            items.append(item)
        return items

    def get(self, id):
        rows = self._conn.execute("SELECT * from items WHERE id = %s", [id])
        row = rows[0]
        return Item(row["id"], row["name"], row["price"], row["stock_count"])

    def create(self, item: Item):
        self._conn.execute(
            "INSERT INTO items (name, price, stock_count) VALUES (%s, %s, 0)",
            [item.name, item.price],
        )

    def delete(self, id: int):
        self._conn.execute("DELETE FROM items WHERE id = %s", [id])
