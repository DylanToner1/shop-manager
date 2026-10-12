from decimal import Decimal

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

    def menu(self) -> int:
        picked = 0
        while picked == 0:
            print("\nWhat do you want to do?")
            print("1. list all items")
            print("2. create a new item")
            print("3. edit an item")
            print("4. list all orders")
            print("5. new order")
            print("0. exit")

            choice = input("Enter option: ")

            try:
                choice = int(choice)
                if choice >= 0 and choice <= 5:
                    return choice
                else:
                    raise

            except:
                print("not a valid choice")

    def list_all_items(self):
        print("Listing all items...")

        items = self.item_repo.all()

        for item in items:
            print(item.format())

    def new_item(self):
        print("Create new item")

        name = input("Enter item name: ")

        price_valid = False
        while not price_valid:
            try:
                price = Decimal(input("Enter item price: ").removeprefix("£"))
                if price > 0:
                    price_valid = True
                else:
                    raise

            except:
                print("Invalid price")

        stock_valid = False
        while not stock_valid:
            try:
                stock = int(input("Enter current item stock: "))

                if stock > 0:
                    stock_valid = True
                else:
                    raise

            except:
                print("Invalid stock level")

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

        id_valid = False
        while not id_valid:
            try:
                id = int(input("Enter item ID: "))

                old_item = self.item_repo.get(id)

                if old_item:
                    id_valid = True
                else:
                    raise

            except:
                print("Invalid ID")

        print("Leave blank to keep the old values")

        new_name = input("Enter new name: ")

        price_valid = False
        while not price_valid:
            try:
                new_price = input("Enter new price: ").removeprefix("£")
                if not new_price:
                    break

                new_price = Decimal(new_price)
                if new_price > 0:
                    price_valid = True
                else:
                    raise

            except:
                print("Invalid price")

        stock_valid = False
        while not stock_valid:
            try:
                new_stock = input("Enter new item stock: ")

                if not new_stock:
                    break

                new_stock = int(new_stock)

                if new_stock > 0:
                    stock_valid = True
                else:
                    raise

            except:
                print("Invalid stock level")

        if not new_name:
            new_name = old_item.name

        if not new_price:
            new_price = old_item.price

        if not new_stock:
            new_stock = old_item.stock_count

        print(
            f"old item: id={id} name={old_item.name}, price=£{old_item.price}, stock level: {old_item.stock_count}"
        )
        print(
            f"new item: id={id} name={new_name}, price=£{new_price}, stock level: {new_stock}"
        )

        try:
            updated_item = Item(
                id=id, name=new_name, price=new_price, stock_count=new_stock
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

    def format_order(self, order: Order):
        item = self.item_repo.get(order.item_id)
        customer = self.customer_repo.get(order.customer_id)
        timestamp_format = order.placed_on.strftime("%Y-%m-%d at %H:%M:%S")
        return f"Order #{order.id} - {item.name} for {customer.name}, ordered on {timestamp_format}"

    def list_all_orders(self):
        print("Listing all orders...\n")

        orders = self.order_repo.all()

        for order in orders:
            print(self.format_order(order))

    def new_order(self):
        print("New order:")

        self.list_all_items()
        print()

        item_valid = False
        while not item_valid:
            try:
                id = int(input("Enter item ID to order: "))

                item = self.item_repo.get(id)

                if item:
                    item_valid = True
                else:
                    raise

            except:
                print("Invalid Item ID")

        self.list_all_customers()
        print()

        customer_valid = False
        while not customer_valid:
            try:
                id = int(input("Enter customer ID: "))

                customer = self.customer_repo.get(id)

                if customer:
                    customer_valid = True
                else:
                    raise

            except:
                print("Invalid Customer ID")

        try:
            new_order = Order(
                id=None, item_id=item.id, customer_id=customer.id, placed_on=None
            )  # class sets placed on to the current time when None

            print(f"Creating order: {self.format_order(new_order)}")

            self.order_repo.create(new_order)

            print("Order created!")

        except Exception as e:
            print(f"failed to create order: {e}")

    def main(self):
        print("Welcome to the shop management program!")

        choice = 999

        while choice != 0:
            choice = self.menu()

            if choice == 0:
                print("Thanks for using the shop management program!")
                break

            print()

            match choice:
                case 1:
                    self.list_all_items()
                case 2:
                    self.new_item()
                case 3:
                    self.edit_item()
                case 4:
                    self.list_all_orders()
                case 5:
                    self.new_order()


if __name__ == "__main__":
    app = App()
    app.main()
