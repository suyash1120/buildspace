from fasthtml.common import *


def ExpBadge(text, is_current=False):
    if is_current:
        return Div(
            Span(cls="exp-pulse-dot"),
            Span(text, cls="exp-badge-text"),
            cls="exp-badge exp-badge-current"
        )
    return Div(
        Span(text, cls="exp-badge-text"),
        cls="exp-badge"
    )


def BulletPoint(text):
    return Li(
        Span("•", cls="exp-bullet-bullet"),
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
    tags=None,
    hand_note=None
):
    return Article(
        Div(
            # Left timeline node / index indicator
            Div(
                Span(f"{num:02d}", cls="exp-index-chip font-glitch"),
                cls="exp-node-col"
            ),

            # Main Card Content
            Div(
                # Card Top Bar / Header
                Div(
                    Div(
                        H3(company, cls="exp-company"),
                        ExpBadge("Current Role" if is_current else period.split("–")[0].strip(), is_current=is_current),
                        cls="exp-title-row"
                    ),
                    Div(
                        Span(role, cls="exp-role-title"),
                        Span("·", cls="exp-meta-dot"),
                        Span(period, cls="exp-period"),
                        Span("·", cls="exp-meta-dot"),
                        Span(location, cls="exp-location"),
                        cls="exp-meta-row"
                    ),
                    cls="exp-card-header"
                ),

                # Optional handwritten builder note
                Div(
                    Span("✏️", cls="card-hand-icon"),
                    Span(hand_note, cls="font-hand card-hand-text"),
                    cls="card-hand-note"
                ) if hand_note else None,

                # Bullet points
                Ul(
                    *[BulletPoint(b) for b in (bullets or [])],
                    cls="exp-bullets"
                ),

                # Tech tags footer
                Div(
                    Span("Technologies & Tools:", cls="exp-tags-label"),
                    Div(
                        *[Span(t, cls="exp-tag") for t in (tags or [])],
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
            Div(
                Div(
                    Span("Experience", cls="section-kicker"),
                    Span("Real teams, real problems, real systems I had the privilege to build", cls="section-description"),
                    cls="section-heading-left",
                ),
                Span("4 Chapters", cls="section-index"),
                cls="section-heading",
            ),

            Div(
                Div(
                    Div(
                        Span("🌱", cls="exp-intro-icon"),
                        Div(
                            P(
                                "Every internship started the same way — walking in with a notebook full of questions, "
                                "and walking out with lessons no textbook could teach. Below isn't just a resume timeline; "
                                "it's where I learned that the best code isn't clever — it's the code your future self understands.",
                                cls="exp-intro-quote font-hand"
                            ),
                            cls="exp-intro-text"
                        ),
                        cls="exp-intro-card"
                    ),
                    cls="exp-intro-wrap"
                ),

                ExperienceCard(
                    num=1,
                    company="Patch ID",
                    role="Developer Intern",
                    period="Jul 2026 – Present",
                    location="Remote · Worldwide",
                    is_current=True,
                    hand_note="learning to sketch systems before writing a single line 📐",
                    bullets=[
                        "Spent the first two weeks doing nothing but drawing boxes and arrows on a whiteboard — turns out, the team that debates architecture together ships faster.",
                        "Designed event-driven pipelines for trust and membership modules where every state change (approved, flagged, expired) triggers the right downstream action at exactly the right time.",
                        "Turns out, the word 'ownership' isn't just a buzzword — each service owns its own data, talks through clean contracts, and nobody's poking around in another service's tables.",
                        "Wrote the kind of documentation I wish I'd inherited — diagrams first, prose second, code third.",
                    ],
                    tags=["Event-Driven Architecture", "System Design", "Data Pipelines", "AI Workflows", "GitHub", "Distributed Systems"],
                ),

                ExperienceCard(
                    num=2,
                    company="Voltup",
                    role="AI Engineering Intern",
                    period="Sep 2025 – Mar 2026",
                    location="Onsite · Pune, India",
                    is_current=False,
                    hand_note="my first time watching real users chat with something I built 💛",
                    bullets=[
                        "Shipped a production RAG chatbot to actual paying customers — nothing quite humbles you like watching your first prod bug pop up in a user demo at 9 AM.",
                        "Groq LLM + FAISS vector search went from 'theoretical speed' to 'wow that actually responds before I finish typing' in a few weeks of iteration.",
                        "Built the FastAPI backend and a snappy Next.js dashboard side-by-side — learned that API contracts written in pencil save a lot of rework.",
                        "Optimized SQL queries until the dashboard loaded in under 800ms with 10k+ rows; slow UIs don't get used, no matter how smart the backend is.",
                    ],
                    tags=["RAG", "Groq LLM", "FAISS", "FastAPI", "Streamlit", "Next.js", "NLP", "PostgreSQL"],
                ),

                ExperienceCard(
                    num=3,
                    company="Mask Polymers Pvt. Ltd.",
                    role="Frontend Development Intern",
                    period="Jan 2025 – May 2025",
                    location="Onsite · Pune, India",
                    is_current=False,
                    hand_note="factory floors taught me more about UX than Figma ever could 🏭",
                    bullets=[
                        "Sat on a plastic chair in the manufacturing plant for a week shadowing the QA team before writing a single component — their workflows, not my assumptions, became the spec.",
                        "Built a reusable React component library for the Kaizen File Management System — role-based access, workflow approvals, and the kind of error messages that actually tell a human what went wrong.",
                        "Designed analytics dashboards that the plant manager actually opened every morning — not because they were pretty, but because they answered the three questions he actually cared about.",
                        "Set up CI/CD on GitHub + Netlify and cried happy tears the first time a deploy finished without me holding my breath.",
                    ],
                    tags=["React", "CI/CD", "GitHub", "Netlify", "Data Visualization", "Role-Based Access", "Enterprise UX"],
                ),

                ExperienceCard(
                    num=4,
                    company="Prepway Solutions",
                    role="Python & Data Science Intern",
                    period="Dec 2024 – Feb 2025",
                    location="Remote · My bedroom desk, actually",
                    is_current=False,
                    hand_note="my first ML model that didn't just overfit on iris data 🌸",
                    bullets=[
                        "Dove into NumPy & Pandas and learned the hard way that 80% of data science is staring at histograms and wondering why the outliers exist.",
                        "Built end-to-end preprocessing pipelines, did more EDA than I thought humanly possible, and discovered that feature engineering isn't alchemy — it's mostly stubbornness.",
                        "Trained ML models for predictive analytics and had the humbling experience of watching my first model score 98% accuracy on the training set and 60% in the wild.",
                        "Experimented with prompt engineering until prompts went from 'write me a thing' to precise 3-part recipes — specificity really is everything with LLMs.",
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
