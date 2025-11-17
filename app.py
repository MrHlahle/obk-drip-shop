from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, os

app = Flask(__name__)
app.secret_key = "obkdrip"

DB_PATH = os.path.join(os.getcwd(), "shop.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session["username"] = username
            return redirect(url_for("shop"))
        else:
            return render_template("login.html", error="Invalid credentials.")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/shop")
def shop():
    conn = get_db()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template("shop.html", products=products)

@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product_id)
    session.modified = True
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    if "cart" not in session or len(session["cart"]) == 0:
        return render_template("cart.html", cart_items=[], total=0)

    conn = get_db()
    cart_items = []
    total = 0

    for pid in session["cart"]:
        product = conn.execute("SELECT * FROM products WHERE id=?", (pid,)).fetchone()
        if product:
            cart_items.append(product)
            total += product["price"]

    conn.close()
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        session["cart"] = []
        return redirect(url_for("order_success"))
    return render_template("checkout.html")

@app.route("/order_success")
def order_success():
    return render_template("order_success.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
