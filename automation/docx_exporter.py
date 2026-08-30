"""Clean-room DOCX exporter for the public SAF documentation pipeline.

The implementation intentionally supports a controlled Markdown subset used by SAF:
headings, paragraphs, unordered/ordered lists, blockquotes and pipe tables.
It uses only Python's standard library and the Open XML package format.
"""
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile
import re

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _run(text: str, *, bold: bool = False, italic: bool = False, code: bool = False) -> str:
    props = []
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    if code:
        props.extend(['<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>', '<w:shd w:fill="F2F2F2"/>'])
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def _inline_runs(text: str) -> str:
    # Small, deterministic inline subset: **bold** and `code`.
    tokens = re.split(r"(\*\*.+?\*\*|`.+?`)", text)
    runs = []
    for token in tokens:
        if not token:
            continue
        if token.startswith("**") and token.endswith("**"):
            runs.append(_run(token[2:-2], bold=True))
        elif token.startswith("`") and token.endswith("`"):
            runs.append(_run(token[1:-1], code=True))
        else:
            runs.append(_run(token))
    return "".join(runs)


def _paragraph(text: str = "", style: str | None = None, *, quote: bool = False) -> str:
    ppr = []
    if style:
        ppr.append(f'<w:pStyle w:val="{style}"/>')
    if quote:
        ppr.extend(['<w:ind w:left="360"/>', '<w:pBdr><w:left w:val="single" w:sz="12" w:space="10" w:color="B7B7B7"/></w:pBdr>'])
    ppr_xml = f"<w:pPr>{''.join(ppr)}</w:pPr>" if ppr else ""
    content = _inline_runs(text) if text else ""
    return f"<w:p>{ppr_xml}{content}</w:p>"


def _cell(text: str, *, header: bool = False, width: int = 2400) -> str:
    shade = '<w:shd w:fill="EDEDED"/>' if header else ""
    runs = _inline_runs(text.strip())
    if header:
        runs = f"<w:r><w:rPr><w:b/></w:rPr><w:t>{escape(text.strip())}</w:t></w:r>"
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>' + shade + '</w:tcPr>'
        f'<w:p>{runs}</w:p></w:tc>'
    )


def _is_separator_row(row: list[str]) -> bool:
    return bool(row) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in row)


def _table(rows: list[list[str]]) -> str:
    rows = [r for r in rows if not _is_separator_row(r)]
    if not rows:
        return ""
    column_count = max(len(r) for r in rows)
    normalized = [r + [""] * (column_count - len(r)) for r in rows]
    table_width = 9300
    cell_width = max(1200, table_width // column_count)
    grid = "<w:tblGrid>" + "".join(f'<w:gridCol w:w="{cell_width}"/>' for _ in range(column_count)) + "</w:tblGrid>"
    trs = []
    for idx, row in enumerate(normalized):
        trs.append("<w:tr>" + "".join(_cell(cell, header=idx == 0, width=cell_width) for cell in row) + "</w:tr>")
    borders = (
        '<w:tblBorders><w:top w:val="single" w:sz="4" w:color="B7B7B7"/>'
        '<w:left w:val="single" w:sz="4" w:color="B7B7B7"/>'
        '<w:bottom w:val="single" w:sz="4" w:color="B7B7B7"/>'
        '<w:right w:val="single" w:sz="4" w:color="B7B7B7"/>'
        '<w:insideH w:val="single" w:sz="4" w:color="D9D9D9"/>'
        '<w:insideV w:val="single" w:sz="4" w:color="D9D9D9"/></w:tblBorders>'
    )
    return f'<w:tbl><w:tblPr><w:tblW w:w="9300" w:type="dxa"/><w:tblLayout w:type="fixed"/>{borders}</w:tblPr>{grid}{"".join(trs)}</w:tbl>'


def markdown_to_document_xml(markdown: str) -> str:
    blocks: list[str] = []
    table_rows: list[list[str]] = []

    def flush_table() -> None:
        nonlocal table_rows
        if table_rows:
            blocks.append(_table(table_rows))
            table_rows = []

    first_h1 = True
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            table_rows.append(stripped.strip("|").split("|"))
            continue
        flush_table()
        if stripped.startswith("<!--"):
            continue
        if not stripped:
            blocks.append(_paragraph())
        elif stripped.startswith("### "):
            blocks.append(_paragraph(stripped[4:], "Heading3"))
        elif stripped.startswith("## "):
            blocks.append(_paragraph(stripped[3:], "Heading2"))
        elif stripped.startswith("# "):
            style = "Title" if first_h1 else "Heading1"
            first_h1 = False
            blocks.append(_paragraph(stripped[2:], style))
        elif stripped.startswith("- "):
            blocks.append(_paragraph("• " + stripped[2:], "ListParagraph"))
        elif re.match(r"^\d+\.\s+", stripped):
            blocks.append(_paragraph(stripped, "ListParagraph"))
        elif stripped.startswith("> "):
            blocks.append(_paragraph(stripped[2:], "Quote", quote=True))
        else:
            blocks.append(_paragraph(stripped))
    flush_table()

    section = (
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="708" w:footer="708"/>'
        '<w:footerReference w:type="default" r:id="rId1"/></w:sectPr>'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<w:body>{"".join(blocks)}{section}</w:body></w:document>'
    )


CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
</Types>'''

ROOT_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

DOCUMENT_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>'''

STYLES = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/><w:sz w:val="22"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="0" w:after="300"/></w:pPr><w:rPr><w:b/><w:sz w:val="38"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="280" w:after="120"/></w:pPr><w:rPr><w:b/><w:sz w:val="30"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="240" w:after="100"/></w:pPr><w:rPr><w:b/><w:sz w:val="26"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="200" w:after="80"/></w:pPr><w:rPr><w:b/><w:sz w:val="23"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="360" w:hanging="180"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Quote"><w:name w:val="Quote"/><w:basedOn w:val="Normal"/><w:rPr><w:i/><w:color w:val="666666"/></w:rPr></w:style>
</w:styles>'''

FOOTER = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="{W}"><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="18"/></w:rPr><w:t>SAF — Generated documentation artifact</w:t></w:r></w:p></w:ftr>'''


def export_docx(path: Path, markdown: str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(path, "w", ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", CONTENT_TYPES)
        package.writestr("_rels/.rels", ROOT_RELS)
        package.writestr("word/document.xml", markdown_to_document_xml(markdown))
        package.writestr("word/styles.xml", STYLES)
        package.writestr("word/footer1.xml", FOOTER)
        package.writestr("word/_rels/document.xml.rels", DOCUMENT_RELS)
    return path
