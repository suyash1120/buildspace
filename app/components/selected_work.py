from fasthtml.common import *


def FlagshipProjectCard():
    """Bespoke flagship spotlight card for 01 / BUILDSPACE."""
    return Article(
        # Top status bar
        Div(
            Div(
                Span("★", cls="flagship-star"),
                Span("FLAGSHIP ECOSYSTEM", cls="flagship-kicker mono"),
                Span("·", cls="flagship-sep"),
                Span("01 / WORKBENCH", cls="flagship-index mono"),
                cls="flagship-badge-group"
            ),
            Div(
                Span(cls="pulse-dot"),
                Span("ACTIVE IN WORKSHOP", cls="flagship-status-text mono"),
                cls="flagship-status-pill"
            ),
            cls="flagship-header"
        ),

        # Main Body: Split Editorial + Telemetry Architecture
        Div(
            # Left Column: Project Info
            Div(
                H3(
                    "BUILDSPACE",
                    cls="flagship-title"
                ),
                P(
                    "A personal developer ecosystem and public engineering workshop. "
                    "Engineered to showcase live systems, ongoing software experiments, and unfiltered architectural retrospectives.",
                    cls="flagship-description"
                ),
                Div(
                    Span("PYTHON", cls="flagship-tech-tag mono"),
                    Span("FASTHTML", cls="flagship-tech-tag mono"),
                    Span("SQLITE", cls="flagship-tech-tag mono"),
                    Span("CUSTOM CSS SYSTEM", cls="flagship-tech-tag mono"),
                    cls="flagship-stack"
                ),
                Div(
                    A(
                        Span("EXPLORE CASE STUDY"),
                        Span("↗", cls="btn-arrow"),
                        href="/projects/buildspace",
                        cls="flagship-cta-primary mono"
                    ),
                    A(
                        Span("ABOUT ARCHITECT"),
                        Span("→", cls="btn-arrow"),
                        href="/#about",
                        cls="flagship-cta-secondary mono"
                    ),
                    cls="flagship-actions"
                ),
                cls="flagship-col-main"
            ),

            # Right Column: Actual BuildSpace Stack & Architecture
            Div(
                Div(
                    Span("ECOSYSTEM STACK & ARCHITECTURE", cls="arch-spec-label mono"),
                    Div(
                        Div(
                            Span("FRAMEWORK", cls="arch-stat-key mono"),
                            Span("FastHTML + Python 3.12", cls="arch-stat-val mono"),
                            cls="arch-stat-row"
                        ),
                        Div(
                            Span("INTERACTION", cls="arch-stat-key mono"),
                            Span("HTMX Asynchronous Components", cls="arch-stat-val mono"),
                            cls="arch-stat-row"
                        ),
                        Div(
                            Span("PERSISTENCE", cls="arch-stat-key mono"),
                            Span("Embedded SQLite (Messages & Logs)", cls="arch-stat-val mono"),
                            cls="arch-stat-row"
                        ),
                        Div(
                            Span("MESSAGING", cls="arch-stat-key mono"),
                            Span("Direct Email Inbox Dispatcher", cls="arch-stat-val mono"),
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
    status="LIVE",
    year="2026",
    is_active_pulse=False,
):
    return Article(
        Div(
            # Card Top Row: Index, Category, Year & Status
            Div(
                Div(
                    Span(number, cls="card-number mono"),
                    Span(f"// {category}", cls="card-category mono"),
                    cls="card-top-left"
                ),
                Div(
                    Div(
                        Span(cls="pulse-dot") if is_active_pulse or status in ["ACTIVE", "LIVE", "IN DEVELOPMENT", "PRODUCTION"] else None,
                        Span(status, cls="card-status-text mono"),
                        cls=f"card-status-pill {'card-status-pill-highlight' if is_active_pulse or status in ['IN DEVELOPMENT', 'ACTIVE'] else ''}"
                    ),
                    Span(year, cls="card-year mono"),
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
                Span("CORE SYSTEM //", cls="card-callout-label mono"),
                Span(innovation_highlight, cls="card-callout-text"),
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
                    Span(item, cls="card-tech-tag mono")
                    for item in stack
                ],
                cls="card-stack"
            ),

            # Action Footer
            Div(
                A(
                    Span("EXPLORE CASE STUDY"),
                    Span("↗", cls="card-arrow"),
                    href=f"/projects/{slug}",
                    cls="card-explore-link mono"
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
                        "02 / SELECTED WORK",
                        cls="section-kicker",
                    ),

                    Span(
                        "CURATED SYSTEMS, TOOLS & EXPERIMENTS",
                        cls="section-description",
                    ),

                    cls="section-heading-left",
                ),

                Span(
                    "7 WORKSHOP BUILDS",
                    cls="section-index",
                ),

                cls="section-heading",
            ),

            # 1. Flagship Spotlight (01 / BUILDSPACE)
            FlagshipProjectCard(),

            # 2. Grid of Bespoke Editorial Projects (02 - 07)
            Div(
                # 02 / CLIPWISE
                ProjectCard(
                    "02",
                    "clipwise",
                    "CLIPWISE",
                    "Full-Stack Learning SaaS with Deep Video Transcript Search",
                    "Enables learners to search educational video concepts and immediately jump to exact timestamped explanations.",
                    "Automated YouTube transcript ingestion engine with millisecond-exact seek triggers via HTMX.",
                    [
                        "FASTHTML",
                        "PYTHON",
                        "HTMX",
                        "SQLITE",
                        "YOUTUBE API",
                    ],
                    "SAAS / HYPERMEDIA",
                    status="IN DEVELOPMENT",
                    year="2026",
                    is_active_pulse=True,
                ),

                # 03 / PULSEAI
                ProjectCard(
                    "03",
                    "pulseai",
                    "PULSEAI",
                    "AI-Powered Knowledge & Document Synthesis Engine",
                    "High-precision document intelligence platform designed to eliminate hallucinations across large technical knowledge bases.",
                    "Hybrid Vector Search (BM25 + Dense Embeddings) with Cross-Encoder Reranking in Qdrant.",
                    [
                        "PYTHON",
                        "FASTAPI",
                        "RAG",
                        "QDRANT",
                        "LLAMAINDEX",
                    ],
                    "AI PRODUCT / RAG",
                    status="IN DEVELOPMENT",
                    year="2026",
                    is_active_pulse=True,
                ),

                # 04 / BILLNEST
                ProjectCard(
                    "04",
                    "billnest",
                    "BILLNEST",
                    "Invoice & Billing Automation Web System for SMBs",
                    "Django web application managing customers, inventory, automatic tax/totals calculation, and payment lifecycles.",
                    "Relational ORM data models with transaction-safe invoice state machines and dynamic form sets.",
                    [
                        "DJANGO",
                        "PYTHON",
                        "SQLITE",
                        "JAVASCRIPT",
                        "MVT",
                    ],
                    "WEB APP / FINTECH",
                    status="IN DEVELOPMENT",
                    year="2025",
                    is_active_pulse=True,
                ),

                # 05 / HOUSEPRICE API
                ProjectCard(
                    "05",
                    "houseprice",
                    "HOUSEPRICE API",
                    "Machine Learning Property Valuation API & Streamlit Dashboard",
                    "High-throughput property valuation service with interactive Streamlit UI delivering instant house price predictions based on multidimensional feature vectors.",
                    "FastAPI REST endpoints and Streamlit frontend with Pydantic request verification and in-memory Scikit-Learn regression inference.",
                    [
                        "FASTAPI",
                        "STREAMLIT",
                        "SCIKIT-LEARN",
                        "PYDANTIC",
                        "PYTHON",
                    ],
                    "MACHINE LEARNING / API",
                    status="API SERVICE",
                    year="2025",
                ),


                # 06 / QUEUELESS
                ProjectCard(
                    "06",
                    "queueless",
                    "QUEUELESS",
                    "Smart Real-Time Appointment & Queue Manager for SMBs",
                    "Cross-platform queue application providing merchants with instant wait-time telemetry and SMS updates.",
                    "Offline-First SQLite state machine with optimistic updates and Flutter/Flet client runtime.",
                    [
                        "FLET",
                        "PYTHON",
                        "SQLITE",
                        "FASTAPI",
                        "TWILIO",
                    ],
                    "SYSTEM ARCHITECTURE / MOBILE",
                    status="ARCHITECTURE DESIGN",
                    year="2025",
                ),

                # 07 / TRACEKIT
                ProjectCard(
                    "07",
                    "tracekit",
                    "TRACEKIT",
                    "Developer Intelligence & Application Observability Platform",
                    "Ultra-low overhead telemetry collector for tracing latency bottlenecks, slow queries, and distributed exceptions.",
                    "Asynchronous non-blocking UDP telemetry buffer with Redis batching and time-series indexing.",
                    [
                        "DJANGO",
                        "PYTHON",
                        "POSTGRESQL",
                        "REDIS",
                        "UDP TELEMETRY",
                    ],
                    "SYSTEM ARCHITECTURE / DEV TOOLS",
                    status="ARCHITECTURE LEVEL",
                    year="2025",
                ),

                cls="projects-editorial-grid",
            ),

            cls="container",
        ),
        id="work",
        cls="selected-work",
    )