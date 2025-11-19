🛍️ OBK Drip Shop — Premium Streetwear Store
https://obk-drip-shop.onrender.com

A modern Flask-powered e-commerce web app featuring premium streetwear, caps, and sneakers.
Built for speed, simplicity, and a clean dark navy + gold UI.

Live Demo: (Your Render URL here)

🚀 Features
🏠 Home Page

Hero section with intro text + hero image

“Enter Shop” and “About OBK Drip” CTAs

Clean gold + navy styling with hover effects

🛒 Shop

Product categories displayed in a clean grid:

Tshirts

Caps

Sneakers

Each item includes:

Product image

Name

Price

Add-to-Cart button

🛍️ Cart System

View all added products

Shows cart total

Remove items

Continue shopping or checkout

💳 Checkout Page

Simple order confirmation

Clean UI

Simulated payment flow

🔐 User Pages

Login page

Register page

🎨 UI / UX Highlights

Dark navy background

Gold pillars (headings, brand title, buttons)

Clean white text

Hover → gold transitions

Mobile-friendly

🏗️ Tech Stack
Area	Technology
Backend	Flask (Python)
Frontend	HTML, Jinja Templates, CSS
Database	SQLite (shop.db)
Web Server	Gunicorn
Deployment	Render (Free Plan)
📁 Project Structure
obk-drip-shop/
│ app.py
│ requirements.txt
│ render.yaml
│ shop.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── hero-demo.jpg
│       ├── hats/
│       ├── shirts/
│       └── sneakers/
│
└── templates/
    ├── base.html
    ├── home.html
    ├── shop.html
    ├── product.html
    ├── cart.html
    ├── checkout.html
    ├── order_success.html
    ├── login.html
    ├── register.html
    └── about.html

⚙️ Installation (Local Setup)
1. Clone repo
git clone https://github.com/MrHlahle/obk-drip-shop
cd obk-drip-shop

2. Install dependencies
pip install -r requirements.txt

3. Run locally
python app.py


Open your browser at:

http://127.0.0.1:5000

🚀 Deployment (Render) https://obk-drip-shop.onrender.com

Push latest code to GitHub

Render reads your render.yaml:

Installs dependencies

Runs Gunicorn server

App deploys automatically on updates

Done!

🧑‍💻 Developer

Obakeng Hlahle
Founder of OBK Drip Shop & Developer of this web app
Passionate about full-stack development, clean UI design, and e-commerce technology.

📜 License

This project is open-source under the MIT License.
