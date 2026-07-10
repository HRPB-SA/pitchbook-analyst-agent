"""Assemble 'The Frontier AI Price Wars' note (.docx).
US Letter, Georgia body, navy headings, real DXA tables with no-split rows
and repeated headers, CHART placeholders as callout paragraphs. No em-dashes
(scanned on build). Mirrors output/Frontier_AI_Price_Wars_Jul2026.md.
"""
import os, re
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, "..", "output")
MD = os.path.join(OUTDIR, "Frontier_AI_Price_Wars_Jul2026.md")
DOCX = os.path.join(OUTDIR, "Frontier_AI_Price_Wars_Jul2026.docx")

NAVY = RGBColor(0x1F, 0x2A, 0x44)
SLATE = RGBColor(0x35, 0x50, 0x6E)
GREY = RGBColor(0x6B, 0x72, 0x80)
INK = RGBColor(0x26, 0x2B, 0x35)
SOFT_HEX = "F2F5F9"
NAVY_HEX = "1F2A44"
BORDER_HEX = "C9D2DE"
CONTENT_W = 9360

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Emu(12240 * 635), Emu(15840 * 635)
for a in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, a, Inches(1))

st = doc.styles["Normal"]
st.font.name = "Georgia"
st.font.size = Pt(10.5)
st.font.color.rgb = INK
st.paragraph_format.space_after = Pt(7)
st.paragraph_format.line_spacing = 1.12


def _style_heading(name, size, color, bold=True, before=10, after=6, italic=False):
    s = doc.styles[name]
    s.font.name = "Georgia"; s.font.size = Pt(size)
    s.font.bold = bold; s.font.italic = italic; s.font.color.rgb = color
    s.paragraph_format.space_before = Pt(before)
    s.paragraph_format.space_after = Pt(after)
    s.paragraph_format.keep_with_next = True
    rpr = s.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for attr in ("w:ascii", "w:hAnsi"):
        rf.set(qn(attr), "Georgia")


_style_heading("Heading 1", 15, NAVY, before=16, after=8)
_style_heading("Heading 2", 12, SLATE, before=12, after=5, italic=True)


def shade(cell, hexfill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), hexfill)
    tcPr.append(shd)


def set_table_width(table, dxa):
    tblPr = table._tbl.tblPr
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW"); tblPr.append(tblW)
    tblW.set(qn("w:w"), str(dxa)); tblW.set(qn("w:type"), "dxa")


def set_cell_width(cell, dxa):
    tcPr = cell._tc.get_or_add_tcPr()
    tcW = tcPr.find(qn("w:tcW"))
    if tcW is None:
        tcW = OxmlElement("w:tcW"); tcPr.append(tcW)
    tcW.set(qn("w:w"), str(dxa)); tcW.set(qn("w:type"), "dxa")


def table_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), BORDER_HEX)
        borders.append(e)
    tblPr.append(borders)


def cell_margins(table):
    tblPr = table._tbl.tblPr
    m = OxmlElement("w:tblCellMar")
    for name, val in (("top", 40), ("left", 80), ("bottom", 40), ("right", 80)):
        e = OxmlElement(f"w:{name}")
        e.set(qn("w:w"), str(val)); e.set(qn("w:type"), "dxa")
        m.append(e)
    tblPr.append(m)


def row_no_split(row, header=False):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))
    if header:
        th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true")
        trPr.append(th)


