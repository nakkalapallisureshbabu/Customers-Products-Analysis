import sqlite3

connection = sqlite3.connect("store.db")

def initialize_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS Customers")
    except:
        pass

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT
    )
    ''')

    for customer in [
        {'name': 'John Doe', 'email': 'john@example.com'},
        {'name': 'Jane Smith', 'email': 'jane@example.com'},
        {'name': 'Mike Johnson', 'email': 'mike@example.com'},
    ]:
        cursor.execute(f"INSERT INTO Customers (name, email) VALUES "
                       f"('{customer['name']}', '{customer['email']}')")

    try:
        cursor.execute("DROP TABLE IF EXISTS Products")
    except:
        pass

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        quantity INTEGER
    )
    ''')

    for product in [
        {'name': 'Product A', 'price': 19.99, 'quantity': 100},
        {'name': 'Product B', 'price': 29.99, 'quantity': 50},
        {'name': 'Product C', 'price': 9.99, 'quantity': 200},
    ]:
        cursor.execute(f"INSERT INTO Products (name, price, quantity) VALUES "
                       f"('{product['name']}', {product['price']}, {product['quantity']})")

    connection.commit()

def get_all_customers():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customers")
    columns = [column[0] for column in cursor.description]
    customers = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return customers

def add_customer(name, email):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Customers (name, email) VALUES "
                   f"('{name}', '{email}')")
    connection.commit()

def get_customer_details(customer_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Customers WHERE id = {customer_id}")
    columns = [column[0] for column in cursor.description]
    customer = dict(zip(columns, cursor.fetchone()))
    return customer

def update_customer(customer_id, name, email):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Customers SET name = '{name}', email = '{email}' "
                   f"WHERE id = {customer_id}")
    connection.commit()

def delete_customer(customer_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Customers WHERE id = {customer_id}")
    connection.commit()

def get_all_products():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    columns = [column[0] for column in cursor.description]
    products = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return products

def add_product(name, price, quantity):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Products (name, price, quantity) VALUES "
                   f"('{name}', {price}, {quantity})")
    connection.commit()

def get_product_details(product_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Products WHERE id = {product_id}")
    columns = [column[0] for column in cursor.description]
    product = dict(zip(columns, cursor.fetchone()))
    return product

def update_product(product_id, name, price, quantity):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Products SET name = '{name}', price = {price}, quantity = {quantity} "
                   f"WHERE id = {product_id}")
    connection.commit()

def delete_product(product_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Products WHERE id = {product_id}")
    connection.commit()

if __name__ == "__main__":
    initialize_database()
