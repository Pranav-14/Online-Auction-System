# 🇮🇳 LocalLoop

> **The Indian C2C Hyperlocal Platform for Auctions, Classifieds & Free Giveaways**

LocalLoop is a modern, full-scale C2C marketplace platform tailored specifically for the Indian market. It seamlessly combines timed auctions, fixed-price/negotiable classifieds, and free item giveaways ("Up for Grabs") into a single hyperlocal experience powered by 6-digit PIN code distance radius filtering and mobile (+91) OTP authentication.

---

## 🌟 Key Features

- 🔨 **Timed Auctions**: Real-time bidding engine with reserve prices, minimum bid increments in Indian Rupees (`₹`), and anti-sniping clock auto-extensions (+3 minutes).
- 🏷️ **Classifieds & Direct Offers**: Direct buyer-seller offer negotiation workflow for fixed-price items.
- 🎁 **Free Giveaways ("Up for Grabs")**: Community-driven item donation and claim reservation system with seller recipient selection.
- 📍 **6-Digit PIN Code Radius Search**: Discover local listings within 5 km, 15 km, 30 km, or 50 km radius of your Indian PIN code or city.
- 📱 **Mobile (+91) OTP Authentication**: Fast, secure mobile login designed for high trust and fraud prevention across Indian telecom networks.
- 💬 **In-App Listing Chat**: Real-time buyer-seller messaging with anti-scam QR code safety alerts.
- 🌟 **Seller Trust Score**: Seller rating and review system (1 to 5 stars + verified seller badges).

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | Python 3.12, Django 5.x |
| **Database & Spatial Engine** | PostgreSQL 16 + PostGIS (with local SQLite fallback) |
| **Caching & Async Workers** | Redis 7, Celery 5.3+ |
| **Frontend Architecture** | HTMX 1.9+, Alpine.js 3.x, Modern Vanilla CSS Tokens |
| **Containerization** | Docker Engine & Docker Compose v2 |
| **CI/CD & Linting** | GitHub Actions, Black, Flake8, Pre-commit |
| **Target Cloud Deployment** | Nginx, Certbot (SSL), AWS (Mumbai `ap-south-1`) |

---

## 🚀 Quickstart (Local Development)

### Option A: Running with Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pranav-14/Online-Auction-System.git
   cd Online-Auction-System
   ```

2. **Copy the environment configuration**:
   ```bash
   cp .env.example .env
   ```

3. **Build and launch containers**:
   ```bash
   docker-compose up --build
   ```
   Open `http://localhost:8000` in your browser.

---

### Option B: Running in Local Python Virtual Environment

1. **Create and activate a Python virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations and start server**:
   ```bash
   $env:USE_SQLITE="True" # On Windows PowerShell
   python manage.py migrate
   python manage.py runserver
   ```
   Open `http://localhost:8000` in your browser.

---

## 🧪 Testing & Code Quality

Run automated unit tests:
```bash
python manage.py test
```

Check code style and formatting:
```bash
black --check .
flake8 . --exclude=venv,env,.venv
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
