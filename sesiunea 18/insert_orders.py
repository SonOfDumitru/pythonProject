import sqlite3
conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

order_data = [
    (1, 1, '2023-12-08'),
    (2, 3, '2023-12-09'),
    (3, 2, '2023-12-10'),
    (4, 1, '2023-12-11'),
    (5, 4, '2023-12-12'),
    (6, 2, '2023-12-13'),
    (7, 3, '2023-12-14'),
    (8, 4, '2023-12-15'),
    (9, 1, '2023-12-16'),
    (10, 2, '2023-12-17'),
]

query = 'insert into Orders(id, customer_id, order_date) Values(?,?,?);'
cursor.executemany(query, order_data)
conn.commit()
conn.close()
