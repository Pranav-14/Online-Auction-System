# 🇮🇳 Indian Kleinanzeigen & Auction Platform: Master Agent Baseline & SDLC Roadmap

> **Authoritative Project Specification & Execution Protocol**  
> **Target Market**: India (INR ₹, 6-Digit PIN Radius Search, +91 Mobile OTP Auth, UPI Payments)  
> **Stack**: Python 3.12 / Django 5.x, PostgreSQL + PostGIS, Redis, Celery, HTMX + Alpine.js, Nginx, Docker, AWS (Mumbai `ap-south-1`)

---

## 🤖 Agent Execution Protocol

When feeding any task from this roadmap to an AI Agent or developer, follow these rules:

1. **Sequential Execution**: Always complete tickets in order of their **Dependencies**. Do not skip ahead.
2. **Definition of Done**: A ticket is only complete when:
   - All code is implemented according to specifications.
   - Automated tests for that feature pass (`python manage.py test`).
   - The status checkbox in this document is updated from `[ ]` to `[x]`.
3. **Context Preservation**: Pass the relevant Ticket section and your current repository state as input.

---

## 💰 Financial Cost Matrix & Operating Expenses (INR ₹ / USD $)

| Phase / Tier | Expense Category | Service / Provider | Monthly Cost (Est.) | Annual / One-time | Notes & Recommendations |
|---|---|---|---|---|---|
| **Phase 1 – 5 (Development)** | Local Machine | Docker Desktop + Python | **₹0 ($0)** | ₹0 | 100% Free on your local machine using SQLite & Docker containers. |
| **Phase 6 (Staging / Testing)** | Cloud VPS | DigitalOcean / Hetzner / AWS | **~₹500 – ₹1,000 ($6 - $12)** | ₹0 | Single 2GB RAM node for Docker containers (Django, Postgres, Redis). |
| **Phase 6 (Live MVP Launch)** | Domain Name | Hostinger / Namecheap | — | **~₹600 – ₹900 ($7 - $11/yr)** | `.in` or `.com` domain with free DNS management. |
| **Phase 6 (Live MVP Launch)** | Cloud Compute | AWS EC2 (t4g.small / Mumbai) | **~₹1,200 – ₹2,200 ($15 - $26)** | ₹0 | ARM-based Graviton2 instance in Mumbai region (`ap-south-1`) for low latency. |
| **Phase 6 (Live MVP Launch)** | Object Storage | AWS S3 (Mumbai `ap-south-1`) | **~₹200 – ₹500 ($2 - $6)** | ₹0 | Stores user listing images with CDN distribution. |
| **Phase 6 (Live MVP Launch)** | Mobile OTP SMS | MSG91 / Twilio | Pay-as-you-go | **~₹0.20 per OTP** | ~₹500 pre-funded balance lasts ~2,500 user logins/verifications. |
| **Phase 6 (Live MVP Launch)** | Payment Gateway | Razorpay / UPI | **0% on UPI** | 2% on Cards | UPI transactions via Razorpay/Paytm are zero-fee in India. |
| **TOTAL ESTIMATED COST** | **MVP Live Operation** | **Combined Stack** | **~₹1,900 – ₹3,700 / mo ($23 - $45/mo)** | **~₹700 / year** | Extremely cost-effective for launch in India. |

---

## 🛠️ Required Installed Software & Development Tooling

### Local Development Environment
- **Python**: 3.12.x
- **Docker Desktop**: Docker Engine 24+ & Docker Compose v2 (for local containerized Postgres & Redis)
- **Git**: Version Control CLI
- **IDE / Code Editor**: VS Code (with Python, Docker, & Django extensions) or Antigravity IDE
- **API Testing**: Postman or Bruno (optional for API testing)

