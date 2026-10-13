from lib.models.item import Item
from lib.db_conn import DatabaseConnection


class ItemRepo:
    def __init__(self, conn: DatabaseConnection):
        self._conn = conn

    def all(self, in_stock=False) -> list[Item]:
        if in_stock:
            rows = self._conn.execute(
                "SELECT * from items WHERE stock_count > 0 ORDER BY id"
            )
        else:
            rows = self._conn.execute("SELECT * from items  ORDER BY id")
        items = []
        for row in rows:
            item = Item(row["id"], row["name"], row["price"], row["stock_count"])
            items.append(item)
        return items

    def get(self, id):
        rows = self._conn.execute("SELECT * from items WHERE id = %s", [id])
        if not rows:
            return None
        row = rows[0]
        return Item(row["id"], row["name"], row["price"], row["stock_count"])

    def create(self, item: Item):
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
