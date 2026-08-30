#!/usr/bin/env python3
from pathlib import Path
from typing import Optional, Tuple
import argparse
import json
import sys

from exporters import compose_markdown, export_all
from validators import validate_sources, validate_references


def load_config(config_path: Path) -> Tuple[Optional[dict], Optional[str]]:
    try:
        raw = config_path.read_text(encoding="utf-8")
        config = json.loads(raw)
    except OSError as exc:
        return None, f"Could not read pipeline.json: {exc}"
    except json.JSONDecodeError as exc:
        return None, f"Invalid pipeline.json: {exc.msg} at line {exc.lineno}, column {exc.colno}."

    if not isinstance(config, dict):
        return None, "Invalid pipeline.json: root value must be an object."

    sources = config.get("sources")
    outputs = config.get("outputs", ["markdown"])
    if not isinstance(sources, list) or not all(isinstance(item, str) and item.strip() for item in sources):
        return None, "Invalid pipeline.json: sources must be a string array."
    if not isinstance(outputs, list) or not all(isinstance(item, str) and item.strip() for item in outputs):
        return None, "Invalid pipeline.json: outputs must be a string array."

    return config, None


def main() -> int:
    parser = argparse.ArgumentParser(description="SAF documentation pipeline reference implementation")
    parser.add_argument("case_dir", help="Directory containing pipeline.json and Markdown sources")
    parser.add_argument("--build-dir", default="build", help="Output directory (default: build)")
    args = parser.parse_args()

    case_dir = Path(args.case_dir).resolve()
    config_path = case_dir / "pipeline.json"
    if not config_path.exists():
        print("ERROR: pipeline.json not found.")
        return 2

    config, config_error = load_config(config_path)
    if config_error:
        print(f"ERROR: {config_error}")
        return 2

    sources = config.get("sources", [])
    title = config.get("title", config.get("name", case_dir.name))
    slug = config.get("name", case_dir.name)
    outputs = config.get("outputs", ["markdown"])

    structural = validate_sources(case_dir, sources)
    references = validate_references(case_dir, sources)
    issues = structural + references
    errors = [issue for issue in issues if issue["severity"] == "ERROR"]

    print("SAF Documentation Pipeline")
    print()
    print(f"Sources discovered: {len(sources)}")
    print(f"Structural validation: {'PASS' if not [i for i in structural if i['severity'] == 'ERROR'] else 'FAIL'}")
    print(f"References validation: {'PASS' if not [i for i in references if i['severity'] == 'ERROR'] else 'FAIL'}")

    for issue in issues:
        location = f" [{issue.get('file')}]" if issue.get("file") else ""
        print(f"{issue['severity']}{location}: {issue['message']}")

    if errors:
        print("Composition: SKIPPED")
        print("Export: SKIPPED")
        print()
        print("Result: INVALID")
        return 1

    markdown = compose_markdown(title, case_dir, sources)
    print("Composition: PASS")

    produced = export_all(Path(args.build_dir), slug, title, markdown, outputs)
    for extension, label in ((".md", "Markdown"), (".html", "HTML"), (".docx", "DOCX")):
        requested = extension.lstrip(".") in outputs or (extension == ".md" and "markdown" in outputs)
        status = "PASS" if any(path.suffix == extension for path in produced) else ("FAIL" if requested else "NOT REQUESTED")
        print(f"{label} export: {status}")

    print()
    print("Result: VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
