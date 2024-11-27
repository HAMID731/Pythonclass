products = {
    "Laptop": 1000,
    "Phone": 500,
    "Headphones": 100
}

cart = []

def add_to_cart(cart, products):
    item = input("Enter the product name to add: ")
    if item in products:
        cart.append((item, products[item]))
        print(f"{item} has been added to your cart.")
    else:
        print("Product not found.")

def remove_from_cart(cart):
    item = input("Enter the product name to remove: ")
    for product in cart:
        if product[0] == item:
            cart.remove(product)
            print(f"{item} has been removed from your cart.")
            return
    print("Item not found in your cart.")

def view_cart(cart):
    if not cart:
        print("Your cart is currently empty.")
    else:
        print("Your cart contains:")
        for item, price in cart:
            print(f"{item}: ${price}")

def calculate_total(cart):
    return sum(price for _, price in cart)

def checkout(cart):
    total = calculate_total(cart)
    if not cart:
        print("Your cart is empty.")
    else:
        print(f"Thank you for shopping with us! Your total is ${total}.")
        cart.clear()

def menu():
    while True:
        print("\nWelcome to Jessica's E-Store!")
        print("1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            for name, price in products.items():
                print(f"{name}: ${price}")
        elif choice == "2":
            add_to_cart(cart, products)
        elif choice == "3":
            remove_from_cart(cart)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            checkout(cart)
        elif choice == "6":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option, try again.")

