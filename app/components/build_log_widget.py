from fasthtml.common import *


def LogItem(date, project, title, description, category, tags):
    return Article(
        # Date & Project Column
        Div(
            Span(date, cls="log-date mono"),
            Span(project, cls="log-project mono"),
            cls="log-meta-col"
        ),

        # Details Column
        Div(
            Div(
                H4(title, cls="log-title"),
                Span(category, cls="log-cat-pill mono"),
                cls="log-title-row"
            ),
            P(description, cls="log-desc"),
            Div(
                *[
                    Span(f"#{t}", cls="log-tag mono")
                    for t in tags
                ],
                cls="log-tags"
            ),
            cls="log-body-col"
        ),

        cls="log-row"
    )


def BuildLogWidget():
    return Section(
        Div(
            # Section heading
            Div(
                Div(
                    Span("03 / CONTINUOUS SHIPPING", cls="section-kicker"),
                    Span("BUILD LOG & ENGINEERING NOTES", cls="section-description"),
                    cls="section-heading-left",
                ),
                Span("PUBLIC CHRONICLE", cls="section-index"),
                cls="section-heading",
            ),

            # Logs stream
            Div(
                LogItem(
                    "26.08.26",
                    "BUILDSPACE",
                    "Polished high-craft editorial UI system & component hierarchy",
                    "Refined design tokens, glassmorphic headers, responsive monospace telemetry, and case study architecture.",
                    "UI/UX",
                    ["fasthtml", "design-system", "css"]
                ),
                LogItem(
                    "22.08.26",
                    "BUILDSPACE",
                    "Implemented FastHTML server component architecture & SQLite data models",
                    "Configured dynamic routing, component decomposition, and zero-bundle frontend delivery.",
                    "CORE",
                    ["python", "fasthtml", "sqlite"]
                ),
                LogItem(
                    "18.08.26",
                    "PULSEAI",
                    "Optimized hybrid chunk retrieval & vector indexing pipeline",
                    "Integrated semantic reranking with BM25 keyword matching for sub-50ms document query times.",
                    "RAG / AI",
                    ["rag", "qdrant", "fastapi"]
                ),
                LogItem(
                    "12.08.26",
                    "QUEUELESS",
                    "Shipped real-time appointment sync & offline queue cache",
                    "Built lightweight local SQLite state syncing with FastAPI backend for low-connectivity environments.",
                    "FEATURE",
                    ["flet", "mobile", "sqlite"]
                ),
                cls="build-logs-stream"
            ),

            # Footer
            Div(
                Span("ALL BUILDS ARE SHIPPED IN THE OPEN", cls="projects-footer-label"),
                A(
                    "EXPLORE ALL LOGS",
                    Span("↗", cls="projects-footer-arrow"),
                    href="/build-log",
                    cls="projects-footer-link",
                ),
                cls="projects-footer"
            ),

            cls="container",
        ),
        id="build-log",
        cls="build-log-section",
    )
