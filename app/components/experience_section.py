from fasthtml.common import *


def ExpBadge(text, is_current=False):
    if is_current:
        return Div(
            Span(cls="exp-pulse-dot"),
            Span(text, cls="exp-badge-text mono"),
            cls="exp-badge exp-badge-current"
        )
    return Div(
        Span(text, cls="exp-badge-text mono"),
        cls="exp-badge"
    )


def BulletPoint(text):
    return Li(
        Span("→", cls="exp-bullet-arrow mono"),
        Span(text, cls="exp-bullet-text"),
        cls="exp-bullet"
    )


def ExperienceCard(
    num,
    company,
    role,
    period,
    location,
    is_current=False,
    bullets=None,
    tags=None
):
    return Article(
        Div(
            # Left timeline node / index indicator
            Div(
                Span(f"0{num}", cls="exp-index-chip mono"),
                cls="exp-node-col"
            ),

            # Main Card Content
            Div(
                # Card Top Bar / Header
                Div(
                    Div(
                        H3(company, cls="exp-company"),
                        ExpBadge("CURRENT ROLE" if is_current else period.split("–")[0].strip().upper(), is_current=is_current),
                        cls="exp-title-row"
                    ),
                    Div(
                        Span(role, cls="exp-role-title mono"),
                        Span("·", cls="exp-meta-dot"),
                        Span(period, cls="exp-period mono"),
                        Span("·", cls="exp-meta-dot"),
                        Span(location, cls="exp-location mono"),
                        cls="exp-meta-row"
                    ),
                    cls="exp-card-header"
                ),

                # Bullet points
                Ul(
                    *[BulletPoint(b) for b in (bullets or [])],
                    cls="exp-bullets"
                ),

                # Tech tags footer
                Div(
                    Span("STACK & PRACTICES //", cls="exp-tags-label mono"),
                    Div(
                        *[Span(t, cls="exp-tag mono") for t in (tags or [])],
                        cls="exp-tags-list"
                    ),
                    cls="exp-card-footer"
                ) if tags else None,

                cls="exp-card-content"
            ),

            cls=f"exp-card-layout {'exp-card-current' if is_current else ''}"
        ),
        cls="exp-card"
    )


def ExperienceSection():
    return Section(
        Div(
            # Section heading
            Div(
                Div(
                    Span("03 / EXPERIENCE", cls="section-kicker mono"),
                    Span("WORK HISTORY & SYSTEM BUILDS", cls="section-description mono"),
                    cls="section-heading-left",
                ),
                Span("4 ROLES · 2024–PRESENT", cls="section-index mono"),
                cls="section-heading",
            ),


            # Timeline list
            Div(
                ExperienceCard(
                    num=1,
                    company="Patch ID",
                    role="Developer Intern",
                    period="Jul 2026 – Present",
                    location="Remote",
                    is_current=True,
                    bullets=[
                        "Designed an event-driven system architecture and data pipelines for user trust/membership modules, integrating AI workflows with automated lifecycle state transitions.",
                        "Architected reliable decoupled service communication, enforced per-service data ownership, and managed continuous team collaboration via GitHub.",
                        "Created detailed system diagrams and architectural documentation to communicate design decisions across the team prior to development.",
                    ],
                    tags=["Event-Driven Architecture", "System Design", "Data Pipelines", "AI", "GitHub", "Distributed Systems"],
                ),


                ExperienceCard(
                    num=2,
                    company="Voltup",
                    role="AI Engineering Intern",
                    period="Sep 2025 – Mar 2026",
                    location="Onsite, Pune",
                    is_current=False,
                    bullets=[
                        "Built production-ready RAG chatbot using Groq LLM, FAISS, FastAPI & Streamlit — deployed on live SaaS platform with real user traffic.",
                        "Engineered vector search & NLP retrieval pipelines; built REST APIs and responsive PWA dashboards using Next.js with optimized SQL queries.",
                    ],
                    tags=["RAG", "Groq LLM", "FAISS", "FastAPI", "Streamlit", "Next.js", "NLP", "PostgreSQL"],
                ),

                ExperienceCard(
                    num=3,
                    company="Mask Polymers Pvt. Ltd.",
                    role="Frontend Development Intern",
                    period="Jan 2025 – May 2025",
                    location="Onsite, Pune",
                    is_current=False,
                    bullets=[
                        "Built reusable React components for an enterprise Kaizen File Management System with role-based access and workflow tracking.",
                        "Designed data visualization dashboards for real-time monitoring and managed automated CI/CD pipelines via GitHub and Netlify.",
                    ],
                    tags=["React", "CI/CD", "GitHub", "Netlify", "Data Visualization", "Role-Based Access"],
                ),

                ExperienceCard(
                    num=4,
                    company="Prepway Solutions",
                    role="Python & Data Science Intern",
                    period="Dec 2024 – Feb 2025",
                    location="Remote",
                    is_current=False,
                    bullets=[
                        "Built Machine Learning models for predictive analytics using NumPy & Pandas; performed end-to-end data preprocessing, EDA, and feature engineering.",
                        "Applied advanced Prompt Engineering techniques to optimize LLM output quality for domain-specific use cases.",
                    ],
                    tags=["Python", "Machine Learning", "NumPy", "Pandas", "EDA", "Prompt Engineering", "LLMs"],
                ),

                cls="exp-timeline"
            ),

            cls="container"
        ),
        id="experience",
        cls="experience-section"
    )
