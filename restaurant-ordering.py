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

# calculate total and displays order summary and writes to receipt.txt 
def calculate_total():
    order_total = 0.0
    with open("receipt.txt", "w") as f:

        # display order summary
        header = f"{'Item':<15}{'Price':>8}{'Qty':>6}{'Item Total':>12}"
        print(header)
        f.write((header + "\n"))
        for item_num, quantity in customer_order.items():
            item_name = menu[item_num]["name"]
            item_price = menu[item_num]["price"]    
            item_total = round(quantity * item_price, 2)
    
            # prints each line item with quantity and price and writes to receipt.txt
            line_item = f"{item_name:<15}{f'${item_price:.2f}':>8}{quantity:>6}{f'${item_total:.2f}':>10}"
            print(line_item)
            f.write(line_item + "\n")
            order_total += item_total

        # prints order total and writes to receipt.txt
        total_line = f"{'Order Total:':<27}{f'${order_total:.2f}':>12}"
        print(total_line)
        f.write(total_line + "\n")
   
        
# place order
def place_order():
    ordering = True
    # display welcome message
    print("Welcome to our restaurant\n")
    while ordering == True:
        display_menu()
        item_ordered = False
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
                item_ordered = True
            else:
                print("Invalid quantity. Please try again.") 
            # prompt user to select if they would like to continue ordering
            while item_ordered == True:
                additional_items = (input("Would you like to order more items? (Y/N): "))
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


# Main execution block
if __name__ == "__main__":
    # calls place_order function to run program
    place_order()