from datetime import datetime, timezone


class Order:
    def __init__(
        self,
        id: int,
        item_id: int,
        customer_id: int,
        placed_on: datetime | None = None,
    ):
        self.id = id
        self.item_id = item_id
        self.customer_id = customer_id
        self.placed_on = placed_on or datetime.now(tz=timezone.utc)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Order({self.id}, {self.item_id}, {self.customer_id}, {self.placed_on.isoformat()})"
