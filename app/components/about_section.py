from fasthtml.common import *


def SkillTag(text):
    return Span(text, cls="skill-tag")


def AchievementItem(text):
    return Li(Span("✓", cls="ach-star"), Span(text, cls="ach-text"), cls="ach-item")


def AboutSection():
    return Section(
        Div(
            Div(
                Div(
                    Span("About", cls="section-kicker"),
                    Span("The person behind the commits — how I build, what I care about, and a few bad jokes", cls="section-description"),
                    cls="section-heading-left",
                ),
                Span("Hey, I'm Suyash 👋", cls="section-index"),
                cls="section-heading",
            ),

            Div(
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
                                Span("Pune, India · GMT+5:30", cls="about-photo-tag"),
                                cls="about-photo-badge"
                            ),
                            Div("caffeine-powered builder ☕", cls="profile-hand-scribble font-hand"),
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

                    Div(
                        Span("Quick Facts", cls="about-side-label"),
                        Div(
                            Div(
                                Div(
                                    Span("🎓", cls="quick-fact-icon"),
                                    Span("Education", cls="quick-fact-label"),
                                    cls="quick-fact-header"
                                ),
                                Span("B.E. Computer Eng · 2022-Present", cls="quick-fact-val"),
                                cls="quick-fact-row"
                            ),
                            Div(
                                Div(
                                    Span("📍", cls="quick-fact-icon"),
                                    Span("Location", cls="quick-fact-label"),
                                    cls="quick-fact-header"
                                ),
                                Span("Pune, India", cls="quick-fact-val"),
                                cls="quick-fact-row"
                            ),
                            Div(
                                Div(
                                    Span("🎯", cls="quick-fact-icon"),
                                    Span("Currently Building", cls="quick-fact-label"),
                                    cls="quick-fact-header"
                                ),
                                Span("Relay · Patch ID · This site", cls="quick-fact-val"),
                                cls="quick-fact-row"
                            ),
                            Div(
                                Div(
                                    Span("🌙", cls="quick-fact-icon"),
                                    Span("Peak Productivity", cls="quick-fact-label"),
                                    cls="quick-fact-header"
                                ),
                                Span("11 PM — 3 AM (sorry, mom)", cls="quick-fact-val"),
                                cls="quick-fact-row"
                            ),
                            cls="quick-facts-card"
                        ),
                        cls="about-edu-section"
                    ),

                    Div(
                        Span("Honors & Stuff", cls="about-side-label"),
                        Ul(
                            AchievementItem("Finalist — COEP Inspiron 4.0 Hackathon '25 (stayed up 36 hours, worth it)"),
                            AchievementItem("Best Innovation Award — SMVITM Hackathon '24"),
                            AchievementItem("Vice-President — ACES (Computer Engg. Students Association)"),
                            cls="ach-list"
                        ),
                        cls="about-ach-section"
                    ),

                    cls="about-col-left"
                ),

                Div(
                    Div(
                        Div(
                            Span("HOW I BUILD THINGS", cls="font-glitch hero-glitch-badge"),
                            Div("ship it. iterate. don't be a perfectionist ⚡", cls="sticky-note"),
                            cls="hero-badge-row"
                        ),
                        H3(
                            "I build software like I cook — ",
                            Span("start simple, taste often, and never skip the garlic.", cls="about-headline-highlight"),
                            cls="about-manifesto-heading"
                        ),
                        P(
                            "Hi! I'm Suyash. I'm the kind of engineer who gets genuinely excited about three things: "
                            "turning messy real-world problems into tidy systems, writing code that my six-months-from-now self "
                            "will still understand, and the moment when a user says 'wait, that just worked?' Like, that's the good stuff.",
                            cls="about-manifesto-tagline"
                        ),
                        P(
                            "I work across the stack — from RAG pipelines that actually answer the question you meant to ask, "
                            "to FastAPI backends that don't fall over when traffic spikes, to React Native apps that feel good in the hand. "
                            "But here's the thing: the tech isn't the point. The point is the human on the other side, trying to get something done.",
                            cls="about-manifesto-tagline"
                        ),
                        P(
                            "Before every line of code I write, I try to ask: would my grandma understand why this exists? "
                            "If the answer is no, I probably need to spend more time with a whiteboard and less time in VS Code.",
                            cls="about-manifesto-tagline"
                        ),
                        cls="about-manifesto-block"
                    ),

                    Div(
                        Span("What I Bring to a Team", cls="about-sub-heading"),
                        Div(
                            Div(
                                Div(
                                    Span("🤝", cls="value-icon"),
                                    Div(
                                        H4("Systems Thinking, Not Just Code", cls="value-title"),
                                        P("I don't just write the function — I ask why the function exists, who it's for, and what breaks when it fails.", cls="value-desc"),
                                        cls="value-text"
                                    ),
                                    cls="value-card"
                                )
                            ),
                            Div(
                                Div(
                                    Span("🧪", cls="value-icon"),
                                    Div(
                                        H4("Bias Toward Shipping", cls="value-title"),
                                        P("A v1 that's in users' hands beats a v0.9 that's perfect on my machine. I prototype fast and iterate honestly.", cls="value-desc"),
                                        cls="value-text"
                                    ),
                                    cls="value-card"
                                )
                            ),
                            Div(
                                Div(
                                    Span("📝", cls="value-icon"),
                                    Div(
                                        H4("Docs Before Deadlines", cls="value-title"),
                                        P("The PR isn't done until the README says why we did it this way. Future-you will thank present-you.", cls="value-desc"),
                                        cls="value-text"
                                    ),
                                    cls="value-card"
                                )
                            ),
                            cls="values-grid"
                        ),
                        cls="about-skills-group"
                    ),

                    Div(
                        Span("Technical Tools I Actually Use", cls="about-sub-heading"),
                        Div(
                            Div(
                                Span("Applied AI & Machine Learning", cls="skill-cat-label"),
                                Div(
                                    SkillTag("RAG"), SkillTag("LLMs"), SkillTag("AI Agents"),
                                    SkillTag("FAISS"), SkillTag("NLP"), SkillTag("Groq"),
                                    SkillTag("Gemini API"), SkillTag("Prompt Engineering"),
                                    SkillTag("Qdrant"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            Div(
                                Span("Languages & Frameworks", cls="skill-cat-label"),
                                Div(
                                    SkillTag("Python"), SkillTag("JavaScript"), SkillTag("FastAPI"),
                                    SkillTag("FastHTML"), SkillTag("React Native"), SkillTag("Next.js"),
                                    SkillTag("Streamlit"), SkillTag("HTMX"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            Div(
                                Span("Mobile & Cross-Platform", cls="skill-cat-label"),
                                Div(
                                    SkillTag("React Native"), SkillTag("Firebase"),
                                    SkillTag("Offline-First SQLite"), SkillTag("REST APIs"),
                                    SkillTag("State Management"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            Div(
                                Span("Databases & Infra", cls="skill-cat-label"),
                                Div(
                                    SkillTag("PostgreSQL"), SkillTag("SQLite"), SkillTag("Redis"),
                                    SkillTag("Docker"), SkillTag("Git/GitHub"),
                                    SkillTag("CI/CD"), SkillTag("Linux"),
                                    cls="skill-tag-group"
                                ),
                                cls="skill-cat-block"
                            ),
                            cls="skills-col-grid"
                        ),
                        cls="about-skills-group"
                    ),

                    Div(
                        Span("Certifications (aka I sat through the videos)", cls="about-sub-heading"),
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
