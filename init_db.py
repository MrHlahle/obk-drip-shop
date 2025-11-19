import sqlite3

conn = sqlite3.connect("shop.db")
c = conn.cursor()

c.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL,
    image TEXT NOT NULL
)
""")

products = [
    ("Classic White Shirt", 299, "shirts", "images/shirts/shirt1.jpg"),
    ("Black Urban Shirt", 350, "shirts", "images/shirts/shirt2.jpg"),
    ("Premium Drip Shirt", 399, "shirts", "images/shirts/shirt3.jpg"),
    ("Streetwear Red Shirt", 329, "shirts", "images/shirts/shirt4.jpg"),
    ("Blue Ice Shirt", 349, "shirts", "images/shirts/shirt5.jpg"),
    ("Champion Shirt", 379, "shirts", "images/shirts/shirt6.jpg"),

    ("Cap Drip 1", 150, "hats", "images/hats/hat1.jpg"),
    ("Cap Drip 2", 160, "hats", "images/hats/hat2.jpg"),
    ("Cap Drip 3", 170, "hats", "images/hats/hat3.jpg"),
    ("Cap Drip 4", 180, "hats", "images/hats/hat4.jpg"),
    ("Cap Drip 5", 190, "hats", "images/hats/hat5.jpg"),
    ("Cap Drip 6", 200, "hats", "images/hats/hat6.jpg"),

    ("Sneaker Alpha", 899, "sneakers", "images/sneakers/sneaker1.jpg"),
    ("Sneaker Blaze", 999, "sneakers", "images/sneakers/sneaker2.jpg"),
    ("Sneaker Turbo", 1099, "sneakers", "images/sneakers/sneaker3.jpg"),
    ("Sneaker Drift", 899, "sneakers", "images/sneakers/sneaker4.jpg"),
    ("Sneaker Shadow", 999, "sneakers", "images/sneakers/sneaker5.jpg"),
    ("Sneaker Ghost", 1099, "sneakers", "images/sneakers/sneaker6.jpg")
]

c.executemany("INSERT INTO products (name, price, category, image) VALUES (?, ?, ?, ?)", products)

conn.commit()
conn.close()

print("✅ Clean database created successfully!")
