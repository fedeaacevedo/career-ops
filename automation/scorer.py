from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from models import Job, ScoreResult, AUTOMATION_DIR


DEFAULT_SETTINGS_PATH = AUTOMATION_DIR / "config" / "settings.yml"
SENIORITY = ["senior", "sr.", "lead", "principal", "staff", "manager", "head", "director", "cto", "jefe", "gerente", "lider", "líder"]


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value.strip('"').strip("'")


def load_settings(path: str | Path = DEFAULT_SETTINGS_PATH) -> dict[str, Any]:
    """Small YAML reader for this repo's simple settings file."""
    settings: dict[str, Any] = {}
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue
        if raw.startswith(" ") or ":" not in raw:
            i += 1
            continue
        key, rest = raw.split(":", 1)
        key = key.strip()
        rest = rest.strip()
        if rest:
            settings[key] = _parse_scalar(rest)
            i += 1
            continue

        items: list[Any] = []
        mapping: dict[str, list[str]] = {}
        i += 1
        while i < len(lines):
            child = lines[i]
            if not child.strip() or child.lstrip().startswith("#"):
                i += 1
                continue
            if not child.startswith(" "):
                break
            stripped = child.strip()
            if stripped.startswith("- "):
                items.append(_parse_scalar(stripped[2:]))
                i += 1
                continue
            if stripped.endswith(":"):
                subkey = stripped[:-1]
                subitems: list[str] = []
                i += 1
                while i < len(lines) and lines[i].startswith("    "):
                    sub = lines[i].strip()
                    if sub.startswith("- "):
                        subitems.append(str(_parse_scalar(sub[2:])))
                    i += 1
                mapping[subkey] = subitems
                continue
            i += 1
        settings[key] = mapping if mapping else items
    return settings


def _contains_any(text: str, keywords: list[str]) -> list[str]:
    hits: list[str] = []
    for keyword in keywords:
        escaped = re.escape(keyword.lower())
        pattern = rf"(?<![a-z0-9]){escaped}(?![a-z0-9])"
        if re.search(pattern, text.lower()):
            hits.append(keyword)
    return hits


def classify_category(text: str, categories: dict[str, list[str]]) -> tuple[str, list[str]]:
    best_category = "Other"
    best_hits: list[str] = []
    for category, keywords in categories.items():
        hits = _contains_any(text, keywords)
        if len(hits) > len(best_hits):
            best_category = category
            best_hits = hits
    return best_category, best_hits


def score_job(job: Job, settings: dict[str, Any] | None = None) -> ScoreResult:
    settings = settings or load_settings()
    text = " ".join([job.title, job.company, job.location, job.description, job.raw])

    include_hits = _contains_any(text, settings.get("include_keywords", []))
    exclude_hits = _contains_any(text, settings.get("exclude_keywords", []))
    english_hard = _contains_any(text, settings.get("english_hard_keywords", []))
    english_ok = _contains_any(text, settings.get("english_ok_keywords", []))
    preferred_geo = _contains_any(text, settings.get("preferred_locations", []))
    bad_geo = _contains_any(text, settings.get("bad_locations", []))
    category, category_hits = classify_category(text, settings.get("categories", {}))

    score = 45
    reasons: list[str] = []
    risks: list[str] = []

    if include_hits:
        boost = min(30, 8 + len(set(include_hits)) * 4)
        score += boost
        reasons.append("Profile keyword match: " + ", ".join(include_hits[:8]))
    if category != "Other":
        score += 10
        reasons.append(f"Category fit: {category} ({', '.join(category_hits[:5])})")
    if _contains_any(text, SENIORITY):
        score += 10
        reasons.append("Seniority aligns with senior/lead/manager trajectory")
    if preferred_geo:
        score += 10
        reasons.append("Location fit: " + ", ".join(preferred_geo[:5]))
    if english_ok:
        score += 5
        reasons.append("English requirement appears compatible: " + ", ".join(english_ok[:4]))

    english_risk = "low"
    if english_hard:
        english_risk = "high"
        score -= 35
        risks.append("Advanced English risk: " + ", ".join(english_hard[:5]))
    elif "english" in text.lower() or "inglés" in text.lower() or "ingles" in text.lower():
        english_risk = "medium"
        risks.append("English mentioned; review exact level before applying")

    geo_fit = "good"
    if bad_geo:
        geo_fit = "bad"
        score -= 30
        risks.append("Geography risk: " + ", ".join(bad_geo[:5]))
    elif not preferred_geo and job.location:
        geo_fit = "medium"
        score -= 5
        risks.append("Location not clearly preferred")

    if exclude_hits:
        score -= min(35, 12 + len(set(exclude_hits)) * 5)
        risks.append("Out-of-profile signals: " + ", ".join(exclude_hits[:6]))

    score = max(0, min(100, score))
    should_apply = score >= int(settings.get("min_score_to_email", 85)) and english_risk != "high" and geo_fit != "bad"
    if not reasons:
        reasons.append("Insufficient positive signals from title/location; manual review recommended")

    return ScoreResult(
        score=score,
        category=category,
        english_risk=english_risk,
        geo_fit=geo_fit,
        should_apply=should_apply,
        reasons=reasons,
        risks=risks,
    )


def _demo() -> None:
    settings = load_settings()
    examples = [
        Job(url="https://example.com/1", company="Example", title="Senior Cloud Architect", location="LATAM Remote"),
        Job(url="https://example.com/2", company="Example", title="Director, Revenue Operations", location="US only", raw="native English required"),
        Job(url="https://example.com/3", company="Example", title="DevOps Engineer", location="Argentina", raw="technical English desirable"),
    ]
    for job in examples:
        result = score_job(job, settings)
        print(f"{job.title}: {result.score}/100 | {result.category} | english={result.english_risk} | geo={result.geo_fit} | apply={result.should_apply}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        _demo()
