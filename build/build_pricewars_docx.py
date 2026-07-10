"""Assemble 'The Frontier AI Price Wars' note (.docx) in the PitchBook
thematic-research template: Calibri Light, US Letter, single column, a
structured cover (metadata form, Credits, Contents, Landing-page hero chart,
Report picks), then Heading 2 sections with blue headers, one real table, and
five embedded 300-DPI charts. No disclaimer, no AIBQ table. Scans for em/en
dashes and fails loudly. Body content mirrors the markdown file.
"""
import os, re
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, "..", "output")
CHARTS = os.path.join(HERE, "..", "charts")
MD = os.path.join(OUTDIR, "Frontier_AI_Price_Wars_Jul2026.md")
DOCX = os.path.join(OUTDIR, "Frontier_AI_Price_Wars_Jul2026.docx")

# body charts in order of CHART: appearance after Key takeaways
BODY_CHARTS = ["pw_cost_curves.png", "pw_sensitivity.png",
               "pw_margin_vs_price.png", "pw_layer_economics.png"]
LANDING_CHART = "pw_pricing_ladder.png"
chart_seen = 0

FONT = "Calibri Light"
BLUE = RGBColor(0x2F, 0x54, 0x96)     # Word Heading 2 blue
INK = RGBColor(0x00, 0x00, 0x00)
GREY = RGBColor(0x59, 0x59, 0x59)
NAVY_HEX = "2F5496"
SOFT_HEX = "EAF0F8"
BORDER_HEX = "BFCBDD"
CONTENT_W = 9840

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Emu(12240 * 635), Emu(15840 * 635)   # US Letter
sec.left_margin = sec.right_margin = Inches(0.75)
sec.top_margin = sec.bottom_margin = Inches(1)

st = doc.styles["Normal"]
st.font.name = FONT
st.font.size = Pt(10)
st.font.color.rgb = INK
st.paragraph_format.space_after = Pt(7)
st.paragraph_format.line_spacing = 1.12


def _rfonts(style):
    rpr = style.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi"):
        rf.set(qn(a), FONT)


_rfonts(st)
h2 = doc.styles["Heading 2"]
h2.font.name = FONT; h2.font.size = Pt(13); h2.font.bold = True
h2.font.color.rgb = BLUE
h2.paragraph_format.space_before = Pt(12); h2.paragraph_format.space_after = Pt(5)
h2.paragraph_format.keep_with_next = True
_rfonts(h2)


def run(p, text, size=10, bold=False, italic=False, color=INK):
    r = p.add_run(text)
    r.font.name = FONT; r.font.size = Pt(size); r.font.bold = bold
    r.font.italic = italic; r.font.color.rgb = color
    return r


def para(text="", size=10, bold=False, italic=False, color=INK, after=7,
         style=None):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(after)
    if text:
        run(p, text, size, bold, italic, color)
    return p


def add_runs(p, text, size=10, color=INK):
    for part in re.split(r"(\*\*.+?\*\*)", text):
        if not part:
            continue
        b = part.startswith("**") and part.endswith("**")
        run(p, part[2:-2] if b else part, size, bold=b, color=color)


# ---- table helpers ----
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


def table_borders(table):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), BORDER_HEX)
        b.append(e)
    tblPr.append(b)


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


def cell_text(cell, text, size=8.6, bold=False, color=INK, align="L"):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = {"L": WD_ALIGN_PARAGRAPH.LEFT, "R": WD_ALIGN_PARAGRAPH.RIGHT,
                   "C": WD_ALIGN_PARAGRAPH.CENTER}[align]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = FONT; r.font.size = Pt(size); r.font.bold = bold
    r.font.color.rgb = color


def md_table(lines):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    rows = [r for r in rows if not set("".join(r)) <= set("-: ")]
    ncols = len(rows[0])
    t = doc.add_table(rows=len(rows), cols=ncols)
    table_borders(t); cell_margins(t); set_table_width(t, CONTENT_W)
    first = 2050
    other = (CONTENT_W - first) // (ncols - 1)
    for i, r in enumerate(rows):
        row_no_split(t.rows[i], header=(i == 0))
        for j, val in enumerate(r):
            c = t.rows[i].cells[j]
            set_cell_width(c, first if j == 0 else other)
            if i == 0:
                shade(c, NAVY_HEX)
                cell_text(c, val, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
                          align="L" if j == 0 else "C")
            else:
                if i % 2 == 0:
                    shade(c, SOFT_HEX)
                cell_text(c, val, align="L" if j == 0 else "C")
    para("", after=2)


def embed(png, caption=None):
    if caption:
        cp = doc.add_paragraph(); cp.paragraph_format.space_after = Pt(2)
        run(cp, "CHART: ", 9.5, bold=True, color=BLUE)
        run(cp, caption, 9.5, italic=True, color=GREY)
    path = os.path.join(CHARTS, png)
    if os.path.exists(path):
        ip = doc.add_paragraph()
        ip.paragraph_format.space_before = Pt(2)
        ip.paragraph_format.space_after = Pt(6)
        ip.add_run().add_picture(path, width=Inches(6.9))


