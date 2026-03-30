# 🛒 E-commerce Order Engine (CLI Based)

## 📌 Project Overview
This project is a **menu-driven CLI-based backend simulation** of an e-commerce platform like Amazon/Flipkart.  
It demonstrates how real-world systems handle **products, carts, orders, payments, concurrency, and failures**.

The system ensures:
- No overselling of products
- Proper stock management
- Safe order processing with rollback
- Simulated multi-user concurrency

---

## ⚙️ Features Implemented

### 🟢 Product Management
- Add new products
- Prevent duplicate product IDs
- View all products
- Maintain stock levels

### 🛒 Cart System (Multi-user)
- Each user has a separate cart
- Add/remove items
- Update quantities
- Real-time stock reservation

### 📦 Order Placement Engine
- Convert cart → order
- Calculate total price
- Atomic operation (all or nothing)
- Clear cart after order

### 💳 Payment Simulation
- Random success/failure
- Handles payment failures gracefully

### 🔄 Transaction Rollback
- If payment fails:
  - Restore stock
  - Cancel order
- Ensures data consistency

### ⚡ Concurrency Handling
- Implemented using locks
- Prevents multiple users from accessing same stock simultaneously

### 📊 Order Management
- View all orders
- Track order details

---

## 🧠 Design Approach

- Modular architecture:
  - `product.py` → product logic  
  - `cart.py` → cart handling  
  - `order.py` → order processing  
  - `payment.py` → payment simulation  
  - `lock.py` → concurrency control  

- Used **in-memory storage (dictionaries)** for simplicity
- Implemented **locking mechanism** to handle concurrent access
- Ensured **atomic transactions** for order placement
- Followed clean and simple CLI-based interaction

---

## 📌 Assumptions

- No real database (data stored in memory)
- Single system execution (CLI)
- Payment is randomly simulated
- One default user (`user1`)
- No UI (console-based application)

---

## ▶️ How to Run the Project

### 🔹 Step 1: Install Python
Make sure Python is installed on your system.

### 🔹 Step 2: Run the application

```bash
python main.py
