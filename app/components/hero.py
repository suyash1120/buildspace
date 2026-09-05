from fasthtml.common import *


def Hero():
    return Section(
        Div(
            # Top status line
            Div(
                Div(
                    Span(cls="pulse-dot"),
                    Span("Building & Shipping", cls="hero-kicker"),
                    Span("·", cls="hero-kicker-sep"),
                    Span("AI Engineer based in Pune, India", cls="hero-kicker-sub"),
                    cls="hero-kicker-group"
                ),
                Span("Public Portfolio & Systems", cls="hero-index"),
                cls="hero-heading-row",
            ),

            # Main Hero Split: Left Statement + Right Editorial Profile
            Div(
                # Left Column: The Human Statement
                Div(
                    Div(
                        H1(
                            "Building intelligent systems, practical AI tools, and ",
                            Span("crafted web products.", cls="hero-headline-highlight"),
                            cls="hero-headline"
                        ),
                        cls="hero-statement",
                    ),

                    P(
                        "Hi, I'm Suyash Rane — an AI Engineer and full-stack builder with a passion for applied machine learning, "
                        "robust backend architectures, and clean product design. Welcome to my personal workshop.",
                        cls="hero-sub-text",
                    ),

                    Div(
                        A(
                            Span("View Projects"),
                            Span("↓", cls="btn-arrow"),
                            href="#work",
                            cls="hero-cta-primary",
                        ),
                        A(
                            Span("About Me"),
                            Span("→", cls="btn-arrow"),
                            href="#about",
                            cls="hero-cta-secondary",
                        ),
                        A(
                            Span("GitHub"),
                            Span("↗", cls="btn-arrow"),
                            href="https://github.com/suyash1120",
                            target="_blank",
                            cls="hero-cta-ghost",
                        ),
                        cls="hero-actions"
                    ),

                    cls="hero-left",
                ),

                # Right Column: Refined Editorial Profile Card
                Div(
                    Div(
                        # Portrait photo
                        Div(
                            Img(
                                src="/static/images/p2.jpg",
                                alt="Suyash Rane",
                                cls="profile-avatar-img"
                            ),
                            Div(
                                Span(cls="pulse-dot"),
                                Span("Available for opportunities", cls="profile-badge-text"),
                                cls="profile-avatar-badge"
                            ),
                            cls="profile-avatar-frame"
                        ),

                        # Profile Meta
                        Div(
                            Div(
                                H2("Suyash Rane", cls="profile-name"),
                                Span("AI Engineer & Product Builder", cls="profile-role"),
                                cls="profile-title-block"
                            ),

                            P(
                                "Crafting production-ready digital products with Python, FastAPI, FastHTML, and modern AI/RAG models.",
                                cls="profile-description",
                            ),

                            Div(
                                Div(
                                    Span("EDUCATION", cls="profile-mini-label"),
                                    Span("B.E. Computer Engineering (8.25 CGPA)", cls="profile-mini-val"),
                                    cls="profile-mini-item"
                                ),
                                Div(
                                    Span("FOCUS", cls="profile-mini-label"),
                                    Span("Applied AI · Full-Stack · System Design", cls="profile-mini-val"),
                                    cls="profile-mini-item"
                                ),
                                cls="profile-mini-grid"
                            ),

                            cls="profile-body"
                        ),

                        cls="profile-card-inner"
                    ),
                    cls="profile-card",
                ),

                cls="hero-main",
            ),

            # Currently Building / Live Workbench Panel
            Div(
                Div(
                    Div(
                        Span("CURRENT FOCUS", cls="workbench-tag"),
                        Span("·", cls="workbench-sep"),
                        Span("Active Project", cls="workbench-focus"),
                        cls="workbench-tag-group"
                    ),
                    Div(
                        Span(cls="pulse-dot"),
                        Span("Active Development", cls="workbench-status"),
                        cls="workbench-status-pill"
                    ),
                    cls="workbench-header"
                ),

                Div(
                    Div(
                        H3("BuildSpace Ecosystem", cls="workbench-title"),
                        P(
                            "An open-source developer hub and live engineering workshop built with Python, FastHTML, and SQLite. "
                            "Created to document real-world systems, applied AI models, and unfiltered architectural retrospectives.",
                            cls="workbench-desc"
                        ),
                        Div(
                            Span("Python 3.12", cls="workbench-pill"),
                            Span("FastHTML", cls="workbench-pill"),
                            Span("SQLite", cls="workbench-pill"),
                            Span("Modern CSS", cls="workbench-pill"),
                            cls="workbench-stack"
                        ),
                        cls="workbench-left-col"
                    ),

                    Div(
                        Div(
                            Span("Role", cls="wb-stat-label"),
                            Span("Creator & Lead Architect", cls="wb-stat-val"),
                            cls="wb-stat-item"
                        ),
                        Div(
                            Span("Architecture", cls="wb-stat-label"),
                            Span("Zero-Bundle Server-Rendered", cls="wb-stat-val"),
                            cls="wb-stat-item"
                        ),
                        Div(
                            Span("Key Focus", cls="wb-stat-label"),
                            Span("Sub-30ms Global Performance", cls="wb-stat-val stat-green"),
                            cls="wb-stat-item"
                        ),
                        cls="wb-stat-right-col"
                    ),

                    cls="workbench-body"
                ),

                Div(
                    Span("Designed with craft · Documented with transparency", cls="workbench-footer-note"),
                    A(
                        Span("Read BuildSpace Case Study"),
                        Span("→", cls="btn-arrow"),
                        href="/projects/buildspace",
                        cls="workbench-footer-link"
                    ),
                    cls="workbench-footer"
                ),

                cls="workbench-panel",
            ),

            cls="container",
        ),
        cls="hero",
    )