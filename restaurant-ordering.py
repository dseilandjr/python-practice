# initialize variables
menu = {
    1: {"name": "Burger", "price": 5.99}, 
    2: {"name": "Pizza", "price": 8.49}, 
    3: {"name": "Salad", "price": 4.99},
    4: {"name": "Drink", "price": 1.99} 
}

customer_order = {}


# displays menu
def display_menu():
    print("Menu")
    for item_num, item_details in menu.items():
        print(f'{item_num}. {item_details["name"]} - ${item_details["price"]:.2f}')

# calculate total and display order summary
def calculate_total():
    order_total = 0.0
    # display order summary
    print("Item  Quantity  Price")
    for item_num, quantity in customer_order.items():
        item_name = menu[item_num]["name"]
        item_price = menu[item_num]["price"]    
        item_total = round(quantity * item_price, 2)
    

        print(f'{item_name}    {quantity}    ${item_total:.2f}')
        order_total += item_total

    print(f"Total: ${order_total:.2f}")

    
# place order
def place_order():
    ordering = True
    # display welcome message
    print("Welcome to our restaurant")
    while ordering == True:
        display_menu()
    # prompt user to select menu item
        item_choice = int(input("Please select an item number: "))
        # check if valid item_choice to add to customer_order dictionary
        if item_choice in menu:
            item_quantity = int(input("How many?: "))
            if item_quantity > 0:
                if item_choice in customer_order:
                    customer_order[item_choice] += item_quantity
                else:
                    customer_order[item_choice] = item_quantity
            else:
                print("Invalid quantity. Please try again.") 
            # prompt user to select if they would like to continue ordering
            while True:
                additional_items = (input("Would you like to order more items? (Y/N)"))
                if additional_items.upper() == "N":
                    ordering = False
                    break
                elif additional_items.upper() == "Y":
                    break
                else:
                    print("Invalid selection. Please try again.") 
        else: 
            print("Invalid selection. Please try again.") 
    # calls calculate_total function to calculate total and display order summary
    calculate_total()        

place_order()