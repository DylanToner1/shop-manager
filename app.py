from helpers import ask_existing, ask_price, ask_stock, ask
from lib.customer_repo import CustomerRepo
from lib.db_conn import DatabaseConnection
from lib.item_repo import ItemRepo
from lib.models.item import Item
from lib.models.order import Order
from lib.order_repo import OrderRepo


class App:
    def __init__(self):
        self.conn = DatabaseConnection()
        self.conn.connect()
        self.item_repo = ItemRepo(self.conn)
        self.order_repo = OrderRepo(self.conn)
        self.customer_repo = CustomerRepo(self.conn)

        self.actions = [
            ("list all items", self.list_all_items),
            ("create a new item", self.new_item),
            ("edit an item", self.edit_item),
            ("list all orders", self.list_all_orders),
            ("new order", self.new_order),
        ]

    def menu(self) -> int:
        print("\nWhat do you want to do?")
        for idx, (label, _) in enumerate(self.actions, start=1):
            print(f"{idx}. {label}")
        print("0. exit")

        return ask(
            "Enter option: ",
            int,
            lambda n: 0 <= n <= len(self.actions),
            "Not a valid choice",
        )

    def list_all_items(self, in_stock=False):
        if not in_stock:
            print("Listing all items...")

        items = self.item_repo.all(in_stock)

        for item in items:
            print(item.format())

    def new_item(self):
        print("Create new item")

        name = ask(
            "Enter item name: ", valid_cond=bool, error="Name required"
        )  # checks if the name isn't blank

        price = ask_price("Enter item price: ")

        stock = ask_stock("Enter item stock level: ")

        print(f"Creating item: name={name}, price=£{price}, stock level: {stock}")

        try:
            item = Item(id=None, name=name, price=price, stock_count=stock)

            self.item_repo.create(item)
            print("Item created!")
        except Exception as e:
            print(f"Item creation failed: {e}")

    def edit_item(self):
        print("Enter the ID of an item to edit:\n")
        self.list_all_items()
        print()

        old_item: Item = ask_existing(
            prompt="Enter item ID: ", repo=self.item_repo, error="Invalid item ID"
        )

        print("Leave blank to keep the old values")

        new_name = input("Enter new name: ") or old_item.name
        new_price = ask_price("Enter new price: ", allow_blank=True) or old_item.price

        stock = ask_stock("Enter new stock level: ", allow_blank=True)
        new_stock = (
            old_item.stock_count if stock is None else stock
        )  # allow new stock to be 0

        print(
            f"old item: id={old_item.id} name={old_item.name}, price=£{old_item.price}, stock level: {old_item.stock_count}"
        )
        print(
            f"new item: id=N/A name={new_name}, price=£{new_price}, stock level: {new_stock}"
        )

        try:
            updated_item = Item(
                id=old_item.id, name=new_name, price=new_price, stock_count=new_stock
            )

            self.item_repo.update(updated_item)
            print("Item updated!")
        except Exception as e:
            print(f"Item update failed: {e}")

    def list_all_customers(self):
        print("Listing all customers...")

        customers = self.customer_repo.all()

        for customer in customers:
            print(customer.format())

    def list_all_orders(self):
        print("Listing all orders...\n")

        orders = self.order_repo.all()

        for order in orders:
            print(self.order_repo.get_summary(order.id).format())

    def new_order(self):
        print("New order:")

        self.list_all_items(in_stock=True)
        print()

        item: Item = ask_existing(
            prompt="Enter item ID to order (only shows items in stock): ",
            repo=self.item_repo,
            valid_cond=lambda item: item.stock_count > 0,
            error="Invalid item ID",
        )

        self.list_all_customers()
        print()

        customer = ask_existing(
            prompt="Enter customer ID: ",
            repo=self.customer_repo,
            error="Invalid customer ID",
        )

        try:
            new_order = Order(
                id=None, item_id=item.id, customer_id=customer.id, placed_on=None
            )  # class sets placed on to the current time when None

            print("Creating order...")

            id = self.order_repo.create(new_order)
            print(f"Created order: {self.order_repo.get_summary(id).format()}")

        except Exception as e:
            print(f"failed to create order: {e}")

    def main(self):
        print("Welcome to the shop management program!")

        while True:
            choice = self.menu()
            if choice == 0:
                break
            print()
            self.actions[choice - 1][1]()

        print("Thanks for using the shop management program!")


if __name__ == "__main__":
    app = App()
    app.main()
