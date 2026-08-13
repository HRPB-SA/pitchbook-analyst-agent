"""Readability layer: plain labels, derived analysis, and the scoring rubric.

The fact store is machine-shaped — `financials.run_rate_ladder_bn[3]` is a
precise name and an unreadable one. This module turns the store into something
a person can read in one pass:

    LABELS      field path -> plain English
    analysis()  metrics the store implies but does not state
    AIBQ        the scoring rubric, its weights, and what each dimension means
    scores()    a company's composite, its band, and how it moved

EMBARGO (Canon Ruling 2, enforced here as in engine/charts.py): nothing in this
module relates a quality score to a valuation. No coefficient, no ratio, no
ranking of one against the other. The two are computed and displayed
separately and never joined.
"""
from __future__ import annotations

import datetime as _dt
import json
import os

from . import schema, store

# --------------------------------------------------------------- plain labels

LABELS = {
    "identity.name": "Legal name",
    "identity.hq": "Headquarters",
    "identity.ceo": "Chief executive",
    "identity.founded": "Founded",
    "identity.pb_entity_id": "PitchBook ID",
    "valuation.post_money_bn": "Valuation at last completed round",
    "valuation.pb_last_known_valuation_bn": "Latest valuation on record",
    "valuation.valuation_ladder_bn": "Valuation history",
    "valuation.rumored_round": "Round in progress",
    "financing.total_raised_bn": "Total raised (equity and debt)",
    "financing.equity_raised_bn": "Equity raised",
    "financing.debt_raised_bn": "Debt raised",
    "financing.last_completed_deal": "Last completed round",
    "financing.active_investors": "Investors on the register",
    "financing.series_l_pre_money_bn": "Pre-money at last round",
    "financials.run_rate_ladder_bn": "Annualised revenue",
    "financials.run_rate_bn": "Annualised revenue",
    "financials.growth_yoy_pct_ladder": "Revenue growth, year on year",
    "financials.growth_yoy_pct": "Revenue growth, year on year",
    "financials.gross_margin_pct_ladder": "Gross margin",
    "financials.gross_margin_pct": "Gross margin",
    "financials.fcf_status": "Cash generation",
    "financials.pb_ttm_field_note": "Note on the PitchBook revenue field",
    "headcount.employees_ladder": "Employees",
    "headcount.employees": "Employees",
    "customers.nrr_pct": "Net revenue retention",
    "customers.orgs": "Customer organisations",
    "customers.customers_1m_plus": "Customers spending over $1M",
    "customers.customers_10m_plus": "Customers spending over $10M",
    "ipo_status.s1_status": "IPO filing status",
    "ipo_status.window": "Expected IPO window",
    "scores.aibq_composite": "Quality score (composite)",
    "scores.aibq_dimensions": "Quality score by dimension",
    "competition.private_valuation_rank": "Rank among private companies",
}

_SUFFIX = [("_bn", " ($bn)"), ("_pct", " (%)"), ("_usd", " ($)"), ("_yoy", " YoY")]


def label(cat: str, field: str) -> str:
    """Plain-English name for a field path, falling back to a tidy-up."""
    base = field.split("[")[0]
    key = f"{cat}.{base}"
    if key in LABELS:
        return LABELS[key]
    s = base.replace("_ladder", "").replace(".", " ")
    unit = ""
    for suf, u in _SUFFIX:
        if s.endswith(suf):
            s, unit = s[: -len(suf)], u
            break
    s = s.replace("_", " ").strip()
    return (s[:1].upper() + s[1:]) + unit


# ------------------------------------------------------------------- analysis

def _latest(profile, cat, *fields):
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


def _num(f):
    if not f:
        return None
    v = f.get("value")
    return v if isinstance(v, (int, float)) else None


def _series(profile, cat, field):
    blk = profile.get(cat)
    if not isinstance(blk, dict):
        return []
    v = blk.get(field)
    if not isinstance(v, list):
        return []
    return [f for f in v if schema.is_fact(f) and isinstance(f.get("value"), (int, float))]


