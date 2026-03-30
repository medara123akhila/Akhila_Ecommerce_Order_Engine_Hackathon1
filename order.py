from cart import carts
from product import products
from payment import process_payment
from lock import get_lock

orders = {}
order_id = 1

def place_order(user):
    global order_id

    if user not in carts or not carts[user]:
        print("❌ Cart empty")
        return

    cart = carts[user]
    total = 0

    # calculate total
    for pid, qty in cart.items():
        total += products[pid].price * qty

    print(f"💰 Total = ₹{total}")

    # lock all products
    locks = [get_lock(pid) for pid in cart]

    for lock in locks:
        lock.acquire()

    try:
        # payment
        if not process_payment():
            print("❌ Payment Failed")

            # rollback
            for pid, qty in cart.items():
                products[pid].stock += qty

            carts[user] = {}
            return

        # success
        orders[order_id] = {
            "user": user,
            "items": cart.copy(),
            "total": total,
            "status": "PAID"
        }

        carts[user] = {}
        print(f"✅ Order placed ID: {order_id}")

        order_id += 1

    finally:
        for lock in locks:
            lock.release()

def view_orders():
    for oid, data in orders.items():
        print(oid, data)