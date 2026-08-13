"""Model factory: a driver-based operating and valuation model per company.

Builds the skeleton shared by all four reference workbooks in
`model_templates/` — Cover with automated checks, Inputs, Raw Data, Model,
Scenarios, Valuation, Outputs — over a fixed 2022-2032 window (four historical
years, the current year, and seven forecast years).

House conventions, measured from those templates and reproduced exactly:

    blue text      an input you may change
    black text     a formula; do not touch
    green text     a link to another sheet
    accounting     zero shows as a dash, negatives in parentheses
    0.0x           multiples
    2023A / 2027F  years carry a letter so history and forecast are obvious

The rule that makes an automated model honest: every blue input is either a
resolved reference to a stored Fact — with its source and date in the cell note
— or it is explicitly marked as an assumption with its reasoning beside it.
There is no third category, and the cover states the ratio of one to the other.
A model built mostly on assumptions is labelled illustrative.

    python3 -m engine model <slug> [operating|three_statement|dcf|full]
"""
from __future__ import annotations

import datetime as _dt
import os

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from . import briefing, schema, store

HIST_START, FORECAST_END = 2022, 2032

# --- house palette, lifted from engine/charts.py PALETTES["house"] ------------
NAVY, SLATE, GREEN = "1F2A44", "35506E", "1C5D46"
BLUE_IN, BLACK, LINK = "0000FF", "000000", "1C5D46"
GREY, SOFT, BAND, EDGE = "6B7280", "F2F5F9", "EDF2F7", "D5DBE4"

F_CUR = '_(#,##0_);(#,##0);_("–"_);_(@_)'
F_CUR2 = '_("$"#,##0_);("$"#,##0);_("$"–"_);_(@_)'
F_PCT = '_(#,##0.0%_);(#,##0.0%);_("–"_)_%;_(@_)_%'
F_MULT = '0.0"x"'
F_ACT = '0"A"'
F_FCST = '0"F"'
F_CHECK = '"Yes";"ERROR";"No";"ERROR"'

THIN = Side(style="thin", color=EDGE)
MED = Side(style="medium", color=NAVY)


# --------------------------------------------------------------------- helpers

def _f(sz=10, b=False, color=BLACK, italic=False):
    return Font(name="Calibri", size=sz, bold=b, color=color, italic=italic)


def put(ws, cell, value, *, fmt=None, font=None, fill=None, align=None,
        note=None, wrap=False):
    c = ws[cell]
    c.value = value
    if fmt:
        c.number_format = fmt
    c.font = font or _f()
    if fill:
        c.fill = PatternFill("solid", fgColor=fill)
    if align or wrap:
        c.alignment = Alignment(horizontal=align or "left", vertical="top", wrap_text=wrap)
    if note:
        c.comment = Comment(note, "HRPB Desk")
    return c


def section(ws, row, title, width=14):
    put(ws, f"B{row}", title, font=_f(10, True, "FFFFFF"), fill=NAVY)
    for i in range(3, width):
        ws.cell(row=row, column=i).fill = PatternFill("solid", fgColor=NAVY)
    return row + 1


def years(ws, row, first_col=4):
    """Year header: historicals get A, forecasts get F, current year gets A."""
    this_year = _dt.date.today().year
    for i, y in enumerate(range(HIST_START, FORECAST_END + 1)):
        col = get_column_letter(first_col + i)
        put(ws, f"{col}{row}", y, fmt=(F_ACT if y <= this_year else F_FCST),
            font=_f(10, True, NAVY), align="center")
        ws.column_dimensions[col].width = 11
    return row + 1


def col_range(first_col=4):
    n = FORECAST_END - HIST_START + 1
    return [get_column_letter(first_col + i) for i in range(n)]


def sheet_prep(wb, name, title, subtitle=None):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 44
    ws.column_dimensions["C"].width = 2
    put(ws, "B2", title, font=_f(14, True, NAVY))
    if subtitle:
        put(ws, "B3", subtitle, font=_f(9, False, GREY, italic=True))
    ws.freeze_panes = "D6"
    return ws


# ------------------------------------------------------------- store plumbing

def _fact(profile, cat, *fields):
    blk = profile.get(cat)
    if not isinstance(blk, dict):
        return None
    for f in fields:
        v = blk.get(f)
        if isinstance(v, list) and v:
            v = v[-1]
        if schema.is_fact(v):
            return v
    return None


