from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from models import Job, ScoreResult, AUTOMATION_DIR


DB_PATH = AUTOMATION_DIR / "data" / "applications.db"


def connect(db_path: str | Path = DB_PATH) -> sqlite3.Connection:
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    init_db(con)
    return con


def init_db(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            url TEXT PRIMARY KEY,
            company TEXT,
            title TEXT,
            location TEXT,
            source TEXT,
            status TEXT NOT NULL DEFAULT 'found',
            score INTEGER,
            category TEXT,
            english_risk TEXT,
            geo_fit TEXT,
            reasons TEXT,
            risks TEXT,
            first_seen TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_seen TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS generated_documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            directory TEXT NOT NULL,
            cv_markdown TEXT,
            email_txt TEXT,
            cv_pdf TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(url, directory)
        );

        CREATE TABLE IF NOT EXISTS sent_emails (
            url TEXT PRIMARY KEY,
            recipient TEXT,
            subject TEXT,
            dry_run INTEGER NOT NULL DEFAULT 1,
            sent_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    con.commit()


def upsert_job(con: sqlite3.Connection, job: Job, status: str = "found") -> None:
    con.execute(
        """
        INSERT INTO jobs (url, company, title, location, source, status)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
            company=excluded.company,
            title=excluded.title,
            location=excluded.location,
            source=excluded.source,
            last_seen=CURRENT_TIMESTAMP
        """,
        (job.url, job.company, job.title, job.location, job.source, status),
    )
    con.commit()


def mark_scored(con: sqlite3.Connection, job: Job, result: ScoreResult) -> None:
    con.execute(
        """
        UPDATE jobs
        SET status='scored', score=?, category=?, english_risk=?, geo_fit=?, reasons=?, risks=?, last_seen=CURRENT_TIMESTAMP
        WHERE url=?
        """,
        (
            result.score,
            result.category,
            result.english_risk,
            result.geo_fit,
            "\n".join(result.reasons),
            "\n".join(result.risks),
            job.url,
        ),
    )
    con.commit()


def mark_generated(con: sqlite3.Connection, job: Job, docs: Any) -> None:
    con.execute("UPDATE jobs SET status='generated', last_seen=CURRENT_TIMESTAMP WHERE url=?", (job.url,))
    con.execute(
        """
        INSERT OR IGNORE INTO generated_documents (url, directory, cv_markdown, email_txt, cv_pdf)
        VALUES (?, ?, ?, ?, ?)
        """,
        (job.url, docs.directory, docs.cv_markdown, docs.email_txt, docs.cv_pdf),
    )
    con.commit()


def already_sent(con: sqlite3.Connection, url: str) -> bool:
    row = con.execute("SELECT 1 FROM sent_emails WHERE url=?", (url,)).fetchone()
    return row is not None


def mark_sent(con: sqlite3.Connection, url: str, recipient: str, subject: str, dry_run: bool) -> None:
    con.execute("UPDATE jobs SET status='sent', last_seen=CURRENT_TIMESTAMP WHERE url=?", (url,))
    con.execute(
        """
        INSERT OR REPLACE INTO sent_emails (url, recipient, subject, dry_run)
        VALUES (?, ?, ?, ?)
        """,
        (url, recipient, subject, 1 if dry_run else 0),
    )
    con.commit()
