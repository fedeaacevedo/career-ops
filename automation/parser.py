from __future__ import annotations

import re
from pathlib import Path

from models import Job, ROOT


URL_RE = re.compile(r"https?://\S+")
CHECK_RE = re.compile(r"^\s*-\s*\[(?P<mark>[ xX!])\]\s*(?P<body>.*)$")


def _strip_number_token(parts: list[str]) -> list[str]:
    if parts and re.match(r"^#\d+$", parts[0].strip()):
        return parts[1:]
    return parts


def _clean(value: str) -> str:
    return value.strip().strip("|").strip()


def parse_pipeline(path: str | Path | None = None) -> list[Job]:
    pipeline_path = Path(path) if path else ROOT / "data" / "pipeline.md"
    if not pipeline_path.exists():
        return []

    jobs: list[Job] = []
    for line in pipeline_path.read_text(encoding="utf-8").splitlines():
        match = CHECK_RE.match(line)
        if not match:
            continue

        mark = match.group("mark").lower()
        body = match.group("body").strip()
        upper_body = body.upper()

        if mark == "!":
            continue
        if "#SKIP" in upper_body:
            continue
        if mark == "x":
            continue

        url_match = URL_RE.search(body)
        if not url_match:
            continue

        url = url_match.group(0)
        body_after_url = body[url_match.end():].strip()
        prefix = body[:url_match.start()].strip()
        parts = [_clean(p) for p in body_after_url.split("|")]
        parts = [p for p in parts if p]
        parts = _strip_number_token([_clean(p) for p in prefix.split("|") if _clean(p)]) + parts
        parts = [p for p in parts if not re.match(r"^#\d+$", p)]

        company = parts[0] if len(parts) > 0 else ""
        title = parts[1] if len(parts) > 1 else ""
        location = parts[2] if len(parts) > 2 else ""

        jobs.append(
            Job(
                url=url,
                company=company,
                title=title,
                location=location,
                status="pending",
                raw=line,
            )
        )

    return jobs


if __name__ == "__main__":
    for job in parse_pipeline():
        print(f"{job.company} | {job.title} | {job.location} | {job.url}")
