from fasthtml.common import *


def FlagshipProjectCard():
    """Bespoke flagship spotlight card for BuildSpace."""
    return Article(
        # Top status bar
        Div(
            Div(
                Span("01", cls="font-glitch flagship-glitch-num"),
                Span("·", cls="flagship-sep"),
                Span("FLAGSHIP SYSTEM", cls="font-glitch flagship-kicker"),
                Span("·", cls="flagship-sep"),
                Span("Live Workshop", cls="flagship-index"),
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
                Div(
                    H3(
                        "BuildSpace",
                        cls="flagship-title"
                    ),
                    Div("⚡ runs this whole site with 0 client JS frameworks!", cls="sticky-note flagship-sticky-note"),
                    cls="flagship-title-wrap"
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
    hand_note=None,
):
    return Article(
        Div(
            # Card Top Row: Category, Year & Status
            Div(
                Div(
                    Span(number, cls="font-glitch card-number-glitch"),
                    Span("·", cls="card-dot-sep"),
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

            # Handwritten note if present
            Div(
                Span("✍️", cls="card-hand-icon"),
                Span(hand_note, cls="font-hand card-hand-text"),
                cls="card-hand-note"
            ) if hand_note else None,

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
            Div(
                Div(
                    Span(
                        "Selected Work",
                        cls="section-kicker",
                    ),
                    Span(
                        "A few things I've built recently — systems that solve real problems for real people",
                        cls="section-description",
                    ),
                    cls="section-heading-left",
                ),
                Span(
                    "3 Projects",
                    cls="section-index",
                ),
                cls="section-heading",
            ),

            FlagshipProjectCard(),

            Div(
                ProjectCard(
                    "02",
                    "relay",
                    "Relay",
                    "Turns messy team conversations into structured tasks — automatically.",
                    "Relay watches what your team says in chat, listens for promises and deadlines, and quietly turns 'I'll do that by Friday' into actual tracked work — so nothing falls through the cracks.",
                    "Groq-powered task extraction from natural language with a React Native mobile app, FastAPI backend, and full project/workspace/team/assignment lifecycle.",
                    [
                        "React Native",
                        "JavaScript",
                        "FastAPI",
                        "Groq LLM",
                        "Python",
                        "PostgreSQL",
                    ],
                    "AI Team Workflow · Mobile",
                    status="In Active Development",
                    year="2026",
                    is_active_pulse=True,
                    hand_note="finally, a task list that writes itself 🎯",
                ),

                ProjectCard(
                    "03",
                    "houseprice",
                    "HousePrice API",
                    "Machine Learning Property Valuation API & Streamlit Dashboard",
                    "High-throughput property valuation service with an interactive Streamlit UI delivering instant house price predictions based on multidimensional feature vectors.",
                    "FastAPI REST endpoints and Streamlit frontend with Pydantic request verification and in-memory Scikit-Learn regression inference under 10ms.",
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
                    hand_note="instant regression inference via FastAPI 📊",
                ),

                cls="projects-editorial-grid",
            ),

            cls="container",
        ),
        id="work",
        cls="selected-work",
    )