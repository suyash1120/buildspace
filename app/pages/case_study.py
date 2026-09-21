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
    "relay": {
        "number": "02",
        "title": "RELAY",
        "subtitle": "Small-team task extraction AI — turns messy chat into structured work, automatically.",
        "category": "AI PRODUCT · MOBILE + API",
        "year": "2026",
        "status": "IN ACTIVE DEVELOPMENT",
        "role": "Founder · Full-Stack & AI Engineer",
        "demo_url": "#",
        "github_url": "https://github.com/suyash1120",
        "problem": (
            "Every small team (2–10 people) has been there. Someone writes in the group chat: "
            "\"Let's launch Friday. Rahul handles backend, Sarah does the landing page, and I need to review analytics.\" "
            "Then Friday comes, and half of it didn't happen because nobody turned that chat into actual tasks. "
            "Important work gets buried in Slack/Teams/Discord messages faster than you can say \"can you send me that again?\""
        ),
        "idea": (
            "Relay sits where your team already talks, quietly listens for action items, deadlines, and ownership — "
            "then turns those throwaway sentences into a real task board. Capture text → AI understands → team reviews → "
            "tasks created with assignees and due dates → team executes. No more manually turning conversations into Jira tickets."
        ),
        "architecture_summary": (
            "A React Native cross-platform mobile app (iOS + Android) pairs with a FastAPI backend that orchestrates "
            "Groq LLM for ultra-fast structured task extraction. Authentication, workspaces, projects, team members, "
            "tasks, assignments, due dates, status tracking, and a project dashboard — all with a PostgreSQL relational core."
        ),
        "architecture_diagram": """[ React Native Mobile App ]
     │  (JavaScript · iOS/Android)
     ▼
[ FastAPI Backend Service ]
     │
     ├──────────────────────────────────┐
     ▼                                  ▼
[ Auth & Workspace Mgmt ]      [ Groq LLM Pipeline ]
     │                            │
     │                   ┌────────┴──────────┐
     │                   ▼                   ▼
     │            [ Task Extractor ]  [ Review Queue ]
     │                   │
     └───────────────────┘
                 ▼
       [ PostgreSQL Database ]
  (workspaces, projects, users,
   tasks, assignments, statuses)
                 │
                 ▼
       [ Project Dashboard UI ]
  (Kanban view · Status · Due dates)""",
        "tech_stack": [
            ("React Native + JavaScript", "Cross-platform mobile app (iOS & Android) with native feel"),
            ("FastAPI + Python", "Async high-throughput backend with Pydantic contracts"),
            ("Groq LLM", "Ultra-low-latency inference for natural language → structured task extraction"),
            ("PostgreSQL", "Relational data model: workspaces → projects → tasks → assignments"),
            ("MVP Feature: Sign up/Login", "Authentication and per-workspace access control"),
            ("MVP Feature: Full Task Lifecycle", "Paste text → AI extract → review → assign → due date → status → dashboard"),
        ],
        "learnings": (
            "The difference between a useful AI tool and a gimmick is the review step. "
            "Relay never creates tasks silently — it always shows humans what it thinks it heard and lets them adjust before anything lands in the project. "
            "That single loop turns 'this AI is annoying' into 'this AI just saved me 20 minutes of copy-pasting.'"
        )
    },
    "houseprice": {
        "number": "03",
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
                        A("← Back to Projects", href="/#work", cls="back-link"),
                        Span(f"Project {data['number']} of 0{total_projects}", cls="case-study-badge"),
                        cls="case-study-nav"
                    ),

                    H1(data["title"], cls="case-study-title"),
                    P(data["subtitle"], cls="case-study-tagline"),

                    # Metadata Grid
                    Div(
                        Div(
                            Span("Category", cls="case-meta-label"),
                            Span(data["category"], cls="case-meta-value"),
                            cls="case-meta-item"
                        ),
                        Div(
                            Span("Year", cls="case-meta-label"),
                            Span(data["year"], cls="case-meta-value"),
                            cls="case-meta-item"
                        ),
                        Div(
                            Span("Status", cls="case-meta-label"),
                            Span(data["status"], cls="case-meta-value"),
                            cls="case-meta-item"
                        ),
                        Div(
                            Span("Role", cls="case-meta-label"),
                            Span(data["role"], cls="case-meta-value"),
                            cls="case-meta-item"
                        ),
                        cls="case-study-meta-grid"
                    ),

                    # Action Buttons
                    Div(
                        A(
                            Span("Live Demo"),
                            Span("→", cls="btn-arrow"),
                            href=data["demo_url"],
                            target="_blank" if data["demo_url"] != "/" else "_self",
                            cls="case-btn-primary"
                        ) if data["demo_url"] != "#" else None,
                        A(
                            Span("GitHub Repository"),
                            Span("↗", cls="btn-arrow"),
                            href=data["github_url"],
                            target="_blank",
                            cls="case-btn-secondary"
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

