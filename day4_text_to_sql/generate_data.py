import sqlite3
from datetime import date, timedelta
import random

# Create database
connection = sqlite3.connect("sales.db")
cursor = connection.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    customer_name TEXT,
    product TEXT,
    region TEXT,
    quantity INTEGER,
    revenue REAL
)
""")

# Sample data
products = [
    ("Laptop", 60000),
    ("Monitor", 18000),
    ("Keyboard", 3000),
    ("Mouse", 1500),
    ("Headphones", 5000)
]

regions = ["North", "South", "East", "West"]

customers = [
    "ABC Pvt Ltd",
    "XYZ Corporation",
    "Tech Solutions",
    "Global Systems",
    "Digital India"
]

# Generate sample sales
start_date = date(2026, 1, 1)

order_id = 1

for i in range(100):
    order_date = start_date + timedelta(days=random.randint(0, 242))

    product, price = random.choice(products)
    region = random.choice(regions)
    customer = random.choice(customers)

    quantity = random.randint(1, 10)
    revenue = quantity * price

    cursor.execute("""
    INSERT INTO sales
    (order_id, order_date, customer_name, product, region, quantity, revenue)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        order_id,
        order_date,
        customer,
        product,
        region,
        quantity,
        revenue
    ))

    order_id += 1

connection.commit()
connection.close()

print("Sales database created successfully!")
print("Database: sales.db")