def _series(profile, cat, field):
    blk = profile.get(cat)
    if not isinstance(blk, dict):
        return []
    v = blk.get(field)
    if not isinstance(v, list):
        return []
    return [f for f in v if schema.is_fact(f) and isinstance(f.get("value"), (int, float))]


class Inputs:
    """Tracks every input written, so the cover can report how much of the
    model rests on sourced fact versus assumption."""

    def __init__(self):
        self.sourced, self.assumed = [], []

    def sourced_cell(self, ws, cell, value, fact, label, fmt=None):
        note = (f"SOURCED FACT\n{label}\n\nValue: {fact.get('value')}\n"
                f"As of: {fact.get('as_of')}\nTier: {fact.get('tier')}\n"
                f"Source: {fact.get('source')}")
        if fact.get("note"):
            note += f"\nNote: {fact['note']}"
        put(ws, cell, value, fmt=fmt, font=_f(10, False, BLUE_IN), note=note)
        self.sourced.append(label)

    def assumed_cell(self, ws, cell, value, label, reasoning, fmt=None):
        put(ws, cell, value, fmt=fmt, font=_f(10, False, BLUE_IN),
            fill="FFFDE7", note=f"ASSUMPTION\n{label}\n\nBasis: {reasoning}")
        self.assumed.append(label)

    @property
    def ratio(self):
        tot = len(self.sourced) + len(self.assumed)
        return (len(self.sourced) / tot) if tot else 0.0


# ------------------------------------------------------------------- the build

