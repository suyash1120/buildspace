from fasthtml.common import *


def SiteFooter():
    return Footer(
        Div(
            Div(
                # Left Brand Column
                Div(
                    Div(
                        Span("BUILDSPACE", cls="footer-brand-title"),
                        Span("·", cls="footer-brand-sep"),
                        Span("SUYASH RANE", cls="footer-brand-author"),
                        cls="footer-brand"
                    ),
                    P(
                        "An open workshop documenting software engineering, applied AI architectures, and interactive digital products.",
                        cls="footer-tagline"
                    ),
                    Div(
                        Span(cls="pulse-dot"),
                        Span("SYSTEM NORMAL · ALL NODES ACTIVE", cls="footer-status-text mono"),
                        cls="footer-status-badge"
                    ),
                    cls="footer-col-main"
                ),

                # Navigation Column
                Div(
                    Span("NAVIGATION", cls="footer-col-title mono"),
                    Ul(
                        Li(A("01 // Workshop", href="/")),
                        Li(A("02 // Selected Work", href="/#work")),
                        Li(A("03 // Experience", href="/#experience")),
                        Li(A("04 // About & Focus", href="/#about")),
                        Li(A("05 // Connect", href="/#connect")),
                        cls="footer-links-list"
                    ),
                    cls="footer-col"
                ),

                # Projects Column
                Div(
                    Span("CASE STUDIES", cls="footer-col-title mono"),
                    Ul(
                        Li(A("01 / BuildSpace", href="/projects/buildspace")),
                        Li(A("02 / Clipwise", href="/projects/clipwise")),
                        Li(A("03 / PulseAI", href="/projects/pulseai")),
                        Li(A("04 / BillNest", href="/projects/billnest")),
                        Li(A("05 / HousePrice API", href="/projects/houseprice")),
                        Li(A("06 / QueueLess", href="/projects/queueless")),
                        Li(A("07 / TraceKit", href="/projects/tracekit")),
                        cls="footer-links-list"
                    ),
                    cls="footer-col"
                ),


                # Connect Column
                Div(
                    Span("CONNECT", cls="footer-col-title mono"),
                    Ul(
                        Li(A("GitHub ↗", href="https://github.com/suyash1120", target="_blank")),
                        Li(A("LinkedIn ↗", href="https://www.linkedin.com/in/suyash-rane-4aaa84258/", target="_blank")),
                        Li(A("X / Twitter ↗", href="https://x.com/SuyashRane10", target="_blank")),
                        Li(A("Email ↗", href="mailto:ranesuyash2004@gmail.com")),
                        cls="footer-links-list"
                    ),
                    cls="footer-col"
                ),

                cls="footer-grid"
            ),

            Div(
                Div(
                    Span("ENGINEERED WITH", cls="footer-sub-label mono"),
                    Span("PYTHON + FASTHTML", cls="footer-sub-tech mono"),
                    cls="footer-sub-left"
                ),
                Span("© 2026 SUYASH RANE — ALL RIGHTS RESERVED", cls="footer-copyright mono"),
                Div(
                    A(
                        Span("BACK TO TOP"),
                        Span("↑", cls="footer-arrow"),
                        href="#",
                        cls="footer-back-top mono"
                    ),
                    cls="footer-sub-right"
                ),
                cls="footer-bottom-bar"
            ),

            cls="container"
        ),
        cls="site-footer"
    )


