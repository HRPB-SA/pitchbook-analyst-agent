"""Databricks 3-statement operating model (companion to the Brick by Brick note).
Structure mirrors the reference workbook: Cover (TOC + checks), Outputs
(dashboard), Inputs (driver switch + sourced assumptions), Model (IS / CF / BS
stacked over supporting schedules), Valuation.
All figures USD millions, fiscal years ending January 31. No em-dashes.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, Reference

NAVY = "1F2A44"; SLATE = "35506E"; GREEN = "1C5D46"; GREY = "6B7280"
SOFT = "F2F5F9"; WARN = "8F3421"; WHITE = "FFFFFF"

FY = ["FY2025A", "FY2026A", "FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
NY = len(FY)
C0 = 5  # first year column = E

thin = Side(style="thin", color="D5DBE4")
border_b = Border(bottom=thin)
f_title = Font(name="Georgia", size=14, bold=True, color=NAVY)
f_h = Font(name="Georgia", size=11, bold=True, color=NAVY)
f_hdr = Font(name="Calibri", size=9, bold=True, color=WHITE)
f_lbl = Font(name="Calibri", size=9)
f_lblb = Font(name="Calibri", size=9, bold=True)
f_src = Font(name="Calibri", size=8, italic=True, color=GREY)
f_num = Font(name="Calibri", size=9)
f_numb = Font(name="Calibri", size=9, bold=True)
fill_hdr = PatternFill("solid", fgColor=NAVY)
fill_soft = PatternFill("solid", fgColor=SOFT)
fill_green = PatternFill("solid", fgColor="EAF2EE")
fill_warn = PatternFill("solid", fgColor="FBF5F3")

NUM = '#,##0;(#,##0)'
NUM1 = '#,##0.0;(#,##0.0)'
PCT = '0.0%'
MULT = '0.0"x"'

# ============================================================ base-case math
rev = [2550.0, 4050.0]
g_base = [0.77, 0.57, 0.40, 0.30, 0.24]
g_best = [0.85, 0.62, 0.45, 0.34, 0.27]
g_worst = [0.55, 0.38, 0.26, 0.18, 0.14]
for g in g_base: rev.append(round(rev[-1] * (1 + g), 0))
gm = [0.80, 0.78, 0.735, 0.725, 0.73, 0.735, 0.74]
gm_best = [0.745, 0.74, 0.745, 0.75, 0.755]
gm_worst = [0.71, 0.695, 0.69, 0.695, 0.70]
rd = [0.20, 0.19, 0.18, 0.175, 0.17, 0.165, 0.16]
sm = [0.36, 0.33, 0.30, 0.28, 0.26, 0.245, 0.23]
ga = [0.08, 0.075, 0.07, 0.065, 0.06, 0.055, 0.05]
sbc = [0.24, 0.22, 0.19, 0.17, 0.155, 0.14, 0.13]
da_pct = 0.02; capex_pct = 0.025
dso = 80; dr_days = 100
debt_rate = 0.0675; cash_yield = 0.04
tax_rate = [0.0, 0.0, 0.0, 0.08, 0.08, 0.18, 0.18]
eq_issue = [10060.0, 5000.0, 1000.0, 0, 0, 0, 0]
debt_draw = [5420.0, 1854.0, 2000.0, 0, 0, 0, 0]
tender = [-6000.0, -2000.0, -4000.0, -1000.0, -1000.0, -1000.0, -1000.0]
acq = [-300.0, -1200.0, -1500.0, -1000.0, -1000.0, -1000.0, -1000.0]
open_bs = dict(cash=1500.0, ar=400.0, ppe=300.0, gw=2600.0, oa=250.0,
               dr=700.0, ol=250.0, debt=0.0, apic=6000.0, ret=-1900.0)

def run_base():
    st = {k: [] for k in ["gp","ebit","ebitda","ie","ii","ebt","tax","ni",
        "d_ar","d_dr","cfo","cfi","cff","dcash","cash","ar","dr","ppe","gw",
        "debt","apic","ret","ta","tl","te","fcf","da","capex","sbc$"]}
    prev = dict(open_bs)
    for i in range(NY):
        r = rev[i]
        gp = r * gm[i]
        da = r * da_pct
        sbc_d = r * sbc[i]
        ebit = gp - r*(rd[i]+sm[i]+ga[i]) - sbc_d - da
        ie = -prev["debt"] * debt_rate
        ii = prev["cash"] * cash_yield
        ebt = ebit + ie + ii
        tax = -max(ebt, 0) * tax_rate[i]
        ni = ebt + tax
        ar = r * dso/365; dr = r * dr_days/365
        d_ar = -(ar - prev["ar"]); d_dr = dr - prev["dr"]
        cfo = ni + da + sbc_d + d_ar + d_dr
        capex = -r * capex_pct
        cfi = capex + acq[i]
        cff = eq_issue[i] + debt_draw[i] + tender[i]
        dcash = cfo + cfi + cff
        cash = prev["cash"] + dcash
        ppe = prev["ppe"] + (-capex) - da
        gw = prev["gw"] + (-acq[i])
        debt = prev["debt"] + debt_draw[i]
        apic = prev["apic"] + eq_issue[i] + sbc_d + tender[i]
        ret = prev["ret"] + ni
        ta = cash + ar + ppe + gw + open_bs["oa"]
        tl = dr + open_bs["ol"] + debt
        te = apic + ret
        fcf = cfo + capex
        for k, v in [("gp",gp),("ebit",ebit),("ebitda",ebit+da),("ie",ie),
            ("ii",ii),("ebt",ebt),("tax",tax),("ni",ni),("d_ar",d_ar),
            ("d_dr",d_dr),("cfo",cfo),("cfi",cfi),("cff",cff),("dcash",dcash),
            ("cash",cash),("ar",ar),("dr",dr),("ppe",ppe),("gw",gw),
            ("debt",debt),("apic",apic),("ret",ret),("ta",ta),("tl",tl),
            ("te",te),("fcf",fcf),("da",da),("capex",capex),("sbc$",sbc_d)]:
            st[k].append(v)
        prev = dict(cash=cash, ar=ar, ppe=ppe, gw=gw, oa=open_bs["oa"],
                    dr=dr, ol=open_bs["ol"], debt=debt, apic=apic, ret=ret)
    return st

B = run_base()
for i in range(NY):
    assert abs(B["ta"][i] - B["tl"][i] - B["te"][i]) < 1e-6, f"unbalanced {i}"

# ============================================================== workbook
wb = openpyxl.Workbook()
ws_cover = wb.active; ws_cover.title = "Cover"
ws_out = wb.create_sheet("Outputs")
ws_in = wb.create_sheet("Inputs")
ws_m = wb.create_sheet("Model")
ws_v = wb.create_sheet("Valuation")

def sheet_prep(ws, widths):
    ws.sheet_view.showGridLines = False
    for col, w in widths.items():
        ws.column_dimensions[col].width = w

def years(ws, row, label="All figures in USD millions unless stated"):
    ws.cell(row, 2, label).font = f_src
    for i, fy in enumerate(FY):
        c = ws.cell(row, C0 + i, fy)
        c.font = f_hdr; c.fill = fill_hdr
        c.alignment = Alignment(horizontal="center")

def put(ws, row, label, vals=None, fmla=None, fmt=NUM, bold=False, src=None,
        indent=1, fill=None, font=None):
    c = ws.cell(row, 2, label)
    c.font = font or (f_lblb if bold else f_lbl)
    c.alignment = Alignment(indent=indent)
    for i in range(NY):
        cc = ws.cell(row, C0 + i)
        if fmla is not None:
            cc.value = fmla(i) if callable(fmla) else fmla[i]
        elif vals is not None:
            v = vals[i] if isinstance(vals, (list, tuple)) else vals
            cc.value = v
        cc.number_format = fmt
        cc.font = f_numb if bold else f_num
        if bold: cc.border = border_b
        if fill: cc.fill = fill
    if src:
        s = ws.cell(row, C0 + NY + 1, src); s.font = f_src
    return row

def section(ws, row, title):
    c = ws.cell(row, 2, title)
    c.font = f_h
    for col in range(2, C0 + NY):
        ws.cell(row, col).fill = fill_soft
    return row

L = lambda i: get_column_letter(C0 + i)   # column letter for year i
P = lambda i: get_column_letter(C0 + i - 1)

# ================================================================ INPUTS
sheet_prep(ws_in, {"A":2,"B":38,"C":10,"D":10,"E":11,"F":11,"G":11,"H":11,
                   "I":11,"J":11,"K":11,"L":2,"M":70})
ws_in.cell(2, 2, "Drivers and Assumptions").font = f_title
ws_in.cell(3, 2, "Every assumption carries its source in column M. Estimates are labeled; "
                 "Databricks is private and discloses no audited financials.").font = f_src
ws_in.cell(5, 2, "Driver Switch  (1 = Best, 2 = Base, 3 = Worst)").font = f_lblb
sw = ws_in.cell(5, 5, 2); sw.font = Font(name="Calibri", size=11, bold=True, color=WARN)
sw.fill = fill_warn; sw.number_format = '0'
ws_in.cell(5, 13, "Scenario flexes revenue growth and gross margin only; cost ratios below are held.").font = f_src

years(ws_in, 7)
r = 8
section(ws_in, r, "Revenue growth, year over year (historical years fixed)"); r += 1
def scen_rows(r, name, hist, best, base, worst, fmt=PCT, src=""):
    put(ws_in, r, name + " - Best",  vals=hist + best,  fmt=fmt); r += 1
    put(ws_in, r, name + " - Base",  vals=hist + base,  fmt=fmt, src=src); r += 1
    put(ws_in, r, name + " - Worst", vals=hist + worst, fmt=fmt); r += 1
    return r
r = scen_rows(r, "Revenue growth", [0.59, 0.588], g_best, g_base, g_worst,
    src="Calibrated to disclosed run-rate ladder: $4.0B/+50% Sep-25, $4.8B/+55% Dec-25, $5.4B/+65% Feb-26, $6.9B/+80% Jun-26 (company press releases; company disclosure Jun 16, 2026). Base decelerates gracefully; NRR >140% alone sustains ~40%+ (company, Feb 9, 2026).")
GROW_BASE_ROW = r - 2   # row of Base growth
r += 1
section(ws_in, r, "Gross margin"); r += 1
r = scen_rows(r, "Gross margin", [0.80, 0.78], gm_best, gm[2:], gm_worst,
    src="74% at Jun-2026, down from >80%, guided lower on agentic compute (company disclosure, Jun 16, 2026). Base holds above the 70% quality gate; Worst breaks it in FY2028E.")
GM_BASE_ROW = r - 2
r += 1
section(ws_in, r, "Operating cost ratios, % of revenue (single path)"); r += 1
RD_ROW = put(ws_in, r, "R&D (ex-SBC)", vals=rd, fmt=PCT,
    src="Estimate; benchmarked to public consumption-software comps at similar scale (no company disclosure)."); r += 1
SM_ROW = put(ws_in, r, "Sales & marketing (ex-SBC)", vals=sm, fmt=PCT,
    src="Estimate; consumption billing lowers S&M intensity as expansion is product-driven (NRR >140%, company, Feb 9, 2026)."); r += 1
GA_ROW = put(ws_in, r, "General & administrative (ex-SBC)", vals=ga, fmt=PCT,
    src="Estimate; scale leverage typical of late-stage software."); r += 1
SBC_ROW = put(ws_in, r, "Stock-based compensation", vals=sbc, fmt=PCT,
    src="Estimate; company runs recurring employee tender programs (Series J use of proceeds, Dec 2024). Public comps at IPO ran 20%+ of revenue."); r += 1
DA_ROW = put(ws_in, r, "Depreciation & amortization", vals=[da_pct]*NY, fmt=PCT,
    src="Estimate; asset-light (compute rented from hyperscalers)."); r += 1
CAPEX_ROW = put(ws_in, r, "Capital expenditure", vals=[capex_pct]*NY, fmt=PCT,
    src="Estimate; asset-light model."); r += 1
r += 1
section(ws_in, r, "Working capital, balance sheet and other"); r += 1
put(ws_in, r, "Days sales outstanding (days)", vals=[dso]*NY, fmt='0',
    src="Estimate; enterprise annual invoicing."); DSO_ROW = r; r += 1
put(ws_in, r, "Deferred revenue (days of revenue)", vals=[dr_days]*NY, fmt='0',
    src="Estimate; committed-use contracts are prepaid then drawn down (company pricing model)."); DRD_ROW = r; r += 1
put(ws_in, r, "Interest rate on debt", vals=[debt_rate]*NY, fmt=PCT,
    src="Estimate; ~$9.3B private facilities led by major banks, Jan 2025 to Feb 2026 (PitchBook deal records)."); IR_ROW = r; r += 1
put(ws_in, r, "Yield on cash", vals=[cash_yield]*NY, fmt=PCT,
    src="Estimate; short-duration treasury yields."); YC_ROW = r; r += 1
put(ws_in, r, "Effective tax rate (on positive EBT)", vals=tax_rate, fmt=PCT,
    src="Estimate; NOL shield from accumulated losses, stepping up as it exhausts."); TAX_ROW = r; r += 1
r += 1
section(ws_in, r, "Financing events (announced; USD millions)"); r += 1
put(ws_in, r, "Equity issuance", vals=eq_issue,
    src="Series J $10.1B Dec-2024 ($62B post); Series K $1.0B Sep-2025 (>$100B); Series L $5.0B equity across Dec-2025/Feb-2026 closes ($134B). Company press releases; PitchBook."); EQ_ROW = r; r += 1
put(ws_in, r, "Debt drawn", vals=debt_draw,
    src="$5.25B facility Jan-2025; $1.8B addition + $54M refi Jan-2026; $2.0B Series L tranche Feb-2026; ~$170M Series J embedded (PitchBook deal records)."); DEBT_ROW = r; r += 1
put(ws_in, r, "Employee liquidity / tender programs (est.)", vals=tender,
    src="Estimate; Series J and the reported next round are explicitly tied to employee liquidity (company statements, Dec 2024; press reports, Jun 2026)."); TEND_ROW = r; r += 1
put(ws_in, r, "Acquisitions & strategic investments (est.)", vals=acq,
    src="Estimate of cash portion; ~19 acquisitions to date incl. MosaicML 2023, Tabular 2024, Neon 2025, Panther announced Jun 16, 2026 (terms undisclosed)."); ACQ_ROW = r; r += 1
r += 1
section(ws_in, r, "Opening balance sheet, Feb 1, 2024 (estimated; no company disclosure)"); r += 1
OPEN_ROW = r
ob_items = [("Cash & investments", open_bs["cash"]), ("Accounts receivable", open_bs["ar"]),
    ("PP&E, net", open_bs["ppe"]), ("Goodwill & intangibles", open_bs["gw"]),
    ("Other assets", open_bs["oa"]), ("Deferred revenue", open_bs["dr"]),
    ("Other liabilities", open_bs["ol"]), ("Debt", open_bs["debt"]),
    ("Paid-in capital (incl. accumulated SBC)", open_bs["apic"]),
    ("Accumulated deficit", open_bs["ret"])]
for name, v in ob_items:
    ws_in.cell(r, 2, name).font = f_lbl
    ws_in.cell(r, 2).alignment = Alignment(indent=1)
    c = ws_in.cell(r, 5, v); c.number_format = NUM; c.font = f_num
    r += 1
ws_in.cell(r, 13, "Opening balances estimated from cumulative equity raised (~$4.2B pre-Series J, PitchBook), "
                  "cumulative burn, and acquisition history. Labeled estimates throughout.").font = f_src

# ================================================================ MODEL
sheet_prep(ws_m, {"A":2,"B":40,"C":6,"D":6,"E":11,"F":11,"G":11,"H":11,
                  "I":11,"J":11,"K":11,"L":2,"M":66})
ws_m.cell(2, 2, "Model: Income Statement, Cash Flow, Balance Sheet").font = f_title
ws_m.cell(3, 2, "FY ends January 31. FY2025A and FY2026A are estimates calibrated to disclosed "
                "run-rates (company does not publish financial statements).").font = f_src
years(ws_m, 5)

SW = "Inputs!$E$5"
def choose(i, best_row, base_row):
    col = L(i)
    return (f"=CHOOSE({SW},Inputs!{col}{best_row},Inputs!{col}{base_row},"
            f"Inputs!{col}{base_row+1})")

r = 7
section(ws_m, r, "INCOME STATEMENT"); r += 1
GROWTH = r
put(ws_m, r, "Revenue growth", fmla=lambda i: choose(i, GROW_BASE_ROW-1, GROW_BASE_ROW),
    fmt=PCT, src="Scenario via Driver Switch; see Inputs for calibration sources."); r += 1
REV = r
put(ws_m, r, "Revenue",
    fmla=lambda i: rev[i] if i < 2 else f"={P(i)}{REV}*(1+{L(i)}{GROWTH})",
    bold=True,
    src="FY25A/FY26A estimated from run-rate ladder: revenue approx. average of opening and closing annualized run-rate (company press releases, Sep 2024 to Feb 2026)."); r += 1
GMR = r
put(ws_m, r, "Gross margin %", fmla=lambda i: choose(i, GM_BASE_ROW-1, GM_BASE_ROW),
    fmt=PCT, src="74% Jun-2026, guided lower (company disclosure, Jun 16, 2026)."); r += 1
COGS = r
put(ws_m, r, "Cost of revenue", fmla=lambda i: f"=-{L(i)}{REV}*(1-{L(i)}{GMR})"); r += 1
GP = r
put(ws_m, r, "Gross profit", fmla=lambda i: f"={L(i)}{REV}+{L(i)}{COGS}", bold=True); r += 2
RD_R = r
put(ws_m, r, "R&D (ex-SBC)", fmla=lambda i: f"=-{L(i)}{REV}*Inputs!{L(i)}{RD_ROW}"); r += 1
SM_R = r
put(ws_m, r, "Sales & marketing (ex-SBC)", fmla=lambda i: f"=-{L(i)}{REV}*Inputs!{L(i)}{SM_ROW}"); r += 1
GA_R = r
put(ws_m, r, "General & administrative (ex-SBC)", fmla=lambda i: f"=-{L(i)}{REV}*Inputs!{L(i)}{GA_ROW}"); r += 1
SBC_R = r
put(ws_m, r, "Stock-based compensation", fmla=lambda i: f"=-{L(i)}{REV}*Inputs!{L(i)}{SBC_ROW}"); r += 1
DA_R = r
put(ws_m, r, "Depreciation & amortization", fmla=lambda i: f"=-{L(i)}{REV}*Inputs!{L(i)}{DA_ROW}"); r += 1
EBIT = r
put(ws_m, r, "EBIT (GAAP basis, est.)",
    fmla=lambda i: f"={L(i)}{GP}+SUM({L(i)}{RD_R}:{L(i)}{DA_R})", bold=True); r += 1
EBITDA = r
put(ws_m, r, "EBITDA", fmla=lambda i: f"={L(i)}{EBIT}-{L(i)}{DA_R}"); r += 2
IE = r
put(ws_m, r, "Interest expense (on opening debt)",
    fmla=lambda i: f"=-{P(i)}{'%d'%(0)}" if False else None); r += 0
# interest rows need BS rows; fill after BS block below via placeholder rows
II = r + 1
EBT = r + 2
TAXR = r + 3
NI = r + 4
for rr, lbl in [(IE, "Interest expense (on opening debt)"),
                (II, "Interest income (on opening cash)"),
                (EBT, "Pre-tax income"), (TAXR, "Tax"), (NI, "Net income")]:
    put(ws_m, rr, lbl, bold=(lbl in ("Pre-tax income", "Net income")))
r = NI + 2

section(ws_m, r, "CASH FLOW STATEMENT"); r += 1
put(ws_m, r, "Net income", fmla=lambda i: f"={L(i)}{NI}"); NI2 = r; r += 1
put(ws_m, r, "Add back: D&A", fmla=lambda i: f"=-{L(i)}{DA_R}"); r += 1
put(ws_m, r, "Add back: SBC", fmla=lambda i: f"=-{L(i)}{SBC_R}"); r += 1
DAR_CF = r
put(ws_m, r, "Change in accounts receivable", vals=None); r += 1
DDR_CF = r
put(ws_m, r, "Change in deferred revenue", vals=None); r += 1
CFO = r
put(ws_m, r, "Cash from operations",
    fmla=lambda i: f"=SUM({L(i)}{NI2}:{L(i)}{DDR_CF})", bold=True); r += 2
CAPEX = r
put(ws_m, r, "Capital expenditure", fmla=lambda i: f"=-{L(i)}{REV}*Inputs!{L(i)}{CAPEX_ROW}"); r += 1
ACQ_CF = r
put(ws_m, r, "Acquisitions & strategic investments (est.)",
    fmla=lambda i: f"=Inputs!{L(i)}{ACQ_ROW}"); r += 1
CFI = r
put(ws_m, r, "Cash from investing",
    fmla=lambda i: f"=SUM({L(i)}{CAPEX}:{L(i)}{ACQ_CF})", bold=True); r += 2
EQ_CF = r
put(ws_m, r, "Equity issuance", fmla=lambda i: f"=Inputs!{L(i)}{EQ_ROW}"); r += 1
DB_CF = r
put(ws_m, r, "Debt drawn", fmla=lambda i: f"=Inputs!{L(i)}{DEBT_ROW}"); r += 1
TD_CF = r
put(ws_m, r, "Employee liquidity / tenders (est.)",
    fmla=lambda i: f"=Inputs!{L(i)}{TEND_ROW}"); r += 1
CFF = r
put(ws_m, r, "Cash from financing",
    fmla=lambda i: f"=SUM({L(i)}{EQ_CF}:{L(i)}{TD_CF})", bold=True); r += 1
DCASH = r
put(ws_m, r, "Change in cash",
    fmla=lambda i: f"={L(i)}{CFO}+{L(i)}{CFI}+{L(i)}{CFF}", bold=True); r += 1
FCF = r
put(ws_m, r, "Free cash flow (CFO + capex)",
    fmla=lambda i: f"={L(i)}{CFO}+{L(i)}{CAPEX}", bold=True, fill=fill_green,
    src="Company confirms FCF positive on TTM and FY2025 bases without magnitude (Feb 9, 2026); level shown is a model output, not a disclosure."); r += 1
FCFM = r
put(ws_m, r, "FCF margin", fmla=lambda i: f"={L(i)}{FCF}/{L(i)}{REV}", fmt=PCT); r += 2

section(ws_m, r, "BALANCE SHEET (closing)"); r += 1
OPEN_E = "Inputs!$E$"
CASH = r
put(ws_m, r, "Cash & investments",
    fmla=lambda i: (f"={OPEN_E}{OPEN_ROW}+{L(i)}{DCASH}" if i == 0
                    else f"={P(i)}{CASH}+{L(i)}{DCASH}"), bold=True); r += 1
AR = r
put(ws_m, r, "Accounts receivable",
    fmla=lambda i: f"={L(i)}{REV}*Inputs!{L(i)}{DSO_ROW}/365"); r += 1
PPE = r
put(ws_m, r, "PP&E, net",
    fmla=lambda i: (f"={OPEN_E}{OPEN_ROW+2}-{L(i)}{CAPEX}+{L(i)}{DA_R}" if i == 0
                    else f"={P(i)}{PPE}-{L(i)}{CAPEX}+{L(i)}{DA_R}")); r += 1
GW = r
put(ws_m, r, "Goodwill & intangibles",
    fmla=lambda i: (f"={OPEN_E}{OPEN_ROW+3}-{L(i)}{ACQ_CF}" if i == 0
                    else f"={P(i)}{GW}-{L(i)}{ACQ_CF}")); r += 1
OA = r
put(ws_m, r, "Other assets", fmla=lambda i: f"={OPEN_E}{OPEN_ROW+4}"); r += 1
TA = r
put(ws_m, r, "Total assets",
    fmla=lambda i: f"=SUM({L(i)}{CASH}:{L(i)}{OA})", bold=True); r += 2
DRB = r
put(ws_m, r, "Deferred revenue",
    fmla=lambda i: f"={L(i)}{REV}*Inputs!{L(i)}{DRD_ROW}/365"); r += 1
OL = r
put(ws_m, r, "Other liabilities", fmla=lambda i: f"={OPEN_E}{OPEN_ROW+6}"); r += 1
DEBTB = r
put(ws_m, r, "Debt",
    fmla=lambda i: (f"={OPEN_E}{OPEN_ROW+7}+{L(i)}{DB_CF}" if i == 0
                    else f"={P(i)}{DEBTB}+{L(i)}{DB_CF}"), bold=True,
    src="~$9.3B by FY2027E: PitchBook deal records, Jan 2025 to Feb 2026."); r += 1
TL = r
put(ws_m, r, "Total liabilities",
    fmla=lambda i: f"=SUM({L(i)}{DRB}:{L(i)}{DEBTB})", bold=True); r += 2
APIC = r
put(ws_m, r, "Paid-in capital (incl. SBC, net of tenders)",
    fmla=lambda i: (f"={OPEN_E}{OPEN_ROW+8}+{L(i)}{EQ_CF}-{L(i)}{SBC_R}+{L(i)}{TD_CF}" if i == 0
                    else f"={P(i)}{APIC}+{L(i)}{EQ_CF}-{L(i)}{SBC_R}+{L(i)}{TD_CF}")); r += 1
RET = r
put(ws_m, r, "Retained earnings / (deficit)",
    fmla=lambda i: (f"={OPEN_E}{OPEN_ROW+9}+{L(i)}{NI}" if i == 0
                    else f"={P(i)}{RET}+{L(i)}{NI}")); r += 1
TE = r
put(ws_m, r, "Total equity",
    fmla=lambda i: f"={L(i)}{APIC}+{L(i)}{RET}", bold=True); r += 1
CHK = r
put(ws_m, r, "Balance check (must be 0)",
    fmla=lambda i: f"=ROUND({L(i)}{TA}-{L(i)}{TL}-{L(i)}{TE},4)",
    fmt='0.0000', fill=fill_warn); r += 2

# back-fill interest / tax rows now that BS rows are known
for i in range(NY):
    col = L(i); pcol = P(i)
    ws_m.cell(IE, C0+i).value = (f"=-{OPEN_E}{OPEN_ROW+7}*Inputs!{col}{IR_ROW}" if i == 0
                                 else f"=-{pcol}{DEBTB}*Inputs!{col}{IR_ROW}")
    ws_m.cell(II, C0+i).value = (f"={OPEN_E}{OPEN_ROW}*Inputs!{col}{YC_ROW}" if i == 0
                                 else f"={pcol}{CASH}*Inputs!{col}{YC_ROW}")
    ws_m.cell(EBT, C0+i).value = f"={col}{EBIT}+{col}{IE}+{col}{II}"
    ws_m.cell(TAXR, C0+i).value = f"=-MAX({col}{EBT},0)*Inputs!{col}{TAX_ROW}"
    ws_m.cell(NI, C0+i).value = f"={col}{EBT}+{col}{TAXR}"
    ws_m.cell(DAR_CF, C0+i).value = (f"=-({col}{AR}-{OPEN_E}{OPEN_ROW+1})" if i == 0
                                     else f"=-({col}{AR}-{pcol}{AR})")
    ws_m.cell(DDR_CF, C0+i).value = (f"={col}{DRB}-{OPEN_E}{OPEN_ROW+5}" if i == 0
                                     else f"={col}{DRB}-{pcol}{DRB}")
ws_m.cell(IE, 2).value = "Interest expense (on opening debt)"
ws_m.cell(II, 2).value = "Interest income (on opening cash)"
ws_m.cell(IE, C0+NY+1, "Convention: interest on opening balances avoids circularity.").font = f_src

# --------------------------------------------------- supporting schedules
r = CHK + 2
section(ws_m, r, "SCHEDULE A: Disclosed run-rate anchors (calibration, not formulas)"); r += 1
anchors = [("Sep 2024 (derived)", 2670, "Implied: $4.0B Sep-25 / 1.50"),
    ("Dec 2024 (derived)", 3100, "Implied: $4.8B Dec-25 / 1.55"),
    ("Feb 2025 (derived)", 3270, "Implied: $5.4B Feb-26 / 1.65"),
    ("Jun 2025 (derived)", 3830, "Implied: $6.9B Jun-26 / 1.80"),
    ("Sep 2025 (disclosed)", 4000, "Company press release, Sep 8, 2025 (+50% YoY; AI line crossed $1.0B)"),
    ("Dec 2025 (disclosed)", 4800, "Company press release, Dec 2025 (+55% YoY)"),
    ("Feb 2026 (disclosed)", 5400, "Company press release, Feb 9, 2026 (+65% YoY; AI $1.4B)"),
    ("Jun 2026 (disclosed)", 6900, "Company disclosure, Jun 16, 2026 (+80% YoY; AI $1.7B; DBSQL $1.5B)")]
ws_m.cell(r, 2, "Point").font = f_hdr; ws_m.cell(r, 2).fill = fill_hdr
ws_m.cell(r, 5, "Annualized run-rate").font = f_hdr; ws_m.cell(r, 5).fill = fill_hdr
ws_m.cell(r, 7, "Source").font = f_hdr; ws_m.cell(r, 7).fill = fill_hdr
r += 1
for i, (pt, v, src) in enumerate(anchors):
    ws_m.cell(r, 2, pt).font = f_lbl
    c = ws_m.cell(r, 5, v); c.number_format = NUM; c.font = f_num
    ws_m.cell(r, 7, src).font = f_src
    if i % 2:
        for col in (2,5,7): ws_m.cell(r, col).fill = fill_soft
    r += 1
r += 1

section(ws_m, r, "SCHEDULE B: Customer cohort build (cross-check of modeled revenue)"); r += 1
years(ws_m, r); r += 1
t10_cnt = [48, 70, 96, 124, 152, 179, 205]
t10_arpu = [27.0, 30.0, 30.0, 31.0, 32.0, 33.0, 34.0]
t1_cnt = [520, 730, 985, 1280, 1600, 1920, 2240]
t1_arpu = [2.75, 2.95, 3.05, 3.15, 3.25, 3.35, 3.45]
tail_cnt = [17.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0]
tail_arpu = [0.052, 0.058, 0.064, 0.070, 0.075, 0.080, 0.085]
T10C = put(ws_m, r, "Customers >$10M / yr (count)", vals=t10_cnt, fmt='0',
    src="70+ disclosed Feb 9, 2026; other years estimated on tier-migration trend."); r += 1
T10A = put(ws_m, r, "Average spend, >$10M tier", vals=t10_arpu, fmt=NUM1,
    src="Estimate; consumption expansion within the tier."); r += 1
T1C = put(ws_m, r, "Customers $1-10M / yr (count)", vals=t1_cnt, fmt='0',
    src="800+ at >$1M incl. the >$10M tier, Feb 9, 2026; growth estimated."); r += 1
T1A = put(ws_m, r, "Average spend, $1-10M tier", vals=t1_arpu, fmt=NUM1,
    src="Estimate."); r += 1
TLC = put(ws_m, r, "Long-tail organizations (thousands)", vals=tail_cnt, fmt='0.0',
    src="20,000+ organizations disclosed Feb 9, 2026."); r += 1
TLA = put(ws_m, r, "Average spend, long tail", vals=tail_arpu, fmt='0.000',
    src="Estimate; self-serve and departmental deployments."); r += 1
IMPL = r
put(ws_m, r, "Implied revenue (cohort build)",
    fmla=lambda i: f"={L(i)}{T10C}*{L(i)}{T10A}+{L(i)}{T1C}*{L(i)}{T1A}+{L(i)}{TLC}*1000*{L(i)}{TLA}",
    bold=True); r += 1
put(ws_m, r, "vs modeled revenue (delta %)",
    fmla=lambda i: f"={L(i)}{IMPL}/{L(i)}{REV}-1", fmt=PCT,
    src="Cross-check only; small residuals accepted. Cohorts are the economic engine, growth rates are the modeling driver."); r += 2

section(ws_m, r, "SCHEDULE C: Revenue by product line"); r += 1
years(ws_m, r); r += 1
ai_sh = [0.20, 0.245, 0.26, 0.27, 0.28, 0.29, 0.30]
sql_sh = [0.20, 0.215, 0.225, 0.235, 0.24, 0.24, 0.24]
AISH = put(ws_m, r, "AI products, % of revenue", vals=ai_sh, fmt=PCT,
    src="AI run-rate: $1.0B Sep-25, $1.4B Feb-26, $1.7B Jun-26 = ~25% of total (company). Forward mix estimated."); r += 1
SQLSH = put(ws_m, r, "Databricks SQL, % of revenue", vals=sql_sh, fmt=PCT,
    src="$1.5B run-rate Jun-2026, doubled YoY (company disclosure, Jun 16, 2026)."); r += 1
put(ws_m, r, "AI products ($M)", fmla=lambda i: f"={L(i)}{REV}*{L(i)}{AISH}"); r += 1
put(ws_m, r, "Databricks SQL ($M)", fmla=lambda i: f"={L(i)}{REV}*{L(i)}{SQLSH}"); r += 1
put(ws_m, r, "Core platform & other ($M)",
    fmla=lambda i: f"={L(i)}{REV}*(1-{L(i)}{AISH}-{L(i)}{SQLSH})"); r += 2

section(ws_m, r, "SCHEDULE D: Funding ladder (completed rounds; feeds nothing, context)"); r += 1
ladder = [("Series A, Sep 2013", 13.9, ""), ("Series B, Jun 2014", 33.4, ""),
    ("Series C, Dec 2016", 60, ""), ("Series D, Sep 2018", 140, ""),
    ("Series E, Jan 2019", 250, ""), ("Series F, Oct 2019", 400, "$6.2B post"),
    ("Series G, Feb 2021", 1000, "$28B post"), ("Series H, Aug 2021", 1600, "$38B post"),
    ("Series I, Nov 2023", 684.6, "$43B post"), ("Series J, Dec 2024", 10230, "$62B post"),
    ("Series K, Sep 2025", 1000, ">$100B post"), ("Series L, Dec 25 + Feb 26", 7000, "$134B post, both closes")]
ws_m.cell(r, 2, "Round").font = f_hdr; ws_m.cell(r, 2).fill = fill_hdr
ws_m.cell(r, 5, "Size ($M)").font = f_hdr; ws_m.cell(r, 5).fill = fill_hdr
ws_m.cell(r, 7, "Post-money").font = f_hdr; ws_m.cell(r, 7).fill = fill_hdr
r += 1
for i, (nm, sz, post) in enumerate(ladder):
    ws_m.cell(r, 2, nm).font = f_lbl
    c = ws_m.cell(r, 5, sz); c.number_format = NUM; c.font = f_num
    ws_m.cell(r, 7, post).font = f_lbl
    if i % 2:
        for col in (2,5,7): ws_m.cell(r, col).fill = fill_soft
    r += 1
ws_m.cell(r, 2, "Lifetime: ~$29.5B total = ~$20.2B equity + ~$9.3B debt (PitchBook 21-deal record, retrieved Jul 21, 2026). "
                "Announced $188B round (Coatue-led, signed Jul 16, 2026) unclosed; excluded everywhere.").font = f_src

# ================================================================ VALUATION
sheet_prep(ws_v, {"A":2,"B":34,"C":12,"D":12,"E":12,"F":12,"G":12,"H":12,"I":12,"J":40})
ws_v.cell(2, 2, "Valuation").font = f_title
ws_v.cell(3, 2, "Anchored on the completed $134B mark (Feb 9, 2026). The announced $188B round (signed Jul 16, 2026, unclosed) is a reference, not an input. "
                "The quality-valuation correlation is embargoed; only the per-point spread is expressed.").font = f_src
r = 5
ws_v.cell(r, 2, "Sensitivity: implied valuation ($B) = mid-2027E run-rate x multiple").font = f_h; r += 1
rr_grid = [9.5, 10.5, 11.5, 12.5, 13.5]
mults = [20, 18, 16, 14, 12, 10]
ws_v.cell(r, 2, "Multiple \\ Run-rate ($B)").font = f_hdr; ws_v.cell(r, 2).fill = fill_hdr
for j, rrv in enumerate(rr_grid):
    c = ws_v.cell(r, 3+j, rrv); c.font = f_hdr; c.fill = fill_hdr; c.number_format = NUM1
r += 1
GRID0 = r
for i, m in enumerate(mults):
    c = ws_v.cell(r, 2, m); c.number_format = MULT; c.font = f_lblb
    for j in range(len(rr_grid)):
        cc = ws_v.cell(r, 3+j, f"={get_column_letter(3+j)}${GRID0-1}*$B{r}")
        cc.number_format = NUM; cc.font = f_num
        if m in (14, 16) and rr_grid[j] == 11.5:
            cc.fill = fill_green; cc.font = f_numb
    r += 1
ws_v.cell(r, 2, "Green: base intersection (~$11.5B at 14-16x, a de-rate from today's 19.4x). Bear $115-130B; Bull $205B+.").font = f_src
r += 2
ws_v.cell(r, 2, "Quality-adjusted pricing (per-point; the only cleared expression)").font = f_h; r += 1
pp = [("Databricks", 134, 8.81), ("Anthropic", 965, 8.20), ("OpenAI", 852, 4.53),
      ("xAI (implied, est.)", 1550, 4.49)]
for h, col in [("Company", 2), ("Mark ($B)", 3), ("AIBQ", 4), ("$B per point", 5)]:
    c = ws_v.cell(r, col, h); c.font = f_hdr; c.fill = fill_hdr
r += 1
for i, (nm, mk, sc) in enumerate(pp):
    ws_v.cell(r, 2, nm).font = f_lblb if i == 0 else f_lbl
    ws_v.cell(r, 3, mk).number_format = NUM
    ws_v.cell(r, 4, sc).number_format = '0.00'
    c = ws_v.cell(r, 5, f"=C{r}/D{r}"); c.number_format = NUM1
    if i == 0:
        for col in (2,3,4,5): ws_v.cell(r, col).fill = fill_green
    r += 1
ws_v.cell(r, 2, "Marks per company announcements / PitchBook, Mar-Jul 2026; xAI slice inside listed SpaceX is an estimate. "
                "No correlation statistic is computed or derivable from this table.").font = f_src
r += 2
ws_v.cell(r, 2, "Growth-adjusted comparison").font = f_h; r += 1
ga_rows = [("", "EV / mark ($B)", "Fwd revenue ($B)", "Multiple", "Growth", "x per growth pt"),
    ("Databricks", 134, 6.9, "=C%d/D%d", 0.80, "=E%d/F%d*1"),
    ("Snowflake", 89, 5.84, "=C%d/D%d", 0.31, "=E%d/F%d*1")]
for j, h in enumerate(ga_rows[0]):
    c = ws_v.cell(r, 2+j, h); c.font = f_hdr; c.fill = fill_hdr
r += 1
for nm, ev, fwd, mf, gr, gf in ga_rows[1:]:
    ws_v.cell(r, 2, nm).font = f_lblb
    ws_v.cell(r, 3, ev).number_format = NUM
    ws_v.cell(r, 4, fwd).number_format = NUM1
    ws_v.cell(r, 5, f"=C{r}/D{r}").number_format = MULT
    ws_v.cell(r, 6, gr).number_format = PCT
    ws_v.cell(r, 7, f"=E{r}/(F{r}*100)").number_format = '0.00"x"'
    r += 1
ws_v.cell(r, 2, "Snowflake: FY27 product revenue guide raised May 27, 2026 (8-K); EV from market data less est. net cash, Jul 7, 2026. "
                "Growth-adjusted, the buyer pays ~half as much per point of growth for Databricks.").font = f_src

# ================================================================ OUTPUTS
sheet_prep(ws_out, {"A":2,"B":30,"C":11,"D":11,"E":11,"F":11,"G":11,"H":11,
                    "I":11,"J":11,"K":11})
ws_out.cell(2, 2, "Dashboard").font = f_title
ws_out.cell(3, 2, "All figures USD millions unless stated; scenario per Inputs!E5 Driver Switch.").font = f_src
years(ws_out, 5)
r = 6
rows_out = [
    ("Revenue", REV, NUM, False), ("Revenue growth", GROWTH, PCT, False),
    ("Gross margin", GMR, PCT, False), ("EBITDA", EBITDA, NUM, False),
    ("EBIT", EBIT, NUM, False), ("Net income", NI, NUM, False),
    ("Free cash flow", FCF, NUM, True), ("FCF margin", FCFM, PCT, False),
    ("Cash & investments (closing)", CASH, NUM, False),
    ("Debt (closing)", DEBTB, NUM, False),
    ("Deferred revenue (closing)", DRB, NUM, False),
]
OUT0 = r
for nm, srcrow, fmt, hl in rows_out:
    put(ws_out, r, nm, fmla=lambda i, s=srcrow: f"=Model!{L(i)}{s}", fmt=fmt,
        bold=hl, fill=fill_green if hl else None)
    r += 1
CHK_OUT = r
put(ws_out, r, "Balance sheet check (0 = balanced)",
    fmla=lambda i: f"=Model!{L(i)}{CHK}", fmt='0.0000', fill=fill_warn); r += 2

ch = BarChart(); ch.type = "col"; ch.title = "Revenue ($M)"
ch.height = 7; ch.width = 15; ch.gapWidth = 60; ch.legend = None
data = Reference(ws_out, min_col=C0, max_col=C0+NY-1, min_row=OUT0, max_row=OUT0)
cats = Reference(ws_out, min_col=C0, max_col=C0+NY-1, min_row=5, max_row=5)
ch.add_data(data, from_rows=True, titles_from_data=False)
ch.set_categories(cats)
ch.series[0].graphicalProperties.solidFill = SLATE
ws_out.add_chart(ch, "B" + str(r + 1))
ch2 = LineChart(); ch2.title = "Margins (%)"
ch2.height = 7; ch2.width = 15
for rr, nm in [(OUT0+2, "Gross margin"), (OUT0+7, "FCF margin")]:
    d = Reference(ws_out, min_col=C0, max_col=C0+NY-1, min_row=rr, max_row=rr)
    ch2.add_data(d, from_rows=True, titles_from_data=False)
ch2.set_categories(cats)
ch2.series[0].graphicalProperties.line.solidFill = NAVY
ch2.series[1].graphicalProperties.line.solidFill = GREEN
ws_out.add_chart(ch2, "H" + str(r + 1))

# ================================================================ COVER
sheet_prep(ws_cover, {"A":3,"B":4,"C":44,"D":14,"E":30,"F":6,"G":30,"H":16})
ws_cover.cell(4, 3, "Databricks, Inc.").font = Font(name="Georgia", size=24, bold=True, color=NAVY)
ws_cover.cell(5, 3, "Three-Statement Operating Model").font = Font(name="Georgia", size=13, color=SLATE, italic=True)
ws_cover.cell(6, 3, "Companion to: Brick by Brick, an institutional deep dive. July 10, 2026; updated July 21, 2026.").font = f_src
ws_cover.cell(7, 3, "All figures USD millions; fiscal years end January 31. FY2025A / FY2026A are "
                    "estimates calibrated to disclosed run-rates; Databricks publishes no financial statements.").font = f_src
r = 10
ws_cover.cell(r, 3, "Table of Contents").font = f_h; r += 1
for nm, desc in [("Outputs", "Dashboard: summary statements, margins, charts"),
                 ("Inputs", "Driver switch (Best / Base / Worst), sourced assumptions, opening balance sheet"),
                 ("Model", "Income statement, cash flow, balance sheet + Schedules A-D"),
                 ("Valuation", "Sensitivity grid, per-point pricing, growth-adjusted comparison")]:
    ws_cover.cell(r, 3, nm).font = f_lblb
    ws_cover.cell(r, 5, desc).font = f_lbl
    r += 1
r += 1
ws_cover.cell(r, 3, "Model Checks").font = f_h; r += 1
ws_cover.cell(r, 3, "Balance sheet balanced in every year?").font = f_lbl
c = ws_cover.cell(r, 5, f"=IF(AND(MAX(Outputs!{L(0)}{CHK_OUT}:{L(NY-1)}{CHK_OUT})<0.001,"
                        f"MIN(Outputs!{L(0)}{CHK_OUT}:{L(NY-1)}{CHK_OUT})>-0.001),\"OK\",\"ERROR\")")
c.font = Font(name="Calibri", size=10, bold=True, color=GREEN); r += 1
ws_cover.cell(r, 3, "Scenario in use (1 Best / 2 Base / 3 Worst)").font = f_lbl
ws_cover.cell(r, 5, "=Inputs!E5").font = f_lblb; r += 1
ws_cover.cell(r, 3, "FCF positive in FY2025A/FY2026A (disclosed fact)?").font = f_lbl
ws_cover.cell(r, 5, f"=IF(AND(Model!{L(0)}{FCF}>0,Model!{L(1)}{FCF}>0),\"OK\",\"REVIEW\")").font = f_lblb; r += 2
ws_cover.cell(r, 3, "Sourcing: company press releases and disclosures (Sep 2024 to Jun 2026); PitchBook deal records "
                    "(entity 59199-40, retrieved Jul 21, 2026); SEC EDGAR (CIK 1587468); public cloud price lists. "
                    "All non-disclosed lines are labeled estimates.").font = f_src

out = "../output/Databricks_Operating_Model_Jul2026.xlsx"
wb.save(out)
print("saved", out)

# ---- print base-case summary for the report ----
hdr = ["", *FY]
print("\n" + " | ".join(hdr))
def row(nm, vals, pct=False):
    print(nm + " | " + " | ".join(
        (f"{v*100:,.1f}%" if pct else f"{v:,.0f}") for v in vals))
row("Revenue", rev)
row("Growth", [0.59, 0.588] + g_base, pct=True)
row("Gross margin", gm, pct=True)
row("EBIT", B["ebit"])
row("EBIT margin", [B["ebit"][i]/rev[i] for i in range(NY)], pct=True)
row("Net income", B["ni"])
row("FCF", B["fcf"])
row("FCF margin", [B["fcf"][i]/rev[i] for i in range(NY)], pct=True)
row("Cash close", B["cash"])
row("Debt close", B["debt"])
row("Deferred revenue", B["dr"])
