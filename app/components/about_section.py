from fasthtml.common import *


def SkillTag(text):
    return Span(text, cls="skill-tag")


def AchievementItem(text):
    return Li(Span("✓", cls="ach-star"), Span(text, cls="ach-text"), cls="ach-item")


def AboutSection():
    return Section(
        Div(
            # Section header
            Div(
                Div(
                    Span("About", cls="section-kicker"),
                    Span("Background, engineering philosophy & skills", cls="section-description"),
                    cls="section-heading-left",
                ),
                Span("Suyash Rane", cls="section-index"),
                cls="section-heading",
            ),


            # Main Layout: Left Portrait + Right Content
            Div(
                # ─── LEFT COLUMN: Portrait Identity Card ─────────────────────
                Div(
                    Div(
                        Div(
                            Img(
                                src="/static/images/p2.jpg",
                                alt="Suyash Rane",
                                cls="about-photo-img"
                            ),
                            Div(
                                Span(cls="pulse-dot"),
                                Span("Based in Pune, India", cls="about-photo-tag"),
                                cls="about-photo-badge"
                            ),
                            cls="about-photo-frame"
                        ),

                        Div(
                            H3("Suyash Rane", cls="about-id-name"),
                            Span("AI Engineer & Product Builder", cls="about-id-role"),
                            P(
                                "B.E. Computer Engineering · NMIET Pune (CGPA 8.25)",
                                cls="about-id-edu"
                            ),
                            Div(
                                A("ranesuyash2004@gmail.com", href="mailto:ranesuyash2004@gmail.com", cls="about-id-link"),
                                A("github.com/suyash1120 ↗", href="https://github.com/suyash1120", target="_blank", cls="about-id-link"),
                                A("LinkedIn ↗", href="https://www.linkedin.com/in/suyash-rane-4aaa84258/", target="_blank", cls="about-id-link"),
                                cls="about-id-links"
                            ),
                            cls="about-id-body"
                        ),

                        cls="about-id-card"
                    ),

                    # Education Card
                    Div(
                        Span("Education", cls="about-side-label"),
                        Div(
                            Div(
                                Span("B.E. in Computer Engineering", cls="edu-degree"),
                                P("PCET's Nutan Maharashtra Institute of Engineering & Technology", cls="edu-school"),
                                Div(
                                    Span("2022 – Present", cls="edu-year"),
                                    Span("·", cls="edu-sep"),
                                    Span("CGPA: 8.25", cls="edu-cgpa"),
                                    cls="edu-meta"
                                ),
                                cls="edu-block"
                            ),
                            cls="about-edu-card"
                        ),
                        cls="about-edu-section"
                    ),

                    # Achievements
                    Div(
                        Span("Honors & Leadership", cls="about-side-label"),
                        Ul(
                            AchievementItem("Finalist – COEP Inspiron 4.0 Hackathon 2025"),
                            AchievementItem("Best Innovation Award – SMVITM Hackathon 2024"),
                            AchievementItem("Vice-President – ACES (Computer Engineering Students)"),
                            cls="ach-list"
                        ),
                        cls="about-ach-section"
                    ),

                    cls="about-col-left"
                ),

                # ─── RIGHT COLUMN: Story + Skills + Certs ────────────────
                Div(
                    # Story / Bio
                    Div(
                        H3(
                            "Turning complex technical problems into ",
                            Span("clean, practical software.", cls="about-headline-highlight"),
                            cls="about-manifesto-heading"
                        ),
                        P(
                            "I'm an engineer passionate about building end-to-end systems that deliver tangible value. "
                            "My focus spans applied machine learning and RAG architectures, high-performance web backends, "
                            "and crafting interactive interfaces with modern web standards.",
                            cls="about-manifesto-tagline"
                        ),
                        P(
                            "Whether architecting decoupled event-driven microservices at my internships or building "
                            "interactive video-learning engines, I care deeply about clean code, system reliability, and product craft.",
                            cls="about-manifesto-tagline"
                        ),
                        cls="about-manifesto-block"
                    ),

                    # Technical Skills
                    Div(
                        Span("Technical Skills", cls="about-sub-heading"),
                        Div(
                            Div(
                                Span("Applied AI & Machine Learning", cls="skill-cat-label"),
                                Div(
                                    SkillTag("RAG"), SkillTag("LLMs"), SkillTag("AI Agents"),
                                    SkillTag("FAISS"), SkillTag("NLP"), SkillTag("Groq"),
                                    SkillTag("Gemini API"), SkillTag("Prompt Engineering"),
                                    SkillTag("Knowledge Graphs"), SkillTag("Qdrant"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            Div(
                                Span("Languages & Frameworks", cls="skill-cat-label"),
                                Div(
                                    SkillTag("Python"), SkillTag("FastAPI"), SkillTag("FastHTML"),
                                    SkillTag("Next.js"), SkillTag("React"), SkillTag("Streamlit"),
                                    SkillTag("Django"), SkillTag("JavaScript"), SkillTag("HTMX"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            Div(
                                Span("Databases & Infrastructure", cls="skill-cat-label"),
                                Div(
                                    SkillTag("PostgreSQL"), SkillTag("SQLite"), SkillTag("Redis"),
                                    SkillTag("REST APIs"), SkillTag("Docker"), SkillTag("Git/GitHub"),
                                    SkillTag("CI/CD"), SkillTag("Postman"), SkillTag("Linux"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            cls="skills-col-grid"
                        ),
                        cls="about-skills-group"
                    ),

                    # Certifications
                    Div(
                        Span("Certifications", cls="about-sub-heading"),
                        Div(
                            Div(
                                Span("Prompt Engineering", cls="cert-title"),
                                Span("Udemy", cls="cert-issuer"),
                                cls="cert-item"
                            ),
                            Div(
                                Span("Python Certification", cls="cert-title"),
                                Span("HackerRank", cls="cert-issuer"),
                                cls="cert-item"
                            ),
                            Div(
                                Span("SQL Certification", cls="cert-title"),
                                Span("HackerRank", cls="cert-issuer"),
                                cls="cert-item"
                            ),
                            cls="cert-grid"
                        ),
                        cls="about-certs-group"
                    ),

                    cls="about-col-right"
                ),

                cls="about-layout-grid"
            ),

            cls="container"
        ),
        id="about",
        cls="about-section"
    )
