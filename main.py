
   from product import *
from cart import *
from order import *

def menu():
    user = "user1"

    while True:
        print("\n===== MENU =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. View Orders")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            pid = input("ID: ")
            name = input("Name: ")
            price = int(input("Price: "))
            stock = int(input("Stock: "))
            add_product(pid, name, price, stock)

        elif ch == "2":
            view_products()

        elif ch == "3":
            pid = input("Product ID: ")
            qty = int(input("Qty: "))
            add_to_cart(user, pid, qty)

        elif ch == "4":
            pid = input("Product ID: ")
            remove_from_cart(user, pid)

        elif ch == "5":
            view_cart(user)

        elif ch == "6":
            place_order(user)

        elif ch == "7":
            view_orders()

        elif ch == "0":
            break

menu()