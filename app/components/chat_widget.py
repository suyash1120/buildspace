from fasthtml.common import *


def ChatWidget():
    """Floating terminal-style direct messenger that dispatches messages to Suyash's inbox."""
    return Div(
        # Floating Trigger Button (collapsed state)
        Button(
            Div(
                Span(cls="chat-pulse-dot"),
                Span("SEND MESSAGE", cls="chat-trigger-text mono"),
                Span("💬", cls="chat-trigger-icon"),
                cls="chat-trigger-inner"
            ),
            id="chat-toggle-btn",
            onclick="document.getElementById('chat-modal').classList.toggle('open')",
            cls="chat-trigger-btn",
            aria_label="Open direct message chat"
        ),

        # Floating Chat Box (expanded window)
        Div(
            # Window Header
            Div(
                Div(
                    Span(cls="chat-pulse-dot"),
                    Span("SUYASH.DEV // DIRECT DISPATCH", cls="chat-header-title mono"),
                    cls="chat-header-left"
                ),
                Button(
                    "✕",
                    onclick="document.getElementById('chat-modal').classList.remove('open')",
                    cls="chat-close-btn mono",
                    aria_label="Close chat"
                ),
                cls="chat-window-header"
            ),

            # Status bar
            Div(
                Span("● CONNECTED", cls="chat-status-indicator mono"),
                Span("DISPATCHES TO: ranesuyash2004@gmail.com", cls="chat-status-dest mono"),
                cls="chat-window-status"
            ),

            # Main Form Body / Response Container
            Div(
                Form(
                    P(
                        "Send a direct message or project inquiry. It will be immediately delivered to my inbox.",
                        cls="chat-intro-text"
                    ),
                    Div(
                        Label("YOUR NAME //", for_="chat_name", cls="chat-label mono"),
                        Input(
                            type="text",
                            id="chat_name",
                            name="name",
                            placeholder="Alex Smith",
                            required=True,
                            cls="chat-input mono"
                        ),
                        cls="chat-field"
                    ),
                    Div(
                        Label("YOUR EMAIL //", for_="chat_email", cls="chat-label mono"),
                        Input(
                            type="email",
                            id="chat_email",
                            name="email",
                            placeholder="alex@company.com",
                            required=True,
                            cls="chat-input mono"
                        ),
                        cls="chat-field"
                    ),
                    Div(
                        Label("MESSAGE //", for_="chat_msg", cls="chat-label mono"),
                        Textarea(
                            id="chat_msg",
                            name="message",
                            rows=3,
                            placeholder="Hey Suyash, let's discuss building...",
                            required=True,
                            cls="chat-textarea"
                        ),
                        cls="chat-field"
                    ),
                    Button(
                        Span("TRANSMIT TO INBOX"),
                        Span("→", cls="chat-btn-arrow"),
                        type="submit",
                        cls="chat-submit-btn mono"
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
