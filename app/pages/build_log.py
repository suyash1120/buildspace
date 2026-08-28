from fasthtml.common import *

from app.components.navbar import Navbar
from app.components.footer import SiteFooter
from app.components.build_log_widget import LogItem


def BuildLogPage():
    return (
        Title("Build Log — Suyash Rane | Public Engineering Chronicle"),
        Navbar(active_page="build_log"),
        Main(
            Section(
                Div(
                    Div(
                        A("← BACK TO WORKSHOP", href="/", cls="back-link mono"),
                        Span("PUBLIC CHRONICLE / 2026", cls="case-study-badge mono"),
                        cls="case-study-nav"
                    ),
                    H1("BUILD LOG", cls="case-study-title"),
                    P(
                        "An unfiltered, chronological record of technical decisions, feature releases, and architectural refactors shipped in public.",
                        cls="case-study-tagline"
                    ),
                    cls="container"
                ),
                cls="case-study-hero"
            ),

            Section(
                Div(
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
                            "15.08.26",
                            "BUILDSPACE",
                            "Drafted visual workbench and live terminal status telemetry",
                            "Prototyped responsive industrial grid widgets and dark-slate status telemetry panels.",
                            "DESIGN",
                            ["css", "wireframes"]
                        ),
                        LogItem(
                            "12.08.26",
                            "QUEUELESS",
                            "Shipped real-time appointment sync & offline queue cache",
                            "Built lightweight local SQLite state syncing with FastAPI backend for low-connectivity environments.",
                            "FEATURE",
                            ["flet", "mobile", "sqlite"]
                        ),
                        LogItem(
                            "08.08.26",
                            "TRACEKIT",
                            "Completed UDP telemetry buffer and async trace batching",
                            "Eliminated in-process HTTP overhead by moving trace spans over async non-blocking UDP packets.",
                            "PERF",
                            ["telemetry", "redis", "django"]
                        ),
                        cls="build-logs-stream"
                    ),
                    cls="container"
                ),
                cls="build-log-section"
            )
        ),
        SiteFooter()
    )

