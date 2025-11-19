import sqlite3

conn = sqlite3.connect("shop.db")
c = conn.cursor()

# SHIRTS
shirts = ["shirt1.jpg", "shirt2.jpg", "shirt3.jpg", "shirt4.jpg", "shirt5.jpg", "shirt6.jpg"]
for i, fname in enumerate(shirts, start=37):  # assuming IDs start at 37
    c.execute("UPDATE products SET image=? WHERE id=?", (f"shirts/{fname}", i))

# HATS
hats = ["hat1.jpg", "hat2.jpg", "hat3.jpg", "hat4.jpg", "hat5.jpg", "hat6.jpg"]
for i, fname in enumerate(hats, start=43):  # adjust start ID
    c.execute("UPDATE products SET image=? WHERE id=?", (f"hats/{fname}", i))

# SNEAKERS
sneakers = ["sneaker1.jpg", "sneaker2.jpg", "sneaker3.jpg", "sneaker4.jpg", "sneaker5.jpg", "sneaker6.jpg"]
for i, fname in enumerate(sneakers, start=49):  # adjust start ID
    c.execute("UPDATE products SET image=? WHERE id=?", (f"sneakers/{fname}", i))

conn.commit()
conn.close()
print("✅ Image paths fixed in shop.db")
