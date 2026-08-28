import os
import smtplib
import sqlite3
import json
import urllib.request
import urllib.parse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DB_PATH = "chat_messages.db"
RECIPIENT_EMAIL = "ranesuyash2004@gmail.com"



def init_db():
    """Ensure local message storage exists."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            email_sent INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


def send_via_web_service(name: str, email: str, message: str) -> bool:
    """Attempts delivery via Web3Forms, Formspree, or Resend API if configured."""
    web3forms_key = os.environ.get("WEB3FORMS_KEY")
    formspree_id = os.environ.get("FORMSPREE_ID")
    resend_key = os.environ.get("RESEND_API_KEY")

    # 1. Web3Forms (No password required, sends straight to recipient)
    if web3forms_key:
        try:
            url = "https://api.web3forms.com/submit"
            payload = {
                "access_key": web3forms_key.strip(),
                "name": name,
                "email": email,
                "message": message,
                "subject": f"[BuildSpace Inquiry] New message from {name}",
                "from_name": "BuildSpace Workshop"
            }
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                url,
                data=data,
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                }
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                res_body = json.loads(response.read().decode("utf-8"))
                if res_body.get("success"):
                    print(f"[Email Dispatch] SUCCESS! Delivered via Web3Forms to {RECIPIENT_EMAIL}")
                    return True
                else:
                    print(f"[Web3Forms Response Message]: {res_body.get('message')}")
        except urllib.error.HTTPError as e:
            err_content = e.read().decode("utf-8", errors="ignore")
            print(f"[Web3Forms HTTP Error {e.code}]: {err_content}")
        except Exception as e:
            print(f"[Web3Forms Error]: {e}")


    # 2. Formspree
    if formspree_id:
        try:
            url = f"https://formspree.io/f/{formspree_id}"
            data = urllib.parse.urlencode({
                "name": name,
                "email": email,
                "message": message,
                "_subject": f"[BuildSpace Inquiry] New message from {name}"
            }).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status in [200, 201]:
                    print(f"[Email Dispatch] Delivered via Formspree to {RECIPIENT_EMAIL}")
                    return True
        except Exception as e:
            print(f"[Formspree Error]: {e}")

    # 3. Resend API
    if resend_key:
        try:
            url = "https://api.resend.com/emails"
            data = json.dumps({
                "from": "BuildSpace <onboarding@resend.dev>",
                "to": [RECIPIENT_EMAIL],
                "reply_to": email,
                "subject": f"[BuildSpace Inquiry] New message from {name}",
                "text": f"From: {name} ({email})\n\nMessage:\n{message}"
            }).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={
                "Authorization": f"Bearer {resend_key}",
                "Content-Type": "application/json"
            })
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status in [200, 201]:
                    print(f"[Email Dispatch] Delivered via Resend to {RECIPIENT_EMAIL}")
                    return True

        except Exception as e:
            print(f"[Resend Error]: {e}")

    return False


def save_and_dispatch_email(name: str, email: str, message: str) -> bool:
    """Saves message to local DB and dispatches email to Suyash's inbox."""
    init_db()
    
    # 1. Save to local SQLite database
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[Chat Storage Error]: {e}")

    # 2. Console notification
    print("\n========================================")
    print("[NEW BUILDSPACE INQUIRY RECEIVED]")
    print(f"From: {name} <{email}>")
    print(f"Target Inbox: {RECIPIENT_EMAIL}")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Message:\n{message}")
    print("========================================\n")

    # 3. Attempt Web Gateway (Web3Forms / Formspree / Resend)
    if send_via_web_service(name, email, message):
        return True

    # 4. Attempt Direct SMTP (Gmail)
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", 587))
    smtp_user = os.environ.get("SMTP_USER", "")
    smtp_pass = os.environ.get("SMTP_PASSWORD", "")

    if smtp_user and smtp_pass:
        try:
            msg = MIMEMultipart()
            msg["From"] = smtp_user
            msg["To"] = RECIPIENT_EMAIL
            msg["Reply-To"] = email
            msg["Subject"] = f"[BuildSpace Inquiry] New message from {name}"

            body = (
                f"You received a new message from BuildSpace:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                f"Message Content:\n"
                f"----------------------------------------\n"
                f"{message}\n"
                f"----------------------------------------\n"
                f"Reply directly to this email to respond to {name}."
            )
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, RECIPIENT_EMAIL, msg.as_string())
            
            print(f"[Email Dispatch] Successfully delivered email via SMTP to {RECIPIENT_EMAIL}")
            return True
        except Exception as e:
            print(f"[Email Dispatch Warning] SMTP failed: {e}")
            return False

    return True

