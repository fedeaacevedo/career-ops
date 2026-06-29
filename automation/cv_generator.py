from __future__ import annotations

import html
import json
import re
import subprocess
import unicodedata
from datetime import date
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from models import AUTOMATION_DIR, ROOT, GeneratedDocuments, Job, ScoreResult


PROFILE_HINTS = {
    "DevOps / SRE / Platform": "devops",
    "Cloud / Solutions Architect": "cloud_architect",
    "Data / Analytics": "data_engineer",
    "IT Management": "it_manager",
    "Technical Project Management": "technical_program_manager",
    "Infrastructure / IT Ops": "platform_engineer",
    "Security / DevSecOps": "security_devsecops",
    "Applications / Business Systems": "applications_manager",
    "SAP / Enterprise Systems": "applications_manager",
    "Other": "solutions_architect",
}

BASE_PROFILES = {
    "devops": ["terraform", "kubernetes", "docker", "ci/cd", "linux", "prometheus", "grafana", "aws", "observability"],
    "cloud_architect": ["aws", "landing zone", "iam", "network", "high availability", "migration", "architecture", "security"],
    "solutions_architect": ["architecture", "integration", "solution design", "stakeholder", "platform", "cloud", "enterprise"],
    "data_engineer": ["etl", "data lake", "big data", "analytics", "pipeline", "sap bw", "sql", "azure"],
    "it_manager": ["leadership", "governance", "budget", "roadmap", "team management", "transformation"],
    "applications_manager": ["application", "erp", "sap", "business systems", "integration", "operations"],
    "security_devsecops": ["devsecops", "security", "iam", "compliance", "threat", "hardening", "vulnerability"],
    "technical_program_manager": ["program", "delivery", "roadmap", "stakeholder", "project", "governance", "budget"],
    "platform_engineer": ["platform", "sre", "reliability", "infrastructure", "observability", "automation", "kubernetes"],
}

SKILL_TERMS = [
    "aws", "azure", "gcp", "terraform", "docker", "kubernetes", "linux", "prometheus", "grafana", "datadog", "zabbix",
    "cloudwatch", "iam", "networking", "ci/cd", "gitlab", "github actions", "nginx", "postgresql", "mysql", "mariadb",
    "active directory", "vmware", "proxmox", "sap", "etl", "data lake", "big data", "analytics", "observability",
    "architecture", "security", "devops", "sre", "platform", "migration", "governance", "budget", "roadmap", "ai",
]

RESPONSIBILITY_HINTS = [
    "design", "build", "operate", "lead", "manage", "own", "deliver", "architect", "automate", "secure", "migrate", "optimize",
]

SOFT_SKILLS_HINTS = [
    "stakeholder management", "communication", "collaboration", "leadership", "teamwork", "ownership", "mentoring", "problem solving",
]

MISSING_SKILL_PRIORITY = [
    "snowflake", "kafka", "airflow", "pyspark", "java", "golang", "rust", "react", "node", "ansible",
]


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:80] or "job"


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip().lower()


def _load_profile() -> dict:
    path = ROOT / "config" / "profile.yml"
    if not path.exists():
        return {}
    raw = path.read_text(encoding="utf-8")

    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw)
        return data if isinstance(data, dict) else {}
    except Exception:
        pass

    # Minimal fallback parser for candidate fields.
    profile: dict = {"candidate": {}, "compensation": {}}
    section = None
    for line in raw.splitlines():
        if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*:\s*$", line):
            section = line.split(":", 1)[0].strip()
            continue
        m = re.match(r"^\s{2}([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", line)
        if not m or section not in profile:
            continue
        k = m.group(1)
        v = m.group(2).strip().strip('"').strip("'")
        profile[section][k] = v
    return profile