def analysis(profile: dict) -> list:
    """Metrics the store implies but does not state, each with its arithmetic
    shown so a reader can check it rather than trust it."""
    out = []

    def add(label_, value, workings, caveat=None, tone="neutral"):
        out.append({"label": label_, "value": value, "workings": workings,
                    "caveat": caveat, "tone": tone})

    val = _latest(profile, "valuation", "pb_last_known_valuation_bn", "post_money_bn")
    rr = _latest(profile, "financials", "run_rate_ladder_bn", "run_rate_bn")
    eq = _latest(profile, "financing", "equity_raised_bn")
    emp = _latest(profile, "headcount", "employees_ladder", "employees")
    v, r, e, h = _num(val), _num(rr), _num(eq), _num(emp)

    if v and r:
        mult = v / r
        add("Price against revenue", f"{mult:.1f} times",
            f"${v:g}B valuation divided by ${r:g}B annualised revenue.",
            "Annualised revenue is the latest period scaled to a year, not a forecast.")

    # Ruling R1: capital efficiency uses EQUITY ONLY. Debt informs risk, never this.
    if v and e:
        add("Value per dollar of equity raised", f"${v / e:.1f}",
            f"${v:g}B valuation divided by ${e:g}B of equity raised. "
            f"Debt is excluded by house rule: it informs risk, never this ratio.")

    if r and h:
        add("Revenue per employee", f"${r * 1_000_000 / h:,.0f}k",
            f"${r:g}B annualised revenue divided by {h:,.0f} employees.")

    g = _series(profile, "financials", "growth_yoy_pct_ladder")
    if len(g) >= 2:
        first, last = g[0], g[-1]
        d = last["value"] - first["value"]
        word = "accelerating" if d > 2 else ("slowing" if d < -2 else "steady")
        add("Growth direction", word,
            f"Growth went from {first['value']:g}% ({first.get('as_of')}) to "
            f"{last['value']:g}% ({last.get('as_of')}).",
            tone="good" if d > 2 else ("warn" if d < -2 else "neutral"))

    m = _series(profile, "financials", "gross_margin_pct_ladder")
    if len(m) >= 2:
        first, last = m[0], m[-1]
        d = last["value"] - first["value"]
        add("Margin direction", f"{last['value']:g}%, {'down' if d < 0 else 'up'} "
            f"{abs(d):g} points",
            f"Gross margin moved from {first['value']:g}% ({first.get('as_of')}) to "
            f"{last['value']:g}% ({last.get('as_of')}).",
            "Falling margin on rising revenue usually means the cost of delivery is climbing.",
            tone="warn" if d < 0 else "good")

    rl = _series(profile, "financials", "run_rate_ladder_bn")
    if len(rl) >= 2:
        a, b = rl[0], rl[-1]
        try:
            d0 = _dt.date.fromisoformat(a["as_of"]); d1 = _dt.date.fromisoformat(b["as_of"])
            yrs = max((d1 - d0).days / 365.25, 0.08)
            if a["value"] > 0:
                cagr = ((b["value"] / a["value"]) ** (1 / yrs) - 1) * 100
                add("Compound growth since first print", f"{cagr:.0f}% a year",
                    f"From ${a['value']:g}B ({a['as_of']}) to ${b['value']:g}B "
                    f"({b['as_of']}), over {yrs:.1f} years.")
        except Exception:
            pass

    if val and val.get("as_of"):
        try:
            age = (_dt.date.today() - _dt.date.fromisoformat(val["as_of"])).days
            add("Age of the valuation", f"{age} days",
                f"Latest mark dated {val['as_of']}.",
                "Private marks go stale quickly; a number this old may not reflect today.",
                tone="warn" if age > 120 else "neutral")
        except Exception:
            pass

    rum = _latest(profile, "valuation", "rumored_round")
    if rum:
        add("Round in progress", "Not adopted",
            str(rum.get("value"))[:220],
            "House rule: an unclosed round never anchors the base case. It is "
            "analysed as a forward signal and adopted only on completion.",
            tone="warn")
    return out


# -------------------------------------------------------------- scoring rubric
# Source: NEXUS Intelligence/system/aibq-pbq-scoring-framework.md (v3.0,
# effective 2026-05-26). Mirrored here so the dashboard can explain a score
# without the reader opening the rubric.

