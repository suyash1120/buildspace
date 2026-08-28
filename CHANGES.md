# 🧱 BUILDSPACE — Architecture & Changelog Blueprint

> **Personal Developer Ecosystem & Open Engineering Workshop**  
> **Author:** Suyash Rane  
> **Email:** `ranesuyash2004@gmail.com`  
> **GitHub:** `https://github.com/suyash1120`  
> **LinkedIn:** `https://www.linkedin.com/in/suyash-rane-4aaa84258/`  
> **X / Twitter:** `https://x.com/SuyashRane10`  
> **Tech Stack:** Python 3.12 · FastHTML · SQLite · HTMX · Custom Design System

---

## 🏛️ BuildSpace Core Architecture & Sitemap

```
BUILDSPACE
│
├── 🧭 1. NAVIGATION (Sticky Frosted Glass)
│   ├── Brand: BUILDSPACE · SUYASH RANE
│   ├── Anchors: WORK (#work) · EXPERIENCE (#experience) · ABOUT (#about) · CONNECT (#connect)
│   └── Live Telemetry Pill: ● ONLINE / 2026
│
├── ⚡ 2. 01 / WORKBENCH (Hero Section)
│   ├── Core Manifesto: → I DESIGN. → I BUILD. → I SHIP.
│   ├── Portrait Identity Card (p2.jpg full-frame portrait, bio, social CTAs)
│   └── Currently Building Panel (Real stack: Python, FastHTML, SQLite, Modern CSS)
│
├── 🛠️ 3. 02 / SELECTED WORK (Curated Workshop Catalog)
│   ├── 01 / BUILDSPACE (Flagship Blueprint Showcase Card)
│   ├── 02 / CLIPWISE (Video Transcript Timestamp Search SaaS — In Development)
│   ├── 03 / PULSEAI (Hybrid Vector RAG Engine — In Development)
│   ├── 04 / BILLNEST (Django Invoice & Billing Automation — In Development)
│   ├── 05 / HOUSEPRICE API (FastAPI ML Valuation & Streamlit Dashboard — API Service)
│   ├── 06 / QUEUELESS (Real-Time Queue Management — Architecture Design)
│   └── 07 / TRACEKIT (Developer Observability Platform — Architecture Level)
│
├── ⏳ 4. 03 / EXPERIENCE (Work History & System Builds)
│   ├── 01 / Patch ID — Developer Intern (Event-Driven Arch, Data Pipelines, AI, GitHub)
│   ├── 02 / Voltup — AI Engineering Intern (RAG Chatbot, Groq LLM, FAISS, FastAPI, Streamlit)
│   ├── 03 / Mask Polymers — Frontend Dev Intern (React, Kaizen FMS, CI/CD, Data Viz)
│   └── 04 / Prepway Solutions — Python & Data Science Intern (ML, NumPy/Pandas, Prompt Eng)
│
├── 👨‍💻 5. 04 / ABOUT (Manifesto, Education & Credentials)
│   ├── Left Column: Sticky Portrait ID Card + NMIET Computer Engineering (CGPA 8.25) + Hackathon Awards
│   ├── Right Column: Manifesto (I DESIGN. I BUILD. I LEARN.)
│   ├── Technical Toolbox (Categorized: AI/ML, Languages/Frameworks, Tools/Infrastructure)
│   └── Certifications (Prompt Engineering, Python Basics, SQL Basics)
│
├── 🌐 6. 05 / CONNECT (Direct Communication Channels)
│   ├── 01 // Source Code (GitHub Profile: suyash1120) ↗
│   ├── 02 // Professional Network (LinkedIn) ↗
│   ├── 03 // Direct Inquiries (Email: ranesuyash2004@gmail.com) →
│   └── 04 // Twitter / X (@SuyashRane10) ↗
│
├── 💬 7. INTERACTIVE CHAT WIDGET (Live Terminal Messenger)
│   ├── Floating trigger button with live pulse radar
│   ├── HTMX asynchronous form submission (No page reloads)
│   └── Dual delivery: SQLite storage (`chat_messages.db`) + Direct Email Dispatch
│
└── 🌑 8. SITE FOOTER
    ├── Navigation Links (Workshop, Selected Work, Experience, About, Connect)
    ├── Deep-Dive Case Studies List (01 through 07)
    └── Social & Direct Channels
```

---

## 📋 Comprehensive Changelog & Milestones

### 🚀 Milestone 1: Live Interactive Chat Widget & Email Dispatcher
* **Floating Messenger UI (`app/components/chat_widget.py`)**:
  * Added floating trigger button (`💬 SEND MESSAGE · ●`) with radar pulse animation.
  * Sleek terminal drawer with dark surface styling, status bar, and close button.
  * Inputs for Name, Email, and Message with instant client validation.
* **Asynchronous HTMX Integration**:
  * Configured `hx-post="/api/send-message"` with targeted inner-HTML swap.
  * Animated success receipt card displayed directly inside the chat window.
* **Dual Persistence & Live Forwarding (`app/services/email_service.py`)**:
  * **Local Database Storage**: Automatically logs all incoming messages into SQLite (`chat_messages.db`).
  * **Live Email Delivery**: Multi-gateway dispatch via **Web3Forms**, **Formspree**, **Resend**, or **Gmail SMTP** straight to `ranesuyash2004@gmail.com`.
  * Integrated `python-dotenv` for zero-configuration environment variable loading.

