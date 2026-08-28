from fasthtml.common import *


def ConnectCard(label, link_text, href, icon_arrow="↗", is_primary=False):
    return A(
        Div(
            Span(label, cls="connect-card-label mono"),
            Span(link_text, cls="connect-card-val"),
            cls="connect-card-left"
        ),
        Span(icon_arrow, cls="connect-card-arrow"),
        href=href,
        target="_blank" if not href.startswith("mailto:") else "_self",
        cls=f"connect-card {'connect-card-primary' if is_primary else ''}"
    )


def ConnectSection():
    return Section(
        Div(
            # Section heading
            Div(
                Div(
                    Span("05 / CONNECT", cls="section-kicker mono"),
                    Span("CHANNELS & DIRECT ACCESS", cls="section-description mono"),
                    cls="section-heading-left",
                ),
                Span("OPEN FOR COLLABORATION", cls="section-index mono"),
                cls="section-heading",
            ),

            # Main Connect Grid
            Div(
                # Left side: Editorial invite
                Div(
                    H3(
                        "Let's Build Something Memorable.",
                        cls="connect-title"
                    ),
                    P(
                        "Whether it's discussing applied AI systems, architecting high-performance backends, "
                        "or exploring product design collaborations — my inbox and channels are always open.",
                        cls="connect-tagline"
                    ),
                    Div(
                        Span(cls="pulse-dot"),
                        Span("AVAILABLE FOR INTERNSHIPS & FREELANCE", cls="connect-status-text mono"),
                        cls="connect-status-badge"
                    ),
                    cls="connect-left-col"
                ),

                # Right side: The 4 Connect Channels
                Div(
                    ConnectCard(
                        "01 // SOURCE CODE",
                        "github.com/suyash1120 ↗",
                        "https://github.com/suyash1120",
                        icon_arrow="↗",
                        is_primary=True
                    ),
                    ConnectCard(
                        "02 // PROFESSIONAL NETWORK",
                        "linkedin.com/in/suyash-rane ↗",
                        "https://www.linkedin.com/in/suyash-rane-4aaa84258/",
                        icon_arrow="↗"
                    ),
                    ConnectCard(
                        "03 // DIRECT EMAIL",
                        "ranesuyash2004@gmail.com",
                        "mailto:ranesuyash2004@gmail.com",
                        icon_arrow="→"
                    ),
                    ConnectCard(
                        "04 // TWITTER / X",
                        "@SuyashRane10 ↗",
                        "https://x.com/SuyashRane10",
                        icon_arrow="↗"
                    ),
                    cls="connect-channels-grid"
                ),

                cls="connect-main-grid"
            ),

            cls="container"
        ),
        id="connect",
        cls="connect-section"
    )
