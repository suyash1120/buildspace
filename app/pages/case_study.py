from fasthtml.common import *

from app.components.navbar import Navbar
from app.components.footer import SiteFooter
from app.components.chat_widget import ChatWidget



# Case study data repository
CASE_STUDIES = {
    "buildspace": {
        "number": "01",
        "title": "BUILDSPACE",
        "subtitle": "Personal developer ecosystem, live workshop & engineering log.",
        "category": "ECOSYSTEM / WEB",
        "year": "2026",
        "status": "ACTIVE WORKSHOP",
        "role": "Lead Architect & Designer",
        "demo_url": "/",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Standard portfolio templates look generic, static, and disconnected from the real engineering process. "
            "They fail to showcase ongoing builds, architectural decision-making, and the organic evolution of software."
        ),
        "idea": (
            "Build a living developer workshop. Instead of treating work as polished relics, BuildSpace treats engineering "
            "as a continuous discipline: pairing an industrial editorial aesthetic with a live build log and deep case studies."
        ),
        "architecture_summary": (
            "Built with Python and FastHTML, delivering server-rendered HTML components without client JavaScript bloat. "
            "SQLite powers data persistence for logs and telemetry, wrapped in a pure custom CSS design system."
        ),
        "architecture_diagram": """[ Browser Client ]
        │  (HTMX / Semantic HTML5)
        ▼
[ FastHTML + ASGI App Router ]
        │
   ┌────┴────────────────────────┐
   ▼                             ▼
[ Component Engine ]     [ SQLite Data Store ]
(Hero, Cards, Logs)     (build_logs, projects)""",
        "tech_stack": [
            ("Python 3.12", "Core runtime and server logic"),
            ("FastHTML", "Hypermedia-first component rendering"),
            ("SQLite", "Embedded zero-config database"),
            ("Custom CSS", "Zero-dependency bespoke design system"),
        ],
        "learnings": (
            "Hypermedia-driven architecture dramatically simplifies frontend development when built with high-craft CSS. "
            "Server components remove state synchronization headaches while keeping page load speeds virtually instantaneous."
        )
    },
    "pulseai": {
        "number": "02",
        "title": "PULSEAI",
        "subtitle": "AI-powered knowledge assistant for searching and understanding complex documents.",
        "category": "AI PRODUCT / RAG",
        "year": "2026",
        "status": "IN DEVELOPMENT",
        "role": "AI Engineer",
        "demo_url": "#",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Developers and researchers struggle to synthesize information across hundreds of technical PDFs and repos. "
            "Traditional LLM context windows suffer from hallucinations and needle-in-a-haystack retrieval drop-offs."
        ),
        "idea": (
            "A high-precision RAG pipeline combining dense vector embeddings with sparse keyword search (BM25) and "
            "cross-encoder reranking to ensure precise, cited, and trustworthy answer generation."
        ),
        "architecture_summary": (
            "Asynchronous document ingestion parses PDFs into contextual semantic chunks. "
            "Queries are routed through a hybrid search retrieval layer in Qdrant before reaching Claude/GPT-4 for synthesis."
        ),
        "architecture_diagram": """[ User Document (PDF/MD) ] ──▶ [ Chunking & Tokenizer ]
                                      │
                                      ▼
                               [ Embedding Model ]
                                      │
                                      ▼
                        [ Qdrant Hybrid Vector Store ]
                                      │
[ Query Engine ] ──▶ [ BM25 + Vector ] ──▶ [ Cross-Encoder Reranker ] ──▶ [ LLM Answer + Citations ]""",
        "tech_stack": [
            ("Python / FastAPI", "High-throughput async backend"),
            ("Qdrant", "Vector database with filtering"),
            ("LlamaIndex", "RAG orchestrator & document pipelines"),
            ("Sentence-Transformers", "Local embedding generation"),
        ],
        "learnings": (
            "Reranking after initial hybrid retrieval improves retrieval accuracy by over 35%. "
            "Chunk size strategy is significantly more critical to response quality than model parameter size."
        )
    },
    "clipwise": {
        "number": "03",
        "title": "CLIPWISE",
        "subtitle": "Full-stack learning SaaS for search & instant timestamp jumping within video transcripts.",
        "category": "SAAS / HYPERMEDIA",
        "year": "2026",
        "status": "IN DEVELOPMENT",
        "role": "Product Builder & Architect",
        "demo_url": "#",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Learners waste countless minutes scrubbing through hour-long educational videos and lecture series "
            "trying to find the exact 2-minute explanation of a specific sub-topic, formula, or concept."
        ),
        "idea": (
            "A hypermedia learning platform that ingests full video transcripts, indexes timestamped concept segments, "
            "and allows users to search topics (e.g. 'Python decorators') and jump directly to the exact timestamp in the video."
        ),
        "architecture_summary": (
            "Built with FastHTML and HTMX for zero-build hypermedia reactivity. Python orchestrates YouTube API "
            "video discovery and transcript retrieval. Structured timestamp indexes are persisted in SQLite for instant querying."
        ),
        "architecture_diagram": """[ User Search: 'Python Decorators' ]
              │
              ▼
    [ FastHTML + HTMX App ]
              │
    ┌─────────┴─────────┐
    ▼                   ▼
[ YouTube Data API ]   [ Transcript Ingestion Engine ]
(Video Discovery)      (Segment & Timestamp Parsing)
    │                   │
    └─────────┬─────────┘
              ▼
    [ SQLite / FTS Index ]
    (02:14 What decorators are)
    (05:47 Creating your first decorator)
    (11:32 Practical example)
              │
              ▼
[ Interactive Video Player + Auto-Seek to Timestamp ]""",
        "tech_stack": [
            ("FastHTML & Python", "Hypermedia web application framework"),
            ("HTMX", "Dynamic live search & timestamp jumping without React bloat"),
            ("SQLite / SQLModel", "Embedded high-speed database layer"),
            ("YouTube Data API", "Automated video discovery & transcript ingestion"),
            ("Text/Semantic Search", "Segment indexing with exact millisecond offsets"),
        ],
        "learnings": (
            "Hypermedia with HTMX eliminates state synchronization overhead when coordinating external video player timecodes. "
            "Granular transcript chunking transforms passive video watching into a searchable interactive textbook."
        )
    },
    "queueless": {
        "number": "04",
        "title": "QUEUELESS",
        "subtitle": "Smart appointment and real-time queue management platform for SMBs.",
        "category": "SYSTEM ARCHITECTURE / MOBILE",
        "year": "2025",
        "status": "ARCHITECTURE DESIGN",
        "role": "Full-Stack Engineer",
        "demo_url": "#",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Small service businesses waste dozens of hours managing walk-ins and appointment cancellations with pen-and-paper "
            "or bloated enterprise software that costs thousands."
        ),
        "idea": (
            "A cross-platform mobile and desktop queue application that gives customers live queue wait times via SMS/QR codes "
            "while providing shop owners with a one-tap management dashboard."
        ),
        "architecture_summary": (
            "Cross-platform client architecture designed with Python Flet (Flutter engine), communicating with a FastAPI backend. "
            "Includes local SQLite caching for seamless offline walk-in creation during network drops."
        ),
        "architecture_diagram": """[ Merchant Device (Flet) ] ──▶ [ Local SQLite Cache ]
              │                               ▲
              ▼                               │
      [ FastAPI Backend ] ◀───────── [ Sync Worker ]
              │
              ▼
   [ Twilio SMS / Live Web QR ]""",
        "tech_stack": [
            ("Python Flet", "Flutter-powered desktop & mobile UI"),
            ("FastAPI", "RESTful API and webhook handlers"),
            ("SQLite & SQLAlchemy", "Local offline-first database"),
            ("Twilio API", "Automated SMS queue updates"),
        ],
        "learnings": (
            "Building offline-first queues required optimistic UI updates and conflict resolution algorithms. "
            "Simplicity of merchant UX was the single highest determinant of business adoption."
        )
    },
    "tracekit": {
        "number": "05",
        "title": "TRACEKIT",
        "subtitle": "Developer intelligence platform for monitoring, debugging, and tracing application bottlenecks.",
        "category": "SYSTEM ARCHITECTURE / DEV TOOLS",
        "year": "2025",
        "status": "ARCHITECTURE LEVEL",
        "role": "Systems Engineer",
        "demo_url": "#",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Modern microservice architectures generate noisy log streams that make pinpointing 99th-percentile latency spikes "
            "tedious and difficult for small engineering teams."
        ),
        "idea": (
            "A lightweight telemetry collector and visual span inspector that automatically instruments Python endpoints "
            "and highlights slowest SQL queries and unhandled downstream exceptions."
        ),
        "architecture_summary": (
            "Python middleware captures span timings with nanosecond precision and asynchronously batches traces via Redis queues "
            "into PostgreSQL for real-time visualization."
        ),
        "architecture_diagram": """[ Client App Middleware ] ──▶ [ Async UDP/HTTP Batcher ]
                                         │
                                         ▼
                                   [ Redis Queue ]
                                         │
                                         ▼
                                  [ Trace Ingestor ]
                                         │
                                         ▼
                               [ PostgreSQL / Timescale ]
                                         │
                                [ Inspector Dashboard ]""",
        "tech_stack": [
            ("Django / Python", "Core dashboard and analytics platform"),
            ("Redis", "High-throughput trace message buffer"),
            ("PostgreSQL", "Time-series span storage"),
            ("Tailwind / Alpine.js", "Live stream UI visualization"),
        ],
        "learnings": (
            "In-process instrumentation overhead must remain under 1ms to be viable for production workloads. "
            "Batching telemetry over UDP completely eliminated blocking request latency."
        )
    },
    "billnest": {
        "number": "06",
        "title": "BILLNEST",
        "subtitle": "Invoice & billing automation web application for small businesses.",
        "category": "WEB APPLICATION / FINTECH",
        "year": "2025",
        "status": "IN DEVELOPMENT",
        "role": "Backend Developer",
        "demo_url": "#",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Small businesses struggle with disorganized billing records, manual calculation errors, "
            "and lack of payment status visibility for pending client invoices."
        ),
        "idea": (
            "A structured Django web application providing customer and inventory management, dynamic invoice creation "
            "with automatic totals, tax calculations, and a clear payment status state machine."
        ),
        "architecture_summary": (
            "Built using Django's MVT pattern with clean relational database models linking Customers, Products, Invoices, "
            "and Line Items. Includes transactional integrity, robust form validation, and instant status updates."
        ),
        "architecture_diagram": """[ Customer Management ] ──┐
                          ▼
[ Product Catalog ] ────▶ [ Invoice Builder ] ──▶ [ Calculation Engine ]
                                │                    (Tax, Subtotal, Grand Total)
                                ▼
                     [ Payment State Machine ]
                     (DRAFT → SENT → PAID / OVERDUE)""",
        "tech_stack": [
            ("Django & Python", "MVT architecture, ORM models, forms & authentication"),
            ("SQLite / PostgreSQL", "Relational database with transactional consistency"),
            ("Django Templates", "Dynamic invoice rendering & export-ready layouts"),
            ("JavaScript", "Dynamic invoice line item calculations & client-side validation"),
        ],
        "learnings": (
            "Strict database foreign-key relationships and invoice status state machines prevent data corruption "
            "when modifying historical product prices or updating client records."
        )
    },
    "houseprice": {
        "number": "07",
        "title": "HOUSEPRICE API",
        "subtitle": "Machine learning property valuation API & interactive Streamlit dashboard.",
        "category": "MACHINE LEARNING / API",
        "year": "2025",
        "status": "API SERVICE",
        "role": "ML & Backend Engineer",
        "demo_url": "#",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Real estate platforms and home buyers need instant, reliable property valuation estimates via interactive interfaces and clean APIs "
            "without requiring heavy client-side computation or unvalidated inputs."
        ),
        "idea": (
            "A high-performance FastAPI microservice coupled with a reactive Streamlit UI that accepts property feature vectors (location, area, bedrooms, "
            "bathrooms, age) and outputs instant house price estimates using a trained machine learning model."
        ),
        "architecture_summary": (
            "Built with FastAPI and Pydantic for strict request/response data validation, paired with a Streamlit interface for live interactive predictions. "
            "Pre-trained Scikit-Learn regression models are loaded into memory on server startup for sub-10ms predictions."
        ),
        "architecture_diagram": """[ User Streamlit UI / REST Client ]
              │
              ▼
[ FastAPI + Pydantic Validator ]
(Schema & Type Verification)
              │
              ▼
[ Feature Transformer Pipeline ]
(Encoding & Scaling)
              │
              ▼
[ Scikit-Learn Valuation Model ]
              │
              ▼
[ Predicted Price Response (<10ms) ]""",
        "tech_stack": [
            ("FastAPI", "High-performance async REST API framework"),
            ("Streamlit", "Interactive data science & prediction dashboard UI"),
            ("Pydantic", "Strict request & response schema validation"),
            ("Scikit-Learn", "Regression model training, serialization & inference"),
            ("Python & Uvicorn", "Lightweight ASGI server runtime"),
        ],
        "learnings": (
            "Decoupling schema validation with Pydantic from model inference prevents invalid payloads from crashing "
            "the prediction pipeline and guarantees consistent JSON error contracts."
        )
    }

}


