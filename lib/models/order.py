from dataclasses import dataclass
from datetime import UTC, datetime


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
        self.placed_on = placed_on or datetime.now(tz=UTC)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Order({self.id}, {self.item_id}, {self.customer_id}, {self.placed_on.isoformat()})"


@dataclass
class OrderSummary:
    id: int
    placed_on: datetime
    item_name: str
    customer_name: str

    def format(self) -> str:
        ts = self.placed_on.strftime("%Y-%m-%d at %H:%M:%S")
        return f"Order #{self.id} - {self.item_name} for {self.customer_name}, ordered on {ts}"
