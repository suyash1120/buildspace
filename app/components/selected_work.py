from fasthtml.common import *


def FlagshipProjectCard():
    """Bespoke flagship spotlight card for BuildSpace."""
    return Article(
        # Top status bar
        Div(
            Div(
                Span("Featured Project", cls="flagship-kicker"),
                Span("·", cls="flagship-sep"),
                Span("Open Source Workshop", cls="flagship-index"),
                cls="flagship-badge-group"
            ),
            Div(
                Span(cls="pulse-dot"),
                Span("In Active Development", cls="flagship-status-text"),
                cls="flagship-status-pill"
            ),
            cls="flagship-header"
        ),

        # Main Body: Split Editorial + Architecture
        Div(
            # Left Column: Project Info
            Div(
                H3(
                    "BuildSpace",
                    cls="flagship-title"
                ),
                P(
                    "A personal developer ecosystem and public engineering workshop. "
                    "Engineered to showcase live systems, ongoing software experiments, and transparent architectural retrospectives.",
                    cls="flagship-description"
                ),
                Div(
                    Span("Python 3.12", cls="flagship-tech-tag"),
                    Span("FastHTML", cls="flagship-tech-tag"),
                    Span("SQLite", cls="flagship-tech-tag"),
                    Span("Custom CSS", cls="flagship-tech-tag"),
                    cls="flagship-stack"
                ),
                Div(
                    A(
                        Span("Explore Case Study"),
                        Span("→", cls="btn-arrow"),
                        href="/projects/buildspace",
                        cls="flagship-cta-primary"
                    ),
                    A(
                        Span("About Me"),
                        Span("→", cls="btn-arrow"),
                        href="/#about",
                        cls="flagship-cta-secondary"
                    ),
                    cls="flagship-actions"
                ),
                cls="flagship-col-main"
            ),

            # Right Column: Actual BuildSpace Stack & Architecture
            Div(
                Div(
                    Span("Architecture & Technical Highlights", cls="arch-spec-label"),
                    Div(
                        Div(
                            Span("Framework", cls="arch-stat-key"),
                            Span("FastHTML + Python 3.12", cls="arch-stat-val"),
                            cls="arch-stat-row"
                        ),
                        Div(
                            Span("Interaction", cls="arch-stat-key"),
                            Span("HTMX Asynchronous Components", cls="arch-stat-val"),
                            cls="arch-stat-row"
                        ),
                        Div(
                            Span("Persistence", cls="arch-stat-key"),
                            Span("Embedded SQLite (Messages & Logs)", cls="arch-stat-val"),
                            cls="arch-stat-row"
                        ),
                        Div(
                            Span("Messaging", cls="arch-stat-key"),
                            Span("Direct Email Dispatch Pipeline", cls="arch-stat-val"),
                            cls="arch-stat-row"
                        ),
                        cls="arch-spec-table"
                    ),
                    cls="arch-spec-box"
                ),
                cls="flagship-col-telemetry"
            ),

            cls="flagship-body"
        ),

        cls="flagship-card"
    )


def ProjectCard(
    number,
    slug,
    title,
    tagline,
    description,
    innovation_highlight,
    stack,
    category,
    status="Live",
    year="2026",
    is_active_pulse=False,
):
    return Article(
        Div(
            # Card Top Row: Category, Year & Status
            Div(
                Div(
                    Span(category, cls="card-category"),
                    cls="card-top-left"
                ),
                Div(
                    Div(
                        Span(cls="pulse-dot") if is_active_pulse else None,
                        Span(status, cls="card-status-text"),
                        cls=f"card-status-pill {'card-status-pill-highlight' if is_active_pulse else ''}"
                    ),
                    Span(year, cls="card-year"),
                    cls="card-top-right"
                ),
                cls="card-header"
            ),

            # Card Title & Subtitle
            H3(
                title,
                cls="card-title"
            ),
            P(
                tagline,
                cls="card-tagline"
            ),

            # Innovation highlight callout
            Div(
                Span("Key Highlight:", cls="card-callout-label"),
                Span(f" {innovation_highlight}", cls="card-callout-text"),
                cls="card-callout-box"
            ),

            # Description
            P(
                description,
                cls="card-desc"
            ),

            # Tech Stack Pills
            Div(
                *[
                    Span(item, cls="card-tech-tag")
                    for item in stack
                ],
                cls="card-stack"
            ),

            # Action Footer
            Div(
                A(
                    Span("Read Case Study"),
                    Span("→", cls="card-arrow"),
                    href=f"/projects/{slug}",
                    cls="card-explore-link"
                ),
                cls="card-footer"
            ),

            cls="card-inner"
        ),
        cls="editorial-project-card"
    )


