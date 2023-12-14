import sqlite3

connection = sqlite3.connect("supermarket.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table customers")
    cursor.execute("drop table products")
except:
    pass

cursor.execute("CREATE TABLE customers(cust_id integer primary key,cust_name text,ph_no integer,email text,pid int,foreign key(pid) references products(prod_id))")
cursor.execute("CREATE TABLE products(prod_id int primary key,prod_name text,use_by_date text)")

cursor.execute("""insert into customers values(1,'suresh', 1234567890, 'xyz@gmail.com', 312 )""")
cursor.execute("""insert into products values(312,'fish', '12-12-2023')""")
connection.commit()
connection.close()
print("done.")
