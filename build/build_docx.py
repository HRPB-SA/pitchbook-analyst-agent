"""Assemble the Databricks 'Brick by Brick' report (.docx).
US Letter, Georgia body, navy headings, pageBreakBefore H1s, dual-width DXA
tables with no-split rows and repeated headers, embedded 300-DPI charts,
page-x-of-y footer with the embargo line. No em-dashes (scanned on build).
"""
import os, json
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import content_r1, content_r2, content_r3, content_r4

HERE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(HERE, "..", "charts")
OUTDIR = os.path.join(HERE, "..", "output")
os.makedirs(OUTDIR, exist_ok=True)

NAVY = RGBColor(0x1F, 0x2A, 0x44)
SLATE = RGBColor(0x35, 0x50, 0x6E)
GREEN = RGBColor(0x1C, 0x5D, 0x46)
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
sec.different_first_page_header_footer = True

st = doc.styles["Normal"]
st.font.name = "Georgia"
st.font.size = Pt(10.5)
st.font.color.rgb = INK
st.paragraph_format.space_after = Pt(7)
st.paragraph_format.line_spacing = 1.12

def _style_heading(name, size, color, bold=True, before=10, after=6,
                   page_break=False, italic=False):
    s = doc.styles[name]
    s.font.name = "Georgia"; s.font.size = Pt(size)
    s.font.bold = bold; s.font.italic = italic; s.font.color.rgb = color
    s.paragraph_format.space_before = Pt(before)
    s.paragraph_format.space_after = Pt(after)
    s.paragraph_format.page_break_before = page_break
    s.paragraph_format.keep_with_next = True
    rpr = s.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for attr in ("w:ascii", "w:hAnsi"):
        rf.set(qn(attr), "Georgia")

_style_heading("Heading 1", 16, NAVY, page_break=True, before=0, after=10)
_style_heading("Heading 2", 12.5, NAVY, before=14, after=5)
_style_heading("Heading 3", 11, SLATE, before=10, after=4, italic=True)

def shade(cell, hexfill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), hexfill)
    tcPr.append(shd)

def set_cell_width(cell, dxa):
    tcPr = cell._tc.get_or_add_tcPr()
    tcW = tcPr.find(qn("w:tcW"))
    if tcW is None:
        tcW = OxmlElement("w:tcW"); tcPr.append(tcW)
    tcW.set(qn("w:w"), str(dxa)); tcW.set(qn("w:type"), "dxa")

def set_table_width(table, dxa):
    tblPr = table._tbl.tblPr
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW"); tblPr.append(tblW)
    tblW.set(qn("w:w"), str(dxa)); tblW.set(qn("w:type"), "dxa")

def table_borders(table, hexcolor=BORDER_HEX, sz="4"):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), sz)
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), hexcolor)
        borders.append(e)
    tblPr.append(borders)

def cell_margins(table, top=40, bottom=40, left=80, right=80):
    tblPr = table._tbl.tblPr
    m = OxmlElement("w:tblCellMar")
    for name, val in (("top", top), ("left", left), ("bottom", bottom),
                      ("right", right)):
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

def cell_text(cell, text, size=8.6, bold=False, color=INK, align="L",
              italic=False, font="Georgia"):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = {"L": WD_ALIGN_PARAGRAPH.LEFT, "R": WD_ALIGN_PARAGRAPH.RIGHT,
                   "C": WD_ALIGN_PARAGRAPH.CENTER}[align]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color

def add_field(paragraph, instr):
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), instr)
    r = OxmlElement("w:r"); t = OxmlElement("w:t"); t.text = "1"
    r.append(t); fld.append(r)
    paragraph._p.append(fld)

def add_para(text, size=10.5, color=INK, italic=False, bold=False,
             align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=7):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    r.font.size = Pt(size); r.font.color.rgb = color
    r.font.italic = italic; r.font.bold = bold
    return p

def add_bullets(items):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Inches(0.28)
        r = p.add_run(it)
        r.font.size = Pt(10.5); r.font.color.rgb = INK