AIBQ = {
    "version": "v3.0",
    "effective": "2026-05-26",
    "formula": "Composite = (CE x w1) + (RQ x w2) + (CI x w3) + (GO x w4) + (MD x w5) - CRA",
    "dimensions": [
        {"code": "CE", "name": "Capital Efficiency", "weight": 20,
         "plain": "How much value the company creates per dollar it consumes.",
         "subs": ["Stage-appropriate capital conversion (40%)", "Gross margin quality (25%)",
                  "Burn trajectory (20%)", "Capital structure health (15%)"]},
        {"code": "RQ", "name": "Revenue Quality", "weight": 25,
         "plain": "Whether the revenue is durable: does it recur, expand, and stick?",
         "subs": ["Net revenue retention (30%)", "Customer concentration risk (20%)",
                  "Enterprise mix and contract size (20%)", "Revenue durability (15%)",
                  "Pricing power (15%)"]},
        {"code": "CI", "name": "Compute Independence", "weight": 15,
         "plain": "How exposed the company is to whoever supplies its computing power.",
         "subs": ["Provider diversification (30%)", "Infrastructure ownership (25%)",
                  "Energy independence (20%)", "Supply chain resilience (15%)",
                  "Contractual lock-in risk (10%)"]},
        {"code": "GO", "name": "Governance Optionality", "weight": 20,
         "plain": "Whether the ownership and board structure leaves a clean path to an exit.",
         "subs": ["Board quality and independence (25%)", "Corporate structure (20%)",
                  "IPO and exit readiness (20%)", "Regulatory landscape (20%)",
                  "Leadership stability (15%)"]},
        {"code": "MD", "name": "Moat Durability", "weight": 20,
         "plain": "How hard it would be for a competitor to take this business away.",
         "subs": ["Technical differentiation (25%)", "Switching costs and lock-in (25%)",
                  "Talent density and retention (20%)", "Data and network effects (15%)",
                  "Brand and category position (15%)"]},
    ],
    "cra": {
        "name": "Compounding Risk Adjustment",
        "plain": "A penalty subtracted when weakness shows up in several dimensions at "
                 "once, because problems compound rather than add.",
        "rules": ["0 to 1 dimensions at or below 3.0: no penalty",
                  "2 dimensions at or below 3.0: subtract 0.25",
                  "3 dimensions at or below 3.0: subtract 0.75",
                  "4 or more dimensions at or below 3.0: subtract 1.50"],
    },
    "bands": [
        {"tier": "Elite", "lo": 8.5, "hi": 10.0,
         "plain": "Best in class across the board; ready for public-company scrutiny."},
        {"tier": "Strong", "lo": 7.0, "hi": 8.49,
         "plain": "Above average nearly everywhere; one weakness tolerated."},
        {"tier": "Adequate", "lo": 5.0, "hi": 6.99,
         "plain": "Mixed. Real strengths offset by material gaps."},
        {"tier": "Developing", "lo": 3.0, "hi": 4.99,
         "plain": "Below average, with structural problems in two or more dimensions."},
        {"tier": "Distressed", "lo": 1.0, "hi": 2.99,
         "plain": "Critical weakness across most dimensions."},
    ],
    "rules": [
        "No score change without showing the arithmetic.",
        "One event cannot move a single dimension by more than 1.0 point.",
        "One event cannot move the composite by more than 0.50 in a day.",
        "Scores carry forward between events. They are never interpolated and "
        "never updated just because time passed.",
        "Every change is tagged High, Medium or Low confidence by source tier.",
        "A change waits 24 hours before it can be cited externally.",
    ],
    "dai": {
        "name": "Data Availability Index",
        "plain": "How much is actually disclosed about this company. Thin disclosure "
                 "widens the confidence band around any score.",
        "levels": ["D1 (1-2): PitchBook profile and press only",
                   "D2 (3-4): plus an investor deck or analyst estimates",
                   "D3 (5-6): plus reported, unaudited financials",
                   "D4 (7-8): plus audited financials and public filings",
                   "D5 (9-10): full public-grade disclosure"],
        "band": "Confidence band = plus or minus (5 - DAI/2)",
    },
}

DIM_BY_CODE = {d["code"]: d for d in AIBQ["dimensions"]}


def band_for(score):
    if not isinstance(score, (int, float)):
        return None
    for b in AIBQ["bands"]:
        if b["lo"] <= score <= b["hi"]:
            return b
    return None


def scores(profile: dict) -> dict:
    """A company's composite, its dimensions, its band, and how it moved."""
    blk = profile.get("scores")
    if not isinstance(blk, dict):
        return {}
    comp = blk.get("aibq_composite")
    dims = blk.get("aibq_dimensions")
    out = {"has": False}

    if schema.is_fact(comp):
        v = comp.get("value")
        out.update(has=True, composite=v, as_of=comp.get("as_of"),
                   tier=comp.get("tier"), source=comp.get("source"),
                   note=comp.get("note"), band=band_for(v))
        # notes record the previous score as "prior 8.92"; surface the move
        import re as _re
        m = _re.search(r"prior\s+([0-9]+\.?[0-9]*)", str(comp.get("note") or ""), _re.I)
        if m and isinstance(v, (int, float)):
            try:
                prior = float(m.group(1))
                out["prior"] = prior
                out["delta"] = round(v - prior, 2)
            except ValueError:
                pass
    if schema.is_fact(dims) and isinstance(dims.get("value"), dict):
        rows = []
        for code, val in dims["value"].items():
            meta = DIM_BY_CODE.get(code)
            rows.append({
                "code": code,
                "name": meta["name"] if meta else code,
                "plain": meta["plain"] if meta else None,
                "weight": meta["weight"] if meta else None,
                "subs": meta["subs"] if meta else [],
                "value": val,
                "is_penalty": code == "CRA",
            })
        order = {d["code"]: i for i, d in enumerate(AIBQ["dimensions"])}
        rows.sort(key=lambda r: order.get(r["code"], 99))
        out["dimensions"] = rows
        out["as_of_dims"] = dims.get("as_of")
        out["source_dims"] = dims.get("source")

    hist = blk.get("aibq_ladder") or blk.get("aibq_composite_ladder")
    if isinstance(hist, list):
        out["history"] = [{"as_of": f.get("as_of"), "value": f.get("value"),
                           "note": f.get("note"), "source": f.get("source")}
                          for f in hist if schema.is_fact(f)]
    return out


# ------------------------------------------------------------------- briefing

def load(slug: str) -> dict:
    return store._read(os.path.join(store.company_dir(slug), "briefing.json"), {})