### Production Server Stack
- **OS**: Linux Ubuntu 24.04 LTS (AWS EC2 or DigitalOcean Droplet)
- **Container Runtime**: Docker Engine + Docker Compose
- **Web Server & Reverse Proxy**: Nginx + Certbot (Let's Encrypt automated SSL)
- **Database & Cache**: PostgreSQL 16 (with PostGIS extension) + Redis 7

---

## 🏗️ DevOps & Automation Architecture: Do You Need Jenkins & Terraform?

### 1. GitHub Actions vs. Jenkins
- **Verdict**: **GitHub Actions is Recommended (Jenkins is NOT required).**
- **Why?**: 
  - **Jenkins** requires hosting and maintaining a dedicated build server (adding ~$20/mo in extra server costs, OS security patches, and maintenance overhead).
  - **GitHub Actions** is 100% cloud-hosted by GitHub, completely **free for up to 2,000 build minutes/month**, lives inside your `.github/workflows/` directory, and deploys directly to your server on `git push main`.

### 2. Terraform (Infrastructure as Code)
- **Verdict**: **Optional in Phase 6 (Not needed for Phase 1–5).**
- **Why?**:
  - During development (Phase 1–5), all infrastructure runs locally in Docker (`docker-compose.yml`).
  - For initial live launch (Phase 6), manually provisioning a single AWS EC2 instance + S3 bucket takes ~10 minutes and incurs $0 overhead.
  - **When to use Terraform**: If you scale up to multiple auto-scaling EC2 instances and managed AWS RDS databases, a lightweight Terraform script (`main.tf`) can be introduced in Phase 6 to document and automate cloud resource provisioning.

---

## 📊 Master Ticket Matrix & Timeline

| Ticket ID | Title | Phase | Target Timeline | Dependencies | Status |
|---|---|---|---|---|---|
| `IN-1` | Setup Project Architecture & Docker Environment | Phase 1 | Day 1-2 | None | [x] Completed |
| `IN-2` | Custom User Model with Mobile (+91) OTP Auth | Phase 1 | Day 3-4 | `IN-1` | [ ] Pending |
| `IN-3` | Jira & CI/CD Automated Code Quality Pipeline | Phase 1 | Day 5 | `IN-1` | [ ] Pending |
| `IN-4` | Global Design System & INR (`₹`) Tokens | Phase 2 | Day 6-7 | `IN-1` | [ ] Pending |
| `IN-5` | Header with Location Modal & Mobile Nav | Phase 2 | Day 8-9 | `IN-4` | [ ] Pending |
| `IN-6` | Listing Card Grid & Badges | Phase 2 | Day 10-11 | `IN-4` | [ ] Pending |
| `IN-7` | Multi-Format Form & Multi-Image Upload | Phase 3 | Day 12-14 | `IN-2`, `IN-6` | [ ] Pending |
| `IN-8` | Bidding Engine with Anti-Sniping Timer | Phase 3 | Day 15-17 | `IN-7` | [ ] Pending |
| `IN-9` | Free Giveaway ("Daan") Claim Workflow | Phase 3 | Day 18-19 | `IN-7` | [ ] Pending |
| `IN-10` | Indian 6-Digit PIN Code Database Integration | Phase 4 | Day 20-21 | `IN-1` | [ ] Pending |
| `IN-11` | Distance Radius Search Engine | Phase 4 | Day 22-24 | `IN-10`, `IN-7` | [ ] Pending |
| `IN-12` | HTMX Faceted Search & Live Filters | Phase 4 | Day 25-26 | `IN-11` | [ ] Pending |
| `IN-13` | Real-Time Buyer-Seller Listing Chat | Phase 5 | Day 27-29 | `IN-2`, `IN-7` | [ ] Pending |
| `IN-14` | User Trust Rating & Review System | Phase 5 | Day 30-31 | `IN-13` | [ ] Pending |
| `IN-15` | Anti-Scam QR Code Warnings & Safety Banners | Phase 5 | Day 32 | `IN-13` | [ ] Pending |
| `IN-16` | AWS Infrastructure Provisioning (Mumbai) | Phase 6 | Day 33-34 | `IN-1` | [ ] Pending |
| `IN-17` | Nginx Reverse Proxy & Let's Encrypt SSL | Phase 6 | Day 35 | `IN-16` | [ ] Pending |
| `IN-18` | CI/CD Automated Deployment to AWS | Phase 6 | Day 36-37 | `IN-17` | [ ] Pending |
| `IN-19` | Production Security Audit & Launch Checklist | Phase 6 | Day 38 | `IN-18` | [ ] Pending |

---

## 📋 Ticket Specifications & Agent Execution Prompts

### PHASE 1: Infrastructure & Indian Mobile Auth

#### `IN-1`: Setup Project Architecture & Docker Environment
- **Target**: Day 1-2 | **Dependencies**: None
- **Files**: `docker-compose.yml`, `Dockerfile`, `.env.example`, `requirements.txt`
- **Goal**: Establish a multi-container Docker environment (Django 5.0+, PostgreSQL 16, Redis 7, Celery Worker).
- **Verification**: `docker-compose up --build` succeeds; `http://localhost:8000` responds.
- **Agent Prompt**:
  > "Execute ticket IN-1: Configure Docker environment with docker-compose.yml containing Services: web (Django 5), db (PostgreSQL), redis, and celery worker. Ensure requirements.txt includes Django>=5.0, psycopg2-binary, redis, celery, Pillow. Test build clean."

#### `IN-2`: Custom User Model with Mobile (+91) OTP Auth
- **Target**: Day 3-4 | **Dependencies**: `IN-1`
- **Files**: `auctions/models.py`, `auctions/views.py`, `auctions/urls.py`
- **Goal**: Implement phone number authentication for India (+91 format) with 6-digit OTP engine (Console/MSG91 backend).
- **Verification**: `python manage.py test auctions.tests.test_auth`
- **Agent Prompt**:
  > "Execute ticket IN-2: Extend User model in auctions/models.py with phone_number (+91 validator), is_phone_verified, and OTP model. Implement login/signup flow with 6-digit OTP verification. Write unit tests for OTP generation and verification."

#### `IN-3`: Automated Code Quality Pipeline
- **Target**: Day 5 | **Dependencies**: `IN-1`
- **Files**: `.github/workflows/ci.yml`, `.pre-commit-config.yaml`
- **Goal**: Create GitHub Actions CI workflow running flake8, black format check, and Django tests on git push.
- **Verification**: `git commit` triggers pre-commit check clean.
- **Agent Prompt**:
  > "Execute ticket IN-3: Setup GitHub Actions CI workflow in .github/workflows/ci.yml that installs dependencies, runs python manage.py test, and checks code style."

---

### PHASE 2: Responsive Indian UI/UX Design System

#### `IN-4`: Global Design System & INR (`₹`) Tokens
- **Target**: Day 6-7 | **Dependencies**: `IN-1`
- **Files**: `auctions/static/auctions/styles.css`, `auctions/templatetags/indian_numbers.py`
- **Goal**: Create CSS design tokens (glassmorphic dark/light palette, responsive grid) and custom Django template tag for Indian number formatting (`150000` -> `₹ 1,50,000`).
- **Verification**: Template tag test passing `₹ 1,50,000`.
- **Agent Prompt**:
  > "Execute ticket IN-4: Create CSS design system in styles.css with CSS variables for colors, typography, glassmorphism, and responsive break points. Create template filter format_inr to format numbers into Indian Rupee format (e.g. ₹ 1,50,000)."

#### `IN-5`: Header with Location Modal & Mobile Nav
- **Target**: Day 8-9 | **Dependencies**: `IN-4`
- **Files**: `auctions/templates/auctions/layout.html`
- **Goal**: Build mobile-first sticky navigation header with PIN code picker modal, search input, category dropdown, and mobile navigation drawer.
- **Verification**: Visual inspection on 360px mobile view and desktop.
- **Agent Prompt**:
  > "Execute ticket IN-5: Overhaul layout.html with responsive header containing sticky search bar, location PIN selection modal, category drawer, and user profile action buttons."

#### `IN-6`: Listing Card Grid & Badges
- **Target**: Day 10-11 | **Dependencies**: `IN-4`
- **Files**: `auctions/templates/auctions/index.html`
- **Goal**: Create responsive grid displaying listing cards with format badges (`AUCTION`, `ZU VERSCHENKEN`, `NEGOTIABLE`), price in ₹, distance badge, and watchlist heart toggle.
- **Verification**: Responsive grid renders cleanly across screen sizes.
- **Agent Prompt**:
  > "Execute ticket IN-6: Build listing card component with format badges (Auction/Giveaway/Fixed), price display in INR, distance indicator, image carousel preview, and watchlist toggle."

---

### PHASE 3: Core Transaction Engine (Auctions, Classifieds & Giveaways)

#### `IN-7`: Multi-Format Listing Form & Multi-Image Upload
- **Target**: Day 12-14 | **Dependencies**: `IN-2`, `IN-6`
- **Files**: `auctions/models.py`, `auctions/forms.py`, `auctions/views.py`
- **Goal**: Build dynamic listing creation supporting Listing Types (`AUCTION`, `FIXED_PRICE`, `GIVEAWAY`), multiple images with WebP thumbnail compression, and item condition options.
- **Verification**: `python manage.py test auctions.tests.test_listings`
- **Agent Prompt**:
  > "Execute ticket IN-7: Refactor Listing model to support listing_type (AUCTION, FIXED_PRICE, GIVEAWAY), condition, multi-image relation. Build dynamic creation form with client image preview and backend thumbnail processing."

#### `IN-8`: Bidding Engine with Anti-Sniping Timer
- **Target**: Day 15-17 | **Dependencies**: `IN-7`
- **Files**: `auctions/models.py`, `auctions/views.py`
- **Goal**: Build real-time bid validation (min increment in ₹, reserve price) and anti-sniping (auto-extends end time by 3 minutes if bid arrives in final 2 minutes).
- **Verification**: Unit tests covering invalid low bids, reserve price logic, and anti-sniping timer extension.
- **Agent Prompt**:
  > "Execute ticket IN-8: Implement bidding logic with minimum increment validation, current highest bid updates, reserve price checks, and anti-sniping extension (+3 minutes if bid placed in final 2 minutes). Write full unit tests."

#### `IN-9`: Free Giveaway ("Daan / Zu Verschenken") Claim Workflow
- **Target**: Day 18-19 | **Dependencies**: `IN-7`
- **Files**: `auctions/models.py`, `auctions/views.py`
- **Goal**: Build request/claim workflow for items listed as `GIVEAWAY`. Interested users submit pickup request; seller selects recipient and generates pickup handshake PIN.
- **Verification**: Test claim state transitions (`ACTIVE` -> `RESERVED` -> `COMPLETED`).
- **Agent Prompt**:
  > "Execute ticket IN-9: Implement giveaway claim workflow allowing users to request free items. Add seller recipient selection and pickup verification PIN state machine."

---

### PHASE 4: Geo-Location & Faceted Search

#### `IN-10`: 6-Digit Indian PIN Code Database Integration
- **Target**: Day 20-21 | **Dependencies**: `IN-1`
- **Files**: `auctions/models.py`, `auctions/management/commands/load_pincodes.py`
- **Goal**: Import Indian PIN Code database mapping 6-digit PINs to District, City, State, Latitude, and Longitude.
- **Verification**: `python manage.py load_pincodes` populates DB; PIN lookup `560038` returns Indiranagar, Bengaluru.
- **Agent Prompt**:
  > "Execute ticket IN-10: Create PinCode model with pincode, area_name, city, state, lat, lng fields. Write management command to load Indian postal PIN code dataset."

#### `IN-11`: Distance Radius Search Engine
- **Target**: Day 22-24 | **Dependencies**: `IN-10`, `IN-7`
- **Files**: `auctions/utils.py`, `auctions/views.py`
- **Goal**: Implement spatial radius search (Haversine formula / PostGIS) filtering listings within 5km, 15km, 30km, 50km of selected PIN Code.
- **Verification**: Test query searching listings within 10km of Bengaluru PIN code.
- **Agent Prompt**:
  > "Execute ticket IN-11: Build radius search utility using spatial distance calculations to filter listings within X km radius of a specified PIN code."

#### `IN-12`: HTMX Faceted Search & Live Filters
- **Target**: Day 25-26 | **Dependencies**: `IN-11`
- **Files**: `auctions/templates/auctions/index.html`, `auctions/templates/auctions/partials/listing_list.html`
- **Goal**: Implement instant faceted filtering by Category, Price (₹ Min - Max), Format (Auction/Free/Sale), and Radius without full page reloads using HTMX.
- **Verification**: Filter inputs trigger instant DOM swap of listing grid.
- **Agent Prompt**:
  > "Execute ticket IN-12: Add HTMX live filtering for category, price range, listing type, and distance radius with dynamic partial template rendering."

---

### PHASE 5: In-App Buyer-Seller Messaging & Trust System

#### `IN-13`: Real-Time Buyer-Seller Listing Chat
- **Target**: Day 27-29 | **Dependencies**: `IN-2`, `IN-7`
- **Files**: `auctions/models.py`, `auctions/views.py`, `auctions/templates/auctions/chat.html`
- **Goal**: Build listing-anchored chat system between buyer and seller with unread notification counts.
- **Verification**: Message sent by Buyer appears instantly in Seller chat thread.
- **Agent Prompt**:
  > "Execute ticket IN-13: Create ChatThread and ChatMessage models linked to User and Listing. Implement chat UI with unread message badges."

#### `IN-14`: User Trust Rating & Review System
- **Target**: Day 30-31 | **Dependencies**: `IN-13`
- **Files**: `auctions/models.py`, `auctions/views.py`
- **Goal**: Post-transaction review engine (1 to 5 stars + review tags). Display seller trust badge on profile & listings.
- **Verification**: Rating score updates profile average correctly.
- **Agent Prompt**:
  > "Execute ticket IN-14: Implement review system allowing buyer/seller to leave 1-5 star ratings and feedback after transaction. Display average rating and badge on user profile."

#### `IN-15`: Anti-Scam QR Code Warnings & Safety Banners
- **Target**: Day 32 | **Dependencies**: `IN-13`
- **Files**: `auctions/templates/auctions/chat.html`
- **Goal**: Add persistent safety banners in chat window highlighting QR code payment scam warnings and safe meetup recommendations for India.
- **Verification**: Banner rendered visibly on chat screen.
- **Agent Prompt**:
  > "Execute ticket IN-15: Add persistent Indian C2C anti-scam warning banners to chat UI advising users never to scan QR codes to receive money."

---

### PHASE 6: Production DevOps & Cloud Launch (AWS Mumbai)

#### `IN-16`: AWS Infrastructure Provisioning (Mumbai)
- **Target**: Day 33-34 | **Dependencies**: `IN-1`
- **Files**: `infra/aws_setup.sh`, `infra/docker-compose.prod.yml`
- **Goal**: Provision AWS EC2 instance in `ap-south-1` (Mumbai) and S3 bucket for media storage.
- **Verification**: AWS S3 upload test passing.
- **Agent Prompt**:
  > "Execute ticket IN-16: Configure production docker-compose.prod.yml with environment variable secrets and setup S3 storage backend for django-storages."

#### `IN-17`: Nginx Reverse Proxy & Let's Encrypt SSL
- **Target**: Day 35 | **Dependencies**: `IN-16`
- **Files**: `infra/nginx.conf`
- **Goal**: Setup Nginx container as reverse proxy with automated Let's Encrypt SSL certificate renewal (Certbot).
- **Verification**: `https://` domain returns A+ security grade.
- **Agent Prompt**:
  > "Execute ticket IN-17: Create Nginx production configuration with SSL termination, Gzip compression, and security header hardening."

#### `IN-18`: CI/CD Automated Deployment to AWS
- **Target**: Day 36-37 | **Dependencies**: `IN-17`
- **Files**: `.github/workflows/deploy.yml`
- **Goal**: Automate deployment via GitHub Actions: build Docker image, run migrations, and reload zero-downtime containers on push to main.
- **Verification**: `git push origin main` deploys automatically to AWS.
- **Agent Prompt**:
  > "Execute ticket IN-18: Write GitHub Actions deploy workflow to SSH into AWS EC2 instance, pull main branch, execute migrations, and restart containers."

#### `IN-19`: Production Security Audit & Launch Checklist
- **Target**: Day 38 | **Dependencies**: `IN-18`
- **Files**: `commerce/settings.py`
- **Goal**: Enforce production security settings (`SECURE_SSL_REDIRECT`, `CSRF_COOKIE_SECURE`, rate limiting with `django-ratelimit`, Sentry logging).
- **Verification**: Security audit command `python manage.py check --deploy` reports zero warnings.
- **Agent Prompt**:
  > "Execute ticket IN-19: Conduct security audit by setting production settings flags, rate limiting views, and configuring Sentry exception reporting."
