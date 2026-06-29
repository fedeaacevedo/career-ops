from __future__ import annotations

import json
import logging
import subprocess
from datetime import date
from pathlib import Path

from cv_generator import generate_cv, pdf_hook_available
from dedup import connect, mark_generated, mark_scored, upsert_job
from email_generator import generate_email
from models import AUTOMATION_DIR, ROOT
from parser import parse_pipeline
from scorer import load_settings, score_job


LOG_PATH = AUTOMATION_DIR / "logs" / "daily.log"


def setup_logging() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )


def run_scan() -> dict[str, str]:
    try:
        result = subprocess.run(
            ["npm", "run", "scan"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=300,
            check=False,
        )
        logging.info("scan exit=%s stdout=%s stderr=%s", result.returncode, result.stdout[-2000:], result.stderr[-2000:])
        return {"status": "ok" if result.returncode == 0 else "failed", "stdout": result.stdout, "stderr": result.stderr}
    except Exception as exc:
        logging.exception("scan failed")
        return {"status": "failed", "error": str(exc)}


def write_reports(results: list[dict], scan_info: dict[str, str], run_day: date) -> tuple[Path, Path]:
    reports_dir = AUTOMATION_DIR / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    md_path = reports_dir / f"daily-{run_day.isoformat()}.md"
    json_path = reports_dir / f"daily-{run_day.isoformat()}.json"

    sorted_results = sorted(results, key=lambda item: item["score"]["score"], reverse=True)
    lines = [
        f"# Daily Job Ranking - {run_day.isoformat()}",
        "",
        f"- Scan status: {scan_info.get('status', 'unknown')}",
        f"- Jobs analyzed: {len(sorted_results)}",
        f"- PDF hook available: {'yes' if pdf_hook_available() else 'no'}",
        "",
        "## Top Offers",
        "",
    ]
    if not sorted_results:
        lines.append("No pending offers found in data/pipeline.md.")
    for idx, item in enumerate(sorted_results, 1):
        job = item["job"]
        score = item["score"]
        lines.extend(
            [
                f"### {idx}. {job['company']} - {job['title']}",
                "",
                f"- Score: {score['score']}/100",
                f"- Category: {score['category']}",
                f"- English risk: {score['english_risk']}",
                f"- Geo fit: {score['geo_fit']}",
                f"- Should apply: {score['should_apply']}",
                f"- Location: {job['location']}",
                f"- URL: {job['url']}",
                f"- Generated CV: {item.get('cv_markdown', '') or 'not generated'}",
                f"- Generated email: {item.get('email_txt', '') or 'not generated'}",
                "- Reasons:",
            ]
        )
        lines.extend([f"  - {reason}" for reason in score["reasons"]])
        if score["risks"]:
            lines.append("- Risks:")
            lines.extend([f"  - {risk}" for risk in score["risks"]])
        lines.append("")

    payload = {"date": run_day.isoformat(), "scan": scan_info, "results": sorted_results}
    md_path.write_text("\n".join(lines), encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return md_path, json_path


def main() -> int:
    setup_logging()
    run_day = date.today()
    settings = load_settings()
    min_generate = int(settings.get("min_score_to_generate", 70))
    min_email = int(settings.get("min_score_to_email", 85))
    ascii_only = bool(settings.get("ascii_only", True))

    logging.info("daily run started")
    scan_info = run_scan()
    jobs = parse_pipeline()
    con = connect()
    results: list[dict] = []

    for job in jobs:
        try:
            upsert_job(con, job)
            score = score_job(job, settings)
            mark_scored(con, job, score)
            item = {
                "job": {
                    "url": job.url,
                    "company": job.company,
                    "title": job.title,
                    "location": job.location,
                    "source": job.source,
                },
                "score": score.as_dict(),
                "cv_markdown": "",
                "email_txt": "",
                "cv_pdf": "",
            }
            if score.score >= min_generate:
                docs = generate_cv(job, score, run_day)
                if score.score >= min_email and score.english_risk != "high" and score.geo_fit != "bad":
                    email_path = generate_email(job, score, docs.directory, ascii_only=ascii_only)
                    docs.email_txt = email_path
                mark_generated(con, job, docs)
                item["cv_markdown"] = docs.cv_markdown
                item["email_txt"] = docs.email_txt
                item["cv_pdf"] = docs.cv_pdf
            results.append(item)
        except Exception as exc:
            logging.exception("failed job url=%s", job.url)
            results.append(
                {
                    "job": {"url": job.url, "company": job.company, "title": job.title, "location": job.location, "source": job.source},
                    "score": {"score": 0, "category": "Other", "english_risk": "medium", "geo_fit": "medium", "should_apply": False, "reasons": [], "risks": [str(exc)]},
                    "cv_markdown": "",
                    "email_txt": "",
                    "cv_pdf": "",
                }
            )

    md_path, json_path = write_reports(results, scan_info, run_day)
    logging.info("daily run completed report=%s json=%s", md_path, json_path)
    print(f"Report: {md_path}")
    print(f"JSON: {json_path}")
    print(f"Jobs analyzed: {len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
