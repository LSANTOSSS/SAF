from pathlib import Path
from typing import Optional
import re

ID_PATTERN = re.compile(r"\b(?:SRC|EVD|HYP|INF|GAP|DEC|RF|RNF|RN|CA)-\d{3}\b")


def safe_source_path(case_dir: Path, name: str) -> Optional[Path]:
    candidate = Path(name)
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    resolved = (case_dir / candidate).resolve()
    try:
        resolved.relative_to(case_dir.resolve())
    except ValueError:
        return None
    return resolved


def validate_sources(case_dir: Path, source_names: list[str]) -> list[dict]:
    issues = []
    if not source_names:
        return [{"severity": "ERROR", "message": "No sources configured."}]

    seen = set()
    for name in source_names:
        if name in seen:
            issues.append({"severity": "ERROR", "file": name, "message": "Duplicate source in configuration."})
        seen.add(name)

        path = safe_source_path(case_dir, name)
        if path is None:
            issues.append({"severity": "ERROR", "file": name, "message": "Source path must stay inside the case directory."})
            continue

        if not path.exists() or not path.is_file():
            issues.append({"severity": "ERROR", "file": name, "message": "Configured source does not exist."})
            continue

        text = path.read_text(encoding="utf-8")
        if not text.strip():
            issues.append({"severity": "ERROR", "file": name, "message": "Source is empty."})
        if not text.lstrip().startswith("#"):
            issues.append({"severity": "WARNING", "file": name, "message": "Source has no Markdown heading at start."})

    return issues


def validate_references(case_dir: Path, source_names: list[str]) -> list[dict]:
    defined = set()
    all_refs = []

    for name in source_names:
        path = safe_source_path(case_dir, name)
        if path is None or not path.exists() or not path.is_file():
            continue

        text = path.read_text(encoding="utf-8")
        all_refs.extend((name, ident) for ident in ID_PATTERN.findall(text))

        for line in text.splitlines():
            if line.lstrip().startswith("#") or line.lstrip().startswith("|"):
                defined.update(ID_PATTERN.findall(line))

    issues = []
    for name, ident in all_refs:
        if ident not in defined:
            issues.append({
                "severity": "WARNING",
                "file": name,
                "message": f"Reference {ident} has no structural definition in configured sources.",
            })

    return issues
