from pathlib import Path
import re

ID_PATTERN = re.compile(r"\b(?:SRC|EVD|HYP|INF|GAP|DEC|RF|RNF|RN|CA)-\d{3}\b")


def validate_sources(case_dir: Path, source_names: list[str]) -> list[dict]:
    issues = []
    if not source_names:
        return [{"severity": "ERROR", "message": "No sources configured."}]

    seen = set()
    for name in source_names:
        path = case_dir / name
        if name in seen:
            issues.append({"severity": "ERROR", "file": name, "message": "Duplicate source in configuration."})
        seen.add(name)

        if not path.exists():
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
        path = case_dir / name
        if not path.exists():
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
