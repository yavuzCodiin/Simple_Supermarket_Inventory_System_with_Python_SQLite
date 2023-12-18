import sqlite3
import time


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return "Product Name: {}\nPrice: {}\nNumber: {}".format(self.name, self.price, self.quantity)


class SuperMarket():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = sqlite3.connect('supermarket.db')
        self.cursor = self.conn.cursor()
        query = "Create Table if not exists supermarket(name TEXT, price FLOAT, quantity INT)"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def add_product(self, product):
        query = "INSERT INTO supermarket values(?, ?, ?)"
        self.cursor.execute(query,(product.name, product.price, product.quantity))
        self.conn.commit()
    
    def remove_product(self,name):
        query = "DELETE FROM supermarket WHERE name =?"
        self.cursor.execute(query,(name,))
        self.conn.commit() 
    
    def list_products(self):
        query = "SELECT * FROM supermarket"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows: 
            for row in rows:
                print("Product Name: {}\nProduct Price: {} $\nProduct Quantity: {}\n ".format(row[0],row[1],row[2]))
        else:
            print("No products in the supermarket")
    
    def update_product(self, product):
        query = "UPDATE supermarket SET price =?, quantity =? WHERE name =?"
        self.cursor.execute(query, (product.price, product.quantity, product.name))
        self.conn.commit() 

    def search_product(self, name):
        query = "SELECT * FROM supermarket WHERE name =?"
        self.cursor.execute(query,(name,))
        rows = self.cursor.fetchall()
        if rows:
            for row in rows:
                print("Product Name: {}\nProduct Price: {} $\nProduct Quantity: {}\n ".format(row[0],row[1],row[2]))
        else:
            print("Product not found")

    def filter_products(self,min_price,max_price):
        query = "SELECT * FROM supermarket WHERE price >=? AND price <=?"
        self.cursor.execute(query,(min_price,max_price))
        rows = self.cursor.fetchall()
        if rows:
            for row in rows:
                print("Product Name: {}\nProduct Price: {} $\nProduct Quantity: {}\n ".format(row[0],row[1],row[2]))
        else:
            print("No products found") 

    print(""" 
          1. Add product 
          2.Remove product
          3.List All Products
          4.Update Product
          5.Search Product
          6.Filter Product by price
          7.Exit
                  

          """)

supermarket = SuperMarket()

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        new_product = Product(name, price, quantity)

        print("{} is being added".format(name))
        time.sleep(2)
        supermarket.add_product(new_product)
        print("{} is added".format(name))


    elif choice == 2:
        name = input("Enter product name: ")

        print("{} is being removed\n".format(name))
        time.sleep(2)
        supermarket.remove_product(name)
        print("{} is removed\n".format(name))

    elif choice == 3:
        supermarket.list_products()
        print("Listing products")
        print("Products are listed")


    elif choice == 4:
        name = input("Enter product name to update: ")
        price = float(input("Enter product price to update: "))
        quantity = int(input("Enter product quantity to update: "))
        new_product = Product(name, price, quantity)

        print("{} is being updated\n".format(name))
        time.sleep(2)
        supermarket.update_product(new_product)
        print("{} is updated\n".format(name))

    elif choice == 5:
        name = input("Enter item name for searching products") 
        print("{} is being searched\n".format(name))
        time.sleep(2)
        supermarket.search_product(name)
        print("{} are listed\n".format(name))

    elif choice == 6:
        print("Please select filter range for product you want to see")
        min_price = int(input("Enter minimum price: "))
        max_price = int(input("Enter maximum price: "))
        supermarket.filter_products(min_price,max_price)

    elif choice == 7:
        break

    else:
        print("Invalid choice")