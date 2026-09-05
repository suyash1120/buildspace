from fasthtml.common import *


def SiteFooter():
    return Footer(
        Div(
            Div(
                # Left Brand Column
                Div(
                    Div(
                        Span("Suyash Rane", cls="footer-brand-title"),
                        Span("·", cls="footer-brand-sep"),
                        Span("BuildSpace", cls="footer-brand-author"),
                        cls="footer-brand"
                    ),
                    P(
                        "An open workshop documenting software engineering, applied AI architectures, and interactive digital products.",
                        cls="footer-tagline"
                    ),
                    Div(
                        Span(cls="pulse-dot"),
                        Span("Available for opportunities · Remote & Pune", cls="footer-status-text"),
                        cls="footer-status-badge"
                    ),
                    cls="footer-col-main"
                ),

                # Navigation Column
                Div(
                    Span("Navigation", cls="footer-col-title"),
                    Ul(
                        Li(A("Home", href="/")),
                        Li(A("Projects", href="/#work")),
                        Li(A("Experience", href="/#experience")),
                        Li(A("About Me", href="/#about")),
                        Li(A("Contact", href="/#connect")),
                        cls="footer-links-list"
                    ),
                    cls="footer-col"
                ),

                # Projects Column
                Div(
                    Span("Case Studies", cls="footer-col-title"),
                    Ul(
                        Li(A("BuildSpace", href="/projects/buildspace")),
                        Li(A("Clipwise", href="/projects/clipwise")),
                        Li(A("PulseAI", href="/projects/pulseai")),
                        Li(A("BillNest", href="/projects/billnest")),
                        Li(A("HousePrice API", href="/projects/houseprice")),
                        Li(A("QueueLess", href="/projects/queueless")),
                        Li(A("TraceKit", href="/projects/tracekit")),
                        cls="footer-links-list"
                    ),
                    cls="footer-col"
                ),


                # Connect Column
                Div(
                    Span("Connect", cls="footer-col-title"),
                    Ul(
                        Li(A("GitHub ↗", href="https://github.com/suyash1120", target="_blank")),
                        Li(A("LinkedIn ↗", href="https://www.linkedin.com/in/suyash-rane-4aaa84258/", target="_blank")),
                        Li(A("X / Twitter ↗", href="https://x.com/SuyashRane10", target="_blank")),
                        Li(A("Direct Email ↗", href="mailto:ranesuyash2004@gmail.com")),
                        cls="footer-links-list"
                    ),
                    cls="footer-col"
                ),

                cls="footer-grid"
            ),

            Div(
                Div(
                    Span("Crafted with", cls="footer-sub-label"),
                    Span("Python + FastHTML", cls="footer-sub-tech"),
                    cls="footer-sub-left"
                ),
                Span("© 2026 Suyash Rane · All rights reserved.", cls="footer-copyright"),
                Div(
                    A(
                        Span("Back to top"),
                        Span("↑", cls="footer-arrow"),
                        href="#",
                        cls="footer-back-top"
                    ),
                    cls="footer-sub-right"
                ),
                cls="footer-bottom-bar"
            ),

            cls="container"
        ),
        cls="site-footer"
    )


