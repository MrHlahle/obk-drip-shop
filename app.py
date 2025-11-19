import os
from flask import Flask, render_template, session, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = "replace-this-with-a-secure-random-key"

# Path to static images
IMAGE_DIR = os.path.join(os.path.dirname(__file__), "static", "images")

def load_products():
    """
    Scan static/images/<category> and build a list of products.
    Each product has an id, name, price, image, category.
    Image paths are relative to /static/images/...
    """
    products = []
    next_id = 1
    # If there are images placed directly under static/images (like hero), ignore files at root
    for category in sorted(os.listdir(IMAGE_DIR)):
        cat_path = os.path.join(IMAGE_DIR, category)
        if not os.path.isdir(cat_path):
            continue
        for filename in sorted(os.listdir(cat_path)):
            if not (filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))):
                continue
            name_base = os.path.splitext(filename)[0].replace("-", " ").replace("_", " ").title()
            # Simple price generation for demo: shirts cheaper than sneakers
            price = 249.00
            if "sneaker" in filename.lower() or "sneakers" in category.lower():
                price = 899.00
            elif "hat" in filename.lower() or "caps" in category.lower() or "hats" in category.lower():
                price = 199.00
            elif "shirt" in filename.lower() or "tshirt" in filename.lower() or "shirts" in category.lower():
                price = 349.00

            product = {
                "id": str(next_id),
                "name": f"{name_base}",
                "price": float(price),
                "image": f"images/{category}/{filename}",
                "category": category.title()
            }
            products.append(product)
            next_id += 1
    return products

# cached for runtime
PRODUCTS = load_products()

def get_product(pid):
    return next((p for p in PRODUCTS if p["id"] == str(pid)), None)

def cart_total(cart):
    total = 0.0
    for pid, item in cart.items():
        total += item["price"] * item["quantity"]
    return total

@app.context_processor
def inject_cart_count():
    cart = session.get("cart", {})
    count = sum(item["quantity"] for item in cart.values())
    return dict(cart_count=count)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/shop")
def shop():
    # Group products by category preserving order
    categories = {}
    for p in PRODUCTS:
        categories.setdefault(p["category"], []).append(p)
    return render_template("shop.html", categories=categories)

@app.route("/product/<pid>")
def product(pid):
    p = get_product(pid)
    if not p:
        flash("Product not found.", "error")
        return redirect(url_for("shop"))
    return render_template("product.html", product=p)

@app.route("/add_to_cart/<pid>", methods=["POST"])
def add_to_cart(pid):
    p = get_product(pid)
    if not p:
        flash("Product not found.", "error")
        return redirect(url_for("shop"))

    cart = session.get("cart", {})
    item = cart.get(pid, {"id": p["id"], "name": p["name"], "price": p["price"], "quantity": 0, "image": p["image"]})
    item["quantity"] = item.get("quantity", 0) + int(request.form.get("quantity", 1))
    cart[pid] = item
    session["cart"] = cart
    flash(f"Added {p['name']} to cart.", "success")
    return redirect(request.referrer or url_for("shop"))

@app.route("/cart")
def view_cart():
    cart = session.get("cart", {})
    total = cart_total(cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/update_cart", methods=["POST"])
def update_cart():
    cart = session.get("cart", {})
    for pid, value in request.form.items():
        if not pid.startswith("qty_"):
            continue
        product_id = pid.split("qty_")[1]
        try:
            qty = int(value)
        except:
            qty = 0
        if qty <= 0:
            cart.pop(product_id, None)
        else:
            if product_id in cart:
                cart[product_id]["quantity"] = qty
    session["cart"] = cart
    return redirect(url_for("view_cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", {})
    if not cart:
        flash("Your cart is empty.", "info")
        return redirect(url_for("shop"))
    if request.method == "POST":
        # Simple fake checkout - in production you'd integrate a payment gateway
        name = request.form.get("name")
        email = request.form.get("email")
        total = cart_total(cart)
        # create order record here if desired
        session.pop("cart", None)
        return render_template("order_success.html", name=name, email=email, total=total)
    total = cart_total(cart)
    return render_template("checkout.html", total=total)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        flash("Login is demo-only. Implement real auth for production.", "info")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        flash("Register is demo-only. Implement real auth for production.", "info")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/order_success")
def order_success():
    return render_template("order_success.html", name=None, email=None, total=0.0)

if __name__ == "__main__":
    # debug True for local dev; remove in production
    app.run(debug=True)