def _extract_section(md: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(md)
    if not match:
        return ""
    start = match.end()
    next_h = re.search(r"^##\s+", md[start:], re.MULTILINE)
    return md[start : start + next_h.start()] if next_h else md[start:]


def _parse_cv(cv_md: str) -> dict:
    summary = _extract_section(cv_md, "Professional Summary").strip()
    experience_block = _extract_section(cv_md, "Experience")
    skills_block = _extract_section(cv_md, "Core Skills")
    certs_block = _extract_section(cv_md, "Certifications and Training")
    langs_block = _extract_section(cv_md, "Languages")
    education_block = _extract_section(cv_md, "Education")
    projects_block = _extract_section(cv_md, "Projects")

    experiences = []
    current = None
    for line in experience_block.splitlines():
        h3 = re.match(r"^###\s+(.+)$", line.strip())
        if h3:
            if current:
                experiences.append(current)
            current = {"company": h3.group(1).strip(), "role": "", "period": "", "bullets": []}
            continue
        if current is None:
            continue
        role_m = re.match(r"^\*\*(.+?)\*\*", line.strip())
        if role_m:
            current["role"] = role_m.group(1).strip()
            continue
        bullet = re.match(r"^-\s+(.+)$", line.strip())
        if bullet:
            current["bullets"].append(bullet.group(1).strip())
            continue
        if line.strip() and not current["period"] and not line.strip().startswith("**"):
            current["period"] = line.strip()
    if current:
        experiences.append(current)

    skills: dict[str, list[str]] = {}
    current_skill = ""
    for line in skills_block.splitlines():
        h3 = re.match(r"^###\s+(.+)$", line.strip())
        if h3:
            current_skill = h3.group(1).strip()
            skills[current_skill] = []
            continue
        item = re.match(r"^-\s+(.+)$", line.strip())
        if item and current_skill:
            skills[current_skill].append(item.group(1).strip())

    certs = [re.sub(r"^-\s+", "", ln.strip()) for ln in certs_block.splitlines() if ln.strip().startswith("- ")]
    langs = [re.sub(r"^-\s+", "", ln.strip()) for ln in langs_block.splitlines() if ln.strip().startswith("- ")]
    education = [ln.strip() for ln in education_block.splitlines() if ln.strip()]
    projects = [ln.strip() for ln in projects_block.splitlines() if ln.strip() and not ln.strip().startswith("##")]

    return {
        "summary": summary,
        "experiences": experiences,
        "skills": skills,
        "certifications": certs,
        "languages": langs,
        "education": education,
        "projects": projects,
    }


def _strip_html(raw_html: str) -> str:
    no_script = re.sub(r"<script[\s\S]*?</script>", " ", raw_html, flags=re.IGNORECASE)
    no_style = re.sub(r"<style[\s\S]*?</style>", " ", no_script, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", no_style)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _fetch_jd_text(job: Job) -> str:
    if job.description and len(job.description.strip()) > 150:
        return job.description.strip()

    try:
        req = Request(
            job.url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
                )
            },
        )
        with urlopen(req, timeout=20) as response:
            body = response.read().decode("utf-8", errors="ignore")
    except (URLError, TimeoutError, ValueError):
        return f"{job.company} {job.title} {job.location} {job.raw}".strip()

    # Prefer JSON-LD job description when available.
    descriptions = []
    for block in re.findall(r"<script[^>]*application/ld\+json[^>]*>([\s\S]*?)</script>", body, flags=re.IGNORECASE):
        try:
            parsed = json.loads(block)
        except json.JSONDecodeError:
            continue
        items = parsed if isinstance(parsed, list) else [parsed]
        for item in items:
            if not isinstance(item, dict):
                continue
            desc = item.get("description")
            if isinstance(desc, str) and len(desc) > 250:
                descriptions.append(_strip_html(desc))
    if descriptions:
        return max(descriptions, key=len)

    return _strip_html(body)


def _extract_keywords(text: str, terms: list[str], limit: int = 20) -> list[str]:
    lower = _norm(text)
    hits = []
    for term in terms:
        if re.search(rf"(?<![a-z0-9]){re.escape(term.lower())}(?![a-z0-9])", lower):
            hits.append(term)
    return hits[:limit]


def _detect_cloud(text: str) -> str:
    clouds = [("AWS", ["aws", "ec2", "rds", "iam", "cloudwatch"]), ("Azure", ["azure", "aks", "devops"]),
              ("GCP", ["gcp", "google cloud", "gke"])]
    lower = _norm(text)
    scores = []
    for name, terms in clouds:
        scores.append((name, sum(1 for t in terms if t in lower)))
    best = max(scores, key=lambda x: x[1])
    return best[0] if best[1] > 0 else ""


