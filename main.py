import os
from pathlib import Path
from fasthtml.common import *

from app.pages.home import HomePage
from app.pages.case_study import CaseStudyPage
from app.pages.about import AboutPage
from app.services.email_service import save_and_dispatch_email

BASE_DIR = Path(__file__).resolve().parent

app, rt = fast_app(
    secret_key=os.environ.get("SECRET_KEY", "buildspace-secret-key-2026-production"),
    static_path=str(BASE_DIR),
    key_fname="/tmp/.sesskey",
    hdrs=(
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400;1,6..72,500&display=swap"
        ),
        Link(
            rel="stylesheet",
            href="/static/css/main.css"
        ),
        Meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0"
        ),
        Meta(
            name="description",
            content="Suyash Rane — AI Engineer & Product Builder | Portfolio & Workshop"
        )
    )
)



@rt("/")
def get():
    return HomePage()


@rt("/projects/{slug}")
def get_case_study(slug: str):
    return CaseStudyPage(slug)


@rt("/about")
def get_about():
    return AboutPage()


@rt("/api/send-message", methods=["POST"])
def post_message(name: str, email: str, message: str):
    save_and_dispatch_email(name, email, message)
    return Div(
        Div("✓", cls="chat-success-icon"),
        H4("Message Received!", cls="chat-success-title"),
        P(
            f"Thanks for reaching out, {name}! I've received your note and will get back to you shortly at {email}.",
            cls="chat-success-desc"
        ),
        Span("Direct notification delivered to Suyash", cls="chat-success-meta"),
        cls="chat-success-box"
    )


# Vercel entrypoint exports
application = app
handler = app


if __name__ == "__main__":
    serve()


