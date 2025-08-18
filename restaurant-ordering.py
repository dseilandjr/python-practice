# initialize variables
burger_price = 5.99
pizza_price = 8.49
salad_price = 4.99
drink_price = 1.99
order_total = 0.0
menu = {1: "Burger", 2: "Pizza", 3: "Salad", 4: "Drink"}
prices = {"Burger": burger_price, "Pizza": pizza_price, "Salad": salad_price, "Drink":drink_price }
customer_order = {}


# display welcome message
print("Welcome to our restaurant")
while True:
    # display menu
    print("Item Number  Item Name        Price")
    print("    1         Burger         $", burger_price)
    print("    2         Pizza          $", pizza_price)
    print("    3         Salad          $", salad_price)   
    print("    4         Drink          $", drink_price)
    
    # prompt user to select menu item
    item_choice = int(input("Please select an item number: "))
    # check if valid item_choice and assigns item_name to use with customer_order dictionary
    if item_choice in menu:
        item_name = menu[item_choice]
        item_quantity = int(input("How many?: "))
        if item_name in customer_order:
            customer_order[item_name] += item_quantity
        else:
            customer_order[item_name] = item_quantity
        additional_items = (input("Would you like to order more items? (Y/N)"))
        if additional_items.upper()== "N":
            break
    else: 
        print("Invalid selection. Please try again.")

# display order summary
print("Item  Quantity  Price")
for item in customer_order:
    quantity = customer_order[item]
    price = prices[item]
    
    item_total = round(quantity * price, 2)
    print(item, " ", quantity, "     $", item_total)
    order_total += item_total

print("Total: $", order_total)

    
    

             

        
    