def col_widths(header, rows):
    n = len(header)
    weights = []
    for j in range(n):
        longest = max([len(str(header[j]))] + [len(str(r[j])) for r in rows])
        weights.append(min(max(longest, 6), 60))
    total = sum(weights)
    return [max(int(CONTENT_W * w / total), 700) for w in weights]

def add_table_block(spec):
    header, rows = spec["header"], spec["rows"]
    align = spec.get("align", "L" * len(header))
    if spec.get("title"):
        tp = add_para(spec["title"], size=9.5, color=NAVY, bold=True,
                      align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3)
        tp.paragraph_format.keep_with_next = True
    t = doc.add_table(rows=len(rows) + 1, cols=len(header))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    set_table_width(t, CONTENT_W)
    table_borders(t)
    cell_margins(t)
    widths = spec.get("widths") or col_widths(header, rows)
    row_no_split(t.rows[0], header=True)
    for r_ in t.rows[1:]:
        row_no_split(r_)
    for j, h in enumerate(header):
        c = t.rows[0].cells[j]
        set_cell_width(c, widths[j])
        shade(c, NAVY_HEX)
        cell_text(c, h, size=8.6, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
                  align="L" if align[j] == "L" else align[j])
    for i, row in enumerate(rows):
        last = (i == len(rows) - 1)
        summary = last and any("total" in str(x).lower() or "Composite" in str(x)
                               for x in row)
        for j, val in enumerate(row):
            c = t.rows[i + 1].cells[j]
            set_cell_width(c, widths[j])
            if summary:
                shade(c, "E2E8F0")
            elif i % 2 == 1:
                shade(c, SOFT_HEX)
            cell_text(c, str(val), size=8.4, align=align[j],
                      bold=summary, color=INK)
    if spec.get("source"):
        add_para(spec["source"], size=7.8, color=GREY, italic=True,
                 align=WD_ALIGN_PARAGRAPH.LEFT, space_after=10)
    else:
        add_para("", size=4, space_after=4)

def add_fig(fname, caption):
    path = os.path.join(CHARTS, fname)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(path, width=Inches(6.5))
    add_para(caption, size=7.8, color=GREY, italic=True,
             align=WD_ALIGN_PARAGRAPH.LEFT, space_after=12)

def render(blocks):
    for b in blocks:
        kind = b[0]
        if kind == "h1":
            doc.add_heading(b[1], level=1)
        elif kind == "h2":
            doc.add_heading(b[1], level=2)
        elif kind == "h3":
            doc.add_heading(b[1], level=3)
        elif kind == "p":
            add_para(b[1])
        elif kind == "bullets":
            add_bullets(b[1])
        elif kind == "table":
            add_table_block(b[1])
        elif kind == "fig":
            add_fig(b[1], b[2])
        else:
            raise ValueError(kind)

# =========================================================== header / footer
hdr = sec.header
hp = hdr.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
hr = hp.add_run("DATABRICKS, INC.  |  BRICK BY BRICK  |  JULY 10, 2026")
hr.font.name = "Georgia"; hr.font.size = Pt(7.5); hr.font.color.rgb = GREY
hr.font.bold = True
pPr = hp._p.get_or_add_pPr()
pbdr = OxmlElement("w:pBdr")
bottom = OxmlElement("w:bottom")
bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "4")
bottom.set(qn("w:space"), "4"); bottom.set(qn("w:color"), BORDER_HEX)
pbdr.append(bottom); pPr.append(pbdr)

ftr = sec.footer
fp = ftr.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
f1 = fp.add_run("Quality-valuation coefficient embargoed; the per-point spread is its only cleared expression  |  "
                "Not investment advice")
