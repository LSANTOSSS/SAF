from pathlib import Path
from tempfile import TemporaryDirectory
import json
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "automation"))
from saf_pipeline import load_config
from validators import validate_sources


class PipelineConfigurationTest(unittest.TestCase):
    def test_invalid_json_returns_controlled_error(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "pipeline.json"
            path.write_text('{"sources": [}', encoding="utf-8")
            config, error = load_config(path)
            self.assertIsNone(config)
            self.assertIn("Invalid pipeline.json", error)

    def test_non_object_root_is_rejected(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "pipeline.json"
            path.write_text("[]", encoding="utf-8")
            config, error = load_config(path)
            self.assertIsNone(config)
            self.assertIn("root value must be an object", error)

    def test_sources_must_be_string_array(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "pipeline.json"
            path.write_text(json.dumps({"sources": ["ok.md", 3]}), encoding="utf-8")
            config, error = load_config(path)
            self.assertIsNone(config)
            self.assertIn("sources", error)


class SourceBoundaryTest(unittest.TestCase):
    def test_parent_traversal_is_blocked(self):
        with TemporaryDirectory() as tmp:
            case = Path(tmp) / "case"
            case.mkdir()
            issues = validate_sources(case, ["../outside.md"])
            self.assertTrue(any(i["severity"] == "ERROR" and "inside the case directory" in i["message"] for i in issues))

    def test_absolute_path_is_blocked(self):
        with TemporaryDirectory() as tmp:
            case = Path(tmp) / "case"
            case.mkdir()
            issues = validate_sources(case, [str(Path(tmp) / "outside.md")])
            self.assertTrue(any(i["severity"] == "ERROR" and "inside the case directory" in i["message"] for i in issues))

    def test_valid_local_source_passes_boundary_check(self):
        with TemporaryDirectory() as tmp:
            case = Path(tmp) / "case"
            case.mkdir()
            (case / "source.md").write_text("# Source\n", encoding="utf-8")
            issues = validate_sources(case, ["source.md"])
            self.assertFalse(any(i["severity"] == "ERROR" for i in issues))


if __name__ == "__main__":
    unittest.main()
