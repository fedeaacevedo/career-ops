from __future__ import annotations

import argparse
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

from dedup import already_sent, connect, mark_sent
from models import AUTOMATION_DIR
from scorer import load_settings


ENV_PATH = AUTOMATION_DIR / "config" / ".env"
SENT_LOG = AUTOMATION_DIR / "sent" / "sent_emails.log"


def load_env(path: Path = ENV_PATH) -> dict[str, str]:
    values = dict(os.environ)
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def _parse_email_file(path: Path) -> tuple[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    subject = "Postulacion - Federico Acevedo"
    body_lines = []
    for line in lines:
        if line.lower().startswith("asunto:"):
            subject = line.split(":", 1)[1].strip()
        else:
            body_lines.append(line)
    return subject, "\n".join(body_lines).strip()


def _metadata_url(email_path: Path) -> str:
    metadata = email_path.parent / "metadata.json"
    if not metadata.exists():
        return str(email_path)
    import json

    return json.loads(metadata.read_text(encoding="utf-8")).get("url", str(email_path))


def _metadata_score(email_path: Path) -> int:
    metadata = email_path.parent / "metadata.json"
    if not metadata.exists():
        return 0
    import json

    return int(json.loads(metadata.read_text(encoding="utf-8")).get("score", {}).get("score", 0))


def _latest_report_email_paths() -> list[Path]:
    reports = sorted((AUTOMATION_DIR / "reports").glob("daily-*.json"))
    if not reports:
        return []
    import json

    payload = json.loads(reports[-1].read_text(encoding="utf-8"))
    paths = []
    for item in payload.get("results", []):
        email_txt = item.get("email_txt")
        if email_txt:
            paths.append(Path(email_txt))
    return paths


def send_pending(dry_run_override: bool | None = None) -> int:
    env = load_env()
    settings = load_settings()
    dry_run = dry_run_override if dry_run_override is not None else env.get("DRY_RUN", "true").lower() != "false"
    limit = int(env.get("DAILY_EMAIL_LIMIT", "10"))
    min_score = int(settings.get("min_score_to_email", "85"))
    user = env.get("GMAIL_USER", "")
    password = env.get("GMAIL_APP_PASSWORD", "")
    from_name = env.get("EMAIL_FROM_NAME", "Federico Acevedo")

    con = connect()
    SENT_LOG.parent.mkdir(parents=True, exist_ok=True)
    sent_count = 0

    email_paths = _latest_report_email_paths() or sorted((AUTOMATION_DIR / "generated").glob("*/*/email.txt"))
    for email_path in email_paths:
        if not email_path.exists():
            continue
        if sent_count >= limit:
            break
        url = _metadata_url(email_path)
        if _metadata_score(email_path) < min_score:
            continue
        if already_sent(con, url):
            continue

        subject, body = _parse_email_file(email_path)
        recipient = ""
        if dry_run:
            print(f"DRY_RUN would send: {subject}\nFrom: {from_name} <{user}>\nTo: {recipient or '[not configured]'}\nBody:\n{body}\n")
            SENT_LOG.write_text("", encoding="utf-8") if not SENT_LOG.exists() else None
            with SENT_LOG.open("a", encoding="utf-8") as fh:
                fh.write(f"DRY_RUN\t{url}\t{subject}\n")
            sent_count += 1
            continue

        if not user or not password or not recipient:
            raise RuntimeError("Real send requires GMAIL_USER, GMAIL_APP_PASSWORD, and a recipient/contact_email.")

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = f"{from_name} <{user}>"
        msg["To"] = recipient
        msg.set_content(body)
        pdf = email_path.parent / "cv.pdf"
        if pdf.exists():
            msg.add_attachment(pdf.read_bytes(), maintype="application", subtype="pdf", filename="Federico-Acevedo-CV.pdf")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(user, password)
            smtp.send_message(msg)
        mark_sent(con, url, recipient, subject, False)
        with SENT_LOG.open("a", encoding="utf-8") as fh:
            fh.write(f"SENT\t{url}\t{subject}\n")
        sent_count += 1

    return sent_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--send", action="store_true")
    args = parser.parse_args()
    override = True if args.dry_run else False if args.send else None
    count = send_pending(override)
    print(f"Processed {count} email(s).")