f1.font.name = "Georgia"; f1.font.size = Pt(6.8); f1.font.color.rgb = GREY
f1.font.italic = True
fp2 = ftr.add_paragraph()
fp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp2.add_run("Page ")
r.font.name = "Georgia"; r.font.size = Pt(7.5); r.font.color.rgb = GREY
add_field(fp2, "PAGE")
r = fp2.add_run(" of ")
r.font.name = "Georgia"; r.font.size = Pt(7.5); r.font.color.rgb = GREY
add_field(fp2, "NUMPAGES")
for fldr in fp2._p.findall(qn("w:fldSimple")):
    for rr in fldr.findall(qn("w:r")):
        rpr = OxmlElement("w:rPr")
        fonts = OxmlElement("w:rFonts"); fonts.set(qn("w:ascii"), "Georgia")
        fonts.set(qn("w:hAnsi"), "Georgia")
        szel = OxmlElement("w:sz"); szel.set(qn("w:val"), "15")
        colel = OxmlElement("w:color"); colel.set(qn("w:val"), "6B7280")
        rpr.append(fonts); rpr.append(szel); rpr.append(colel)
        rr.insert(0, rpr)

fp_ftr = sec.first_page_footer.paragraphs[0]
fp_ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp_ftr.add_run("CONFIDENTIAL  |  For institutional recipients only  |  Not for redistribution")
r.font.name = "Georgia"; r.font.size = Pt(7.5); r.font.color.rgb = GREY
r.font.italic = True

