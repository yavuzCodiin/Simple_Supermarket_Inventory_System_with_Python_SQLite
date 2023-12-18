# <ins>Simple_Supermarket_Inventory_System_with_Python_SQLite</ins>

# <ins>The Supermarket Project</ins>

The Supermarket Project is a virtual simulation of a supermarket’s inventory management system. It’s designed to replicate the essential functions of tracking and maintaining a supermarket’s product stock. Users can interact with the system to add new products, update existing ones, remove items no longer in stock, and search or filter products based on specific criteria like price.

## <ins>Development Approach</ins>

The project development is divided into two phases:

1. **Phase 1**: Building a streamlined and organized database for the supermarket.
2. **Phase 2**: Enhancing the system with user interface and user experience design.

### <ins>Phase 1 - Basic Structure</ins>

### Initial Setup

Importing required modules:

```python
import sqlite3
import time
```

### Product Class

The `Product` class is designed with the following parameters: `name`, `price`, and `quantity`.

#### Understanding the Code

- **self in Python**: 
  - `self` is used to refer to the instance of the class. It allows access to the attributes and methods of the class in other methods within the class.

- **__init__ Method**: 
  - `__init__` is a special method in Python, known as a constructor. It is automatically called when you create a new instance of a class.
  - In the `Product` class, `__init__` is used to initialize the new `Product` object with specific attributes - `name`, `price`, and `quantity`.

```python
class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```

- **__str__ Method**: 
  - `__str__` is another special method in Python, used to provide a human-readable representation of the object.
  - When you print an instance of the `Product` class or use the `str()` function on it, this method is called.
  - It returns a formatted string that includes the product’s `name`, `price`, and `quantity`, making it easier to understand what the product object represents when printed.

```python
    def __str__(self):
        return "Product Name: {}\nPrice: {}\nNumber: {}".format(self.name, self.price, self.quantity)
```

# SuperMarket Class

## Creating a Connection in SuperMarket Class

The `create_connection` method in the SuperMarket class sets up a connection to the SQLite database. This is essential for executing SQL commands and managing the supermarket database.

`sqlite3.connect('supermarket.db')` creates (or opens, if it already exists) a file named `supermarket.db` which serves as the SQLite database. All the data of the supermarket will be stored in this file.

## Creating a Table with SQL Command

In the `create_connection` method, the line `query = "CREATE TABLE IF NOT EXISTS supermarket (name TEXT, price FLOAT, quantity INT)"` is an SQL command that creates a new table named `supermarket` in the database if it doesn’t already exist. This table is designed to store product information with columns for name, price, and quantity.

## Committing Changes with self.conn.commit()

Whenever you execute a command that changes the data in the database (like adding, updating, or deleting a product), you need to commit these changes. `self.conn.commit()` ensures that these changes are saved in the database file.

```python
class SuperMarket():
    def __init__(self):
        self.create_connection()
```

## Methods

### add_product()

The `add_product` method is responsible for adding new products into our store. When there is a new item to be placed on the virtual shelves, this method takes a `Product` object, unpacks its details, and places them into the `supermarket` table of the `supermarket.db` database. It serves as a way to tell our digital inventory, "Hey, here's something new for you!"

```python
def add_product(self, product):
        query = "INSERT INTO supermarket values(?, ?, ?)"
        self.cursor.execute(query,(product.name, product.price, product.quantity))
        self.conn.commit()
```

### remove_product()

Consider the `remove_product` method as the one that assists in taking items off the shelves. Whenever a product is no longer available or needed, this method comes into play. Simply provide the name of the product, and it meticulously removes all traces of that product from our database. This is how we ensure our inventory remains tidy and current.

```python
def remove_product(self, name):
    query = "DELETE FROM supermarket WHERE name = ?"
    self.cursor.execute(query, (name,))
    self.conn.commit()
```

### list_product()

The `list_product` function displays all the products currently available in the store. It fetches and presents the entire list of products from our database. This function is extremely useful for quickly checking what’s in stock and getting a comprehensive overview of our inventory.

```python
def list_products(self):
    query = "SELECT * FROM supermarket"
    self.cursor.execute(query)
    rows = self.cursor.fetchall()
    if rows: 
        for row in rows:
            print("Product Name: {}\nProduct Price: {} $\nProduct Quantity: {}\n".format(row[0], row[1], row[2]))
    else:
        print("No products in the supermarket")
```

### update_product()

The `update_product` method is used whenever a product's details require an update, such as when the price changes or a new batch arrives with different quantities. This method allows for the modification of existing product details in our database, ensuring that the inventory information remains accurate and up to date.

```python
def update_product(self, product):
    query = "UPDATE supermarket SET price = ?, quantity = ? WHERE name = ?"
    self.cursor.execute(query, (product.price, product.quantity, product.name))
    self.conn.commit()
```

### search_product()

The `search_product` method is the go-to solution when there's a need to find a specific product. By providing the product's name, this method delves into the database and fetches all available information about that particular product.


```python
def search_product(self, name):
    query = "SELECT * FROM supermarket WHERE name = ?"
    self.cursor.execute(query, (name,))
    rows = self.cursor.fetchall()
    if rows:
        for row in rows:
            print("Product Name: {}\nProduct Price: {} $\nProduct Quantity: {}\n".format(row[0], row[1], row[2]))
    else:
        print("Product not found")
```

### filter_product()

The `filter_product` method is particularly useful when there's a need to view products within a specific price range. This functionality can be invaluable for planning sales, analyzing stock, or making strategic decisions based on pricing. It enables filtering and displaying products that fall within the defined price criteria.

```python
def filter_products(self, min_price, max_price):
    query = "SELECT * FROM supermarket WHERE price >= ? AND price <= ?"
    self.cursor.execute(query, (min_price, max_price))
    rows = self.cursor.fetchall()
    if rows:
        for row in rows:
            print("Product Name: {}\nProduct Price: {} $\nProduct Quantity: {}\n".format(row[0], row[1], row[2]))
    else:
        print("No products found")
```

### create_connection() & close_connection()

These two methods are the fundamental start and end points of our interaction with the database. `create_connection` opens up the pathway to our database for any action we need to take. It establishes a connection that allows us to interact with the database, perform queries, and manage our data. Conversely, `close_connection` neatly wraps things up once we're done with our database operations. It ensures that the connection to the database is properly closed, maintaining the integrity and order of our data management process.

```python
def create_connection(self):
    self.conn = sqlite3.connect('supermarket.db')
    self.cursor = self.conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS supermarket (name TEXT, price FLOAT, quantity INT)"
    self.cursor.execute(query)
    self.conn.commit()
```

## The Loop and Choice Table

### `Choice` Table

The choice table is presented to the user to select the desired operation:

```python
print(""" 
    1. Add product 
    2. Remove product
    3. List All Products
    4. Update Product
    5. Search Product
    6. Filter Product by price
    7. Exit
""")
```

### `While` Loop

```python
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
        print("Listing products...")
        time.sleep(2)
        supermarket.list_products()
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
        supermarket.filter_products(min_price, max_price)

    elif choice == 7:
        break

    else:
        print("Invalid choice")
```


















