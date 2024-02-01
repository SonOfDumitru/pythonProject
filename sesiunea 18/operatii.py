import sqlite3
from pprint import pprint

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

def update_product_price(product_id,new_price):
    cursor.execute('update Products set price = ? where id = ?',[new_price, product_id])
    conn.commit()

update_product_price(1,899.99)



def delete_product_by_id(product_id):
    cursor.execute('delete from Products where id = ?',[product_id])
    conn.commit()

delete_product_by_id(4)



def get_products_by_category(category):
    cursor.execute('select * from Products where category = ?',[category])
    product = cursor.fetchall()
    pprint(product)

get_products_by_category('Electronics')
