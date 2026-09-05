from fasthtml.common import *


def ChatWidget():
    """Floating modern messenger that dispatches messages to Suyash's inbox."""
    return Div(
        # Floating Trigger Button (collapsed state)
        Button(
            Div(
                Span(cls="chat-pulse-dot"),
                Span("Send a Message", cls="chat-trigger-text"),
                Span("💬", cls="chat-trigger-icon"),
                cls="chat-trigger-inner"
            ),
            id="chat-toggle-btn",
            onclick="document.getElementById('chat-modal').classList.toggle('open')",
            cls="chat-trigger-btn",
            aria_label="Open message dialog"
        ),

        # Floating Chat Box (expanded window)
        Div(
            # Window Header
            Div(
                Div(
                    Span(cls="chat-pulse-dot"),
                    Span("Direct Message · Suyash Rane", cls="chat-header-title"),
                    cls="chat-header-left"
                ),
                Button(
                    "✕",
                    onclick="document.getElementById('chat-modal').classList.remove('open')",
                    cls="chat-close-btn",
                    aria_label="Close chat"
                ),
                cls="chat-window-header"
            ),

            # Status bar
            Div(
                Span("● Active", cls="chat-status-indicator"),
                Span("Delivers straight to my personal inbox", cls="chat-status-dest"),
                cls="chat-window-status"
            ),

            # Main Form Body / Response Container
            Div(
                Form(
                    P(
                        "Have a question, opportunity, or idea to build? Send a note directly to my inbox.",
                        cls="chat-intro-text"
                    ),
                    Div(
                        Label("Your Name", for_="chat_name", cls="chat-label"),
                        Input(
                            type="text",
                            id="chat_name",
                            name="name",
                            placeholder="e.g. Alex Smith",
                            required=True,
                            cls="chat-input"
                        ),
                        cls="chat-field"
                    ),
                    Div(
                        Label("Your Email", for_="chat_email", cls="chat-label"),
                        Input(
                            type="email",
                            id="chat_email",
                            name="email",
                            placeholder="alex@company.com",
                            required=True,
                            cls="chat-input"
                        ),
                        cls="chat-field"
                    ),
                    Div(
                        Label("Message", for_="chat_msg", cls="chat-label"),
                        Textarea(
                            id="chat_msg",
                            name="message",
                            rows=3,
                            placeholder="Hi Suyash, I'd love to chat about...",
                            required=True,
                            cls="chat-textarea"
                        ),
                        cls="chat-field"
                    ),
                    Button(
                        Span("Send Message"),
                        Span("→", cls="chat-btn-arrow"),
                        type="submit",
                        cls="chat-submit-btn"
                    ),
                    hx_post="/api/send-message",
                    hx_target="#chat-form-container",
                    hx_swap="innerHTML",
                    cls="chat-form"
                ),
                id="chat-form-container",
                cls="chat-window-body"
            ),

            id="chat-modal",
            cls="chat-modal-window"
        ),

        id="chat-widget-root",
        cls="chat-widget-root"
    )
