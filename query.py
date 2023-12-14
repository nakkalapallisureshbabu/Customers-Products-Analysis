import sqlite3
connection = sqlite3.connect("supermarket.db")
cursor = connection.cursor()
customers = cursor.execute("select * from customers")
print(customers.fetchall())
products = cursor.execute("select * from products")
print(products.fetchall())
