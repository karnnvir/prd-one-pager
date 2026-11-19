#!/usr/bin/env python3
"""Build a formatted PRD .docx from a JSON spec.

Usage:
    python3 build_prd_docx.py spec.json "PRD - Short title - v0.1.docx"

Requires python-docx (pip install python-docx).

Spec format:
{
  "title": "Product / feature name",
  "subtitle": "One-line description",          (optional)
  "status": "Draft v0.1",                       (shown in header/footer)
  "meta": [["Author", "..."], ["Status", "..."]],   (optional metadata table, 2 or 4 columns per row)
  "blocks": [
    {"type": "h1", "text": "1. TL;DR"},
    {"type": "h2", "text": "Sub heading"},
    {"type": "p", "text": "Text with **bold** and [OPEN: gap - owner - how to close]"},
    {"type": "bullets", "items": ["a", "b"]},
    {"type": "numbered", "items": ["a", "b"]},
    {"type": "table", "header": ["Col1", "Col2"], "rows": [["a", "b"]], "widths": [1.2, 3.0]},
    {"type": "callout", "text": "Key message", "label": "Decision needed"},
    {"type": "page_break"}
  ]
}

Inline formatting inside any text: **bold**, and [OPEN: ...] which is highlighted amber so
unresolved items are easy to spot. Widths are in inches (page content width is about 7.0in).
"""
import json
import re
import sys

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_COLOR_INDEX
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor
except ImportError:
    sys.exit("python-docx is required: pip install python-docx")

NAVY = RGBColor(0x0B, 0x2E, 0x59)
GREY = RGBColor(0x55, 0x55, 0x55)
FONT = "Calibri"
BODY_PT = 10
TOKEN = re.compile(r"(\*\*.+?\*\*|\[OPEN[^\]]*\])")


