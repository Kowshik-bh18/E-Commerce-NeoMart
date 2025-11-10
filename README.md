<h1 align="center">🛒 E-Commerce NeoMart</h1>
<p align="center">
  <em>Redefining Online Shopping, the Smart Way.</em><br/>
  A next-generation full-stack e-commerce platform built with <b>Django REST Framework</b> and <b>React</b>, featuring authentication, order management, AI-powered chatbot, and seamless checkout experience.
</p>

---

## 🚀 Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,django,react,sqlite,html,css,js" alt="Tech Stack Logos" />
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Backend-Django%20REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Frontend-React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/UI-Chakra%20UI-319795?style=for-the-badge&logo=chakraui&logoColor=white"/></a>
</p>

---

## 🌟 Features

- 🔐 **JWT Authentication** — Secure login, signup, and token-based sessions  
- 🛍️ **Product Catalog** — Categorized product listings with advanced filters  
- 🛒 **Shopping Cart** — Persistent cart with live updates  
- 📦 **Order Management** — Complete checkout and order tracking system  
- 💬 **AI Chatbot Assistant** — Product recommendation and Q&A bot  
- 🧾 **Invoice Generation** — Auto-generated PDF invoices after checkout  
- 🔎 **Search & Filtering** — Smart product search via Django filters  
- 🧭 **Admin Dashboard** — Manage products, users, and orders  

---

## ⚙️ Backend Setup (Django + DRF)

```bash
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate environment
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 3. Install dependencies
cd backend
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Load sample data (optional)
python scripts/seed.py

# 6. Start development server
python manage.py runserver
