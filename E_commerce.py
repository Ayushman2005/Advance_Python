inventory = [
    {"id": 101, "name": "Wireless Headphones", "price": 50.00, "stock": 10},
    {"id": 102, "name": "Gaming Mouse", "price": 25.50, "stock": 5},
    {"id": 103, "name": "Mechanical Keyboard", "price": 80.00, "stock": 8},
    {"id": 104, "name": "USB-C Hub", "price": 15.00, "stock": 20},
    {"id": 105, "name": "Monitor Stand", "price": 30.00, "stock": 3}
]

cart = []

def display_products():
    print("\n--- Available Products ---")
    print(f"{'ID':<5} {'Name':<25} {'Price':<10} {'Stock':<5}")
    print("-" * 50)
    for item in inventory:
        print(f"{item['id']:<5} {item['name']:<25} ${item['price']:<9.2f} {item['stock']:<5}")
    print("-" * 50)

def add_to_cart():
    try:
        display_products()
        product_id = int(input("Enter the Product ID to add: "))
        
        found_product = None
        for item in inventory:
            if item['id'] == product_id:
                found_product = item
                break
        
        if found_product:
            product_quantity = int(input(f"Enter quantity for '{found_product['name']}': "))
            
            if product_quantity <= 0:
                print("Quantity must be greater than 0.")
            elif product_quantity > found_product['stock']:
                print(f"Sorry, we only have {found_product['stock']} in stock.")
            else:
                item_in_cart = None
                for c_item in cart:
                    if c_item['name'] == found_product['name']:
                        item_in_cart = c_item
                        break
                
                if item_in_cart:
                    item_in_cart['qty'] += product_quantity
                else:
                    cart.append({
                        "name": found_product['name'],
                        "price": found_product['price'],
                        "qty": product_quantity
                    })
                
                found_product['stock'] -= product_quantity
                print(f"Added {product_quantity} x {found_product['name']} to cart.")
        else:
            print("Invalid Product ID.")
    except ValueError:
        print("Please enter a valid number.")

def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n--- Remove Item ---")
    for index, item in enumerate(cart):
        print(f"{index + 1}. {item['name']} (Qty: {item['qty']})")
    
    try:
        selection = int(input("Select the item number to remove: "))
        if 1 <= selection <= len(cart):
            cart_item = cart[selection - 1]
            remove_qty = int(input(f"How many '{cart_item['name']}' to remove? "))
            
            if remove_qty > cart_item['qty'] or remove_qty <= 0:
                print("Invalid quantity.")
            else:
                for product in inventory:
                    if product['name'] == cart_item['name']:
                        product['stock'] += remove_qty
                        break
                
                if remove_qty == cart_item['qty']:
                    cart.pop(selection - 1)
                    print(f"Removed all '{cart_item['name']}' from cart.")
                else:
                    cart_item['qty'] -= remove_qty
                    print(f"Removed {remove_qty} x '{cart_item['name']}'. Remaining in cart: {cart_item['qty']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n--- Your Cart ---")
    print(f"{'Name':<25} {'Qty':<5} {'Price':<10} {'Subtotal':<10}")
    print("-" * 55)
    
    total = 0
    for item in cart:
        item_total = item['price'] * item['qty']
        print(f"{item['name']:<25} {item['qty']:<5} ${item['price']:<9.2f} ${item_total:.2f}")
        total += item_total
        
    print("-" * 55)
    print(f"Grand Total: ${total:.2f}")

def checkout():
    if not cart:
        print("\nYour cart is empty. Add items before checking out.")
        return
        
    view_cart()
    confirm = input("\nProceed to payment? (yes/no): ").lower()
    if confirm == 'yes':
        print("\nProcessing payment...")
        print("Payment successful! Thank you for your purchase.")
        cart.clear()
    else:
        print("\nCheckout cancelled.")

def main():
    while True:
        print("\n=== STORE MENU ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            remove_from_cart()
        elif choice == '5':
            checkout()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
main()