def _analyze_jd(job: Job, jd_text: str) -> dict:
    lower = _norm(jd_text)
    seniority = "senior" if any(k in lower for k in ["senior", "sr", "lead", "principal", "manager", "director", "head"]) else "mid"
    english = "B2" if any(k in lower for k in ["b2", "intermediate english"]) else ("C1+" if any(k in lower for k in ["c1", "c2", "fluent english", "native english"]) else "")
    modality = "remote" if "remote" in lower else ("hybrid" if "hybrid" in lower else ("on-site" if "on-site" in lower or "onsite" in lower else ""))
    responsibilities = []
    for sentence in re.split(r"[.;•\n]", jd_text):
        clean = sentence.strip()
        if len(clean) < 40:
            continue
        if any(v in clean.lower() for v in RESPONSIBILITY_HINTS):
            responsibilities.append(clean[:220])
    responsibilities = responsibilities[:12]

    analysis = {
        "role": job.title or "",
        "seniority": seniority,
        "english": english,
        "cloud": _detect_cloud(jd_text),
        "skills": _extract_keywords(jd_text, SKILL_TERMS, limit=30),
        "keywords": _extract_keywords(jd_text, SKILL_TERMS + SOFT_SKILLS_HINTS + RESPONSIBILITY_HINTS, limit=35),
        "responsibilities": responsibilities,
        "soft_skills": _extract_keywords(jd_text, SOFT_SKILLS_HINTS, limit=8),
        "location": job.location or "",
        "modality": modality,
        "industry": "fintech" if "fintech" in lower else ("retail" if "retail" in lower else ("enterprise" if "enterprise" in lower else "")),
        "leadership": any(k in lower for k in ["lead", "manager", "director", "head", "team leadership"]),
        "management": any(k in lower for k in ["stakeholder", "roadmap", "budget", "team management", "governance"]),
        "devops": any(k in lower for k in ["devops", "ci/cd", "sre", "terraform", "kubernetes"]),
        "cloud_flag": any(k in lower for k in ["cloud", "aws", "azure", "gcp"]),
        "architecture": any(k in lower for k in ["architecture", "architect", "solution design"]),
        "security": any(k in lower for k in ["security", "iam", "devsecops", "compliance"]),
        "datos": any(k in lower for k in ["data", "etl", "analytics", "data lake", "big data"]),
        "infraestructura": any(k in lower for k in ["infrastructure", "linux", "network", "platform"]),
        "aplicaciones": any(k in lower for k in ["application", "business systems", "erp"]),
        "sap": "sap" in lower,
        "ai": any(k in lower for k in ["ai", "machine learning", "ml", "llm"]),
        "observabilidad": any(k in lower for k in ["observability", "prometheus", "grafana", "datadog"]),
    }
    return analysis


def _score_text_relevance(text: str, targets: list[str]) -> int:
    if not targets:
        return 0
    source = _norm(text)
    hits = sum(1 for t in set(targets) if _norm(t) and _norm(t) in source)
    return max(0, min(100, int((hits / max(1, len(set(targets)))) * 100)))


def _experience_scores(cv_data: dict, jd_analysis: dict) -> list[dict]:
    targets = jd_analysis.get("skills", []) + jd_analysis.get("keywords", [])
    results = []
    for exp in cv_data["experiences"]:
        blob = " ".join([exp.get("company", ""), exp.get("role", ""), " ".join(exp.get("bullets", []))])
        score = _score_text_relevance(blob, targets)
        if any(k in _norm(blob) for k in ["manager", "lead", "cto"]) and jd_analysis.get("leadership"):
            score = min(100, score + 8)
        if jd_analysis.get("cloud") and jd_analysis["cloud"].lower() in _norm(blob):
            score = min(100, score + 8)
        results.append({"company": exp.get("company", ""), "score": score})
    return sorted(results, key=lambda x: x["score"], reverse=True)


def _choose_profile(jd_analysis: dict, category_hint: str) -> str:
    seed = PROFILE_HINTS.get(category_hint, "solutions_architect")
    text = " ".join(jd_analysis.get("keywords", []) + jd_analysis.get("skills", []) + jd_analysis.get("responsibilities", []))
    best_profile = seed
    best_score = -1
    for profile_name, keys in BASE_PROFILES.items():
        score = _score_text_relevance(text, keys)
        if profile_name == seed:
            score += 5
        if score > best_score:
            best_profile = profile_name
            best_score = score
    return best_profile


