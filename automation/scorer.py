from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from models import Job, ScoreResult, AUTOMATION_DIR


DEFAULT_SETTINGS_PATH = AUTOMATION_DIR / "config" / "settings.yml"
SENIORITY = ["senior", "sr.", "lead", "principal", "staff", "manager", "head", "director", "cto", "jefe", "gerente", "lider", "líder"]
RISK_ORDER = {"low": 0, "medium": 1, "high": 2}
CLIENT_FACING_KEYWORDS = [
    "client-facing",
    "customer-facing",
    "solutions architect",
    "partner solutions architect",
    "consulting",
    "sales engineering",
    "technical account manager",
]
ENGLISH_MARKET_HIGH_UK = ["uk", "united kingdom", "ireland", "dublin", "london", "england", "scotland"]
ENGLISH_MARKET_HIGH_US = ["united states", "usa", "us remote", "canada", "australia"]
ENGLISH_MARKET_MEDIUM = ["germany", "netherlands", "emea"]
GEO_BAD_MARKET = ENGLISH_MARKET_HIGH_UK + ENGLISH_MARKET_HIGH_US
GEO_GOOD_MARKET = ["spain", "latam", "latin america", "argentina", "uruguay", "chile", "mexico", "colombia", "brazil", "brasil", "remote", "worldwide"]
GEO_MEDIUM_MARKET = ["emea", "germany", "netherlands"]
GEO_BAD_EXCEPTIONS = ["latam", "worldwide", "spain"]


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


def _contains_market(text: str, markers: list[str]) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in markers)


def _bump_risk(level: str) -> str:
    if level == "low":
        return "medium"
    if level == "medium":
        return "high"
    return "high"


def _higher_risk(current: str, candidate: str) -> str:
    return candidate if RISK_ORDER[candidate] > RISK_ORDER[current] else current


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
    english_risk = "low"
    location_text = (job.location or "").lower()
    content_text = " ".join([job.title, job.description, job.raw]).lower()
    client_facing = _contains_any(content_text, CLIENT_FACING_KEYWORDS)
    if english_hard:
        english_risk = "high"
        score -= 35
        risks.append("Advanced English risk: " + ", ".join(english_hard[:5]))
    elif _contains_market(location_text, ENGLISH_MARKET_HIGH_UK):
        english_risk = "high"
        score -= 25
        risks.append("English risk inferred from UK/Ireland market")
    elif _contains_market(location_text, ENGLISH_MARKET_HIGH_US):
        english_risk = "high"
        score -= 30
        risks.append("English risk inferred from US/Canada/Australia market")
    elif _contains_market(location_text, ENGLISH_MARKET_MEDIUM):
        english_risk = "medium"
        score -= 15
        risks.append("English risk inferred from Germany/Netherlands/EMEA market")
    elif "english" in text.lower() or "inglés" in text.lower() or "ingles" in text.lower():
        english_risk = "medium"
        risks.append("English mentioned; review exact level before applying")

    if english_ok:
        english_ok_text = " ".join(english_ok).lower()
        english_ok_risk = "medium" if any(token in english_ok_text for token in ["intermediate", "b1", "b2"]) else "low"
        score += 5
        english_risk = _higher_risk(english_risk, english_ok_risk)
        reasons.append("English requirement appears compatible: " + ", ".join(english_ok[:4]))

    if client_facing:
        bumped = _bump_risk(english_risk)
        if bumped != english_risk:
            english_risk = bumped
            risks.append("Client-facing role increases English risk")

    geo_fit = "good"
    has_bad_market = _contains_market(location_text, GEO_BAD_MARKET)
    has_bad_exception = _contains_market(location_text, GEO_BAD_EXCEPTIONS)
    has_good_market = _contains_market(location_text, GEO_GOOD_MARKET)
    has_medium_market = _contains_market(location_text, GEO_MEDIUM_MARKET)

    if _contains_market(location_text, ENGLISH_MARKET_HIGH_UK) and not has_bad_exception:
        geo_fit = "bad"
        score -= 30
        risks.append("Geo risk: role appears focused on UK/Ireland")
    elif _contains_market(location_text, ENGLISH_MARKET_HIGH_US) and not has_bad_exception:
        geo_fit = "bad"
        score -= 30
        risks.append("Geo risk: role appears focused on US/Canada/Australia")
    elif has_bad_market and not has_bad_exception:
        geo_fit = "bad"
        score -= 30
        risks.append("Geography risk: role appears focused on non-target market")
    elif has_good_market or preferred_geo:
        geo_fit = "good"
    elif has_medium_market:
        geo_fit = "medium"
        score -= 10
        risks.append("Geography fit is medium for EMEA/Germany/Netherlands")
    elif bad_geo:
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
    if geo_fit == "bad":
        should_apply = False
    elif english_risk == "high" and score < 90:
        should_apply = False
    else:
        should_apply = score >= 75 and geo_fit != "bad" and english_risk != "high"
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


def _run_tests() -> None:
    settings = load_settings()
    tests: list[tuple[str, Job, Any]] = [
        (
            "typeform multi-market should not be low english risk",
            Job(
                url="https://example.com/typeform",
                company="Typeform",
                title="Senior Data Platform Engineer",
                location="Spain/Germany/Ireland/Netherlands/UK Remote",
                description="Data platform role",
            ),
            lambda r: r.english_risk in {"medium", "high"},
        ),
        (
            "uk role should be geo bad and high english risk",
            Job(
                url="https://example.com/uk",
                company="Example",
                title="Platform Engineer",
                location="London, United Kingdom",
                description="Backend platform role",
            ),
            lambda r: r.geo_fit == "bad" and r.english_risk == "high" and r.should_apply is False,
        ),
        (
            "client-facing should increase english risk by one level",
            Job(
                url="https://example.com/client",
                company="Example",
                title="Solutions Architect",
                location="Spain",
                description="Client-facing consulting role",
            ),
            lambda r: r.english_risk in {"medium", "high"},
        ),
    ]

    failed = 0
    for name, job, assertion in tests:
        result = score_job(job, settings)
        if not assertion(result):
            failed += 1
            print(f"FAIL: {name} -> {result.as_dict()}")

    if failed:
        raise SystemExit(f"{failed} tests failed")
    print(f"OK: {len(tests)} tests passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        _run_tests()
