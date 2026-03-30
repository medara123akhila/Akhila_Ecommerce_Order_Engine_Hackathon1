from product import products
from lock import get_lock

carts = {}

def get_cart(user):
    if user not in carts:
        carts[user] = {}
    return carts[user]

def add_to_cart(user, pid, qty):
    if pid not in products:
        print("❌ Product not found")
        return

    lock = get_lock(pid)

    with lock:
        if products[pid].stock < qty:
            print("❌ Not enough stock")
            return
        
        cart = get_cart(user)
        cart[pid] = cart.get(pid, 0) + qty
        products[pid].stock -= qty

        print("✅ Added to cart")

def remove_from_cart(user, pid):
    cart = get_cart(user)

    if pid in cart:
        qty = cart[pid]
        products[pid].stock += qty
        del cart[pid]
        print("✅ Removed from cart")

def view_cart(user):
    cart = get_cart(user)
    print("🛒 Cart:", cart)