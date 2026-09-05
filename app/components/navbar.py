from fasthtml.common import *


def Navbar(active_page="home"):
    return Header(
        Div(
            A(
                Span("Suyash Rane", cls="nav-brand-title"),
                Span("·", cls="nav-brand-dot"),
                Span("BuildSpace", cls="nav-brand-sub"),
                href="/",
                cls="nav-logo"
            ),

            Nav(
                A("Projects", href="/#work", cls=f"nav-link {'active' if active_page == 'projects' else ''}"),
                A("Experience", href="/#experience", cls="nav-link"),
                A("About", href="/#about", cls=f"nav-link {'active' if active_page == 'about' else ''}"),
                A("Contact", href="/#connect", cls="nav-link"),
                cls="nav-links"
            ),

            Div(
                Span(cls="pulse-dot"),
                Span("Available for opportunities", cls="nav-status-label"),
                cls="nav-meta"
            ),

            cls="nav-inner"
        ),
        cls="site-nav"
    )
