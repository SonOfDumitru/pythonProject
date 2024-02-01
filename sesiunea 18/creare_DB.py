import sqlite3

conn = sqlite3.connect('Marketplace.db')
cursor = conn.cursor()

script = '''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
address TEXT,
city TEXT,
postal_code TEXT,
country TEXT
);

CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name  TEXT NOT NULL,
category TEXT NOT NULL,
price REAL NOT NULL,
stock_count INTEGER DEFAULT 1,
description TEXT
);

CREATE TABLE IF NOT EXISTS Orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_id INTEGER NOT NULL,
order_date TEXT
);

CREATE TABLE IF NOT EXISTS Order_Items(
id INTEGER PRIMARY KEY AUTOINCREMENT,
order_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
quantity INTEGER DEFAULT 0,
total_price REAL NOT NULL
);
'''
cursor.executescript(script)
