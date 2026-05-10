# Menu
menu = {
    "burger": 100,
    "pizza": 200,
    "fries": 50
}

cart = {}
#save to the file
def save_order(item, qty):
    with open("orders.txt", "a") as file:
        file.write(f"{item} x {qty}\n")

# Show menu
def show_menu():
    print("\n--- MENU ---")
    for item in menu:
        print(item, "-", menu[item])

# Add item
def add_item():
    item = input("Enter item: ").lower()
    if item in menu:
        qty = int(input("Enter quantity: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
            save_order(item,qty)
    
        print("Added to cart")
    else:
        print("Item not found")

# View cart
def view_cart():
    total = 0
    print("\n--- CART ---")
    for item in cart:
        price = menu[item] * cart[item]
        total += price
        print(item, "x", cart[item], "=", price)
    print("Total =", total)

# Main program
while True:
    print("\n1. Show Menu")
    print("2. Add Item")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")