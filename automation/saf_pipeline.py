#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import sys

from exporters import compose_markdown, export_all
from validators import validate_sources, validate_references


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

    config = json.loads(config_path.read_text(encoding="utf-8"))
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
    print("Markdown export: " + ("PASS" if any(path.suffix == ".md" for path in produced) else "NOT REQUESTED"))
    print("HTML export: " + ("PASS" if any(path.suffix == ".html" for path in produced) else "NOT REQUESTED"))
    print()
    print("Result: VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
