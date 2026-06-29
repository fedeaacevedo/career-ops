from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_DIR = Path(__file__).resolve().parent


@dataclass
class Job:
    url: str
    company: str = ""
    title: str = ""
    location: str = ""
    status: str = "pending"
    source: str = "pipeline"
    description: str = ""
    contact_email: str = ""
    raw: str = ""


@dataclass
class ScoreResult:
    score: int
    category: str
    english_risk: str
    geo_fit: str
    should_apply: bool
    reasons: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "score": self.score,
            "category": self.category,
            "english_risk": self.english_risk,
            "geo_fit": self.geo_fit,
            "should_apply": self.should_apply,
            "reasons": self.reasons,
            "risks": self.risks,
        }


@dataclass
class GeneratedDocuments:
    directory: str
    cv_markdown: str
    email_txt: str = ""
    cv_pdf: str = ""