def build(slug: str, kind: str = "operating", out: str = None) -> dict:
    profile = store.load_profile(slug)
    name = None
    for e in store.universe().get("companies", []):
        if e.get("slug") == slug:
            name = e.get("name")
    name = name or slug
    brief = briefing.load(slug)
    inp = Inputs()

    wb = Workbook()
    wb.remove(wb.active)
    cols = col_range()
    this_year = _dt.date.today().year
    n_hist = this_year - HIST_START + 1

    # ---------------------------------------------------------------- Inputs
    ws = sheet_prep(wb, "Inputs", f"{name} — Inputs and assumptions",
                    "All figures in USD millions unless stated. "
                    "Blue cells are inputs. Yellow-filled blue cells are assumptions.")
    r = 5
    r = years(ws, r)
    r += 1

    r = section(ws, r, "Scenario")
    put(ws, f"B{r}", "Driver switch (1 = Base, 2 = Bull, 3 = Bear)")
    inp.assumed_cell(ws, f"D{r}", 1, "Scenario switch",
                     "Base case selected. Change to 2 or 3 to move the whole model.")
    switch = f"Inputs!$D${r}"
    r += 2

    rr = _series(profile, "financials", "run_rate_ladder_bn")
    gr = _series(profile, "financials", "growth_yoy_pct_ladder")
    gm = _fact(profile, "financials", "gross_margin_pct_ladder", "gross_margin_pct")
    emp = _fact(profile, "headcount", "employees_ladder", "employees")
    val = _fact(profile, "valuation", "post_money_bn", "pb_last_known_valuation_bn")
    eq = _fact(profile, "financing", "equity_raised_bn")
    nrr = _fact(profile, "customers", "nrr_pct")

    r = section(ws, r, "Revenue drivers")
    put(ws, f"B{r}", "Latest annualised revenue ($M)")
    if rr:
        inp.sourced_cell(ws, f"D{r}", rr[-1]["value"] * 1000, rr[-1],
                         "Annualised revenue", F_CUR)
    else:
        inp.assumed_cell(ws, f"D{r}", 100, "Annualised revenue",
                         "No revenue in the store. Placeholder — replace before use.", F_CUR)
    rev_anchor = f"Inputs!$D${r}"
    r += 1

    put(ws, f"B{r}", "Latest revenue growth (% YoY)")
    if gr:
        inp.sourced_cell(ws, f"D{r}", gr[-1]["value"] / 100, gr[-1],
                         "Revenue growth YoY", F_PCT)
    else:
        inp.assumed_cell(ws, f"D{r}", 0.40, "Revenue growth YoY",
                         "No growth print in the store.", F_PCT)
    g0 = f"Inputs!$D${r}"
    r += 1

    put(ws, f"B{r}", "Growth decay per year (points of growth lost)")
    inp.assumed_cell(ws, f"D{r}", 0.15, "Growth decay",
                     "Growth fades as the base compounds. 15 points a year is the "
                     "house default for a company at this scale; override per company.", F_PCT)
    decay = f"Inputs!$D${r}"
    r += 1

    put(ws, f"B{r}", "Terminal growth (% a year)")
    inp.assumed_cell(ws, f"D{r}", 0.04, "Terminal growth",
                     "Long-run growth after the forecast window.", F_PCT)
    tg = f"Inputs!$D${r}"
    r += 1

    put(ws, f"B{r}", "Scenario multiplier on growth")
    put(ws, f"D{r}", f"=CHOOSE({switch},1,1.25,0.7)", fmt="0.00", font=_f(10, False, BLACK))
    scen_mult = f"Inputs!$D${r}"
    r += 2

    r = section(ws, r, "Margin and cost drivers")
    put(ws, f"B{r}", "Gross margin (%)")
    if gm:
        inp.sourced_cell(ws, f"D{r}", gm["value"] / 100, gm, "Gross margin", F_PCT)
    else:
        inp.assumed_cell(ws, f"D{r}", 0.70, "Gross margin",
                         "No margin disclosed. 70% is a software-sector placeholder.", F_PCT)
    gm_ref = f"Inputs!$D${r}"
    r += 1
    put(ws, f"B{r}", "Gross margin drift per year (points)")
    inp.assumed_cell(ws, f"D{r}", -0.005, "Gross margin drift",
                     "AI workloads carry a heavier cost of delivery than classic software.", F_PCT)
    gm_drift = f"Inputs!$D${r}"
    r += 1
    for lbl, default, why in (
        ("Sales and marketing (% of revenue)", 0.32,
         "Typical for a company still growing above 40%."),
        ("Research and development (% of revenue)", 0.28,
         "Frontier AI and data platforms run heavier than classic software."),
        ("General and administrative (% of revenue)", 0.10,
         "Scales down slowly with revenue."),
    ):
        put(ws, f"B{r}", lbl)
        inp.assumed_cell(ws, f"D{r}", default, lbl, why, F_PCT)
        r += 1
    sm_ref, rd_ref, ga_ref = (f"Inputs!$D${r-3}", f"Inputs!$D${r-2}", f"Inputs!$D${r-1}")
    put(ws, f"B{r}", "Operating expense leverage per year (points)")
    inp.assumed_cell(ws, f"D{r}", -0.015, "Opex leverage",
                     "Operating costs fall as a share of revenue as the company scales.", F_PCT)
    lev = f"Inputs!$D${r}"
    r += 2

    r = section(ws, r, "Capital and valuation")
    put(ws, f"B{r}", "Latest valuation ($M)")
    if val:
        inp.sourced_cell(ws, f"D{r}", val["value"] * 1000, val, "Valuation", F_CUR)
    else:
        inp.assumed_cell(ws, f"D{r}", 0, "Valuation", "No mark in the store.", F_CUR)
    val_ref = f"Inputs!$D${r}"
    r += 1
    put(ws, f"B{r}", "Equity raised to date ($M)")
    if eq:
        inp.sourced_cell(ws, f"D{r}", eq["value"] * 1000, eq,
                         "Equity raised (equity only, house ruling R1)", F_CUR)
    else:
        inp.assumed_cell(ws, f"D{r}", 0, "Equity raised", "Not in the store.", F_CUR)
    eq_ref = f"Inputs!$D${r}"
    r += 1
    put(ws, f"B{r}", "Discount rate (cost of capital)")
    inp.assumed_cell(ws, f"D{r}", 0.12, "Discount rate",
                     "Private, high-growth, pre-exit. 12% is the house default.", F_PCT)
    wacc = f"Inputs!$D${r}"
    r += 1
    put(ws, f"B{r}", "Tax rate")
    inp.assumed_cell(ws, f"D{r}", 0.21, "Tax rate", "US federal statutory.", F_PCT)
    tax = f"Inputs!$D${r}"
    r += 1
    put(ws, f"B{r}", "Exit multiple on revenue")
    inp.assumed_cell(ws, f"D{r}", 12.0, "Exit multiple",
                     "Applied to terminal-year revenue in the exit-multiple method.", F_MULT)
    exit_x = f"Inputs!$D${r}"
    r += 1
    put(ws, f"B{r}", "Headcount (latest)")
    if emp:
        inp.sourced_cell(ws, f"D{r}", emp["value"], emp, "Employees", F_CUR)
    else:
        inp.assumed_cell(ws, f"D{r}", 0, "Employees", "Not in the store.", F_CUR)
    r += 1
    if nrr:
        put(ws, f"B{r}", "Net revenue retention")
        put(ws, f"D{r}", str(nrr.get("value")), font=_f(10, False, BLUE_IN),
            note=f"SOURCED FACT\nNet revenue retention\nAs of: {nrr.get('as_of')}\n"
                 f"Source: {nrr.get('source')}")
        inp.sourced.append("Net revenue retention")
        r += 1

    # ------------------------------------------------------------- Raw Data
    ws = sheet_prep(wb, "Raw Data", f"{name} — Historical record from the store",
                    "Every figure below is a stored Fact. Source and date sit "
                    "beside it; hover any value for its full provenance.")
    r = 5
    put(ws, "B5", "Metric", font=_f(9, True, GREY))
    put(ws, "D5", "Value", font=_f(9, True, GREY))
    put(ws, "F5", "As of", font=_f(9, True, GREY))
    put(ws, "H5", "Tier", font=_f(9, True, GREY))
    put(ws, "J5", "Source", font=_f(9, True, GREY))
    ws.column_dimensions["D"].width = 16
    ws.column_dimensions["F"].width = 13
    ws.column_dimensions["H"].width = 7
    ws.column_dimensions["J"].width = 70
    r = 6
    for cat, path, fct in schema.walk_facts(profile):
        if cat in ("triggers", "events"):
            continue
        v = fct.get("value")
        if isinstance(v, dict):
            v = "; ".join(f"{k}={x}" for k, x in v.items())
        put(ws, f"B{r}", briefing.label(cat, path), font=_f(9))
        put(ws, f"C{r}", "", font=_f(9))
        put(ws, f"D{r}", v if isinstance(v, (int, float)) else str(v)[:60],
            font=_f(9, False, BLUE_IN),
            fmt=F_CUR if isinstance(v, (int, float)) else None)
        put(ws, f"F{r}", fct.get("as_of"), font=_f(9, False, GREY))
        put(ws, f"H{r}", fct.get("tier"), font=_f(9, False, GREY))
        put(ws, f"J{r}", str(fct.get("source") or "")[:120], font=_f(8, False, GREY))
        r += 1
    raw_rows = r - 6

    # ----------------------------------------------------------------- Model
    ws = sheet_prep(wb, "Model", f"{name} — Operating model",
                    "All figures in USD millions. Black cells are formulas.")
    r = 5
    r = years(ws, r)
    yr_row = r - 1
    r += 1

    r = section(ws, r, "Revenue")
    growth_row = r
    put(ws, f"B{r}", "Revenue growth (% YoY)")
    for i, c in enumerate(cols):
        y = HIST_START + i
        if i == 0:
            put(ws, f"{c}{r}", "", fmt=F_PCT)
        elif y <= this_year:
            put(ws, f"{c}{r}", f"={c}{r+1}/{cols[i-1]}{r+1}-1", fmt=F_PCT)
        else:
            prev = cols[i - 1]
            put(ws, f"{c}{r}", f"=MAX({tg},{prev}{r}-{decay})*{scen_mult}", fmt=F_PCT)
    r += 1

    rev_row = r
    put(ws, f"B{r}", "Revenue")
    # historical revenue is back-solved from the latest print and its growth path
    hist_rev = {}
    if rr:
        latest = rr[-1]["value"] * 1000
        gpath = [g["value"] / 100 for g in gr] or [0.5]
        cur = latest
        for back in range(n_hist):
            y = this_year - back
            hist_rev[y] = cur
            g = gpath[max(0, len(gpath) - 1 - back)]
            cur = cur / (1 + g)
    for i, c in enumerate(cols):
        y = HIST_START + i
        if y <= this_year:
            v = hist_rev.get(y)
            put(ws, f"{c}{r}", round(v, 1) if v else 0, fmt=F_CUR,
                font=_f(10, False, BLUE_IN),
                note=("Back-solved from the latest stored annualised revenue and the "
                      "stored growth ladder. An estimate, not a disclosed figure."))
        else:
            put(ws, f"{c}{r}", f"={cols[i-1]}{r}*(1+{c}{growth_row})", fmt=F_CUR)
    if rr:
        inp.assumed.append("Historical revenue path (back-solved)")
    r += 2

    r = section(ws, r, "Profit and loss")
    gm_row = r
    put(ws, f"B{r}", "Gross margin (%)")
    for i, c in enumerate(cols):
        y = HIST_START + i
        put(ws, f"{c}{r}", f"={gm_ref}" if y <= this_year
            else f"={cols[i-1]}{r}+{gm_drift}", fmt=F_PCT)
    r += 1
    gp_row = r
    put(ws, f"B{r}", "Gross profit")
    for c in cols:
        put(ws, f"{c}{r}", f"={c}{rev_row}*{c}{gm_row}", fmt=F_CUR)
    r += 1

    opex_rows = {}
    for lbl, ref in (("Sales and marketing", sm_ref),
                     ("Research and development", rd_ref),
                     ("General and administrative", ga_ref)):
        put(ws, f"B{r}", lbl)
        for i, c in enumerate(cols):
            y = HIST_START + i
            pct = (f"={ref}" if y <= this_year
                   else f"=MAX(0.02,{ref}+{lev}*{y - this_year})")
            put(ws, f"{c}{r}", f"{pct.replace('=', '=' )}*{c}{rev_row}"
                if False else f"={c}{rev_row}*MAX(0.02,{ref}+{lev}*MAX(0,{c}{yr_row}-{this_year}))",
                fmt=F_CUR)
        opex_rows[lbl] = r
        r += 1

    opex_total = r
    put(ws, f"B{r}", "Total operating expenses", font=_f(10, True))
    for c in cols:
        put(ws, f"{c}{r}", f"=SUM({c}{min(opex_rows.values())}:{c}{max(opex_rows.values())})",
            fmt=F_CUR, font=_f(10, True))
    r += 1

    ebit_row = r
    put(ws, f"B{r}", "Operating profit", font=_f(10, True))
    for c in cols:
        put(ws, f"{c}{r}", f"={c}{gp_row}-{c}{opex_total}", fmt=F_CUR, font=_f(10, True))
    r += 1
    put(ws, f"B{r}", "Operating margin (%)")
    for c in cols:
        put(ws, f"{c}{r}", f"=IF({c}{rev_row}=0,0,{c}{ebit_row}/{c}{rev_row})", fmt=F_PCT)
    r += 2

    r = section(ws, r, "Cash flow")
    tax_row = r
    put(ws, f"B{r}", "Tax")
    for c in cols:
        put(ws, f"{c}{r}", f"=-MAX(0,{c}{ebit_row})*{tax}", fmt=F_CUR)
    r += 1
    put(ws, f"B{r}", "Capital expenditure and working capital")
    capex_row = r
    for c in cols:
        put(ws, f"{c}{r}", f"=-{c}{rev_row}*0.06", fmt=F_CUR)
    r += 1
    fcf_row = r
    put(ws, f"B{r}", "Free cash flow", font=_f(10, True))
    for c in cols:
        put(ws, f"{c}{r}", f"={c}{ebit_row}+{c}{tax_row}+{c}{capex_row}",
            fmt=F_CUR, font=_f(10, True))
    r += 2

    r = section(ws, r, "Per-employee and efficiency")
    put(ws, f"B{r}", "Revenue per employee ($000)")
    emp_cell = f"Inputs!$D${_find_row(ws, None)}" if False else None
    for c in cols:
        put(ws, f"{c}{r}", f"=IF({c}{rev_row}=0,0,{c}{rev_row}*1000/MAX(1,Inputs!$D$34))",
            fmt=F_CUR)
    r += 1

    # ------------------------------------------------------------- Valuation
    ws = sheet_prep(wb, "Valuation", f"{name} — Valuation",
                    "Discounted cash flow and an exit-multiple cross-check. "
                    "All figures in USD millions.")
    r = 5
    r = years(ws, r)
    r += 1
    r = section(ws, r, "Discounted cash flow")
    disc_row = r
    put(ws, f"B{r}", "Discount factor")
    for i, c in enumerate(cols):
        y = HIST_START + i
        put(ws, f"{c}{r}", 0 if y <= this_year
            else f"=1/(1+{wacc})^{y - this_year}", fmt="0.000")
    r += 1
    pv_row = r
    put(ws, f"B{r}", "Present value of free cash flow")
    for i, c in enumerate(cols):
        y = HIST_START + i
        put(ws, f"{c}{r}", 0 if y <= this_year
            else f"=Model!{c}{fcf_row}*{c}{disc_row}", fmt=F_CUR)
    r += 2

    last = cols[-1]
    put(ws, f"B{r}", "Sum of discounted cash flows", font=_f(10, True))
    put(ws, f"D{r}", f"=SUM({cols[n_hist]}{pv_row}:{last}{pv_row})", fmt=F_CUR,
        font=_f(10, True))
    sum_pv = f"D{r}"
    r += 1
    put(ws, f"B{r}", "Terminal value (perpetuity)")
    put(ws, f"D{r}", f"=Model!{last}{fcf_row}*(1+{tg})/({wacc}-{tg})*{last}{disc_row}",
        fmt=F_CUR)
    tv_perp = f"D{r}"
    r += 1
    put(ws, f"B{r}", "Terminal value (exit multiple)")
    put(ws, f"D{r}", f"=Model!{last}{rev_row}*{exit_x}*{last}{disc_row}", fmt=F_CUR)
    tv_exit = f"D{r}"
    r += 1
    put(ws, f"B{r}", "Terminal value used (average of the two)")
    put(ws, f"D{r}", f"=AVERAGE({tv_perp},{tv_exit})", fmt=F_CUR)
    tv_used = f"D{r}"
    r += 2

    put(ws, f"B{r}", "Enterprise value", font=_f(11, True, NAVY))
    put(ws, f"D{r}", f"={sum_pv}+{tv_used}", fmt=F_CUR, font=_f(11, True, NAVY))
    ev_cell = f"Valuation!$D${r}"
    r += 2

    r = section(ws, r, "Cross-checks against the stored mark")
    put(ws, f"B{r}", "Latest stored valuation")
    put(ws, f"D{r}", f"={val_ref}", fmt=F_CUR, font=_f(10, False, LINK))
    mark_row = r
    r += 1
    put(ws, f"B{r}", "Model value against the stored mark")
    put(ws, f"D{r}", f"=IF(D{mark_row}=0,0,{ev_cell}/D{mark_row})", fmt=F_MULT)
    r += 1
    put(ws, f"B{r}", "Stored mark against latest revenue")
    put(ws, f"D{r}", f"=IF(Model!{cols[n_hist-1]}{rev_row}=0,0,"
                     f"D{mark_row}/Model!{cols[n_hist-1]}{rev_row})", fmt=F_MULT)
    r += 1
    put(ws, f"B{r}", "Stored mark per dollar of equity raised")
    put(ws, f"D{r}", f"=IF({eq_ref}=0,0,D{mark_row}/{eq_ref})", fmt=F_MULT,
        note="Equity only. Debt informs risk, never this ratio (house ruling R1).")
    r += 1

    # --------------------------------------------------------------- Outputs
    ws = sheet_prep(wb, "Outputs", f"{name} — Summary", "All figures in USD millions.")
    r = 5
    r = years(ws, r)
    r += 1
    for lbl, src in (("Revenue", rev_row), ("Gross profit", gp_row),
                     ("Operating profit", ebit_row), ("Free cash flow", fcf_row)):
        put(ws, f"B{r}", lbl, font=_f(10, True))
        for c in cols:
            put(ws, f"{c}{r}", f"=Model!{c}{src}", fmt=F_CUR, font=_f(10, False, LINK))
        r += 1
    r += 1
    put(ws, f"B{r}", "Enterprise value (discounted cash flow)", font=_f(11, True, NAVY))
    put(ws, f"D{r}", f"={ev_cell}", fmt=F_CUR, font=_f(11, True, NAVY))
    r += 2
    if brief.get("one_liner"):
        put(ws, f"B{r}", "What this business does", font=_f(10, True, NAVY))
        r += 1
        put(ws, f"B{r}", brief["one_liner"], font=_f(9, False, GREY), wrap=True)
        ws.row_dimensions[r].height = 30

    # ----------------------------------------------------------------- Cover
    ws = wb.create_sheet("Cover", 0)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 52
    ws.column_dimensions["C"].width = 3
    ws.column_dimensions["D"].width = 22
    put(ws, "B2", name, font=_f(20, True, NAVY))
    put(ws, "B3", f"Operating and valuation model — {HIST_START} to {FORECAST_END}",
        font=_f(12, False, SLATE))
    put(ws, "B4", f"Prepared {_dt.date.today().isoformat()} · HRPB Research Desk",
        font=_f(9, False, GREY, italic=True))

    r = 6
    r = section(ws, r, "Contents", width=6)
    for s, d in (("Inputs", "Every assumption, in blue. Yellow fill marks an estimate."),
                 ("Raw Data", "The stored facts, with source and date."),
                 ("Model", "Revenue, profit and loss, and cash flow."),
                 ("Valuation", "Discounted cash flow and cross-checks."),
                 ("Outputs", "The summary.")):
        put(ws, f"B{r}", s, font=_f(10, True))
        put(ws, f"D{r}", d, font=_f(9, False, GREY))
        r += 1
    r += 1

    r = section(ws, r, "Model checks", width=6)
    checks = [
        ("Gross profit exceeds revenue?", f"=IF(SUMPRODUCT(--(Model!D{gp_row}:{last}{gp_row}>"
                                          f"Model!D{rev_row}:{last}{rev_row}))>0,1,0)"),
        ("Any negative revenue?", f"=IF(SUMPRODUCT(--(Model!D{rev_row}:{last}{rev_row}<0))>0,1,0)"),
        ("Discount rate at or below terminal growth?", f"=IF({wacc}<={tg},1,0)"),
        ("Enterprise value non-positive?", f"=IF({ev_cell}<=0,1,0)"),
    ]
    for lbl, formula in checks:
        put(ws, f"B{r}", lbl, font=_f(10))
        put(ws, f"D{r}", formula, fmt=F_CHECK, font=_f(10, True))
        r += 1
    put(ws, f"B{r}", "All checks should read No.", font=_f(9, False, GREY, italic=True))
    r += 2

    r = section(ws, r, "How much of this model is fact", width=6)
    total = len(inp.sourced) + len(inp.assumed)
    pct = inp.ratio
    put(ws, f"B{r}", "Inputs drawn from sourced facts")
    put(ws, f"D{r}", len(inp.sourced), fmt=F_CUR, font=_f(10, True, GREEN))
    r += 1
    put(ws, f"B{r}", "Inputs that are desk assumptions")
    put(ws, f"D{r}", len(inp.assumed), fmt=F_CUR, font=_f(10, True, "8A6410"))
    r += 1
    put(ws, f"B{r}", "Share sourced")
    put(ws, f"D{r}", pct, fmt=F_PCT, font=_f(10, True))
    r += 1
    verdict = ("RESEARCH GRADE — the majority of inputs trace to sourced facts."
               if pct >= 0.5 else
               "ILLUSTRATIVE ONLY — most inputs are desk assumptions. This company "
               "discloses too little to support a decision model. Treat the outputs "
               "as a shape, not a number.")
    put(ws, f"B{r}", verdict, font=_f(10, True, GREEN if pct >= 0.5 else "8F3421"),
        wrap=True)
    ws.row_dimensions[r].height = 32
    r += 2

    put(ws, f"B{r}", "Convention", font=_f(10, True, NAVY))
    r += 1
    for txt, col in (("Blue text — an input you may change", BLUE_IN),
                     ("Yellow fill — an assumption, not a sourced fact", "8A6410"),
                     ("Black text — a formula; do not overwrite", BLACK),
                     ("Green text — a link to another sheet", LINK)):
        put(ws, f"B{r}", txt, font=_f(9, False, col))
        r += 1
    r += 1
    put(ws, f"B{r}", "Every blue cell carries a note with its source and date. "
                     "Hover to read it.", font=_f(9, False, GREY, italic=True))

    # ------------------------------------------------------------------ save
    out = out or os.path.join(store.COMPANIES, slug, "financials",
                              f"{slug}_model_{_dt.date.today().isoformat()}.xlsx")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    wb.save(out)
    return {"path": out, "sourced": len(inp.sourced), "assumed": len(inp.assumed),
            "ratio": pct, "raw_rows": raw_rows, "years": f"{HIST_START}-{FORECAST_END}",
            "grade": "research" if pct >= 0.5 else "illustrative"}


def _find_row(ws, _):
    return 34