---

### 🛠️ Milestone 2: Catalog Expansion & Case Studies (7 Projects)
Expanded Selected Work catalog to 7 projects with bespoke case studies at `/projects/{slug}`:
1. **`01 / BUILDSPACE`** (Flagship Ecosystem)
   * *Stack*: Python 3.12 · FastHTML · SQLite · Custom CSS.
   * Replaced synthetic telemetry with authentic ecosystem specifications.
2. **`02 / CLIPWISE`** (Full-Stack Learning SaaS)
   * *Concept*: Video transcript concept search with instant millisecond timestamp seeking.
   * *Stack*: FastHTML · Python · HTMX · SQLite · YouTube Data API.
   * *Status*: `IN DEVELOPMENT` (with active radar pulse badge).
3. **`03 / PULSEAI`** (Knowledge & Document Synthesis Engine)
   * *Concept*: Hybrid Vector Search (BM25 + Dense Embeddings) with Cross-Encoder Reranking in Qdrant.
   * *Stack*: Python · FastAPI · RAG · Qdrant · LlamaIndex.
   * *Status*: `IN DEVELOPMENT`.
4. **`04 / BILLNEST`** (Invoice & Billing Automation System)
   * *Concept*: Django web application managing inventory, automatic totals calculation, and payment lifecycles.
   * *Stack*: Django · Python · SQLite · JavaScript · MVT.
   * *Status*: `IN DEVELOPMENT`.
5. **`05 / HOUSEPRICE API`** (Machine Learning Property Valuation Service)
   * *Concept*: High-throughput valuation REST API with interactive Streamlit UI and in-memory Scikit-Learn inference.
   * *Stack*: FastAPI · Streamlit · Scikit-Learn · Pydantic · Python.
   * *Status*: `API SERVICE`.
6. **`06 / QUEUELESS`** (Smart Real-Time Queue & Appointment Manager)
   * *Concept*: Offline-first SQLite state machine with Flutter/Flet client runtime and Twilio SMS telemetry.
   * *Stack*: Flet · Python · SQLite · FastAPI · Twilio.
   * *Status*: `ARCHITECTURE DESIGN`.
7. **`07 / TRACEKIT`** (Developer Intelligence & Observability Platform)
   * *Concept*: Ultra-low overhead telemetry collector with non-blocking UDP batching and Redis time-series indexing.
   * *Stack*: Django · Python · PostgreSQL · Redis · UDP Telemetry.
   * *Status*: `ARCHITECTURE LEVEL`.

---

### ⏳ Milestone 3: Experience Section Overhaul
* **Editorial Dark-Accented Timeline (`app/components/experience_section.py`)**:
  * Visual vertical gradient rail with circular sequence nodes (`01`, `02`, `03`, `04`).
  * High-contrast typography on crisp `#FFFFFF` cards with subtle shadow and border hover highlights.
  * Pulsing `● CURRENT ROLE` status badge for active positions.
* **Curated Resume Experience History**:
  * **Patch ID** *(Developer Intern — Jul 2026–Present)*: Event-driven system architecture, data pipelines, AI workflows, decoupled service communication, GitHub workflows.
  * **Voltup** *(AI Engineering Intern — Sep 2025–Mar 2026)*: Production RAG chatbot with Groq LLM, FAISS, FastAPI, Streamlit, Next.js PWA dashboards.
  * **Mask Polymers Pvt. Ltd.** *(Frontend Dev Intern — Jan 2025–May 2025)*: React components, Kaizen File Management System, real-time data viz dashboards, CI/CD (GitHub/Netlify).
  * **Prepway Solutions** *(Python & Data Science Intern — Dec 2024–Feb 2025)*: Predictive ML models, NumPy/Pandas, EDA, feature engineering, Prompt Engineering.

---

### 👨‍💻 Milestone 4: About Section & Credentials
* **Magazine Layout (`app/components/about_section.py`)**:
  * **Sticky Portrait ID Card**: Integrated `p2.jpg` full-frame photo, location badge, role, and direct social links.
  * **Education Card**: PCET's Nutan Maharashtra Institute of Engineering & Technology (B.E. Computer Engineering, 2022–Present, CGPA: 8.25).
  * **Achievements List**: COEP Inspiron 4.0 Hackathon Finalist, SMVITM Best Innovation Award, ACES Vice-President.
  * **Technical Toolbox**: Categorized skill pills (AI/ML, Languages/Frameworks, Tools/Infrastructure).
  * **Certifications**: Prompt Engineering (Udemy), Python Basics (HackerRank), SQL Basics (HackerRank).

---

### 🎨 Milestone 5: UI Polishing & Spacing Rhythm
* **Section Numbering Synchronized**:
  * `01 / WORKBENCH` → `02 / SELECTED WORK` → `03 / EXPERIENCE` → `04 / ABOUT` → `05 / CONNECT`.
* **Tightened Vertical Cadence**:
  * Replaced oversized 80px–120px section padding with an editorial rhythm (`44px–48px` top, `52px–56px` bottom).
  * Removed dead margin between Connect section and Site Footer (`margin-top: 0`).
  * Optimized grid gaps (`24px` on desktop, `20px` on tablet/mobile).
* **Cross-Browser & Console Compatibility**:
  * Sanitized console logging for Windows `cp1252` encoding safety.
  * Removed footer button from Selected Work section as requested.
