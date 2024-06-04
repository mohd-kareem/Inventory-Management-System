import tkinter as tk
import mysql.connector

# Function to connect to MySQL database
def connect_to_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kareem890",
        database="Inventory"
    )
    return db

# Function to add a product to the database
def add_product(name, quantity, price):
    db = connect_to_database()
    cursor = db.cursor()
    query = "INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, quantity, price))
    db.commit()
    db.close()

# Function to display all products
def display_products():
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)
    db.close()

# Tkinter GUI
def add_product_window():
    def add_product_to_db():
        name = name_entry.get()
        quantity = int(quantity_entry.get())
        price = int(price_entry.get())
        add_product(name, quantity, price)
        name_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Add Product")

    name_label = tk.Label(root, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    quantity_label = tk.Label(root, text="Quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(root)
    quantity_entry.pack()

    price_label = tk.Label(root, text="Price:")
    price_label.pack()
    price_entry = tk.Entry(root)
    price_entry.pack()

    add_button = tk.Button(root, text="Add Product", command=add_product_to_db)
    add_button.pack()
    
    root.mainloop()
        
add_product_window()
display_products()