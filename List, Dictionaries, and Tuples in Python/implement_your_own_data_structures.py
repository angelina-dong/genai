# start with empty dictionary
inventory = {}

# add starting apple and banana items
inventory.update({"apple" : (10, 2.5), "banana": (20, 1.2)})

# display's the current inventory
def display_inventory():
    print("Current inventory: ")
    for i, (q, p) in inventory.items():
        print(f"Item: {i}, Quantity: {q}, Price: ${p}")

# calculate and display's the current inventory's total value
def calculate_total_value():
    total = sum(q * p for q, p in inventory.values())
    print(f"Total inventory value: ${total:.2f}")

# adds a NEW item to the inventory
def add_item(item, quantity, price):
    if item not in inventory:
        inventory[item] = (quantity, price)
        print(f"Added {item} to inventory!")
    else:
        print(f"{item.capitalize()} is already in the inventory. Please only add new items.")

# updates an ALREADY EXISTING item in the inventory
def update_item(item, quantity, price):
    if item in inventory:
        inventory[item] = (quantity, price)
        print("Updated inventory.")
    else:
        print(f"{item.capitalize()} does not exist in the inventory. Please only update existing items.")

# deletes an ALREADY EXISTING item from the inventory
def remove_item(item):
    if item in inventory:
        del inventory[item]
        print(f"Deleted {item} from inventory.")
    else:
        print(f"{item.capitalize()} is not in the inventory. Please only remove existing items.")

print("Welcome to the Inventory Manager!")
display_inventory()

# keeps track of when user wants to stop editing the inventory
edit_inventory = True

# loops options until the user chooses (types) the "exit" option
while edit_inventory:

    # prompt user for option
    option = input('Type "add" to add a new item, "update" to update an existing item, "remove" to completely delete an item, "display" to show the current inventory and total value, or "exit" to stop making edits to the current inventory: ')
    
    # add new item to the inventory
    if option == 'add':
        item = input("Enter item name: ")
        quantity = int(input("Enter the item's quantity: "))
        price = float(input("Enter the item's price: "))
        add_item(item.lower(), quantity, price)
    
    # update an existing item in the inventory
    elif option == 'update':
        item = input("Enter item name: ")
        element_to_update = input('Enter "quantity" to update the quantity, "price" to update the price, or "both" to update both quantity and price: ')

        # update the item's quantity
        if element_to_update == 'quantity':
            quantity = int(input("Enter the item's updated quantity: "))
            update_item(item.lower(), quantity, inventory[item][1])

        # update the item's price
        elif element_to_update == 'price':
            price = float(input("Enter the item's updated price: "))
            update_item(item.lower(), inventory[item][0], price)
        
        # update the item's quantity and price
        elif element_to_update == 'both':
            quantity = int(input("Enter the item's updated quantity: "))
            price = float(input("Enter the item's updated price: "))
            update_item(item.lower(), quantity, price)

        # handle an invalid option
        else:
            print("Invalid option. Please try again.")

    # completely delete/remove an item from the inventory
    elif option == 'remove':
        item_to_remove = input("Enter the name of the item to remove: ")
        remove_item(item_to_remove.lower())

    # display the current inventory and its total value
    elif option == 'display':
        display_inventory()
        calculate_total_value()
    
    # exit the option loop to stop editing the inventory
    elif option == "exit":
        edit_inventory = False

        # display current inventory and total value on exit
        display_inventory()
        calculate_total_value()
        break

    # handle all other inputs - invalid options
    else:
        print("Invalid option. Please try again.")

    