def cell_text(cell, text, size=8.6, bold=False, color=INK, align="L", italic=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = {"L": WD_ALIGN_PARAGRAPH.LEFT, "R": WD_ALIGN_PARAGRAPH.RIGHT,
                   "C": WD_ALIGN_PARAGRAPH.CENTER}[align]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = "Georgia"; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic; r.font.color.rgb = color


def add_runs(p, text, size=10.5, color=INK):
    """Split **bold** markdown spans into runs."""
    for part in re.split(r"(\*\*.+?\*\*)", text):
        if not part:
            continue
        bold = part.startswith("**") and part.endswith("**")
        r = p.add_run(part[2:-2] if bold else part)
        r.font.name = "Georgia"; r.font.size = Pt(size)
        r.font.bold = bold; r.font.color.rgb = color


def para(text, size=10.5, color=INK, style=None, italic=False):
    p = doc.add_paragraph(style=style)
    if italic:
        r = p.add_run(re.sub(r"\*\*(.+?)\*\*", r"\1", text))
        r.font.name = "Georgia"; r.font.size = Pt(size)
        r.font.italic = True; r.font.color.rgb = color
    else:
        add_runs(p, text, size=size, color=color)
    return p


def callout(text, kind):
    """CHART:/TABLE: placeholder as a shaded single-cell table."""
    t = doc.add_table(rows=1, cols=1)
    table_borders(t); cell_margins(t); set_table_width(t, CONTENT_W)
    row_no_split(t.rows[0])
    c = t.rows[0].cells[0]
    set_cell_width(c, CONTENT_W); shade(c, SOFT_HEX)
    c.text = ""
    p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(kind + ": ")
    r.font.name = "Georgia"; r.font.size = Pt(9.2); r.font.bold = True
    r.font.color.rgb = NAVY
    r2 = p.add_run(text)
    r2.font.name = "Georgia"; r2.font.size = Pt(9.2); r2.font.italic = True
    r2.font.color.rgb = INK
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def md_table(lines):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    rows = [r for r in rows if not set("".join(r)) <= set("-: ")]
    ncols = len(rows[0])
    t = doc.add_table(rows=len(rows), cols=ncols)
    table_borders(t); cell_margins(t); set_table_width(t, CONTENT_W)
    first_w = 1900
    other_w = (CONTENT_W - first_w) // (ncols - 1)
    for i, r in enumerate(rows):
        row_no_split(t.rows[i], header=(i == 0))
        for j, val in enumerate(r):
            c = t.rows[i].cells[j]
            set_cell_width(c, first_w if j == 0 else other_w)
            if i == 0:
                shade(c, NAVY_HEX)
                cell_text(c, val, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
                          align="L" if j == 0 else "C")
            else:
                if i % 2 == 0:
                    shade(c, SOFT_HEX)
                cell_text(c, val, align="L" if j == 0 else "C")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


# ---- Header block ----
title = doc.add_paragraph()
r = title.add_run("The Frontier AI Price Wars")
r.font.name = "Georgia"; r.font.size = Pt(22); r.font.bold = True
r.font.color.rgb = NAVY
title.paragraph_format.space_after = Pt(2)
para("PitchBook Institutional Research Group | Late-Stage Company Research",
     size=10, color=SLATE)
para("Analyst: Harrison Rolfes, Senior Research Director   |   July 10, 2026",
     size=10, color=SLATE)
para("Evidence tiers: T1, primary or SEC-grade disclosure. T2, PitchBook data, "
     "priced financings, direct company statements. T3, vendor claims and trade "
     "press. Vendor-reported benchmarks and pricing claims are discounted one "
     "tier on receipt. Figures not in our canonical dataset are flagged as our "
     "estimates or assumptions and tiered.", size=8.8, color=GREY, italic=True)

# ---- Parse the markdown mirror ----
lines = open(MD, encoding="utf-8").read().splitlines()
i = 0
# skip everything up to the first section heading
while not lines[i].startswith("## "):
    i += 1

while i < len(lines):
    ln = lines[i]
    if ln.startswith("## "):
        doc.add_paragraph(ln[3:], style="Heading 1")
    elif ln.startswith("**") and ln.rstrip().endswith("**") and len(ln) < 90:
        doc.add_paragraph(ln.strip("* "), style="Heading 2")
    elif ln.startswith("|"):
        block = []
        while i < len(lines) and lines[i].startswith("|"):
            block.append(lines[i]); i += 1
        md_table(block)
        continue
    elif ln.startswith("TABLE:") or ln.startswith("CHART:"):
        kind, rest = ln.split(":", 1)
        callout(rest.strip(), kind)
    elif ln.startswith("- ") or re.match(r"^\d+\. ", ln):
        text = re.sub(r"^(- |\d+\. )", "", ln)
        style = "List Bullet" if ln.startswith("- ") else "List Number"
        p = para(text, style=style)
        p.paragraph_format.space_after = Pt(4)
    elif ln.startswith("All figures T2") or ln.startswith("All prices T1"):
        para(ln, size=8.6, color=GREY, italic=True)
    elif ln.startswith("*") and ln.rstrip().endswith("*") and not ln.startswith("**"):
        para(ln.strip("*"), size=8.8, color=GREY, italic=True)
    elif ln.strip() in ("", "---"):
        pass
    else:
        para(ln)
    i += 1

# ---- Em-dash scan and save ----
from docx.oxml.ns import qn as _qn
xml = doc.element.xml
for ch, name in (("—", "em-dash"), ("–", "en-dash")):
    if ch in xml:
        raise SystemExit(f"FATAL: {name} found in document")
doc.save(DOCX)
print("saved", DOCX)
