from item import Item
from ShoppingCart import ShoppingCart
# Reading Items names and prices from the file "Available_items.txt"
# Load available items from file
def load_items_from_file(file_name):
    items = {}
    with open(file_name, 'r') as file:
        for line in file:
            name, price = line.strip().split(':')
            items[name] = Item(name, float(price))
    return items

def main():
    available_items = load_items_from_file('available_items.txt')
    basket = ShoppingCart()

    while True:
        print("\n**** Shopping cart options ****")
        print("1: Add item")
        print("2: Remove item")
        print("3: Update quantity")
        print("4: View shopping basket")
        print("5: Calculate total cost")
        print("6: Empty shopping basket")
        print("0: Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter the name of the item you want to add: ")
            if item_name in available_items:
                quantity = int(input("Enter the quantity: "))
                basket.add_item(available_items[item_name], quantity)
                print("Item added to basket.")
            else:
                print("Item not found.")

        elif choice == "2":
            item_name = input("Enter the name of the item you want to remove: ")
            if item_name in available_items:
                quantity = int(input("Enter the quantity: "))
                basket.remove_item(available_items[item_name], quantity)
                print("Item removed from basket.")
            else:
                print("Item not found in basket.")

        elif choice == "3":
            item_name = input("Enter the name of the item you want to update: ")
            if item_name in available_items:
                quantity = int(input("Enter the new quantity: "))
                basket.update_quantity(available_items[item_name], quantity)
                print("Quantity updated.")
            else:
                print("Item not found in basket.")

        elif choice == "4":
            basket.view_basket()

        elif choice == "5":
            total_cost = basket.calculate_total_cost()
            print(f"Total cost of the basket: ${total_cost:.2f}")

        elif choice == "6":
            basket.empty_basket()
            print("Basket emptied.")

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