# ================================================================== COVER
def cover():
    add_para("", size=10, space_after=26)
    add_para("AN INSTITUTIONAL DEEP DIVE", size=10, color=GREY, bold=True,
             align=WD_ALIGN_PARAGRAPH.LEFT, space_after=6)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("Databricks, Inc.")
    r.font.name = "Georgia"; r.font.size = Pt(30); r.font.bold = True
    r.font.color.rgb = NAVY
    add_para("Brick by Brick: Understanding the Business",
             size=14, color=SLATE, italic=True,
             align=WD_ALIGN_PARAGRAPH.LEFT, space_after=4)
    add_para("What each layer of the $134 billion company is, what it earns, what it means now, "
             "and what it implies next. With a seven-year three-statement operating model "
             "(companion workbook).",
             size=10.5, color=INK, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=14)

    t = doc.add_table(rows=1, cols=3)
    set_table_width(t, CONTENT_W)
    table_borders(t, hexcolor=NAVY_HEX, sz="8")
    cell_margins(t, top=130, bottom=130, left=120, right=120)
    heads = [("BUSINESS QUALITY (AIBQ)", "8.81  /  ELITE",
              "Highest in the Frontier Five; the cohort's only Elite rating"),
             ("QUALITY-ADJUSTED PRICE", "$15.2B / POINT",
              "Cheapest in cohort vs ~$118B (Anthropic) and ~$188B (OpenAI) per point"),
             ("MODEL BASE CASE", "$155-190B",
              "12-month view, anchored on the $134B mark; reported round not adopted")]
    for j, (a, bb, cc) in enumerate(heads):
        c = t.rows[0].cells[j]
        set_cell_width(c, CONTENT_W // 3)
        shade(c, "EAF2EE" if j == 0 else SOFT_HEX)
        c.text = ""
        p1 = c.paragraphs[0]; p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(a); r1.font.name = "Georgia"; r1.font.size = Pt(7.5)
        r1.font.bold = True; r1.font.color.rgb = GREY
        p2 = c.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run(bb); r2.font.name = "Georgia"; r2.font.size = Pt(13)
        r2.font.bold = True
        r2.font.color.rgb = GREEN if j == 0 else NAVY
        p3 = c.add_paragraph(); p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p3.paragraph_format.space_after = Pt(0)
        r3 = p3.add_run(cc); r3.font.name = "Georgia"; r3.font.size = Pt(7.3)
        r3.font.color.rgb = GREY
    add_para("", size=6, space_after=8)

    add_table_block({
        "title": "Snapshot (all figures re-verified July 10, 2026)",
        "header": ["Metric", "Value", "Source, date"],
        "rows": [
            ["Last completed mark", "$134B (held flat across two closes)", "Series L; company, Dec 2025; PitchBook deal record, Feb 9, 2026"],
            ["Reported round (not adopted)", "$165-175B, in talks, unclosed", "Press reports, Jun 9, 2026; PitchBook note, Jul 7, 2026"],
            ["Revenue run-rate", "$6.9B, +80% YoY, accelerating", "Company disclosure, Jun 16, 2026"],
            ["Gross margin", "74% (from >80%), guided lower", "Company disclosure, Jun 16, 2026"],
            ["Free cash flow", "Positive (TTM and FY2025; magnitude undisclosed)", "Company, Feb 9, 2026"],
            ["Net revenue retention", ">140%", "Company, Feb 9, 2026"],
            ["Customers", "20,000+ orgs; 800+ >$1M/yr; 70+ >$10M/yr; >60% of Fortune 500", "Company, Feb 9, 2026"],
            ["Lifetime capital", "~$29.5B (~$20.2B equity + ~$9.3B debt)", "PitchBook 21-deal record, Jul 2026"],
            ["Run-rate multiple", "19.4x ($134B / $6.9B)", "Derived"],
            ["Listing status", "No S-1 on file; 2026 ruled out; 2027 earliest", "SEC EDGAR, Jul 10, 2026; company, Jun 4, 2026"],
        ],
        "align": "LLL",
        "source": "Prepared by Harrison Rolfes, Senior Research Director  |  July 10, 2026  |  Companion workbook: Databricks_Operating_Model_Jul2026.xlsx.",
    })

# ================================================================ CONTENTS
TOC_SECTIONS = [
    "Executive Summary: The House That Data Built",
    "The Foundation: What Databricks Is",
    "The Bricks: Products and Services, Layer by Layer",
    "The Mortar: How the Money Is Made",
    "The Builders: Customers and What They Do",
    "The Neighborhood: Competition on Three Fronts",
    "The Blueprint: Strategy, Read Through Actions",
    "The Ledger: The Financial Picture",
    "The Appraisal: What the Business Is Worth",
    "The Stress Test: What Would Change the Answer",
    "The Verdict",
]
TOC_EXHIBITS = [
    (1, "The per-point ladder: valuation per unit of quality"),
    (2, "Revenue composition by product line"),
    (3, "The valuation ladder: six marks in five years"),
    (4, "The absorption wall: listings vs issuance capacity"),
    (5, "The acceleration: run-rate and growth, four prints"),
    (6, "Gross margin vs the 70% efficiency gate"),
    (7, "Capital efficiency across the Frontier Five"),
    (8, "AIBQ dimension radar vs cohort average"),
    (9, "Growth-adjusted multiples vs Snowflake"),
    (10, "Valuation football field, 12-month view"),
    (11, "Sensitivity: run-rate by multiple"),
]

def add_toc():
    pages = {}
    pfile = os.path.join(HERE, "toc_pages.json")
    if os.path.exists(pfile):
        pages = json.load(open(pfile))
    doc.add_heading("Contents", level=1)

    def toc_row(t, title, pg, size=9.2):
        r_ = t.add_row()
        c1, c2 = r_.cells
        set_cell_width(c1, CONTENT_W - 900)
        set_cell_width(c2, 900)
        cell_text(c1, title, size=size, color=INK)
        cell_text(c2, str(pg), size=8.8, color=GREY, align="R")

    t = doc.add_table(rows=0, cols=2)
    set_table_width(t, CONTENT_W)
    cell_margins(t, top=26, bottom=26)
    for title in TOC_SECTIONS:
        toc_row(t, title, pages.get(title, ""))
    doc.add_heading("Exhibits", level=3)
    t2 = doc.add_table(rows=0, cols=2)
    set_table_width(t2, CONTENT_W)
    cell_margins(t2, top=22, bottom=22)
    for num, title in TOC_EXHIBITS:
        toc_row(t2, f"Figure {num}.  {title}", pages.get(f"fig{num}", ""),
                size=8.6)

cover()
add_toc()
render(content_r1.BLOCKS)
render(content_r2.BLOCKS)
render(content_r3.BLOCKS)
render(content_r4.BLOCKS)

out = os.path.join(OUTDIR, "Databricks_BrickByBrick_Jul2026.docx")
doc.save(out)
print("saved", out)

import zipfile
z = zipfile.ZipFile(out)
bad = [n for n in z.namelist()
       if n.endswith(".xml") and "—" in z.read(n).decode("utf8", "ignore")]
print("EMDASH-CHECK:", "FAIL " + str(bad) if bad else "PASS (zero U+2014)")
