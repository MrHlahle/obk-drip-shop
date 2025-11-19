from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "OBKDRIPSECRET"

DATABASE = "shop.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ======================
# HOME PAGE (Netflix Layout)
# ======================
@app.route("/")
def home():
    conn = get_db()
    shirts = conn.execute("SELECT * FROM products WHERE category='shirts'").fetchall()
    sneakers = conn.execute("SELECT * FROM products WHERE category='sneakers'").fetchall()
    hats = conn.execute("SELECT * FROM products WHERE category='hats'").fetchall()
    conn.close()

    return render_template("home.html", shirts=shirts, sneakers=sneakers, hats=hats)


# ======================
# SHOP PAGE
# ======================
@app.route("/shop")
def shop():
    conn = get_db()
    shirts = conn.execute("SELECT * FROM products WHERE category='shirts'").fetchall()
    sneakers = conn.execute("SELECT * FROM products WHERE category='sneakers'").fetchall()
    hats = conn.execute("SELECT * FROM products WHERE category='hats'").fetchall()
    conn.close()

    return render_template("shop.html", shirts=shirts, sneakers=sneakers, hats=hats)


# ======================
# PRODUCT DETAILS
# ======================
@app.route("/product/<int:product_id>")
def product_page(product_id):
    conn = get_db()
    product = conn.execute("SELECT * FROM products WHERE id=?", (product_id,)).fetchone()
    conn.close()
    return render_template("product.html", product=product)


# ======================
# CART SYSTEM
# ======================
@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])

    total = sum(float(item["price"]) for item in cart_items)

    return render_template("cart.html", cart=cart_items, total=total)


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    conn = get_db()
    product = conn.execute("SELECT * FROM products WHERE id=?", (product_id,)).fetchone()
    conn.close()

    if product:
        item = {"id": product["id"], "name": product["name"], "price": product["price"]}

        if "cart" not in session:
            session["cart"] = []

        session["cart"].append(item)
        session.modified = True

    return redirect(url_for("cart"))


# ======================
# CHECKOUT
# ======================
@app.route("/checkout")
def checkout():
    cart_items = session.get("cart", [])
    if not cart_items:
        return redirect(url_for("cart"))

    total = sum(float(item["price"]) for item in cart_items)

    return render_template("checkout.html", total=total)


@app.route("/order_success")
def order_success():
    session.pop("cart", None)
    return render_template("order_success.html")


# ======================
# USER AUTH
# ======================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password)).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("home"))
        else:
            return "Invalid login!"

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()

        existing = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        if existing:
            conn.close()
            return "Email already registered!"

        conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                     (name, email, password))
        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))


# ======================
# RENDER DEPLOY FIX
# ======================
@app.route('/static/<path:path>')
def send_static(path):
    return app.send_static_file(path)


# ======================
# RUN
# ======================
if __name__ == "__main__":
    app.run(debug=True)