# ==================== COVER ====================
para("Q3 2026  The Frontier AI Price Wars", size=14, bold=True, after=2)
para("It reads as a price war. On the right unit of account, it is a "
     "segmentation event.", size=12, bold=True, color=BLUE, after=8)

meta = [
    ("Data filepath: ", "R&E - Thematic Research\\Frontier AI\\Price Wars Jul2026"),
    ("Chart as-of date: ", "July 10, 2026"),
    ("Chart geography: ", "Global"),
    ("Research type: ", "Emerging Tech"),
    ("Access level: ", "Client only (Platform only, no preview on N&A)"),
    ("Chart count: ", "5"),
    ("Table count: ", "1"),
]
for label, val in meta:
    p = para("", size=10, after=1)
    run(p, label, 10, bold=True)
    run(p, val, 10)

para("Credits", size=12, bold=True, after=2)
para("Harrison Rolfes, Senior Research Director", size=10, after=1)
para("Published on July 10, 2026", size=10, after=8)

para("Contents", size=12, bold=True, after=2)
contents = [
    "Key takeaways",
    "1. What you are buying: the technology behind a token price",
    "2. The unit of account: cost per completed task",
    "3. Margin mechanics: who can subsidize, and is this a war?",
    "4. The barbell and the squeezed middle",
    "5. Market implications",
    "6. Consumer implications",
    "7. The surface decides",
    "What would change the call",
    "References",
]
for c in contents:
    para(c, size=10, after=1)
para("", after=6)

para("Landing page", size=12, bold=True, after=4)
embed(LANDING_CHART,
      "The pricing ladder, from the free consumer tier to the restricted "
      "premium anchor. One market, a spread past 30x, with two crowded ends "
      "and a hollow middle.")
para("The July 2026 repricing looks like a price war and is mostly a "
     "segmentation event. On the right unit of account, cost per completed "
     "task rather than price per token, a two-to-three-point reliability gap "
     "funds a five-times token premium, and the market splits into a barbell: "
     "cheapest-useful inference at one end, most-reliable premium surface at "
     "the other, a hollow commodity middle. This note builds that argument "
     "from the token up and draws the read-through for public books, private "
     "books, and the consumer.", size=10, after=8)

para("Report picks", size=12, bold=True, after=2)
para("Databricks: Brick by Brick (July 2026)", size=10, after=1)
para("AI Compute and Power: The Buildout Is a Scarcity Trade (forthcoming)",
     size=10, after=8)

para("Evidence tiers: T1, primary or SEC-grade. T2, PitchBook data and direct "
     "company statements. T3, vendor claims and trade press, discounted one "
     "tier on receipt. Figures not in our canonical dataset are flagged as our "
     "estimates and tiered.", size=8.6, italic=True, color=GREY, after=10)

# page break before the body
doc.add_page_break()

# ==================== BODY ====================
lines = open(MD, encoding="utf-8").read().splitlines()
i = 0
while not lines[i].startswith("## Key takeaways"):
    i += 1

while i < len(lines):
    ln = lines[i]
    if ln.startswith("## "):
        doc.add_paragraph(ln[3:], style="Heading 2")
    elif ln.startswith("**") and ln.rstrip().endswith("**") and len(ln) < 90:
        para(ln.strip("* "), size=10.5, bold=True, color=INK, after=3)
    elif ln.startswith("|"):
        block = []
        while i < len(lines) and lines[i].startswith("|"):
            block.append(lines[i]); i += 1
        md_table(block)
        continue
    elif ln.startswith("TABLE:"):
        p = para("", after=2)
        run(p, "TABLE: ", 9.5, bold=True, color=BLUE)
        run(p, ln.split(":", 1)[1].strip(), 9.5, italic=True, color=GREY)
    elif ln.startswith("CHART:"):
        cap = ln.split(":", 1)[1].strip()
        png = BODY_CHARTS[chart_seen]; chart_seen += 1
        embed(png, cap)
    elif ln.startswith("- ") or re.match(r"^\d+\. ", ln):
        text = re.sub(r"^(- |\d+\. )", "", ln)
        p = doc.add_paragraph(style="List Bullet" if ln.startswith("- ")
                              else "List Number")
        p.paragraph_format.space_after = Pt(4)
        add_runs(p, text, size=10)
    elif ln.startswith("*") and ln.rstrip().endswith("*") and not ln.startswith("**"):
        para(ln.strip("*"), size=8.6, italic=True, color=GREY)
    elif ln.startswith("All prices T1"):
        para(ln, size=8.6, italic=True, color=GREY)
    elif ln.strip() in ("", "---"):
        pass
    else:
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(7)
        add_runs(p, ln, size=10)
    i += 1

# ---- em-dash scan and save ----
xml = doc.element.xml
for ch, name in (("—", "em-dash"), ("–", "en-dash")):
    if ch in xml:
        raise SystemExit(f"FATAL: {name} found in document")
doc.save(DOCX)
print("saved", DOCX, "| body charts used:", chart_seen)