def _reorder_items_by_relevance(items: list[str], targets: list[str]) -> list[str]:
    return sorted(items, key=lambda item: _score_text_relevance(item, targets), reverse=True)


def _rewrite_cv(cv_data: dict, profile: str, job: Job, jd_analysis: dict, exp_scores: list[dict]) -> dict:
    targets = jd_analysis.get("skills", []) + jd_analysis.get("keywords", [])
    top_keywords = [k for k in jd_analysis.get("keywords", []) if k][:10]
    top_skills = [k for k in jd_analysis.get("skills", []) if k][:8]
    top_exp = ", ".join([x["company"] for x in exp_scores[:3] if x["company"]])
    role = job.title or "Technology Role"
    company = job.company or "the company"

    summary = (
        f"Technology leader with hands-on delivery in cloud, infrastructure and operations. "
        f"Tailored for {role} at {company}, this version prioritizes evidence in {profile.replace('_', ' ')} "
        f"with direct experience from {top_exp or 'previous roles'} and practical depth in "
        f"{', '.join(top_skills[:6]) or 'cloud, reliability and delivery'}."
    )

    exp_score_map = {x["company"]: x["score"] for x in exp_scores}
    experiences = []
    for exp in cv_data["experiences"]:
        ordered = _reorder_items_by_relevance(exp.get("bullets", []), targets)
        experiences.append(
            {
                "company": exp.get("company", ""),
                "role": exp.get("role", ""),
                "period": exp.get("period", ""),
                "bullets": ordered,
                "score": exp_score_map.get(exp.get("company", ""), 0),
            }
        )

    skill_categories = []
    for cat, items in cv_data["skills"].items():
        ordered_items = _reorder_items_by_relevance(items, targets)
        skill_categories.append({"name": cat, "items": ordered_items, "score": _score_text_relevance(" ".join(items), targets)})
    skill_categories.sort(key=lambda c: c["score"], reverse=True)

    projects = cv_data["projects"][:]
    if not projects and exp_scores:
        projects = [f"{e['company']}: Most relevant program for this role (match {e['score']}%)" for e in exp_scores[:3]]

    rewritten = {
        "summary": summary,
        "keywords": top_keywords,
        "experiences": experiences,
        "skill_categories": skill_categories,
        "projects": projects,
        "education": cv_data["education"],
        "certifications": cv_data["certifications"],
        "languages": cv_data["languages"],
    }
    return rewritten


def _coverage_score(text: str, keywords: list[str]) -> int:
    if not keywords:
        return 0
    lower = _norm(text)
    hits = sum(1 for kw in set(keywords) if _norm(kw) and _norm(kw) in lower)
    return int((hits / max(1, len(set(keywords)))) * 100)


def _salary_fit(jd_text: str, profile: dict) -> str:
    target = _norm(str(profile.get("compensation", {}).get("target_range", "")))
    if not target:
        return "unknown"
    m = re.search(r"(usd|u\$s|\$)\s*([\d.,]+)", jd_text.lower())
    if not m:
        return "unknown"
    return "good"


def _compute_match(jd_analysis: dict, rewritten: dict, cv_data: dict, profile_data: dict, result: ScoreResult) -> dict:
    cv_blob = " ".join(
        [
            rewritten["summary"],
            " ".join(" ".join(exp["bullets"]) for exp in rewritten["experiences"]),
            " ".join(" ".join(cat["items"]) for cat in rewritten["skill_categories"]),
        ]
    )
    skill_match = _coverage_score(cv_blob, jd_analysis.get("skills", []))
    leadership_match = 85 if jd_analysis.get("leadership") and any("manager" in _norm(e["role"]) or "lead" in _norm(e["role"]) for e in cv_data["experiences"]) else 60
    cloud_match = 90 if jd_analysis.get("cloud_flag") and any(jd_analysis.get("cloud", "").lower() in _norm(cv_blob) for _ in [0]) else 55
    english_risk = result.english_risk
    salary_fit = _salary_fit(cv_blob + " " + " ".join(jd_analysis.get("responsibilities", [])), profile_data)
    match = int(round((skill_match * 0.45) + (leadership_match * 0.25) + (cloud_match * 0.2) + (result.score * 0.1)))

    missing = []
    cv_lower = _norm(cv_blob)
    jd_lower = _norm(" ".join(jd_analysis.get("skills", []) + jd_analysis.get("keywords", [])))
    for skill in MISSING_SKILL_PRIORITY:
        if skill in jd_lower and skill not in cv_lower:
            missing.append(skill.title())
    interview_probability = max(5, min(95, int(match * (0.86 if english_risk == "high" else 0.95))))

    return {
        "match": match,
        "skill_match": skill_match,
        "leadership_match": leadership_match,
        "cloud_match": cloud_match,
        "english_risk": english_risk,
        "salary_fit": salary_fit,
        "missing": missing,
        "interview_probability": interview_probability,
    }


