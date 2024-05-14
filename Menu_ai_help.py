# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set up order list
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to Katie's Variety Food Truck.")

# Continuously allow customers to order
place_order = True
while place_order:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}

    # Display menu categories
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")
    if menu_category.isdigit() and int(menu_category) in menu_items:
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")

        # Display items in the selected category
        print(f"What {menu_category_name} item would you like to order?")
        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    print(f"{i}      | {key} - {key2}{' ' * (24 - len(key + key2) - 3)} | ${value2}")
                    menu_items[i] = {"Item name": key + " - " + key2, "Price": value2}
                    i += 1
            else:
                print(f"{i}      | {key}{' ' * (24 - len(key))} | ${value}")
                menu_items[i] = {"Item name": key, "Price": value}
                i += 1

        menu_item_number = input("Choose the item number you want to order: ")
        if menu_item_number.isdigit() and int(menu_item_number) in menu_items:
            quantity = input("How many would you like to order? ")
            quantity = int(quantity) if quantity.isdigit() else 1
            order_list.append({"Item name": menu_items[int(menu_item_number)]["Item name"],
                               "Price": menu_items[int(menu_item_number)]["Price"],
                               "Quantity": quantity})
        else:
            print("Invalid item number.")
    else:
        print("Invalid menu selection.")

    # Ask to continue or complete the order
    keep_order=True
    while keep_order:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        keep_order=False
#        if keep_ordering.lower() in ["y", "yes"]:
 #           break
  #      elif keep_ordering.lower() in ["n", "no"]:
 #           place_order = False
 #           break
 #       else:
 #           print("Please respond with 'Y' for Yes or 'N.")
  #       # match case
        match keep_ordering.lower(): 
        # pattern 1
            case "y":
                place_order = True
 #              break
            # pattern 2
            case "n":
                place_order = False
 #              break
            case _:
                print("Please respond with 'Y' for Yes or 'N for No.")
# Print out the customer's order
print("This is what we are preparing for you.\n")

total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

total_cost = 0  # Initialize total cost

# Loop through the items in the customer's order
for item in order_list:
    item_name = item['Item name']
    price = item['Price']
    quantity = item['Quantity']

    # Calculate total cost for the item
    item_total = price * quantity
    total_cost += item_total  # Add to the overall total cost

    # Prepare item details for display
    name_spaces = ' ' * (24 - len(item_name))
    price_str = f"${price:.2f}"
    price_spaces = ' ' * (8 - len(price_str))
    quantity_str = str(quantity)
    quantity_spaces = ' ' * (10 - len(quantity_str))

    # Print each item
    print(f"{item_name}{name_spaces}|{price_str}{price_spaces}|{quantity_spaces}{quantity}")

# Print the total cost
print("\nTotal cost: $" + f"{total_cost:.2f}")