def CaseStudyPage(slug):
    data = CASE_STUDIES.get(slug, CASE_STUDIES["buildspace"])
    total_projects = len(CASE_STUDIES)
    
    return (
        Title(f"{data['title']} — Case Study | Suyash Rane"),
        Navbar(active_page="projects"),
        Main(
            # Hero Header
            Section(
                Div(
                    # Navigation Breadcrumb
                    Div(
                        A("← BACK TO WORKSHOP", href="/#work", cls="back-link mono"),
                        Span(f"PROJECT {data['number']} / 0{total_projects}", cls="case-study-badge mono"),
                        cls="case-study-nav"
                    ),

                    H1(data["title"], cls="case-study-title"),
                    P(data["subtitle"], cls="case-study-tagline"),

                    # Metadata Grid
                    Div(
                        Div(
                            Span("CATEGORY", cls="case-meta-label mono"),
                            Span(data["category"], cls="case-meta-value"),
                            cls="case-meta-item"
                        ),
                        Div(
                            Span("YEAR", cls="case-meta-label mono"),
                            Span(data["year"], cls="case-meta-value mono"),
                            cls="case-meta-item"
                        ),
                        Div(
                            Span("STATUS", cls="case-meta-label mono"),
                            Span(data["status"], cls="case-meta-value mono"),
                            cls="case-meta-item"
                        ),
                        Div(
                            Span("ROLE", cls="case-meta-label mono"),
                            Span(data["role"], cls="case-meta-value"),
                            cls="case-meta-item"
                        ),
                        cls="case-study-meta-grid"
                    ),

                    # Action Buttons
                    Div(
                        A(
                            Span("LIVE DEMO"),
                            Span("→", cls="btn-arrow"),
                            href=data["demo_url"],
                            target="_blank" if data["demo_url"] != "/" else "_self",
                            cls="case-btn-primary mono"
                        ) if data["demo_url"] != "#" else None,
                        A(
                            Span("GITHUB REPOSITORY"),
                            Span("↗", cls="btn-arrow"),
                            href=data["github_url"],
                            target="_blank",
                            cls="case-btn-secondary mono"
                        ),
                        cls="case-study-actions"
                    ),

                    cls="container"
                ),
                cls="case-study-hero"
            ),

            # Main Deep-Dive Content
            Section(
                Div(
                    # Section 1: Problem
                    Div(
                        Div(
                            Span("01", cls="case-section-num mono"),
                            H2("The Problem", cls="case-section-title"),
                            cls="case-section-heading"
                        ),
                        Div(
                            P(data["problem"]),
                            cls="case-prose"
                        ),
                        cls="case-section-block"
                    ),

                    # Section 2: The Idea
                    Div(
                        Div(
                            Span("02", cls="case-section-num mono"),
                            H2("The Idea & Solution", cls="case-section-title"),
                            cls="case-section-heading"
                        ),
                        Div(
                            P(data["idea"]),
                            cls="case-prose"
                        ),
                        cls="case-section-block"
                    ),

                    # Section 3: Architecture
                    Div(
                        Div(
                            Span("03", cls="case-section-num mono"),
                            H2("How I Built It & Architecture", cls="case-section-title"),
                            cls="case-section-heading"
                        ),
                        Div(
                            P(data["architecture_summary"]),
                            Div(
                                Span("SYSTEM TOPOLOGY", cls="arch-card-title mono"),
                                Pre(data["architecture_diagram"], cls="arch-code-snippet"),
                                cls="arch-card"
                            ),
                            cls="case-prose"
                        ),
                        cls="case-section-block"
                    ),

                    # Section 4: Tech Stack
                    Div(
                        Div(
                            Span("04", cls="case-section-num mono"),
                            H2("Tech Stack & Rationale", cls="case-section-title"),
                            cls="case-section-heading"
                        ),
                        Div(
                            Div(
                                *[
                                    Div(
                                        Span("●", cls="tech-bullet"),
                                        Span(f"{tech}: {desc}"),
                                        cls="tech-card-pill"
                                    )
                                    for tech, desc in data["tech_stack"]
                                ],
                                cls="tech-grid"
                            ),
                            cls="case-prose"
                        ),
                        cls="case-section-block"
                    ),

                    # Section 5: What I Learned
                    Div(
                        Div(
                            Span("05", cls="case-section-num mono"),
                            H2("Key Retrospectives & What I Learned", cls="case-section-title"),
                            cls="case-section-heading"
                        ),
                        Div(
                            P(data["learnings"]),
                            cls="case-prose"
                        ),
                        cls="case-section-block"
                    ),

                    cls="container"
                ),
                cls="case-study-content"
            ),
        ),
        ChatWidget(),
        SiteFooter()
    )