def _render_cv_markdown(name: str, rewritten: dict) -> str:
    lines = [
        f"# {name}",
        "",
        "## Professional Summary",
        "",
        rewritten["summary"],
        "",
        "## Experience",
        "",
    ]
    for exp in rewritten["experiences"]:
        lines.append(f"### {exp['company']}")
        if exp.get("role"):
            lines.append(f"**{exp['role']}**  ")
        if exp.get("period"):
            lines.append(exp["period"])
        lines.append("")
        for bullet in exp.get("bullets", []):
            lines.append(f"- {bullet}")
        lines.append("")

    lines.extend(["## Core Skills", ""])
    for cat in rewritten["skill_categories"]:
        lines.append(f"### {cat['name']}")
        for item in cat["items"]:
            lines.append(f"- {item}")
        lines.append("")

    if rewritten["projects"]:
        lines.extend(["## Projects", ""])
        for item in rewritten["projects"]:
            lines.append(f"- {item}")
        lines.append("")

    if rewritten["certifications"]:
        lines.extend(["## Certifications and Training", ""])
        for cert in rewritten["certifications"]:
            lines.append(f"- {cert}")
        lines.append("")

    if rewritten["languages"]:
        lines.extend(["## Languages", ""])
        for lang in rewritten["languages"]:
            lines.append(f"- {lang}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def _experience_to_html(experiences: list[dict]) -> str:
    blocks = []
    for exp in experiences:
        bullets = "".join([f"<li>{html.escape(b)}</li>" for b in exp.get("bullets", [])])
        blocks.append(
            (
                '<div class="job">'
                '<div class="job-header">'
                f'<div class="job-company">{html.escape(exp.get("company", ""))}</div>'
                f'<div class="job-period">{html.escape(exp.get("period", ""))}</div>'
                "</div>"
                f'<div class="job-role">{html.escape(exp.get("role", ""))}</div>'
                f"<ul>{bullets}</ul>"
                "</div>"
            )
        )
    return "\n".join(blocks)


def _skills_to_html(skill_categories: list[dict]) -> str:
    blocks = []
    for cat in skill_categories:
        items = ", ".join(html.escape(x) for x in cat.get("items", []))
        blocks.append(
            '<div class="skill-group">'
            f'<div class="skill-category">{html.escape(cat.get("name", ""))}</div>'
            f'<div class="skill-items">{items}</div>'
            "</div>"
        )
    return "\n".join(blocks)


def _render_cv_html(template: str, profile: dict, rewritten: dict) -> str:
    candidate = profile.get("candidate", {}) if isinstance(profile.get("candidate", {}), dict) else {}
    name = candidate.get("full_name") or "Candidate"
    phone = candidate.get("phone") or ""
    email_val = candidate.get("email") or ""
    linkedin = candidate.get("linkedin") or ""
    portfolio = candidate.get("portfolio_url") or linkedin or ""
    location = candidate.get("location") or ""

    competencies = rewritten["keywords"] or [item for cat in rewritten["skill_categories"] for item in cat["items"][:2]][:8]
    competencies_html = "".join([f'<span class="competency-tag">{html.escape(k)}</span>' for k in competencies[:8]])
    certs_html = "".join([f"<div>{html.escape(c)}</div>" for c in rewritten["certifications"]])
    education_html = "".join([f'<div class="edu-item"><div class="edu-degree">{html.escape(e)}</div></div>' for e in rewritten["education"]])
    projects_html = "".join([f'<div class="project"><div class="project-desc">{html.escape(p)}</div></div>' for p in rewritten["projects"][:4]])

    out = template
    replacements = {
        "{{LANG}}": "en",
        "{{PAGE_WIDTH}}": "210mm",
        "{{PHOTO}}": "",
        "{{NAME}}": html.escape(name),
        "{{PHONE}}": html.escape(phone),
        "{{EMAIL}}": html.escape(email_val),
        "{{LINKEDIN_URL}}": html.escape(linkedin),
        "{{LINKEDIN_DISPLAY}}": html.escape(linkedin.replace("https://", "").replace("http://", "") or "LinkedIn"),
        "{{PORTFOLIO_URL}}": html.escape(portfolio),
        "{{PORTFOLIO_DISPLAY}}": html.escape(portfolio.replace("https://", "").replace("http://", "") or "Portfolio"),
        "{{LOCATION}}": html.escape(location),
        "{{SECTION_SUMMARY}}": "Professional Summary",
        "{{SUMMARY_TEXT}}": html.escape(rewritten["summary"]),
        "{{SECTION_COMPETENCIES}}": "Core Competencies",
        "{{COMPETENCIES}}": competencies_html,
        "{{SECTION_EXPERIENCE}}": "Work Experience",
        "{{EXPERIENCE}}": _experience_to_html(rewritten["experiences"]),
        "{{SECTION_PROJECTS}}": "Projects",
        "{{PROJECTS}}": projects_html,
        "{{SECTION_EDUCATION}}": "Education",
        "{{EDUCATION}}": education_html,
        "{{SECTION_CERTIFICATIONS}}": "Certifications",
        "{{CERTIFICATIONS}}": certs_html,
        "{{SECTION_SKILLS}}": "Skills",
        "{{SKILLS}}": _skills_to_html(rewritten["skill_categories"]),
    }
    for key, value in replacements.items():
        out = out.replace(key, value)
    return out


def _generate_pdf(html_path: Path, pdf_path: Path) -> str:
    script = ROOT / "generate-pdf.mjs"
    if not script.exists():
        return ""
    proc = subprocess.run(
        ["node", str(script), str(html_path), str(pdf_path), "--format=a4"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return str(pdf_path) if proc.returncode == 0 and pdf_path.exists() else ""


def _cover_letter(job: Job, rewritten: dict, jd_analysis: dict, match: dict, candidate_name: str) -> str:
    top_resp = jd_analysis.get("responsibilities", [])[:3]
    top_exp = [x for x in rewritten["experiences"][:3]]
    lines = [
        f"# Cover Letter — {job.title} at {job.company}",
        "",
        f"Hola equipo de {job.company},",
        "",
        f"Quiero postularme al rol de {job.title}. Esta carta está armada sobre experiencia real de mi CV, "
        f"enfocada en los problemas que la posición describe: {'; '.join(top_resp) if top_resp else 'operación cloud, confiabilidad y ejecución técnica'}.",
        "",
        "Experiencia más relevante para este rol:",
        "",
    ]
    for exp in top_exp:
        lead = exp.get("bullets", [""])[0]
        lines.append(f"- **{exp.get('company', '')} ({exp.get('role', '')})**: {lead}")
    lines.extend(
        [
            "",
            f"Mi nivel de ajuste estimado para esta oferta es {match.get('match', 0)}%, "
            f"con foco en skill match ({match.get('skill_match', 0)}%) y cloud match ({match.get('cloud_match', 0)}%).",
            "",
            f"Gracias por el tiempo y quedo disponible para conversar.",
            "",
            f"Saludos,",
            candidate_name,
        ]
    )
    return "\n".join(lines).strip() + "\n"


def _email_text(job: Job, rewritten: dict, match: dict, candidate_name: str, profile: dict) -> str:
    candidate = profile.get("candidate", {}) if isinstance(profile.get("candidate", {}), dict) else {}
    role = job.title or "la posición"
    company = job.company or "su equipo"
    top_focus = ", ".join((rewritten.get("keywords") or [])[:4]) or "cloud, infraestructura y delivery"
    english = match.get("english_risk", "medium")
    return (
        f"Asunto: Postulación - {role} - {candidate_name}\n\n"
        f"Hola {company},\n\n"
        f"Me interesa avanzar con el rol de {role}. Tengo experiencia real en {top_focus}, "
        f"con foco en operación productiva y ejecución técnica.\n\n"
        f"Para este puesto mi ajuste estimado es {match.get('match', 0)}% "
        f"(skill {match.get('skill_match', 0)}%, cloud {match.get('cloud_match', 0)}%, riesgo de inglés {english}).\n\n"
        f"Si les parece, coordinamos una charla esta semana.\n\n"
        f"Gracias,\n"
        f"{candidate_name}\n"
        f"{candidate.get('email', '')}\n"
        f"{job.url}\n"
    )


def _quality_gate(cv_text: str, job: Job, jd_analysis: dict) -> bool:
    lower = _norm(cv_text)
    role_ok = _norm(job.title) in lower if job.title else True
    company_ok = _norm(job.company) in lower if job.company else True
    keyword_hits = sum(1 for kw in jd_analysis.get("keywords", [])[:10] if _norm(kw) and _norm(kw) in lower)
    return role_ok and company_ok and keyword_hits >= 3


def generate_cv(job: Job, result: ScoreResult, run_date: date | None = None) -> GeneratedDocuments:
    run_date = run_date or date.today()
    source_cv = ROOT / "cv.md"
    if not source_cv.exists():
        raise FileNotFoundError(f"Missing base CV: {source_cv}")

    profile_data = _load_profile()
    cv_data = _parse_cv(source_cv.read_text(encoding="utf-8"))
    jd_text = _fetch_jd_text(job)
    jd_analysis = _analyze_jd(job, jd_text)
    exp_scores = _experience_scores(cv_data, jd_analysis)
    selected_profile = _choose_profile(jd_analysis, result.category)
    rewritten = _rewrite_cv(cv_data, selected_profile, job, jd_analysis, exp_scores)
    match = _compute_match(jd_analysis, rewritten, cv_data, profile_data, result)

    candidate = profile_data.get("candidate", {}) if isinstance(profile_data.get("candidate", {}), dict) else {}
    candidate_name = candidate.get("full_name") or "Candidate"
    target_dir = AUTOMATION_DIR / "generated" / run_date.isoformat() / slugify(f"{job.company}-{job.title}")
    target_dir.mkdir(parents=True, exist_ok=True)

    cv_text = _render_cv_markdown(candidate_name, rewritten)
    if not _quality_gate(cv_text, job, jd_analysis):
        # Stronger explicit tailoring pass if the first rendering is not specific enough.
        rewritten["summary"] = (
            f"Targeted for {job.title} at {job.company}. "
            f"Evidence-first profile in {selected_profile.replace('_', ' ')}, prioritizing {', '.join(jd_analysis.get('skills', [])[:8])} "
            f"based on real experience across {', '.join([x['company'] for x in exp_scores[:3]])}."
        )
        cv_text = _render_cv_markdown(candidate_name, rewritten)

    cv_path = target_dir / "cv.md"
    cv_path.write_text(cv_text, encoding="utf-8")

    template_path = ROOT / "templates" / "cv-template.html"
    html_path = target_dir / "cv.html"
    if template_path.exists():
        html_path.write_text(_render_cv_html(template_path.read_text(encoding="utf-8"), profile_data, rewritten), encoding="utf-8")

    pdf_path = _generate_pdf(html_path, target_dir / "cv.pdf") if html_path.exists() else ""

    cover_letter_path = target_dir / "cover_letter.md"
    cover_letter_path.write_text(_cover_letter(job, rewritten, jd_analysis, match, candidate_name), encoding="utf-8")

    email_path = target_dir / "email.txt"
    email_path.write_text(_email_text(job, rewritten, match, candidate_name, profile_data), encoding="utf-8")

    metadata = {
        "url": job.url,
        "company": job.company,
        "title": job.title,
        "location": job.location,
        "score": result.as_dict(),
        "selected_profile": selected_profile,
        "jd_analysis": jd_analysis,
        "experience_scores": exp_scores,
        "match": match,
        "outputs": {
            "cv_markdown": str(cv_path),
            "cv_pdf": pdf_path,
            "cover_letter_md": str(cover_letter_path),
            "email_txt": str(email_path),
        },
    }
    (target_dir / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")

    return GeneratedDocuments(directory=str(target_dir), cv_markdown=str(cv_path), cv_pdf=pdf_path, email_txt=str(email_path))


def pdf_hook_available() -> bool:
    return (ROOT / "generate-pdf.mjs").exists()
