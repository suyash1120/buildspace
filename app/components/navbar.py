from fasthtml.common import *


def Navbar(active_page="home"):
    return Header(
        Div(
            A(
                Span("BUILDSPACE", cls="nav-brand-title"),
                Span("·", cls="nav-brand-dot"),
                Span("WORKSHOP", cls="nav-brand-sub"),
                href="/",
                cls="nav-logo"
            ),

            Nav(
                A("WORK", href="/#work", cls=f"nav-link {'active' if active_page == 'projects' else ''}"),
                A("EXPERIENCE", href="/#experience", cls="nav-link"),
                A("ABOUT", href="/#about", cls=f"nav-link {'active' if active_page == 'about' else ''}"),
                A("CONNECT", href="/#connect", cls="nav-link"),
                cls="nav-links"
            ),

            Div(
                Span(cls="pulse-dot"),
                Span("ONLINE", cls="nav-status-label"),
                Span("/", cls="nav-divider"),
                Span("2026", cls="nav-year"),
                cls="nav-meta"
            ),

            cls="nav-inner"
        ),
        cls="site-nav"
    )
