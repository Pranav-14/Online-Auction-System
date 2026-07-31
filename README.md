# 🇮🇳 LocalLoop

> **The Indian C2C Hyperlocal Platform for Auctions, Classifieds & Free Giveaways**

LocalLoop is a modern, full-scale C2C marketplace platform tailored for the Indian market. It combines timed auctions, fixed-price/negotiable classifieds, and free item giveaways ("Daan") into a single, seamless hyperlocal experience backed by 6-digit PIN code distance radius filtering and mobile (+91) OTP authentication.

---

## 🌟 Key Features

- 🔨 **Timed Auctions**: Real-time bidding with reserve prices, minimum bid increments in ₹, and anti-sniping clock auto-extension (+3 minutes).
- 🏷️ **Classifieds / Fixed Price (VB)**: Direct buyer-seller offer negotiation workflow.
- 🎁 **Free Giveaways ("Daan")**: Community-driven item donation and claim reservation system.
- 📍 **6-Digit PIN Code Radius Search**: Discover local listings within 5 km, 15 km, 30 km, or 50 km of your Indian PIN code or city.
- 📱 **Mobile (+91) OTP Verification**: Fast, secure mobile login designed for high trust and fraud prevention.
- 💬 **In-App Listing Chat**: Real-time buyer-seller messaging with anti-scam QR code safety alerts.
- 🌟 **Seller Trust Score**: Rating and review system (1 to 5 stars + verified badges).

---

## 🛠️ Technology Stack

- **Backend Framework**: Python 3.12, Django 5.x
- **Database**: PostgreSQL 16 + PostGIS (with local SQLite fallback)
- **Caching & Async Workers**: Redis 7, Celery 5.3+
- **Frontend Layer**: HTMX, Alpine.js, Vanilla CSS Modern Token System
- **Containerization**: Docker & Docker Compose
- **Production Server**: Nginx, Certbot (SSL), AWS (Mumbai `ap-south-1`)

---

## 🚀 Quickstart (Local Development)

### Option A: Running with Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranav-14/LocalLoop.git
   cd LocalLoop
   ```

2. Copy the environment variables file:
   ```bash
   cp .env.example .env
   ```

3. Spin up containers:
   ```bash
   docker-compose up --build
   ```
   Open `http://localhost:8000` in your browser.

---

### Option B: Running Standalone Python Virtual Environment

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   Open `http://localhost:8000` in your browser.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
