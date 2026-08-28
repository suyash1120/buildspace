from fasthtml.common import *


def Hero():
    return Section(
        Div(
            # Top status line
            Div(
                Div(
                    Span(cls="pulse-dot"),
                    Span("BUILDING IN PUBLIC", cls="hero-kicker mono"),
                    Span("·", cls="hero-kicker-sep"),
                    Span("OPEN WORKSHOP", cls="hero-kicker-sub mono"),
                    cls="hero-kicker-group"
                ),
                Span("01 / WORKBENCH", cls="hero-index mono"),
                cls="hero-heading-row",
            ),

            # Main Hero Split: Left Statement + Right Editorial Profile
            Div(
                # Left Column: The Big Manifesto
                Div(
                    Div(
                        Div(
                            Span("→", cls="hero-arrow"),
                            Span("I DESIGN.", cls="hero-line-text"),
                            cls="hero-line",
                        ),
                        Div(
                            Span("→", cls="hero-arrow"),
                            Span("I BUILD.", cls="hero-line-text"),
                            cls="hero-line",
                        ),
                        Div(
                            Span("→", cls="hero-arrow"),
                            Span("I SHIP.", cls="hero-line-text"),
                            cls="hero-line",
                        ),
                        cls="hero-statement",
                    ),

                    P(
                        "An open workshop documenting software engineering, applied AI architectures, and interactive digital products built with craft.",
                        cls="hero-sub-text",
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
                                Span("AVAILABLE FOR BUILDS", cls="profile-badge-text mono"),
                                cls="profile-avatar-badge"
                            ),
                            cls="profile-avatar-frame"
                        ),

                        # Profile Meta
                        Div(
                            Div(
                                H2("Suyash Rane", cls="profile-name"),
                                Span("AI ENGINEER / BUILDER", cls="profile-role mono"),
                                cls="profile-title-block"
                            ),

                            P(
                                "Designing and building production digital products, applied AI systems, and developer tools for the modern web.",
                                cls="profile-description",
                            ),

                            Div(
                                A(
                                    Span("ABOUT ME"),
                                    Span("↗", cls="button-arrow"),
                                    href="#about",
                                    cls="profile-btn-primary mono",
                                ),
                                A(
                                    Span("GITHUB"),
                                    Span("↗", cls="button-arrow"),
                                    href="https://github.com/suyash1120",
                                    target="_blank",
                                    cls="profile-btn-ghost mono",
                                ),

                                cls="profile-actions"
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
                        Span("CURRENTLY BUILDING", cls="workbench-tag mono"),
                        Span("·", cls="workbench-sep"),
                        Span("ACTIVE FOCUS", cls="workbench-focus mono"),
                        cls="workbench-tag-group"
                    ),
                    Div(
                        Span(cls="pulse-dot"),
                        Span("SYSTEM ACTIVE", cls="workbench-status mono"),
                        cls="workbench-status-pill"
                    ),
                    cls="workbench-header"
                ),

                Div(
                    Div(
                        H3("BUILDSPACE", cls="workbench-title"),
                        P(
                            "Personal developer ecosystem and live engineering workshop built with Python, FastHTML, and SQLite.",
                            cls="workbench-desc"
                        ),
                        Div(
                            Span("PYTHON", cls="workbench-pill mono"),
                            Span("FASTHTML", cls="workbench-pill mono"),
                            Span("SQLITE", cls="workbench-pill mono"),
                            Span("MODERN CSS", cls="workbench-pill mono"),
                            cls="workbench-stack"
                        ),
                        cls="workbench-left-col"
                    ),

                    Div(
                        Div(
                            Span("STATUS", cls="wb-stat-label mono"),
                            Span("ACTIVE SPRINT", cls="wb-stat-val mono stat-green"),
                            cls="wb-stat-item"
                        ),
                        Div(
                            Span("VERSION", cls="wb-stat-label mono"),
                            Span("0.1.0-alpha", cls="wb-stat-val mono"),
                            cls="wb-stat-item"
                        ),
                        Div(
                            Span("ARCHITECTURE", cls="wb-stat-label mono"),
                            Span("HYPERMEDIA SSR", cls="wb-stat-val mono"),
                            cls="wb-stat-item"
                        ),
                        cls="workbench-right-col"
                    ),

                    cls="workbench-body"
                ),

                Div(
                    Span("LAST COMMITTED: TODAY · ZERO CLIENT JAVASCRIPT BUNDLE", cls="workbench-footer-note mono"),
                    A(
                        Span("EXPLORE BLUEPRINT"),
                        Span("↗", cls="btn-arrow"),
                        href="/projects/buildspace",
                        cls="workbench-footer-link mono"
                    ),
                    cls="workbench-footer"
                ),

                cls="workbench-panel",
            ),

            cls="container",
        ),
        cls="hero",
    )
