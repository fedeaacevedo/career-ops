from __future__ import annotations

import json
import unicodedata
from datetime import date
from pathlib import Path

from cv_generator import slugify
from models import Job, ScoreResult, AUTOMATION_DIR


def _ascii(value: str) -> str:
    return unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")


def _load_metadata(directory: Path) -> dict:
    path = directory / "metadata.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def build_email(job: Job, result: ScoreResult, ascii_only: bool = True, metadata: dict | None = None) -> str:
    metadata = metadata or {}
    match = metadata.get("match", {}) if isinstance(metadata.get("match", {}), dict) else {}
    selected_profile = metadata.get("selected_profile", "")
    focus = ", ".join((metadata.get("jd_analysis", {}).get("skills", []) or [])[:4])
    if not focus:
        focus = "cloud, infraestructura y delivery"
    role = job.title or "la posicion"
    company = job.company or "su equipo"
    text = f"""Asunto: Postulacion - {role} - Federico Acevedo

Hola {company},

Me interesa postularme a {role}. Vengo trabajando en entornos reales de {focus}, con foco en operacion productiva y ejecucion tecnica.

Para este puesto tengo un ajuste estimado de {match.get("match", result.score)}%, con perfil seleccionado: {selected_profile or "general"}.

Si les parece, coordinamos una charla para profundizar experiencia y alcance.

Gracias,
Federico Acevedo

Referencia: {job.url}
Score interno: {result.score}/100 - {result.category}
"""
    return _ascii(text) if ascii_only else text


def generate_email(job: Job, result: ScoreResult, directory: str | Path | None = None, ascii_only: bool = True) -> str:
    target_dir = Path(directory) if directory else AUTOMATION_DIR / "generated" / date.today().isoformat() / slugify(f"{job.company}-{job.title}")
    target_dir.mkdir(parents=True, exist_ok=True)
    metadata = _load_metadata(target_dir)
    path = target_dir / "email.txt"
    path.write_text(build_email(job, result, ascii_only=ascii_only, metadata=metadata), encoding="utf-8")
    return str(path)