def SelectedWork():
    return Section(
        Div(
            # Section heading
            Div(
                Div(
                    Span(
                        "Selected Work",
                        cls="section-kicker",
                    ),
                    Span(
                        "Featured systems, applied AI tools & software experiments",
                        cls="section-description",
                    ),
                    cls="section-heading-left",
                ),
                Span(
                    "7 Projects",
                    cls="section-index",
                ),
                cls="section-heading",
            ),

            # 1. Flagship Spotlight (01 / BUILDSPACE)
            FlagshipProjectCard(),

            # 2. Grid of Bespoke Editorial Projects (02 - 07)
            Div(
                # 02 / Clipwise
                ProjectCard(
                    "02",
                    "clipwise",
                    "Clipwise",
                    "Full-Stack Learning Platform with Deep Video Transcript Search",
                    "Enables learners to search educational video concepts and immediately jump to exact timestamped explanations.",
                    "Automated YouTube transcript ingestion engine with millisecond-exact seek triggers via HTMX.",
                    [
                        "FastHTML",
                        "Python",
                        "HTMX",
                        "SQLite",
                        "YouTube API",
                    ],
                    "Video SaaS",
                    status="In Development",
                    year="2026",
                    is_active_pulse=True,
                ),

                # 03 / PulseAI
                ProjectCard(
                    "03",
                    "pulseai",
                    "PulseAI",
                    "AI-Powered Knowledge & Document Synthesis Engine",
                    "High-precision document intelligence platform designed to eliminate hallucinations across large technical knowledge bases.",
                    "Hybrid Vector Search (BM25 + Dense Embeddings) with Cross-Encoder Reranking in Qdrant.",
                    [
                        "Python",
                        "FastAPI",
                        "RAG",
                        "Qdrant",
                        "LlamaIndex",
                    ],
                    "AI & RAG Engine",
                    status="In Development",
                    year="2026",
                    is_active_pulse=True,
                ),

                # 04 / BillNest
                ProjectCard(
                    "04",
                    "billnest",
                    "BillNest",
                    "Invoice & Billing Automation Web System for SMBs",
                    "Django web application managing customers, inventory, automatic tax/totals calculation, and payment lifecycles.",
                    "Relational ORM data models with transaction-safe invoice state machines and dynamic form sets.",
                    [
                        "Django",
                        "Python",
                        "SQLite",
                        "JavaScript",
                        "HTML5/CSS3",
                    ],
                    "Fintech Web App",
                    status="In Development",
                    year="2025",
                    is_active_pulse=True,
                ),

                # 05 / HousePrice API
                ProjectCard(
                    "05",
                    "houseprice",
                    "HousePrice API",
                    "Machine Learning Property Valuation API & Streamlit Dashboard",
                    "High-throughput property valuation service with interactive Streamlit UI delivering instant house price predictions based on multidimensional feature vectors.",
                    "FastAPI REST endpoints and Streamlit frontend with Pydantic request verification and in-memory Scikit-Learn regression inference.",
                    [
                        "FastAPI",
                        "Streamlit",
                        "Scikit-Learn",
                        "Pydantic",
                        "Python",
                    ],
                    "ML Service & API",
                    status="Live API",
                    year="2025",
                ),

                # 06 / QueueLess
                ProjectCard(
                    "06",
                    "queueless",
                    "QueueLess",
                    "Smart Real-Time Appointment & Queue Manager for SMBs",
                    "Cross-platform queue application providing merchants with instant wait-time estimates and SMS updates.",
                    "Offline-First SQLite state machine with optimistic updates and client-side runtime.",
                    [
                        "Flet",
                        "Python",
                        "SQLite",
                        "FastAPI",
                        "Twilio API",
                    ],
                    "Mobile & Real-Time",
                    status="Prototype",
                    year="2025",
                ),

                # 07 / TraceKit
                ProjectCard(
                    "07",
                    "tracekit",
                    "TraceKit",
                    "Developer Intelligence & Application Observability Platform",
                    "Ultra-low overhead telemetry collector for tracing latency bottlenecks, slow queries, and distributed exceptions.",
                    "Asynchronous non-blocking UDP telemetry buffer with Redis batching and time-series indexing.",
                    [
                        "Django",
                        "Python",
                        "PostgreSQL",
                        "Redis",
                        "UDP Buffer",
                    ],
                    "Observability & DevTools",
                    status="System Architecture",
                    year="2025",
                ),

                cls="projects-editorial-grid",
            ),

            cls="container",
        ),
        id="work",
        cls="selected-work",
    )