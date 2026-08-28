from fasthtml.common import *

from app.pages.home import HomePage
from app.pages.case_study import CaseStudyPage
from app.pages.about import AboutPage
from app.services.email_service import save_and_dispatch_email

app, rt = fast_app(
    hdrs=(
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
            content="BUILDSPACE — Suyash Rane | AI Engineer & Product Builder Public Workshop"
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
        H4("Message Transmitted", cls="chat-success-title"),
        P(
            f"Thank you, {name}. Your transmission has been sent directly to Suyash's inbox.",
            cls="chat-success-desc"
        ),
        Span("DESTINATION: ranesuyash2004@gmail.com", cls="chat-success-meta mono"),
        cls="chat-success-box"
    )


if __name__ == "__main__":
    serve()

