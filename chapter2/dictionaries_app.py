# Write an simple app to calculate the total price of fruits in the inventory
# Needs to be able to add and remove items from the inventory


fruits_inventory = {
    "apple": {"quantity": 10, "price": 1.5},
    "banana": {"quantity": 5, "price": 1},
    "cherry": {"quantity": 3, "price": 2},
}


def add_item_to_inventory(item_name, quantity, price):
    # Check if the item already exists in the inventory
    # If it does, update the quantity and price
    # If it doesn't, add a new item to the inventory
    # Print the updated inventory

    if item_name in fruits_inventory:
        fruits_inventory[item_name]["quantity"] += quantity
    else:
        fruits_inventory[item_name] = {"quantity": quantity, "price": price}


def calculate_total_stock():
    total_value = sum(
        [item["quantity"] * item["price"] for item in fruits_inventory.values()]
    )
    return total_value


def remove_item_from_inventory(item_name, quantity_to_remove):
    # Check if the item exists in the inventory
    # If it does, update the quantity
    # If the quantity is 0, remove the item from the inventory
    # Print the updated inventory

    if item_name in fruits_inventory:
        if fruits_inventory[item_name]["quantity"] >= quantity_to_remove:
            fruits_inventory[item_name]["quantity"] -= quantity_to_remove
        else:
            print("Quantity to remove is greater than the available quantity")
    else:
        print("Item not found in inventory")


total_value = calculate_total_stock()
print("Stock value : ", total_value)

print("-------------------------")

add_item_to_inventory("orange", 5, 2)
total_value_after_adding_item = calculate_total_stock()
print("Stock value after adding item: ", total_value_after_adding_item)

print("-------------------------")

remove_item_from_inventory("apple", 5)
total_value_after_removing_item = calculate_total_stock()
print("Stock value after removing item: ", total_value_after_removing_item)