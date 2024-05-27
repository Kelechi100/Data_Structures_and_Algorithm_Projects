from item import Item



	#constructors
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name] += quantity
        else:
            self.items[item.name] = quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name] -= quantity
            if self.items[item.name] <= 0:
                del self.items[item.name]

    def update_quantity(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] = quantity

    def view_basket(self):
        if not self.items:
            print("Your shopping basket is empty.")
        else:
            print("Shopping Basket:")
            for item_name, quantity in self.items.items():
                print(f"{item_name}: Quantity - {quantity}")

    def calculate_total_cost(self):
        total_cost = 0
        for item_name, quantity in self.items.items():
            total_cost += quantity * [item_name].price
        return total_cost

    def empty_basket(self):
        self.items = {}

    def is_empty(self):
        return not bool(self.items)

    def is_item_in_basket(self, item):
        return item.name in self.items