def shade(cell, hex_fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    tc_pr.append(shd)


def cell_margins(table, top=40, bottom=40, left=70, right=70):
    tbl_pr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tbl_pr.append(mar)


def repeat_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def no_split(row):
    tr_pr = row._tr.get_or_add_trPr()
    tr_pr.append(OxmlElement("w:cantSplit"))


def add_runs(par, text, size=BODY_PT, color=None, bold=False):
    """Add text to a paragraph, honouring **bold** and highlighting [OPEN: ...]."""
    for part in TOKEN.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = par.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("[OPEN"):
            run = par.add_run(part)
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
            run.bold = bold
        else:
            run = par.add_run(part)
            run.bold = bold
        run.font.size = Pt(size)
        run.font.name = FONT
        if color is not None and not part.startswith("[OPEN"):
            run.font.color.rgb = color


def set_para(par, before=0, after=3, line=1.05):
    pf = par.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line


def add_page_number(par):
    for instr in ("PAGE",):
        run = par.add_run()
        begin = OxmlElement("w:fldChar")
        begin.set(qn("w:fldCharType"), "begin")
        it = OxmlElement("w:instrText")
        it.set(qn("xml:space"), "preserve")
        it.text = instr
        end = OxmlElement("w:fldChar")
        end.set(qn("w:fldCharType"), "end")
        run._r.append(begin)
        run._r.append(it)
        run._r.append(end)
        run.font.size = Pt(8)
        run.font.name = FONT
        run.font.color.rgb = GREY


def build(spec, out_path):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.left_margin = sec.right_margin = Inches(0.75)
    sec.top_margin, sec.bottom_margin = Inches(0.7), Inches(0.7)

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(BODY_PT)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)

    status = spec.get("status", "Draft")
    title = spec.get("title", "PRD")

    # Header / footer
    hp = sec.header.paragraphs[0]
    add_runs(hp, f"{title}  |  PRD  |  {status}  |  Confidential", size=8, color=GREY)
    fp = sec.footer.paragraphs[0]
    add_runs(fp, "Page ", size=8, color=GREY)
    add_page_number(fp)

    # Title block
    tp = doc.add_paragraph()
    add_runs(tp, title, size=20, color=NAVY, bold=True)
    set_para(tp, after=0)
    if spec.get("subtitle"):
        sp = doc.add_paragraph()
        add_runs(sp, spec["subtitle"], size=10.5, color=GREY)
        set_para(sp, after=4)

    # Metadata table
    meta = spec.get("meta") or []
    if meta:
        ncols = max(len(r) for r in meta)
        t = doc.add_table(rows=0, cols=ncols)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell_margins(t, 25, 25, 60, 60)
        for r in meta:
            cells = t.add_row().cells
            for i in range(ncols):
                val = r[i] if i < len(r) else ""
                p = cells[i].paragraphs[0]
                is_label = i % 2 == 0
                add_runs(p, val, size=8.5, bold=is_label, color=NAVY if is_label else None)
                set_para(p, after=0)
                if is_label:
                    shade(cells[i], "EAF0F8")
        doc.add_paragraph().paragraph_format.space_after = Pt(2)

    for b in spec.get("blocks", []):
        kind = b.get("type")
        if kind in ("h1", "h2"):
            par = doc.add_paragraph()
            if kind == "h1":
                add_runs(par, b["text"], size=12, color=NAVY, bold=True)
                set_para(par, before=7, after=2)
                # bottom rule
                p_pr = par._p.get_or_add_pPr()
                bdr = OxmlElement("w:pBdr")
                bottom = OxmlElement("w:bottom")
                bottom.set(qn("w:val"), "single")
                bottom.set(qn("w:sz"), "6")
                bottom.set(qn("w:space"), "1")
                bottom.set(qn("w:color"), "0B2E59")
                bdr.append(bottom)
                p_pr.append(bdr)
            else:
                add_runs(par, b["text"], size=10.5, color=NAVY, bold=True)
                set_para(par, before=4, after=1)
            par.paragraph_format.keep_with_next = True
        elif kind == "p":
            par = doc.add_paragraph()
            add_runs(par, b["text"])
            set_para(par)
        elif kind in ("bullets", "numbered"):
            style = "List Bullet" if kind == "bullets" else "List Number"
            for item in b["items"]:
                par = doc.add_paragraph(style=style)
                add_runs(par, item)
                set_para(par, after=1)
                par.paragraph_format.left_indent = Inches(0.22)
        elif kind == "table":
            header, rows = b["header"], b["rows"]
            t = doc.add_table(rows=1, cols=len(header))
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            t.autofit = False
            cell_margins(t)
            repeat_header(t.rows[0])
            for i, h in enumerate(header):
                c = t.rows[0].cells[i]
                shade(c, "0B2E59")
                p = c.paragraphs[0]
                add_runs(p, h, size=8.5, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
                set_para(p, after=0)
            for r in rows:
                row = t.add_row()
                no_split(row)
                for i in range(len(header)):
                    val = r[i] if i < len(r) else ""
                    p = row.cells[i].paragraphs[0]
                    add_runs(p, str(val), size=8.5)
                    set_para(p, after=0, line=1.0)
            widths = b.get("widths")
            if widths:
                for row in t.rows:
                    for i, w in enumerate(widths[: len(header)]):
                        row.cells[i].width = Inches(w)
            sp = doc.add_paragraph()
            set_para(sp, after=2)
            sp.paragraph_format.line_spacing = 0.6
        elif kind == "callout":
            t = doc.add_table(rows=1, cols=1)
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            cell_margins(t, 60, 60, 100, 100)
            c = t.rows[0].cells[0]
            shade(c, "EAF0F8")
            p = c.paragraphs[0]
            if b.get("label"):
                add_runs(p, b["label"] + ": ", size=BODY_PT, bold=True, color=NAVY)
            add_runs(p, b["text"], size=BODY_PT)
            set_para(p, after=0)
            sp = doc.add_paragraph()
            set_para(sp, after=2)
            sp.paragraph_format.line_spacing = 0.6
        elif kind == "page_break":
            doc.add_page_break()
        else:
            raise ValueError(f"Unknown block type: {kind}")

    doc.save(out_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        build(json.load(f), sys.argv[2])
    print(f"Wrote {sys.argv[2]}")
