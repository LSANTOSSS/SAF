from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "automation"))
from docx_exporter import export_docx


class DocxExporterTest(unittest.TestCase):
    SAMPLE = """# Test Document

> Generated content.

## Requirements

A paragraph with **bold** and `inline code`.

- First item
- Second item

| ID | Requirement |
|---|---|
| RF-001 | Create a reservation |
| RF-002 | Reject overlaps |
"""

    def test_creates_openxml_package_with_styles_footer_and_table(self):
        with TemporaryDirectory() as tmp:
            path = export_docx(Path(tmp) / "test.docx", self.SAMPLE)
            self.assertTrue(path.exists())
            with ZipFile(path) as package:
                names = set(package.namelist())
                self.assertIn("[Content_Types].xml", names)
                self.assertIn("word/document.xml", names)
                self.assertIn("word/styles.xml", names)
                self.assertIn("word/footer1.xml", names)
                xml = package.read("word/document.xml").decode("utf-8")
                self.assertIn("<w:tbl>", xml)
                self.assertIn("RF-001", xml)
                self.assertIn("Heading2", xml)

    def test_does_not_copy_markdown_table_separator(self):
        with TemporaryDirectory() as tmp:
            path = export_docx(Path(tmp) / "test.docx", self.SAMPLE)
            with ZipFile(path) as package:
                xml = package.read("word/document.xml").decode("utf-8")
                self.assertNotIn("---", xml)


if __name__ == "__main__":
    unittest.main()
