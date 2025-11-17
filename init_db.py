import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    image TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("DELETE FROM products")

products = [
    ('Authentic Swag T-Shirt', 'Luxury cotton tee for premium drip.', 799, 'shirts/image1.jpeg'),
    ('Dope Flex Tee', 'Street-style essential for kings.', 899, 'shirts/image2.jpeg'),
    ('Urban OG Tee', 'Classic minimalist drip.', 749, 'shirts/image3.jpeg'),
    ('Elite Mode Shirt', 'Perfect for bold streetwear looks.', 850, 'shirts/image4.jpeg'),
    ('Street Legend Tee', 'Premium comfort with signature swag.', 950, 'shirts/image5.jpeg'),
    ('Drip Edition Shirt', 'High-quality fabric with timeless design.', 890, 'shirts/image6.jpeg'),

    ('Dope Swag Hat', 'Signature snapback for real ones.', 720, 'hats/image15.jpeg'),
    ('DripFlex Hat', 'Iconic clean-cut cap for daily wear.', 770, 'hats/image16.jpeg'),
    ('OBK Elite Cap', 'Modern street drip in every angle.', 850, 'hats/image17.jpeg'),
    ('Authentic OG Hat', 'Subtle and bold everyday drip.', 800, 'hats/image18.jpeg'),
    ('HypeMode Cap', 'Adjustable, clean, premium styled.', 750, 'hats/image13.jpeg'),
    ('FlexEdition Hat', 'For those who live high-style.', 880, 'hats/image14.jpeg'),

    ('Hi-Top Swag Sneakers', 'Premium leather sneakers for top drip.', 1500, 'sneakers/image12.jpeg'),
    ('OBK Boost Runners', 'Engineered for comfort and style.', 1700, 'sneakers/image11.jpeg'),
    ('Street King Sneakers', 'Your everyday sneaker upgrade.', 1600, 'sneakers/image9.jpeg'),
    ('Urban Supreme Sneakers', 'Low-top perfection for daily fits.', 1800, 'sneakers/image10.jpeg'),
    ('Velocity X Sneakers', 'Built for swagger and movement.', 1650, 'sneakers/image7.jpeg'),
    ('FlexRider Sneakers', 'High-drip edition with slick build.', 1750, 'sneakers/image8.jpeg')
]

cursor.executemany(
    "INSERT INTO products (name, description, price, image) VALUES (?, ?, ?, ?)",
    products
)

conn.commit()
conn.close()

print("✅ Database created successfully!")
