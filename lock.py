from threading import Lock

product_locks = {}

def get_lock(pid):
    if pid not in product_locks:
        product_locks[pid] = Lock()
    return product_locks[pid]