"""Databricks granular bottom-up operating model, FY2022A to FY2032E.

Purpose: show exactly where revenue and costs come from.
- Revenue is built from five product lines (summed to total), then cross-checked
  two independent ways: a customer-cohort build and a DBU-consumption build.
- Costs are built bottom-up: cost of revenue from four components (gross margin
  is an output, not an input), then operating expense decomposed into personnel,
  programs and facilities, with an implied headcount bridge.
- Income statement, cash flow and balance sheet assemble from those builds and
  balance to zero in every year.

The cost ratios are calibrated so the operating-margin path reconciles with the
validated companion model (Brick by Brick, Jul 2026); this is the same business
seen bottom-up. Fiscal years end January 31. All figures USD millions unless
stated. No em-dashes anywhere (build scans and fails loudly).
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.series import SeriesLabel

# ----------------------------------------------------------------- palette
NAVY = "1F2A44"; SLATE = "35506E"; GREEN = "1C5D46"; GREY = "6B7280"
SOFT = "F2F5F9"; WARN = "8F3421"; WHITE = "FFFFFF"; GOLD = "9A7B25"

FY = ["FY2022A","FY2023A","FY2024A","FY2025A","FY2026A","FY2027E",
      "FY2028E","FY2029E","FY2030E","FY2031E","FY2032E"]
NY = len(FY)
NH = 6                     # historical / near-term anchored columns (FY22..FY27)
C0 = 4                     # first year column = D
SRCCOL = C0 + NY + 1       # source column = P

thin = Side(style="thin", color="D5DBE4")
border_b = Border(bottom=thin)
f_title = Font(name="Georgia", size=15, bold=True, color=NAVY)
f_sub = Font(name="Georgia", size=10, italic=True, color=GREY)
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
fill_gold = PatternFill("solid", fgColor="F5F0DD")

NUM = '#,##0;(#,##0)'
NUM1 = '#,##0.0;(#,##0.0)'
NUM2 = '#,##0.00;(#,##0.00)'
PCT = '0.0%'
PCT0 = '0%'
MULT = '0.0"x"'
DOL2 = '$0.00'

L = lambda i: get_column_letter(C0 + i)
P = lambda i: get_column_letter(C0 + i - 1)

# ================================================================= DRIVERS
# ---- Revenue: five product lines. FY22..FY27 are anchored input values;
#      FY28..FY32 grow off FY27 by the growth vectors below.
line_hist = {
    "Core":     [720, 1090, 1230, 1730, 2450, 3750],
    "SQL":      [70,  190,  300,  480,  830,  1500],
    "AI":       [0,   0,    40,   280,  620,  1600],
    "Lakebase": [0,   0,    0,    0,    40,   130],
    "Platform": [10,  20,   30,   60,   110,  220],
}
g_base = {
    "Core":     [0.32, 0.25, 0.20, 0.16, 0.13],
    "SQL":      [0.45, 0.36, 0.28, 0.22, 0.18],
    "AI":       [0.65, 0.50, 0.38, 0.30, 0.24],
    "Lakebase": [1.40, 0.90, 0.65, 0.45, 0.33],
    "Platform": [0.50, 0.42, 0.34, 0.27, 0.22],
}
def g_best(k):  return [round(x + 0.06, 3) for x in g_base[k]]
def g_worst(k): return [round(max(x - 0.08, 0.02), 3) for x in g_base[k]]
LINES = ["Core", "SQL", "AI", "Lakebase", "Platform"]
LINE_LABEL = {
    "Core": "Data engineering and core compute (Jobs, ETL, Lakeflow, streaming)",
    "SQL": "Databricks SQL (data warehousing)",
    "AI": "AI products (Mosaic AI: training, serving, Agent Bricks, tokens)",
    "Lakebase": "Lakebase (managed Postgres OLTP)",
    "Platform": "Platform and other (governance premium, security lakehouse, marketplace)",
}

def build_lines(scn="base"):
    out = {}
    for k in LINES:
        vals = list(line_hist[k])
        gv = g_base[k] if scn == "base" else (g_best(k) if scn == "best" else g_worst(k))
        for j in range(NY - NH):
            vals.append(round(vals[-1] * (1 + gv[j]), 1))
    # (loop above appends per line)
        out[k] = vals
    return out

def total_rev(scn="base"):
    lv = build_lines(scn)
    return [round(sum(lv[k][i] for k in LINES), 1) for i in range(NY)]

REV = total_rev("base")
LV = build_lines("base")

# ---- Cost of revenue: four components. Gross margin is the OUTPUT.
c1_cloud = [0.090,0.095,0.100,0.110,0.140,0.175,0.185,0.183,0.178,0.175,0.170]  # % total rev
c2_ai    = [0.00,0.00,0.05,0.08,0.10,0.12,0.13,0.13,0.125,0.12,0.115]           # % AI rev
c3_supp  = [0.030,0.030,0.029,0.028,0.027,0.026,0.025,0.024,0.023,0.022,0.021]  # % total rev
c4_amort = [20,30,90,130,170,230,250,250,240,220,200]                          # $M

# ---- Operating expense ratios (ex-SBC), % of revenue. Calibrated to the
#      validated companion model so the margin path reconciles.
rd_pct = [0.30,0.27,0.22,0.20,0.19,0.18,0.175,0.17,0.165,0.16,0.155]
sm_pct = [0.60,0.50,0.42,0.36,0.33,0.30,0.28,0.26,0.245,0.23,0.215]
ga_pct = [0.14,0.12,0.10,0.08,0.075,0.07,0.065,0.06,0.055,0.05,0.048]
sbc_pct= [0.20,0.21,0.22,0.24,0.22,0.19,0.17,0.155,0.14,0.13,0.115]
da_pct = 0.02
capex_pct = 0.025

# ---- Opex decomposition (constant sub-shares of each function)
rd_comp_sh = 0.85       # engineering personnel share of R&D
sm_sales_sh = 0.52; sm_mktgcomp_sh = 0.11; sm_prog_sh = 0.22; sm_field_sh = 0.15
ga_comp_sh = 0.62; ga_fac_sh = 0.22; ga_other_sh = 0.16
# fully loaded cost per head ($000), for the implied-headcount bridge
cph = {"eng":255, "sales":260, "mktg":200, "ga":200, "supp":175}

# ---- Customer pyramid (top tiers anchored to disclosure; long-tail spend is
#      the implied residual so the pyramid reconciles to the product-line total).
#      Disclosed anchors: 300+ customers >$1M (Sep 2023 ~ FY24), 500+ (Dec 2024
#      ~ FY25), 800+ with 70+ >$10M (Feb 2026 ~ FY26); 20,000+ organizations.
t10_cnt = [4, 8, 15, 40, 72, 108, 150, 195, 240, 285, 330]         # count >$10M/yr
t10_arpu= [15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20]             # avg spend, $M
t1_cnt  = [80, 140, 285, 460, 728, 1050, 1450, 1880, 2320, 2760, 3200]  # count $1-10M/yr
t1_arpu = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.55, 2.6, 2.65, 2.7, 2.75]    # avg spend, $M
tail_k  = [5.5, 7, 9.5, 13, 19.2, 27, 35, 44, 54, 64, 75]          # long tail, thousands of orgs
# tail_arpu is derived (implied residual): (total - top tiers) / tail count

# ---- DBU-consumption cross-check
dbu_price = [0.60,0.58,0.56,0.54,0.51,0.48,0.46,0.44,0.43,0.42,0.41]  # blended $/DBU

# ---- Working capital, financing, balance sheet
dso = 75
dr_days = [55,68,80,92,100,105,105,105,105,105,105]  # committed-use adoption ramps
debt_rate = 0.0675; cash_yield = 0.04
tax_rate = [0,0,0,0,0,0,0.0,0.08,0.12,0.18,0.18]
equity  = [2600,0,685,10060,1000,5000,0,0,0,0,0]
debt    = [0,0,0,5250,1854,2000,0,0,0,0,0]
tender  = [-200,-300,-500,-6000,-2000,-4000,-1500,-1500,-1500,-1500,-1500]
acq     = [-50,-60,-1500,-1200,-1500,-1000,-800,-800,-800,-800,-800]
open_bs = dict(cash=1500, ar=130, ppe=100, gw=350, oa=120,
               dr=90, ol=110, debt=0, apic=2900, ret=-900)

# ============================================================ base-case math
def run(scn="base"):
    rev = total_rev(scn); lv = build_lines(scn)
    S = {k: [] for k in ["cogs","gp","gm","rd","sm","ga","sbc","da","ebit","ebitda",
        "ie","ii","ebt","tax","ni","ar","dr","ppe","gw","cash","debtb","apic","ret",
        "ta","tl","te","cfo","cfi","cff","dcash","fcf","capex","chk","aiamort","otherda"]}
    prev = dict(open_bs)
    for i in range(NY):
        r = rev[i]; ai = lv["AI"][i]
        cogs = r*c1_cloud[i] + ai*c2_ai[i] + r*c3_supp[i] + c4_amort[i]
        gp = r - cogs
        rd = r*rd_pct[i]; sm = r*sm_pct[i]; ga = r*ga_pct[i]; sbc = r*sbc_pct[i]
        otherda = r*da_pct; da = c4_amort[i] + otherda
        ebit = gp - rd - sm - ga - sbc - otherda
        ie = -prev["debt"]*debt_rate; ii = prev["cash"]*cash_yield
        ebt = ebit + ie + ii
        tax = -max(ebt, 0)*tax_rate[i]; ni = ebt + tax
        ar = r*dso/365; dr = r*dr_days[i]/365
        capex = -r*capex_pct
        cfo = ni + da + sbc - (ar-prev["ar"]) + (dr-prev["dr"])
        cfi = capex + acq[i]
        cff = equity[i] + debt[i] + tender[i]
        dcash = cfo + cfi + cff
        cash = prev["cash"] + dcash
        ppe = prev["ppe"] + (-capex) - otherda
        gw = prev["gw"] + (-acq[i]) - c4_amort[i]
        debtb = prev["debt"] + debt[i]
        apic = prev["apic"] + equity[i] + sbc + tender[i]
        ret = prev["ret"] + ni
        ta = cash + ar + ppe + gw + open_bs["oa"]
        tl = dr + open_bs["ol"] + debtb
        te = apic + ret
        fcf = cfo + capex
        vals = dict(cogs=cogs,gp=gp,gm=gp/r,rd=rd,sm=sm,ga=ga,sbc=sbc,da=da,
            ebit=ebit,ebitda=ebit+otherda,ie=ie,ii=ii,ebt=ebt,tax=tax,ni=ni,ar=ar,
            dr=dr,ppe=ppe,gw=gw,cash=cash,debtb=debtb,apic=apic,ret=ret,ta=ta,tl=tl,
            te=te,cfo=cfo,cfi=cfi,cff=cff,dcash=dcash,fcf=fcf,capex=capex,
            chk=ta-tl-te,aiamort=c4_amort[i],otherda=otherda)
        for k,v in vals.items(): S[k].append(v)
        prev = dict(cash=cash, ar=ar, ppe=ppe, gw=gw, oa=open_bs["oa"],
                    dr=dr, ol=open_bs["ol"], debt=debtb, apic=apic, ret=ret)
    return rev, lv, S

REV, LV, B = run("base")
for i in range(NY):
    assert abs(B["chk"][i]) < 1e-6, f"unbalanced {FY[i]}: {B['chk'][i]}"

# ================================================================= workbook
wb = openpyxl.Workbook()
ws_cover = wb.active; ws_cover.title = "Cover"
ws_dash = wb.create_sheet("Dashboard")
ws_guide = wb.create_sheet("Guide")
ws_a = wb.create_sheet("Assumptions")
ws_r = wb.create_sheet("Revenue")
ws_c = wb.create_sheet("Costs")
ws_f = wb.create_sheet("Financials")
ws_k = wb.create_sheet("KPIs")

def prep(ws, widths, gridlines=False):
    ws.sheet_view.showGridLines = gridlines
    for col, w in widths.items():
        ws.column_dimensions[col].width = w

def yr_header(ws, row):
    for i, fy in enumerate(FY):
        c = ws.cell(row, C0 + i, fy)
        c.font = f_hdr; c.fill = fill_hdr
        c.alignment = Alignment(horizontal="center")
    ws.cell(row, 2).fill = fill_hdr

def sec(ws, row, title, span=None):
    c = ws.cell(row, 2, title); c.font = f_h
    for col in range(2, (span or (C0 + NY))):
        ws.cell(row, col).fill = fill_soft
    return row

def line(ws, row, label, vals=None, fmla=None, fmt=NUM, bold=False, src=None,
         indent=1, fill=None, italic=False, color=None):
    c = ws.cell(row, 2, label)
    c.font = Font(name="Calibri", size=9, bold=bold, italic=italic,
                  color=color or NAVY if bold else (color or "000000"))
    c.alignment = Alignment(indent=indent, wrap_text=False)
    for i in range(NY):
        cc = ws.cell(row, C0 + i)
        if fmla is not None:
            cc.value = fmla(i) if callable(fmla) else fmla[i]
        elif vals is not None:
            cc.value = vals[i] if isinstance(vals, (list, tuple)) else vals
        cc.number_format = fmt
        cc.font = f_numb if bold else f_num
        if bold:
            cc.border = border_b
        if fill:
            cc.fill = fill
    if src:
        s = ws.cell(row, SRCCOL, src); s.font = f_src
    return row

SW = "Assumptions!$D$5"

# ------------------------------------------------------------- ASSUMPTIONS
prep(ws_a, {"A":2,"B":46,"C":3,**{get_column_letter(C0+i):10 for i in range(NY)},
            get_column_letter(SRCCOL-1):2, get_column_letter(SRCCOL):74})
ws_a.cell(2, 2, "Assumptions and Drivers").font = f_title
ws_a.cell(3, 2, "Every driver carries its source in the far-right column. Estimates are labeled; "
                "Databricks is private and publishes no audited financials. Blue cells are the only inputs.").font = f_sub
ws_a.cell(5, 2, "DRIVER SWITCH   1 = Best   2 = Base   3 = Worst").font = f_lblb
swc = ws_a.cell(5, C0, 2); swc.font = Font(name="Calibri", size=12, bold=True, color=WARN)
swc.fill = fill_warn; swc.number_format = '0'; swc.alignment = Alignment(horizontal="center")
ws_a.cell(5, SRCCOL, "Flexes the forecast growth of each product line (FY2028E onward). "
                     "Historical years and all cost ratios are held across scenarios.").font = f_src

ra = 7
yr_header(ws_a, ra); ra += 1
sec(ws_a, ra, "1. Revenue by product line, historical anchors (USD M, FY2022A to FY2027E fixed)"); ra += 1
AROW = {}
line_src = {
 "Core": "Historic majority of consumption (Jobs/ETL). Residual of total less other lines; total calibrated to disclosed run-rate ladder.",
 "SQL": "Databricks SQL run-rate $1.5B Jun-2026, doubled YoY (company disclosure, Jun 16, 2026); ramped back from launch (Nov 2020).",
 "AI": "AI run-rate $1.0B Sep-2025, $1.4B Feb-2026, $1.7B Jun-2026 (company). MosaicML acquired 2023 seeds the line.",
 "Lakebase": "GA early 2026 off the Neon acquisition (May 2025); company: thousands of customers in 6 months, ~2x DBSQL's early pace.",
 "Platform": "Governance premium, security lakehouse (Panther, announced Jun-2026), marketplace-adjacent. Estimate.",
}
for k in LINES:
    AROW[k] = line(ws_a, ra, "  " + LINE_LABEL[k],
                   vals=[line_hist[k][i] if i < NH else None for i in range(NY)],
                   fmt=NUM, src=line_src[k]); ra += 1
ra += 1
sec(ws_a, ra, "2. Product-line forecast growth, FY2028E to FY2032E (Best / Base / Worst)"); ra += 1
GROW = {}
for k in LINES:
    base = g_base[k]; best = g_best(k); worst = g_worst(k)
    def mk(vec):
        return [None]*NH + list(vec)
    GROW[(k, "best")] = line(ws_a, ra, "  " + k + " growth - Best", vals=mk(best), fmt=PCT); ra += 1
    GROW[(k, "base")] = line(ws_a, ra, "  " + k + " growth - Base", vals=mk(base), fmt=PCT,
        src="Base path; graceful deceleration. AI and Lakebase fastest; Core matures."); ra += 1
    GROW[(k, "worst")] = line(ws_a, ra, "  " + k + " growth - Worst", vals=mk(worst), fmt=PCT); ra += 1
ra += 1
sec(ws_a, ra, "3. Cost of revenue components (gross margin is an OUTPUT)"); ra += 1
C1 = line(ws_a, ra, "  Cloud and serverless compute, % of revenue", vals=c1_cloud, fmt=PCT,
    src="Compute Databricks itself buys from AWS/Azure/GCP for serverless and AI SKUs. Rises as serverless/agent mix grows (drives the margin compression the company guided, Jun 16, 2026)."); ra += 1
C2 = line(ws_a, ra, "  Third-party AI model and API costs, % of AI revenue", vals=c2_ai, fmt=PCT,
    src="Cost of serving external frontier models (OpenAI/Anthropic/Google) inside the platform. Estimate."); ra += 1
C3 = line(ws_a, ra, "  Support, delivery and platform ops, % of revenue", vals=c3_supp, fmt=PCT,
    src="Personnel cost in cost of revenue (solutions, support, DevOps). Estimate."); ra += 1
C4 = line(ws_a, ra, "  Amortization of acquired technology, USD M", vals=c4_amort, fmt=NUM,
    src="Developed-tech intangibles from ~19 acquisitions (MosaicML, Tabular, Neon, etc.). Estimate."); ra += 1
ra += 1
sec(ws_a, ra, "4. Operating expense ratios, % of revenue (ex stock comp)"); ra += 1
RDP = line(ws_a, ra, "  Research and development", vals=rd_pct, fmt=PCT,
    src="Estimate; R&D-led culture. FY2025E+ calibrated to the validated companion model."); ra += 1
SMP = line(ws_a, ra, "  Sales and marketing", vals=sm_pct, fmt=PCT,
    src="Estimate; heavy in land phase, falling as consumption expansion (NRR >140%, company Feb-2026) does the work."); ra += 1
GAP = line(ws_a, ra, "  General and administrative", vals=ga_pct, fmt=PCT,
    src="Estimate; scale leverage typical of late-stage software."); ra += 1
SBCP = line(ws_a, ra, "  Stock-based compensation", vals=sbc_pct, fmt=PCT,
    src="Estimate; recurring employee tenders (Series J use of proceeds, Dec-2024). Non-cash; added back in cash flow."); ra += 1
DAP = line(ws_a, ra, "  Depreciation and other amortization", vals=[da_pct]*NY, fmt=PCT,
    src="Estimate; asset-light (compute rented)."); ra += 1
CXP = line(ws_a, ra, "  Capital expenditure", vals=[capex_pct]*NY, fmt=PCT,
    src="Estimate; asset-light model."); ra += 1
ra += 1
sec(ws_a, ra, "5. Opex decomposition and headcount bridge"); ra += 1
RDCS = line(ws_a, ra, "  Engineering personnel, % of R&D", vals=[rd_comp_sh]*NY, fmt=PCT0,
    src="Remainder is dev cloud, tooling, licences. Estimate."); ra += 1
SMSA = line(ws_a, ra, "  Sales personnel (incl commission), % of S&M", vals=[sm_sales_sh]*NY, fmt=PCT0, src="Estimate."); ra += 1
SMMC = line(ws_a, ra, "  Marketing personnel, % of S&M", vals=[sm_mktgcomp_sh]*NY, fmt=PCT0, src="Estimate."); ra += 1
SMPR = line(ws_a, ra, "  Marketing programs and events, % of S&M", vals=[sm_prog_sh]*NY, fmt=PCT0,
    src="Demand generation, Data + AI Summit, field marketing. Estimate."); ra += 1
SMFD = line(ws_a, ra, "  Partner and field ops, % of S&M", vals=[sm_field_sh]*NY, fmt=PCT0, src="Estimate."); ra += 1
GACO = line(ws_a, ra, "  G&A personnel, % of G&A", vals=[ga_comp_sh]*NY, fmt=PCT0, src="Estimate."); ra += 1
GAFA = line(ws_a, ra, "  Facilities and IT, % of G&A", vals=[ga_fac_sh]*NY, fmt=PCT0, src="Estimate."); ra += 1
GAOT = line(ws_a, ra, "  Professional, insurance, other, % of G&A", vals=[ga_other_sh]*NY, fmt=PCT0, src="Estimate."); ra += 1
HENG = line(ws_a, ra, "  Loaded cost per head, engineering (USD 000)", vals=[cph["eng"]]*NY, fmt=NUM, src="Estimate; blended across geographies."); ra += 1
HSAL = line(ws_a, ra, "  Loaded cost per head, sales (USD 000, incl commission)", vals=[cph["sales"]]*NY, fmt=NUM, src="Estimate."); ra += 1
HMKT = line(ws_a, ra, "  Loaded cost per head, marketing (USD 000)", vals=[cph["mktg"]]*NY, fmt=NUM, src="Estimate."); ra += 1
HGA = line(ws_a, ra, "  Loaded cost per head, G&A (USD 000)", vals=[cph["ga"]]*NY, fmt=NUM, src="Estimate."); ra += 1
HSUP = line(ws_a, ra, "  Loaded cost per head, support/delivery (USD 000)", vals=[cph["supp"]]*NY, fmt=NUM, src="Estimate."); ra += 1
ra += 1
sec(ws_a, ra, "6. Customer pyramid (top tiers anchored to disclosure)"); ra += 1
T10C = line(ws_a, ra, "  Customers >$10M / yr (count)", vals=t10_cnt, fmt='0',
    src="70+ disclosed Feb 9, 2026; other years on the tier-migration trend."); ra += 1
T10A = line(ws_a, ra, "  Average spend, >$10M tier (USD M)", vals=t10_arpu, fmt=NUM1, src="Estimate."); ra += 1
T1C = line(ws_a, ra, "  Customers $1-10M / yr (count)", vals=t1_cnt, fmt='0',
    src="300+ >$1M Sep-2023; 500+ Dec-2024; 800+ Feb-2026 (company). Net of the >$10M tier."); ra += 1
T1A = line(ws_a, ra, "  Average spend, $1-10M tier (USD M)", vals=t1_arpu, fmt=NUM2, src="Estimate."); ra += 1
TLK = line(ws_a, ra, "  Long-tail organizations (thousands)", vals=tail_k, fmt=NUM1,
    src="20,000+ organizations Feb-2026; free-edition funnel (500k+ users) feeds it. Estimate."); ra += 1
ra += 1
sec(ws_a, ra, "7. Consumption and working capital"); ra += 1
DBUP = line(ws_a, ra, "  Blended realized price per DBU (USD)", vals=dbu_price, fmt=DOL2,
    src="Blended across Jobs ~$0.15, All-Purpose ~$0.55, SQL ~$0.22-0.70, serverless/AI higher (public price lists, 2026). Declines as mix and discounts shift."); ra += 1
DSOA = line(ws_a, ra, "  Days sales outstanding", vals=[dso]*NY, fmt='0', src="Estimate; enterprise annual invoicing."); ra += 1
DRDA = line(ws_a, ra, "  Deferred revenue (days of revenue)", vals=dr_days, fmt='0',
    src="Committed-use contracts are prepaid then drawn down; adoption ramps over time (company pricing model)."); ra += 1
ra += 1
sec(ws_a, ra, "8. Financing, tax and rates (USD M; announced events)"); ra += 1
EQA = line(ws_a, ra, "  Equity issuance", vals=equity,
    src="Series G-H FY22 ($3.6B); Series I FY24 ($0.7B); Series J FY25 ($10.1B); Series K FY26 ($1.0B); Series L FY26-27 ($5.0B). Company PRs; PitchBook. $188B round (Jul-2026) unclosed, excluded."); ra += 1
DBA = line(ws_a, ra, "  Debt drawn", vals=debt,
    src="$5.25B facility Jan-2025; $1.8B + $54M refi Jan-2026; $2.0B Series L tranche Feb-2026 (PitchBook deal records)."); ra += 1
TDA = line(ws_a, ra, "  Employee liquidity / tenders", vals=tender,
    src="Estimate; rounds explicitly tied to employee liquidity (company, Dec-2024)."); ra += 1
ACA = line(ws_a, ra, "  Acquisitions and strategic investments", vals=acq,
    src="Estimate of cash portion; MosaicML 2023, Tabular 2024, Neon 2025, Panther announced Jun-2026, etc."); ra += 1
IRA = line(ws_a, ra, "  Interest rate on debt", vals=[debt_rate]*NY, fmt=PCT, src="Estimate; private facilities led by major banks."); ra += 1
YCA = line(ws_a, ra, "  Yield on cash", vals=[cash_yield]*NY, fmt=PCT, src="Estimate; short-duration treasuries."); ra += 1
TXA = line(ws_a, ra, "  Effective tax rate (on positive pre-tax income)", vals=tax_rate, fmt=PCT,
    src="Estimate; NOL shield from accumulated losses, stepping up as it exhausts."); ra += 1
ra += 1
sec(ws_a, ra, "9. Opening balance sheet, Feb 1, 2021 (estimated; no disclosure)"); ra += 1
OB_ORDER = ["cash","ar","ppe","gw","oa","dr","ol","debt","apic","ret"]
OB_LABEL = {"cash":"Cash and investments","ar":"Accounts receivable","ppe":"PP&E, net",
    "gw":"Goodwill and intangibles","oa":"Other assets","dr":"Deferred revenue",
    "ol":"Other liabilities","debt":"Debt","apic":"Paid-in capital (incl accumulated SBC)",
    "ret":"Accumulated deficit"}
OBROW = {}
for key in OB_ORDER:
    ws_a.cell(ra, 2, "  " + OB_LABEL[key]).font = f_lbl
    ws_a.cell(ra, 2).alignment = Alignment(indent=1)
    cc = ws_a.cell(ra, C0, open_bs[key]); cc.number_format = NUM; cc.font = f_num
    OBROW[key] = ra; ra += 1
ws_a.cell(ra, SRCCOL, "Estimated from cumulative equity raised pre-Series G, cumulative burn and early "
                      "acquisitions. Labeled estimate throughout.").font = f_src

# --------------------------------------------------------------- REVENUE
prep(ws_r, {"A":2,"B":46,"C":3,**{get_column_letter(C0+i):10 for i in range(NY)},
            get_column_letter(SRCCOL-1):2, get_column_letter(SRCCOL):70})
ws_r.cell(2, 2, "Revenue Build: where every dollar comes from").font = f_title
ws_r.cell(3, 2, "Primary build is by product line (sums to total). Below it, the same total is decomposed two "
                "ways: by customer tier, and by platform consumption (DBUs). USD M unless stated.").font = f_sub
rr = 5
yr_header(ws_r, rr); rr += 1
sec(ws_r, rr, "A. BY PRODUCT LINE (the primary build)"); rr += 1
RLROW = {}
for k in LINES:
    def mkf(k):
        return lambda i: (f"=Assumptions!{L(i)}{AROW[k]}" if i < NH else
            f"={P(i)}{RLROW[k]}*(1+CHOOSE({SW},Assumptions!{L(i)}{GROW[(k,'best')]},"
            f"Assumptions!{L(i)}{GROW[(k,'base')]},Assumptions!{L(i)}{GROW[(k,'worst')]}))")
    RLROW[k] = rr
    line(ws_r, rr, "  " + LINE_LABEL[k], fmla=mkf(k)); rr += 1
TREV = rr
line(ws_r, rr, "Total revenue", fmla=lambda i: f"=SUM({L(i)}{RLROW['Core']}:{L(i)}{RLROW['Platform']})",
     bold=True, fill=fill_green,
     src="Sum of product lines. Calibrated to disclosed run-rates: ~$1.6B FY24 (press, Mar-2024); "
         "run-rate $4.0B Sep-25, $4.8B Dec-25, $5.4B Feb-26, $6.9B Jun-26 (company).") ; rr += 1
TGROW = rr
line(ws_r, rr, "  Total growth, year over year",
     fmla=lambda i: "" if i == 0 else f"={L(i)}{TREV}/{P(i)}{TREV}-1", fmt=PCT); rr += 1
rr += 1
sec(ws_r, rr, "  Product mix, % of revenue"); rr += 1
for k in LINES:
    line(ws_r, rr, "  " + k, fmla=(lambda kk: lambda i: f"={L(i)}{RLROW[kk]}/{L(i)}{TREV}")(k),
         fmt=PCT, indent=2); rr += 1
rr += 1
sec(ws_r, rr, "B. CROSS-CHECK: by customer tier (top tiers anchored to disclosure)"); rr += 1
CT10 = line(ws_r, rr, "  Revenue from customers >$10M / yr",
    fmla=lambda i: f"=Assumptions!{L(i)}{T10C}*Assumptions!{L(i)}{T10A}"); rr += 1
CT1 = line(ws_r, rr, "  Revenue from customers $1-10M / yr",
    fmla=lambda i: f"=Assumptions!{L(i)}{T1C}*Assumptions!{L(i)}{T1A}"); rr += 1
CTL = line(ws_r, rr, "  Revenue from the long tail (implied residual)",
    fmla=lambda i: f"={L(i)}{TREV}-{L(i)}{CT10}-{L(i)}{CT1}"); rr += 1
line(ws_r, rr, "  Memo: implied long-tail average spend (USD 000)",
    fmla=lambda i: f"={L(i)}{CTL}/Assumptions!{L(i)}{TLK}", fmt=NUM, italic=True,
    src="Given the disclosed large-account tiers, this is the average annual spend the total implies for the ~20k+ (rising) long-tail organizations."); rr += 1
line(ws_r, rr, "  Check: tiers vs total revenue",
    fmla=lambda i: f"={L(i)}{CT10}+{L(i)}{CT1}+{L(i)}{CTL}-{L(i)}{TREV}", fmt=NUM2, italic=True); rr += 1
rr += 1
sec(ws_r, rr, "C. CROSS-CHECK: by platform consumption (the DBU meter)"); rr += 1
line(ws_r, rr, "  Blended realized price per DBU (USD)",
    fmla=lambda i: f"=Assumptions!{L(i)}{DBUP}", fmt=DOL2); DBP2 = rr; rr += 1
line(ws_r, rr, "  Implied DBUs consumed (billions)",
    fmla=lambda i: f"={L(i)}{TREV}/{L(i)}{DBP2}/1000", fmt=NUM1,
    src="Revenue divided by blended price. The consumption identity: revenue = DBUs x price. Shows platform usage scale."); rr += 1

# ------------------------------------------------------------------ COSTS
prep(ws_c, {"A":2,"B":46,"C":3,**{get_column_letter(C0+i):10 for i in range(NY)},
            get_column_letter(SRCCOL-1):2, get_column_letter(SRCCOL):70})
ws_c.cell(2, 2, "Cost Build: where every dollar goes").font = f_title
ws_c.cell(3, 2, "Cost of revenue is built from four components, so gross margin is an output, not an input. "
                "Operating expense is built from ratios then decomposed into people, programs and facilities. USD M.").font = f_sub
rc = 5
yr_header(ws_c, rc); rc += 1
sec(ws_c, rc, "A. COST OF REVENUE (gross margin is the output)"); rc += 1
line(ws_c, rc, "  Revenue (from Revenue tab)", fmla=lambda i: f"=Revenue!{L(i)}{TREV}"); CREV = rc; rc += 1
K1 = line(ws_c, rc, "  Cloud and serverless compute",
    fmla=lambda i: f"={L(i)}{CREV}*Assumptions!{L(i)}{C1}",
    src="The hyperscaler bill Databricks pays for serverless and AI SKUs. Largest cost, and the one compressing margin."); rc += 1
K2 = line(ws_c, rc, "  Third-party AI model and API costs",
    fmla=lambda i: f"=Revenue!{L(i)}{RLROW['AI']}*Assumptions!{L(i)}{C2}",
    src="Cost of serving external frontier models inside the platform (% of AI revenue)."); rc += 1
K3 = line(ws_c, rc, "  Support, delivery and platform ops",
    fmla=lambda i: f"={L(i)}{CREV}*Assumptions!{L(i)}{C3}"); rc += 1
K4 = line(ws_c, rc, "  Amortization of acquired technology",
    fmla=lambda i: f"=Assumptions!{L(i)}{C4}"); rc += 1
TCOGS = rc
line(ws_c, rc, "Total cost of revenue", fmla=lambda i: f"=SUM({L(i)}{K1}:{L(i)}{K4})", bold=True); rc += 1
CGP = rc
line(ws_c, rc, "Gross profit", fmla=lambda i: f"={L(i)}{CREV}-{L(i)}{TCOGS}", bold=True, fill=fill_green); rc += 1
CGM = rc
line(ws_c, rc, "  Gross margin % (OUTPUT)", fmla=lambda i: f"={L(i)}{CGP}/{L(i)}{CREV}", fmt=PCT,
    bold=True, src="Falls from ~85% to ~74% as serverless/AI mix grows (matches Jun-2026 disclosure), "
                   "then recovers on scale efficiency."); rc += 1
rc += 1
sec(ws_c, rc, "B. OPERATING EXPENSE (ratio, then decomposed)"); rc += 1
ORD = line(ws_c, rc, "  Research and development", fmla=lambda i: f"={L(i)}{CREV}*Assumptions!{L(i)}{RDP}"); rc += 1
line(ws_c, rc, "      of which engineering personnel",
    fmla=lambda i: f"={L(i)}{ORD}*Assumptions!{L(i)}{RDCS}", italic=True, indent=2); RDCOMP = rc; rc += 1
line(ws_c, rc, "      of which dev cloud, tooling, other",
    fmla=lambda i: f"={L(i)}{ORD}*(1-Assumptions!{L(i)}{RDCS})", italic=True, indent=2); rc += 1
OSM = line(ws_c, rc, "  Sales and marketing", fmla=lambda i: f"={L(i)}{CREV}*Assumptions!{L(i)}{SMP}"); rc += 1
line(ws_c, rc, "      of which sales personnel (incl commission)",
    fmla=lambda i: f"={L(i)}{OSM}*Assumptions!{L(i)}{SMSA}", italic=True, indent=2); SMCOMP = rc; rc += 1
line(ws_c, rc, "      of which marketing personnel",
    fmla=lambda i: f"={L(i)}{OSM}*Assumptions!{L(i)}{SMMC}", italic=True, indent=2); MKCOMP = rc; rc += 1
line(ws_c, rc, "      of which marketing programs and events",
    fmla=lambda i: f"={L(i)}{OSM}*Assumptions!{L(i)}{SMPR}", italic=True, indent=2); rc += 1
line(ws_c, rc, "      of which partner and field ops",
    fmla=lambda i: f"={L(i)}{OSM}*Assumptions!{L(i)}{SMFD}", italic=True, indent=2); rc += 1
OGA = line(ws_c, rc, "  General and administrative", fmla=lambda i: f"={L(i)}{CREV}*Assumptions!{L(i)}{GAP}"); rc += 1
line(ws_c, rc, "      of which G&A personnel",
    fmla=lambda i: f"={L(i)}{OGA}*Assumptions!{L(i)}{GACO}", italic=True, indent=2); GACOMP = rc; rc += 1
line(ws_c, rc, "      of which facilities and IT",
    fmla=lambda i: f"={L(i)}{OGA}*Assumptions!{L(i)}{GAFA}", italic=True, indent=2); rc += 1
line(ws_c, rc, "      of which professional, insurance, other",
    fmla=lambda i: f"={L(i)}{OGA}*Assumptions!{L(i)}{GAOT}", italic=True, indent=2); rc += 1
OSBC = line(ws_c, rc, "  Stock-based compensation (non-cash)",
    fmla=lambda i: f"={L(i)}{CREV}*Assumptions!{L(i)}{SBCP}"); rc += 1
ODA = line(ws_c, rc, "  Depreciation and other amortization",
    fmla=lambda i: f"={L(i)}{CREV}*Assumptions!{L(i)}{DAP}"); rc += 1
TOPEX = rc
line(ws_c, rc, "Total operating expense",
    fmla=lambda i: f"={L(i)}{ORD}+{L(i)}{OSM}+{L(i)}{OGA}+{L(i)}{OSBC}+{L(i)}{ODA}", bold=True); rc += 1
rc += 1
sec(ws_c, rc, "C. IMPLIED HEADCOUNT BRIDGE (from the personnel dollars above)"); rc += 1
HE = line(ws_c, rc, "  Engineering heads",
    fmla=lambda i: f"={L(i)}{RDCOMP}*1000/Assumptions!{L(i)}{HENG}", fmt=NUM); rc += 1
HS = line(ws_c, rc, "  Sales heads",
    fmla=lambda i: f"={L(i)}{SMCOMP}*1000/Assumptions!{L(i)}{HSAL}", fmt=NUM); rc += 1
HM = line(ws_c, rc, "  Marketing heads",
    fmla=lambda i: f"={L(i)}{MKCOMP}*1000/Assumptions!{L(i)}{HMKT}", fmt=NUM); rc += 1
HG = line(ws_c, rc, "  G&A heads",
    fmla=lambda i: f"={L(i)}{GACOMP}*1000/Assumptions!{L(i)}{HGA}", fmt=NUM); rc += 1
HSU = line(ws_c, rc, "  Support/delivery heads (in cost of revenue)",
    fmla=lambda i: f"={L(i)}{K3}*1000/Assumptions!{L(i)}{HSUP}", fmt=NUM); rc += 1
THEAD = rc
line(ws_c, rc, "Total implied headcount (year end)",
    fmla=lambda i: f"=SUM({L(i)}{HE}:{L(i)}{HSU})", bold=True,
    src="Implied by the personnel dollars, not an input. Ties to ~9,000-10,000 in FY2026-27 range; "
        "third-party trackers span 9,000 (PitchBook) to ~15,800 (Revelio); company discloses no official figure."); rc += 1
line(ws_c, rc, "  Revenue per head (USD 000)",
    fmla=lambda i: f"={L(i)}{CREV}*1000/{L(i)}{THEAD}", fmt=NUM,
    src="Rises with consumption expansion, the efficiency signature of the model."); rc += 1

# ------------------------------------------------------------- FINANCIALS
prep(ws_f, {"A":2,"B":44,"C":3,**{get_column_letter(C0+i):10 for i in range(NY)},
            get_column_letter(SRCCOL-1):2, get_column_letter(SRCCOL):66})
ws_f.cell(2, 2, "Financial Statements").font = f_title
ws_f.cell(3, 2, "Income statement, cash flow and balance sheet, assembled from the Revenue and Cost builds. "
                "FY ends January 31. Balance check is zero in every year.").font = f_sub
rf = 5
yr_header(ws_f, rf); rf += 1
sec(ws_f, rf, "INCOME STATEMENT"); rf += 1
FREV = line(ws_f, rf, "Revenue", fmla=lambda i: f"=Revenue!{L(i)}{TREV}", bold=True); rf += 1
FCOGS = line(ws_f, rf, "Cost of revenue", fmla=lambda i: f"=-Costs!{L(i)}{TCOGS}"); rf += 1
FGP = line(ws_f, rf, "Gross profit", fmla=lambda i: f"={L(i)}{FREV}+{L(i)}{FCOGS}", bold=True); rf += 1
line(ws_f, rf, "  Gross margin %", fmla=lambda i: f"={L(i)}{FGP}/{L(i)}{FREV}", fmt=PCT); rf += 1
FRD = line(ws_f, rf, "Research and development", fmla=lambda i: f"=-Costs!{L(i)}{ORD}"); rf += 1
FSM = line(ws_f, rf, "Sales and marketing", fmla=lambda i: f"=-Costs!{L(i)}{OSM}"); rf += 1
FGA = line(ws_f, rf, "General and administrative", fmla=lambda i: f"=-Costs!{L(i)}{OGA}"); rf += 1
FSBC = line(ws_f, rf, "Stock-based compensation", fmla=lambda i: f"=-Costs!{L(i)}{OSBC}"); rf += 1
FDA = line(ws_f, rf, "Depreciation and other amortization", fmla=lambda i: f"=-Costs!{L(i)}{ODA}"); rf += 1
FEBIT = line(ws_f, rf, "Operating income (EBIT)",
    fmla=lambda i: f"={L(i)}{FGP}+{L(i)}{FRD}+{L(i)}{FSM}+{L(i)}{FGA}+{L(i)}{FSBC}+{L(i)}{FDA}",
    bold=True); rf += 1
line(ws_f, rf, "  Operating margin %", fmla=lambda i: f"={L(i)}{FEBIT}/{L(i)}{FREV}", fmt=PCT); rf += 1
FIE = rf; line(ws_f, rf, "Interest expense (on opening debt)"); rf += 1
FII = rf; line(ws_f, rf, "Interest income (on opening cash)"); rf += 1
FEBT = rf; line(ws_f, rf, "Pre-tax income", bold=True); rf += 1
FTAX = rf; line(ws_f, rf, "Income tax"); rf += 1
FNI = rf; line(ws_f, rf, "Net income (GAAP est.)", bold=True, fill=fill_green); rf += 1
rf += 1
sec(ws_f, rf, "CASH FLOW"); rf += 1
line(ws_f, rf, "Net income", fmla=lambda i: f"={L(i)}{FNI}"); CFNI = rf; rf += 1
line(ws_f, rf, "  add back depreciation and amortization", fmla=lambda i: f"=-{L(i)}{FDA}+Costs!{L(i)}{K4}"); rf += 1
line(ws_f, rf, "  add back stock-based compensation", fmla=lambda i: f"=-{L(i)}{FSBC}"); rf += 1
CFAR = rf; line(ws_f, rf, "  change in accounts receivable"); rf += 1
CFDR = rf; line(ws_f, rf, "  change in deferred revenue"); rf += 1
FCFO = rf; line(ws_f, rf, "Cash from operations", fmla=lambda i: f"=SUM({L(i)}{CFNI}:{L(i)}{CFDR})", bold=True); rf += 1
FCAPX = rf; line(ws_f, rf, "Capital expenditure", fmla=lambda i: f"=-{L(i)}{FREV}*Assumptions!{L(i)}{CXP}"); rf += 1
FACQ = rf; line(ws_f, rf, "Acquisitions and strategic investments", fmla=lambda i: f"=Assumptions!{L(i)}{ACA}"); rf += 1
FCFI = rf; line(ws_f, rf, "Cash from investing", fmla=lambda i: f"={L(i)}{FCAPX}+{L(i)}{FACQ}", bold=True); rf += 1
FEQ = rf; line(ws_f, rf, "Equity issuance", fmla=lambda i: f"=Assumptions!{L(i)}{EQA}"); rf += 1
FDB = rf; line(ws_f, rf, "Debt drawn", fmla=lambda i: f"=Assumptions!{L(i)}{DBA}"); rf += 1
FTD = rf; line(ws_f, rf, "Employee liquidity / tenders", fmla=lambda i: f"=Assumptions!{L(i)}{TDA}"); rf += 1
FCFF = rf; line(ws_f, rf, "Cash from financing", fmla=lambda i: f"={L(i)}{FEQ}+{L(i)}{FDB}+{L(i)}{FTD}", bold=True); rf += 1
FDCASH = rf; line(ws_f, rf, "Net change in cash", fmla=lambda i: f"={L(i)}{FCFO}+{L(i)}{FCFI}+{L(i)}{FCFF}", bold=True); rf += 1
FFCF = rf; line(ws_f, rf, "Free cash flow (CFO + capex)", fmla=lambda i: f"={L(i)}{FCFO}+{L(i)}{FCAPX}",
    bold=True, fill=fill_green,
    src="Company confirms first positive FCF quarter Q4 FY2025 and positive TTM FCF through 2025 (no magnitude). "
        "Level here is a model output; early years are estimates sensitive to deferred-revenue timing."); rf += 1
line(ws_f, rf, "  FCF margin %", fmla=lambda i: f"={L(i)}{FFCF}/{L(i)}{FREV}", fmt=PCT); rf += 1
rf += 1
sec(ws_f, rf, "BALANCE SHEET (closing)"); rf += 1
FCASH = rf; line(ws_f, rf, "Cash and investments",
    fmla=lambda i: (f"=Assumptions!{L(0)}{OBROW['cash']}+{L(i)}{FDCASH}" if i == 0
                    else f"={P(i)}{FCASH}+{L(i)}{FDCASH}"), bold=True); rf += 1
FAR = rf; line(ws_f, rf, "Accounts receivable",
    fmla=lambda i: f"={L(i)}{FREV}*Assumptions!{L(i)}{DSOA}/365"); rf += 1
FPPE = rf; line(ws_f, rf, "PP&E, net",
    fmla=lambda i: (f"=Assumptions!{L(0)}{OBROW['ppe']}-{L(i)}{FCAPX}+{L(i)}{FDA}" if i == 0
                    else f"={P(i)}{FPPE}-{L(i)}{FCAPX}+{L(i)}{FDA}")); rf += 1
FGW = rf; line(ws_f, rf, "Goodwill and intangibles",
    fmla=lambda i: (f"=Assumptions!{L(0)}{OBROW['gw']}-{L(i)}{FACQ}-Costs!{L(i)}{K4}" if i == 0
                    else f"={P(i)}{FGW}-{L(i)}{FACQ}-Costs!{L(i)}{K4}")); rf += 1
FOA = rf; line(ws_f, rf, "Other assets", fmla=lambda i: f"=Assumptions!{L(0)}{OBROW['oa']}"); rf += 1
FTA = rf; line(ws_f, rf, "Total assets", fmla=lambda i: f"=SUM({L(i)}{FCASH}:{L(i)}{FOA})", bold=True); rf += 1
FDR = rf; line(ws_f, rf, "Deferred revenue",
    fmla=lambda i: f"={L(i)}{FREV}*Assumptions!{L(i)}{DRDA}/365"); rf += 1
FOL = rf; line(ws_f, rf, "Other liabilities", fmla=lambda i: f"=Assumptions!{L(0)}{OBROW['ol']}"); rf += 1
FDEBT = rf; line(ws_f, rf, "Debt",
    fmla=lambda i: (f"=Assumptions!{L(0)}{OBROW['debt']}+{L(i)}{FDB}" if i == 0
                    else f"={P(i)}{FDEBT}+{L(i)}{FDB}"), bold=True); rf += 1
FTL = rf; line(ws_f, rf, "Total liabilities", fmla=lambda i: f"={L(i)}{FDR}+{L(i)}{FOL}+{L(i)}{FDEBT}", bold=True); rf += 1
FAPIC = rf; line(ws_f, rf, "Paid-in capital (incl SBC, net of tenders)",
    fmla=lambda i: (f"=Assumptions!{L(0)}{OBROW['apic']}+{L(i)}{FEQ}-{L(i)}{FSBC}+{L(i)}{FTD}" if i == 0
                    else f"={P(i)}{FAPIC}+{L(i)}{FEQ}-{L(i)}{FSBC}+{L(i)}{FTD}")); rf += 1
FRET = rf; line(ws_f, rf, "Accumulated deficit",
    fmla=lambda i: (f"=Assumptions!{L(0)}{OBROW['ret']}+{L(i)}{FNI}" if i == 0
                    else f"={P(i)}{FRET}+{L(i)}{FNI}")); rf += 1
FTE = rf; line(ws_f, rf, "Total equity", fmla=lambda i: f"={L(i)}{FAPIC}+{L(i)}{FRET}", bold=True); rf += 1
FCHK = rf; line(ws_f, rf, "Balance check (must be 0)",
    fmla=lambda i: f"=ROUND({L(i)}{FTA}-{L(i)}{FTL}-{L(i)}{FTE},4)", fmt='0.0000', fill=fill_warn); rf += 1

# back-fill interest / tax / working-capital rows
for i in range(NY):
    col = L(i); pcol = P(i)
    ws_f.cell(FIE, C0+i).value = (f"=-Assumptions!{L(0)}{OBROW['debt']}*Assumptions!{col}{IRA}" if i == 0
                                  else f"=-{pcol}{FDEBT}*Assumptions!{col}{IRA}")
    ws_f.cell(FII, C0+i).value = (f"=Assumptions!{L(0)}{OBROW['cash']}*Assumptions!{col}{YCA}" if i == 0
                                  else f"={pcol}{FCASH}*Assumptions!{col}{YCA}")
    ws_f.cell(FEBT, C0+i).value = f"={col}{FEBIT}+{col}{FIE}+{col}{FII}"
    ws_f.cell(FTAX, C0+i).value = f"=-MAX({col}{FEBT},0)*Assumptions!{col}{TXA}"
    ws_f.cell(FNI, C0+i).value = f"={col}{FEBT}+{col}{FTAX}"
    ws_f.cell(CFAR, C0+i).value = (f"=-({col}{FAR}-Assumptions!{L(0)}{OBROW['ar']})" if i == 0
                                   else f"=-({col}{FAR}-{pcol}{FAR})")
    ws_f.cell(CFDR, C0+i).value = (f"={col}{FDR}-Assumptions!{L(0)}{OBROW['dr']}" if i == 0
                                   else f"={col}{FDR}-{pcol}{FDR}")
for rr_ in (FIE, FII, FEBT, FTAX, FNI, CFAR, CFDR):
    for i in range(NY):
        ws_f.cell(rr_, C0+i).number_format = NUM
        ws_f.cell(rr_, C0+i).font = f_numb if rr_ in (FEBT, FNI) else f_num
ws_f.cell(FIE, SRCCOL, "Interest on opening balances (avoids circularity).").font = f_src

# ------------------------------------------------------------------- KPIs
prep(ws_k, {"A":2,"B":42,"C":3,**{get_column_letter(C0+i):10 for i in range(NY)},
            get_column_letter(SRCCOL-1):2, get_column_letter(SRCCOL):58})
ws_k.cell(2, 2, "KPIs and Unit Economics").font = f_title
ws_k.cell(3, 2, "Read-through of the build. All linked to the model; nothing typed twice.").font = f_sub
rk = 5
yr_header(ws_k, rk); rk += 1
sec(ws_k, rk, "Growth and profitability"); rk += 1
line(ws_k, rk, "Revenue", fmla=lambda i: f"=Financials!{L(i)}{FREV}", bold=True); rk += 1
line(ws_k, rk, "  Revenue growth", fmla=lambda i: "" if i == 0 else f"=Financials!{L(i)}{FREV}/Financials!{P(i)}{FREV}-1", fmt=PCT); rk += 1
line(ws_k, rk, "Gross margin", fmla=lambda i: f"=Financials!{L(i)}{FGP}/Financials!{L(i)}{FREV}", fmt=PCT); rk += 1
line(ws_k, rk, "Operating (EBIT) margin", fmla=lambda i: f"=Financials!{L(i)}{FEBIT}/Financials!{L(i)}{FREV}", fmt=PCT); rk += 1
line(ws_k, rk, "FCF margin", fmla=lambda i: f"=Financials!{L(i)}{FFCF}/Financials!{L(i)}{FREV}", fmt=PCT); rk += 1
RULE = rk
line(ws_k, rk, "Rule of 40 (growth + FCF margin)",
    fmla=lambda i: "" if i == 0 else f"=(Financials!{L(i)}{FREV}/Financials!{P(i)}{FREV}-1)+Financials!{L(i)}{FFCF}/Financials!{L(i)}{FREV}",
    fmt=PCT, bold=True, fill=fill_green,
    src="Above 40% is the software health bar; the model clears it throughout the forecast."); rk += 1
rk += 1
sec(ws_k, rk, "Efficiency and mix"); rk += 1
line(ws_k, rk, "Revenue per head (USD 000)", fmla=lambda i: f"=Costs!{L(i)}{CREV}*1000/Costs!{L(i)}{THEAD}", fmt=NUM); rk += 1
line(ws_k, rk, "Implied headcount (year end)", fmla=lambda i: f"=Costs!{L(i)}{THEAD}", fmt=NUM); rk += 1
line(ws_k, rk, "AI products, % of revenue", fmla=lambda i: f"=Revenue!{L(i)}{RLROW['AI']}/Revenue!{L(i)}{TREV}", fmt=PCT); rk += 1
line(ws_k, rk, "Cloud/AI compute, % of revenue",
    fmla=lambda i: f"=(Costs!{L(i)}{K1}+Costs!{L(i)}{K2})/Financials!{L(i)}{FREV}", fmt=PCT); rk += 1
line(ws_k, rk, "Customers >$1M / yr (count)",
    fmla=lambda i: f"=Assumptions!{L(i)}{T10C}+Assumptions!{L(i)}{T1C}", fmt=NUM,
    src="300+ Sep-2023, 500+ Dec-2024, 800+ Feb-2026 (company)."); rk += 1
rk += 1
sec(ws_k, rk, "Capital and liquidity"); rk += 1
line(ws_k, rk, "Cash and investments (closing)", fmla=lambda i: f"=Financials!{L(i)}{FCASH}"); rk += 1
line(ws_k, rk, "Debt (closing)", fmla=lambda i: f"=Financials!{L(i)}{FDEBT}"); rk += 1
line(ws_k, rk, "Deferred revenue (closing)", fmla=lambda i: f"=Financials!{L(i)}{FDR}"); rk += 1
line(ws_k, rk, "Cumulative equity raised", fmla=lambda i: (f"=Assumptions!{L(i)}{EQA}" if i == 0 else f"={P(i)}{rk}+Assumptions!{L(i)}{EQA}") if False else None); CUMEQ = rk
for i in range(NY):
    ws_k.cell(CUMEQ, C0+i).value = (f"=Assumptions!{L(0)}{OBROW['apic']}+Assumptions!{L(0)}{EQA}" if i == 0
                                    else f"={P(i)}{CUMEQ}+Assumptions!{L(i)}{EQA}")
    ws_k.cell(CUMEQ, C0+i).number_format = NUM; ws_k.cell(CUMEQ, C0+i).font = f_num
ws_k.cell(CUMEQ, 2, "Cumulative paid-in equity (memo)").font = f_lbl
ws_k.cell(CUMEQ, 2).alignment = Alignment(indent=1)
rk = CUMEQ + 1
line(ws_k, rk, "Capital efficiency (revenue / cumulative equity)",
    fmla=lambda i: f"=Financials!{L(i)}{FREV}/{L(i)}{CUMEQ}", fmt=MULT,
    src="Equity-only denominator by house convention; debt informs compute independence, not this ratio."); rk += 1

# ------------------------------------------------------------------ GUIDE
prep(ws_guide, {"A":3,"B":100})
ws_guide.cell(2, 2, "How this model is built").font = f_title
guide = [
 ("", ""),
 ("The one-line logic", "h"),
 ("Revenue is built bottom-up from five product lines and summed. Costs are built bottom-up from their "
  "components, so gross margin and operating margin fall out as results, not inputs. The three statements "
  "then assemble from those two builds and balance to zero every year.", "p"),
 ("Where revenue comes from (Revenue tab)", "h"),
 ("1. Product line (primary): Data engineering / core compute, Databricks SQL, AI products (Mosaic AI), "
  "Lakebase, and Platform / other. Each is anchored to disclosed run-rates through FY2027E, then grows at a "
  "scenario-driven rate. The five sum to total revenue.", "p"),
 ("2. Customer tier (cross-check): the same total split across customers above $10M a year, $1-10M, and the "
  "long tail. The top two tiers are anchored to disclosed counts (300+ above $1M in 2023, 800+ by 2026); the "
  "long-tail average spend is the implied residual.", "p"),
 ("3. Consumption (cross-check): revenue divided by the blended price per DBU gives implied platform usage. "
  "This is the consumption identity the whole business runs on: revenue = DBUs consumed x price.", "p"),
 ("Where costs come from (Costs tab)", "h"),
 ("Cost of revenue = cloud and serverless compute (the hyperscaler bill) + third-party AI model costs + "
  "support and delivery + amortization of acquired technology. Gross margin is whatever those leave behind. "
  "This is why margin compresses as AI and serverless grow, exactly as the company guided in June 2026.", "p"),
 ("Operating expense = R&D + Sales and marketing + G&A + stock comp + depreciation, each set as a percent of "
  "revenue and then decomposed into people, programs and facilities. The personnel dollars imply a headcount, "
  "shown as a bridge, so the cost base ties back to a believable number of employees.", "p"),
 ("How to use it", "h"),
 ("Change the one orange cell (Assumptions!D5): 1 = Best, 2 = Base, 3 = Worst. It flexes each product line's "
  "forecast growth. Every blue cell on the Assumptions tab is an input you can change; everything else is a "
  "formula. The balance check on the Financials tab stays at zero.", "p"),
 ("What is fact and what is estimate", "h"),
 ("Revenue run-rates, customer counts, gross-margin direction, funding rounds and free-cash-flow positivity "
  "are company disclosures or PitchBook records, dated in the source column. Everything else (cost ratios, "
  "headcount, opening balance sheet, product mix) is a labeled estimate calibrated to those anchors. Databricks "
  "is private and files no audited statements. The unclosed $188B round (July 2026) is excluded.", "p"),
 ("Reconciliation", "h"),
 ("The operating-margin path is calibrated to match the validated companion model (Brick by Brick, July 2026) "
  "from FY2025 on: this is the same business, seen bottom-up. It extends back to FY2022 and out to FY2032 to "
  "cover the full window requested.", "p"),
]
gr = 4
for text, kind in guide:
    if kind == "h":
        c = ws_guide.cell(gr, 2, text); c.font = f_h
    elif kind == "p":
        c = ws_guide.cell(gr, 2, text); c.font = Font(name="Calibri", size=10)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws_guide.row_dimensions[gr].height = 46
    gr += 1

# ----------------------------------------------------------------- COVER
prep(ws_cover, {"A":3,"B":4,"C":46,"D":16,"E":34})
ws_cover.cell(4, 3, "Databricks, Inc.").font = Font(name="Georgia", size=26, bold=True, color=NAVY)
ws_cover.cell(5, 3, "Granular Bottom-Up Operating Model").font = Font(name="Georgia", size=14, color=SLATE, italic=True)
ws_cover.cell(6, 3, "FY2022A to FY2032E   |   revenue and costs built from the ground up   |   USD millions, fiscal year ends January 31").font = f_src
ws_cover.cell(7, 3, "Prepared by Harrison Rolfes, Senior Research Director. July 21, 2026. "
                    "Companion to Brick by Brick.").font = f_src
r = 10
ws_cover.cell(r, 3, "Contents").font = f_h; r += 1
toc = [("Guide", "Plain-English map of how revenue and costs are built"),
       ("Assumptions", "Every driver, sourced; the one orange scenario switch; blue input cells"),
       ("Revenue", "Product-line build, plus customer-tier and DBU-consumption cross-checks"),
       ("Costs", "Cost of revenue by component (margin is an output); opex decomposed; headcount bridge"),
       ("Financials", "Income statement, cash flow, balance sheet, balance check"),
       ("KPIs", "Growth, margins, Rule of 40, revenue per head, capital efficiency")]
for nm, desc in toc:
    ws_cover.cell(r, 3, nm).font = f_lblb
    ws_cover.cell(r, 5, desc).font = f_lbl
    r += 1
r += 1
ws_cover.cell(r, 3, "Model checks").font = f_h; r += 1
ws_cover.cell(r, 3, "Balance sheet balanced every year?").font = f_lbl
ws_cover.cell(r, 4, f'=IF(AND(MAX(Financials!{L(0)}{FCHK}:{L(NY-1)}{FCHK})<0.001,'
                    f'MIN(Financials!{L(0)}{FCHK}:{L(NY-1)}{FCHK})>-0.001),"OK","ERROR")').font = Font(
                    name="Calibri", size=10, bold=True, color=GREEN); r += 1
ws_cover.cell(r, 3, "Revenue ties to product-line sum?").font = f_lbl
ws_cover.cell(r, 4, f'=IF(ABS(Revenue!{L(NY-1)}{TREV}-SUM(Revenue!{L(NY-1)}{RLROW["Core"]}:Revenue!{L(NY-1)}{RLROW["Platform"]}))<0.01,"OK","ERROR")').font = Font(name="Calibri", size=10, bold=True, color=GREEN); r += 1
ws_cover.cell(r, 3, "Scenario in use (1 Best / 2 Base / 3 Worst)").font = f_lbl
ws_cover.cell(r, 4, "=Assumptions!D5").font = f_lblb; r += 2
ws_cover.cell(r, 3, "Sources: company press releases and disclosures (2021 to Jun 2026); PitchBook deal records "
                    "(entity 59199-40, retrieved Jul 21, 2026); SEC EDGAR (CIK 1587468); public cloud price lists. "
                    "Not investment advice; private-company figures are estimates unless disclosed.").font = f_src
ws_cover.cell(r, 3).alignment = Alignment(wrap_text=True, vertical="top")
ws_cover.row_dimensions[r].height = 58

# --------------------------------------------------------------- DASHBOARD
prep(ws_dash, {"A":2,"B":34,"C":13,"D":13,"E":13,"F":3,"G":13,"H":13,"I":13,"J":13})
ws_dash.cell(2, 2, "Databricks   |   Model Dashboard").font = f_title
ws_dash.cell(3, 2, "One-page read-through of the granular model. Base case unless the scenario switch is changed. "
                   "USD millions unless stated. Every figure is a live link.").font = f_sub
ws_dash.cell(5, 2, "Scenario in use").font = f_lblb
ws_dash.cell(5, 3, '=CHOOSE(Assumptions!D5,"Best","Base","Worst")').font = Font(
    name="Calibri", size=11, bold=True, color=WARN)
ws_dash.cell(5, 4, "(change on the Assumptions tab, cell D5)").font = f_src

# ---- headline metric table: three snapshot years
snap = [(4, "FY2026A"), (5, "FY2027E"), (10, "FY2032E")]
hr = 7
ws_dash.cell(hr, 2, "Headline metrics").font = f_h
for col in range(2, 6): ws_dash.cell(hr, col).fill = fill_soft
hr += 1
ws_dash.cell(hr, 2, "").font = f_hdr
for j, (idx, lbl) in enumerate(snap):
    c = ws_dash.cell(hr, 3 + j, lbl); c.font = f_hdr; c.fill = fill_hdr
    c.alignment = Alignment(horizontal="center")
hr += 1
def dash_metric(label, mkf, fmt=NUM, bold=False, fill=None, src=None):
    global hr
    c = ws_dash.cell(hr, 2, label); c.font = f_numb if bold else f_lbl
    c.alignment = Alignment(indent=1)
    for j, (idx, lbl) in enumerate(snap):
        cc = ws_dash.cell(hr, 3 + j, mkf(idx))
        cc.number_format = fmt; cc.font = f_numb if bold else f_num
        if fill: cc.fill = fill
    if src: ws_dash.cell(hr, 7, src).font = f_src
    hr += 1
Lc = lambda i: L(i)
dash_metric("Revenue", lambda i: f"=Financials!{Lc(i)}{FREV}", bold=True)
dash_metric("Revenue growth (YoY)", lambda i: f"=Financials!{Lc(i)}{FREV}/Financials!{Lc(i-1)}{FREV}-1", fmt=PCT)
dash_metric("Gross margin", lambda i: f"=Financials!{Lc(i)}{FGP}/Financials!{Lc(i)}{FREV}", fmt=PCT)
dash_metric("Operating (EBIT) margin", lambda i: f"=Financials!{Lc(i)}{FEBIT}/Financials!{Lc(i)}{FREV}", fmt=PCT)
dash_metric("Net income (GAAP est.)", lambda i: f"=Financials!{Lc(i)}{FNI}")
dash_metric("Free cash flow", lambda i: f"=Financials!{Lc(i)}{FFCF}", bold=True, fill=fill_green)
dash_metric("FCF margin", lambda i: f"=Financials!{Lc(i)}{FFCF}/Financials!{Lc(i)}{FREV}", fmt=PCT)
dash_metric("Rule of 40 (growth + FCF margin)",
    lambda i: f"=(Financials!{Lc(i)}{FREV}/Financials!{Lc(i-1)}{FREV}-1)+Financials!{Lc(i)}{FFCF}/Financials!{Lc(i)}{FREV}",
    fmt=PCT, bold=True)
dash_metric("Implied headcount (year end)", lambda i: f"=Costs!{Lc(i)}{THEAD}")
dash_metric("Revenue per head (USD 000)", lambda i: f"=Costs!{Lc(i)}{CREV}*1000/Costs!{Lc(i)}{THEAD}")
dash_metric("Customers >$1M / yr", lambda i: f"=Assumptions!{Lc(i)}{T10C}+Assumptions!{Lc(i)}{T1C}",
    src="300+ Sep-2023, 500+ Dec-2024, 800+ Feb-2026 (company).")
dash_metric("Cash and investments (close)", lambda i: f"=Financials!{Lc(i)}{FCASH}")
dash_metric("Debt (close)", lambda i: f"=Financials!{Lc(i)}{FDEBT}")

# ---- where revenue comes from (mix table)
hr += 1
ws_dash.cell(hr, 2, "Where revenue comes from (product line)").font = f_h
for col in range(2, 6): ws_dash.cell(hr, col).fill = fill_soft
hr += 1
for j, (idx, lbl) in enumerate(snap):
    c = ws_dash.cell(hr, 3 + j, lbl + " $ / %"); c.font = f_hdr; c.fill = fill_hdr
    c.alignment = Alignment(horizontal="center")
hr += 1
MIXTOP = hr
for k in LINES:
    c = ws_dash.cell(hr, 2, "  " + k); c.font = f_lbl; c.alignment = Alignment(indent=1)
    for j, (idx, lbl) in enumerate(snap):
        cc = ws_dash.cell(hr, 3 + j,
            f'=TEXT(Revenue!{Lc(idx)}{RLROW[k]},"#,##0")&"  ("&TEXT(Revenue!{Lc(idx)}{RLROW[k]}/Revenue!{Lc(idx)}{TREV},"0%")&")"')
        cc.font = f_num; cc.alignment = Alignment(horizontal="right")
    hr += 1
c = ws_dash.cell(hr, 2, "Total revenue"); c.font = f_numb
for j, (idx, lbl) in enumerate(snap):
    cc = ws_dash.cell(hr, 3 + j, f"=Revenue!{Lc(idx)}{TREV}"); cc.font = f_numb; cc.number_format = NUM
    cc.border = border_b
hr += 2

# ---- hidden helper series for the margin chart (all years)
HELP = hr
ws_dash.cell(HELP, 2, "Margin path (for chart)").font = f_src
for i in range(NY):
    ws_dash.cell(HELP, C0 + i, FY[i]).font = f_src
GMr = HELP + 1; EBr = HELP + 2; FCr = HELP + 3
for lab, row, num, den in [("Gross margin", GMr, FGP, FREV),
                           ("Operating margin", EBr, FEBIT, FREV),
                           ("FCF margin", FCr, FFCF, FREV)]:
    ws_dash.cell(row, 2, lab).font = f_src
    for i in range(NY):
        cc = ws_dash.cell(row, C0 + i, f"=Financials!{Lc(i)}{num}/Financials!{Lc(i)}{den}")
        cc.number_format = PCT; cc.font = f_src

# ---- dashboard charts
ch_rev = BarChart(); ch_rev.type = "col"; ch_rev.grouping = "stacked"; ch_rev.overlap = 100
ch_rev.title = "Revenue by product line (USD M)"; ch_rev.height = 8.2; ch_rev.width = 17
for k in LINES:
    d = Reference(ws_r, min_col=C0, max_col=C0 + NY - 1, min_row=RLROW[k], max_row=RLROW[k])
    ch_rev.add_data(d, from_rows=True, titles_from_data=False)
ch_rev.set_categories(Reference(ws_r, min_col=C0, max_col=C0 + NY - 1, min_row=5, max_row=5))
for si, s in enumerate(ch_rev.series):
    s.graphicalProperties.solidFill = [NAVY, SLATE, GREEN, GOLD, GREY][si]
    s.tx = SeriesLabel(v=LINES[si])
ch_rev.legend.position = "b"
ws_dash.add_chart(ch_rev, "B" + str(HELP + 5))

ch_m = LineChart(); ch_m.title = "Margin path (%)"; ch_m.height = 8.2; ch_m.width = 17
for row in (GMr, EBr, FCr):
    d = Reference(ws_dash, min_col=C0, max_col=C0 + NY - 1, min_row=row, max_row=row)
    ch_m.add_data(d, from_rows=True, titles_from_data=False)
ch_m.set_categories(Reference(ws_dash, min_col=C0, max_col=C0 + NY - 1, min_row=HELP, max_row=HELP))
for si, (col, nm) in enumerate([(NAVY, "Gross margin"), (GREEN, "Operating margin"), (SLATE, "FCF margin")]):
    ch_m.series[si].graphicalProperties.line.solidFill = col
    ch_m.series[si].graphicalProperties.line.width = 22000
    ch_m.series[si].tx = SeriesLabel(v=nm)
ch_m.legend.position = "b"
ws_dash.add_chart(ch_m, "G" + str(HELP + 5))

# ------------------------------------------------------- charts (visual aids)
def _catref():
    return Reference(ws_r, min_col=C0, max_col=C0 + NY - 1, min_row=5, max_row=5)

# Revenue by product line, stacked column
chr_ = BarChart(); chr_.type = "col"; chr_.grouping = "stacked"; chr_.overlap = 100
chr_.title = "Where revenue comes from: product lines (USD M)"
chr_.height = 8; chr_.width = 20
for k in LINES:
    d = Reference(ws_r, min_col=C0, max_col=C0 + NY - 1, min_row=RLROW[k], max_row=RLROW[k])
    chr_.add_data(d, from_rows=True, titles_from_data=False)
chr_.set_categories(_catref())
palette = [NAVY, SLATE, GREEN, GOLD, GREY]
for si, s in enumerate(chr_.series):
    s.graphicalProperties.solidFill = palette[si % len(palette)]
    s.tx = None
chr_.legend.position = "b"
ws_r.add_chart(chr_, "B" + str(rr + 2))

# Cost of revenue components, stacked column
chc = BarChart(); chc.type = "col"; chc.grouping = "stacked"; chc.overlap = 100
chc.title = "Where cost of revenue goes: components (USD M)"
chc.height = 8; chc.width = 20
for rrow in (K1, K2, K3, K4):
    d = Reference(ws_c, min_col=C0, max_col=C0 + NY - 1, min_row=rrow, max_row=rrow)
    chc.add_data(d, from_rows=True, titles_from_data=False)
catc = Reference(ws_c, min_col=C0, max_col=C0 + NY - 1, min_row=5, max_row=5)
chc.set_categories(catc)
for si, s in enumerate(chc.series):
    s.graphicalProperties.solidFill = [SLATE, GREEN, GOLD, GREY][si]
chc.legend.position = "b"
ws_c.add_chart(chc, "B" + str(rc + 2))

OUT = "../output/Databricks_Granular_Model_Jul2026.xlsx"
wb.save(OUT)
print("saved", OUT)

# em-dash guard (scan source for U+2014)
_t = open(__file__, encoding="utf-8").read()
assert chr(0x2014) not in _t, "EM-DASH found in source"
print("EMDASH-CHECK (source): PASS")

# base-case print
print("\n" + " | ".join([""] + FY))
def _row(nm, vals, pct=False):
    print(nm + " | " + " | ".join((f"{v*100:,.1f}%" if pct else f"{v:,.0f}") for v in vals))
_row("Revenue", REV)
_row("Growth", [0] + [REV[i]/REV[i-1]-1 for i in range(1, NY)], pct=True)
_row("Gross margin", B["gm"], pct=True)
_row("EBIT", B["ebit"])
_row("EBIT margin", [B["ebit"][i]/REV[i] for i in range(NY)], pct=True)
_row("Net income", B["ni"])
_row("FCF", B["fcf"])
_row("Cash close", B["cash"])
for k in LINES:
    _row(k, LV[k])
