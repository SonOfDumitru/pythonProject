import sqlite3
from pprint import pprint

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

product_data = [
    ('Laptop', 'Electronics', 999.99, 50, 'Powerful laptop with high-end specifications for work and gaming'),
    ('Smartphone', 'Electronics', 499.99, 100, 'Feature-rich smartphone with a large display and advanced camera'),
    ('Running Shoes', 'Footwear', 79.99, 200, 'Comfortable running shoes with excellent arch support'),
    ('Coffee Maker', 'Appliances', 149.99, 30, 'Automatic coffee maker with programmable settings'),
    ('Desk Chair', 'Furniture', 129.99, 20, 'Ergonomic desk chair with adjustable height and lumbar support'),
    ('Backpack', 'Fashion', 49.99, 150, 'Stylish backpack with multiple compartments for everyday use'),
    ('Dumbbell Set', 'Fitness', 89.99, 50, 'Versatile dumbbell set for strength training at home'),
    ('Digital Camera', 'Electronics', 699.99, 10, 'High-resolution digital camera with advanced imaging features'),
    ('Cookware Set', 'Kitchen', 179.99, 25, 'Non-stick cookware set with a variety of pots and pans'),
    ('Gaming Mouse', 'Gaming', 59.99, 75, 'Precision gaming mouse with customizable RGB lighting'),
]
query = 'insert into Products (name, category, price, stock_count, description) Values (?,?,?,?,?);'
cursor.executemany(query, product_data)
conn.commit()
conn.close()
