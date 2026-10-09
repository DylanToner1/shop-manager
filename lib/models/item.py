class Item:
    def __init__(self, id: int, name: str, price: float, stock_count: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock_count = stock_count

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Item({self.id}, {self.name}, {self.price}, {self.stock_count})"
