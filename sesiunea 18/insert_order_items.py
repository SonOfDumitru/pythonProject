import sqlite3

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

order_items_data = [
    (1, 1, 2, 1999.98),
    (2, 3, 1, 79.99),
    (3, 2, 3, 1499.97),
    (4, 4, 1, 129.99),
    (5, 5, 2, 259.98),
    (6, 6, 1, 49.99),
    (7, 8, 1, 699.99),
    (8, 7, 2, 179.98),
    (9, 9, 1, 59.99),
    (10, 10, 3, 179.97),
]

query = 'insert into Orders_Items(order_id, product_id, quantity, total_price) Values(?,?,?,?);'
cursor.executemany(query, order_items_data)
conn.commit()
conn.close()
