from fasthtml.common import *


def SkillTag(text):
    return Span(text, cls="skill-tag mono")


def AchievementItem(text):
    return Li(Span("★", cls="ach-star"), Span(text, cls="ach-text"), cls="ach-item")


def AboutSection():
    return Section(
        Div(
            # Section header
            Div(
                Div(
                    Span("04 / ABOUT", cls="section-kicker mono"),
                    Span("ENGINEER · BUILDER · LEARNER", cls="section-description mono"),
                    cls="section-heading-left",
                ),
                Span("SUYASH RANE", cls="section-index mono"),
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
                                Span("PUNE, INDIA · REMOTE READY", cls="about-photo-tag mono"),
                                cls="about-photo-badge"
                            ),
                            cls="about-photo-frame"
                        ),

                        Div(
                            H3("Suyash Rane", cls="about-id-name"),
                            Span("AI ENGINEER / PRODUCT BUILDER", cls="about-id-role mono"),
                            P(
                                "B.E. Computer Engineering · NMIET Pune · CGPA 8.25",
                                cls="about-id-edu mono"
                            ),
                            Div(
                                A("ranesuyash2004@gmail.com", href="mailto:ranesuyash2004@gmail.com", cls="about-id-link mono"),
                                A("github.com/suyash1120", href="https://github.com/suyash1120", target="_blank", cls="about-id-link mono"),
                                A("LinkedIn ↗", href="https://www.linkedin.com/in/suyash-rane-4aaa84258/", target="_blank", cls="about-id-link mono"),
                                cls="about-id-links"
                            ),
                            cls="about-id-body"
                        ),

                        cls="about-id-card"
                    ),

                    # Education Card
                    Div(
                        Span("EDUCATION", cls="about-side-label mono"),
                        Div(
                            Div(
                                Span("B.E. COMPUTER ENGINEERING", cls="edu-degree mono"),
                                P("PCET's Nutan Maharashtra Institute of Engineering & Technology", cls="edu-school"),
                                Div(
                                    Span("2022 – PRESENT", cls="edu-year mono"),
                                    Span("·", cls="edu-sep"),
                                    Span("CGPA: 8.25", cls="edu-cgpa mono"),
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
                        Span("ACHIEVEMENTS", cls="about-side-label mono"),
                        Ul(
                            AchievementItem("Finalist – COEP Inspiron 4.0 Hackathon 2025"),
                            AchievementItem("Best Innovation Award – SMVITM Hackathon 2024"),
                            AchievementItem("Vice-President – ACES"),
                            cls="ach-list"
                        ),
                        cls="about-ach-section"
                    ),

                    cls="about-col-left"
                ),

                # ─── RIGHT COLUMN: Manifesto + Skills + Certs ────────────────
                Div(
                    # Manifesto
                    Div(
                        H3(
                            Span("I DESIGN.", cls="about-manifesto-line"),
                            Span("I BUILD.", cls="about-manifesto-line"),
                            Span("I LEARN.", cls="about-manifesto-line"),
                            cls="about-manifesto-heading"
                        ),
                        P(
                            "A developer building production AI systems, backend infrastructure, and "
                            "editorial web products. Focused on Python, RAG pipelines, hypermedia "
                            "architectures, and crafting interfaces that feel deliberate.",
                            cls="about-manifesto-tagline"
                        ),
                        cls="about-manifesto-block"
                    ),

                    # Technical Skills
                    Div(
                        Span("TECHNICAL SKILLS", cls="about-sub-heading mono"),
                        Div(
                            Div(
                                Span("AI / ML", cls="skill-cat-label mono"),
                                Div(
                                    SkillTag("RAG"), SkillTag("LLMs"), SkillTag("AI Agents"),
                                    SkillTag("FAISS"), SkillTag("NLP"), SkillTag("Groq LLM"),
                                    SkillTag("Gemini API"), SkillTag("Prompt Engineering"),
                                    SkillTag("Knowledge Graphs"), SkillTag("Generative AI"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            Div(
                                Span("LANGUAGES & FRAMEWORKS", cls="skill-cat-label mono"),
                                Div(
                                    SkillTag("Python"), SkillTag("FastAPI"), SkillTag("FastHTML"),
                                    SkillTag("Next.js"), SkillTag("React"), SkillTag("React Native"),
                                    SkillTag("Streamlit"), SkillTag("Django"), SkillTag("JavaScript"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            Div(
                                Span("TOOLS & INFRASTRUCTURE", cls="skill-cat-label mono"),
                                Div(
                                    SkillTag("REST APIs"), SkillTag("SQL"), SkillTag("GitHub"),
                                    SkillTag("Netlify"), SkillTag("Postman"), SkillTag("Figma"),
                                    SkillTag("SQLite"), SkillTag("PostgreSQL"), SkillTag("Docker"),
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
                        Span("CERTIFICATIONS", cls="about-sub-heading mono"),
                        Div(
                            Div(
                                Span("PROMPT ENGINEERING", cls="cert-title mono"),
                                Span("Udemy", cls="cert-issuer"),
                                cls="cert-item"
                            ),
                            Div(
                                Span("PYTHON BASICS", cls="cert-title mono"),
                                Span("HackerRank", cls="cert-issuer"),
                                cls="cert-item"
                            ),
                            Div(
                                Span("SQL BASICS", cls="cert-title mono"),
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
