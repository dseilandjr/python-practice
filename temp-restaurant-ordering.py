# # Define variables
#  
# Item number name of item price
# 1 Burger $5.99
# 2 Pizza $8.49
# 3 Salad $4.99
# 4 Drink $1.99

menu = {
    "Burger" : 5.99,
    "Pizza" : 8.49,
    "Salad" : 4.99,
    "Drink" : 1.99
}

# # display welcome
# PRINT statement - WELCOME TO RESTAURANT
print("Welcome to our restaurant")
# Initiate WHILE loop 
while True:
# # display menu items
#  Display menu items - (print statement) - for loop initiate menu_items
    print("Item | Name | Price")
    item_number = 1
    for item, price in menu.items():
        print(f' {item_number}    {item}  ${price}')
        item_number += 1
# # prompt menu selection
# Prompt menu selection (user input)
    item_choice = int(input("Choose an item: "))

# # prompt qty
# Prompt qty 
    item_qty = int(input("How many?: "))

# STOP HERE

