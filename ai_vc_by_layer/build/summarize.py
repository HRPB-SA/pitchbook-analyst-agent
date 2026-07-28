# CONTEXT: AI-VC-BY-LAYER - reads the three PitchBook layer datasets, writes the
# combined company-level CSV, and prints the layer totals used in the report.
# Every figure in the report's tables must reproduce from this script.
import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
LAYERS = {
    "Model": "model_layer.json",
    "Data/Infrastructure": "infra_layer.json",
    "Application": "app_layer.json",
}

rows = []
for layer, fname in LAYERS.items():
    for c in json.loads((DATA / fname).read_text()):
        lr = c.get("last_round") or {}
        rows.append({
            "layer": layer,
            "subsegment": c.get("subsegment", ""),
            "company": c["company"],
            "pbid": c.get("pbid", ""),
            "hq_country": c.get("hq_country", ""),
            "status": c.get("status", ""),
            "vc_equity_raised_usd_m": c.get("vc_equity_raised_usd_m"),
            "debt_or_other_usd_m": c.get("debt_or_other_usd_m"),
            "total_raised_usd_m": c.get("total_raised_usd_m"),
            "last_round_date": lr.get("date"),
            "last_round_type": lr.get("type"),
            "last_round_size_usd_m": lr.get("size_usd_m"),
            "last_post_val_usd_m": lr.get("post_val_usd_m"),
            "notes": c.get("notes", ""),
        })

rows.sort(key=lambda r: (r["layer"], -(r["vc_equity_raised_usd_m"] or 0)))
out = DATA / "companies.csv"
with out.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

def total(pred):
    return sum(r["vc_equity_raised_usd_m"] or 0 for r in rows if pred(r))

model = total(lambda r: r["layer"] == "Model")
infra = total(lambda r: r["layer"] == "Data/Infrastructure")
app = total(lambda r: r["layer"] == "Application")
app_exdef = total(lambda r: r["layer"] == "Application" and r["subsegment"] != "defense")
defense = app - app_exdef
meta_scale = 14300.0  # Meta's 49% primary into Scale AI, booked by PitchBook as a VC round
big3 = total(lambda r: r["company"] in ("OpenAI", "Anthropic", "xAI"))
grand = model + infra + app
grand_incl_meta = grand + meta_scale

n = {L: sum(1 for r in rows if r["layer"] == L) for L in LAYERS}
assert len(rows) == sum(n.values())
assert abs((model + infra + app) - grand) < 0.01

print(f"companies.csv written: {len(rows)} companies "
      f"(model {n['Model']}, infra {n['Data/Infrastructure']}, app {n['Application']})")
print(f"Model layer VC equity:          ${model:,.1f}M")
print(f"  of which OpenAI+Anthropic+xAI ${big3:,.1f}M ({100*big3/model:.1f}% of layer)")
print(f"Data/Infrastructure VC equity:  ${infra:,.1f}M (ex Meta-Scale strategic)")
print(f"  incl Meta-Scale $14.3B:       ${infra+meta_scale:,.1f}M")
print(f"Application VC equity:          ${app:,.1f}M")
print(f"  ex defense (Anduril/Shield/Helsing): ${app_exdef:,.1f}M (defense ${defense:,.1f}M)")
print(f"GRAND TOTAL (narrow VC equity): ${grand:,.1f}M")
print(f"GRAND TOTAL incl Meta-Scale:    ${grand_incl_meta:,.1f}M")
print(f"Layer shares (narrow): model {100*model/grand:.1f}% / infra {100*infra/grand:.1f}% "
      f"/ app {100*app/grand:.1f}%")

debt = sum(r["debt_or_other_usd_m"] or 0 for r in rows
           if r["company"] not in ("Zhipu AI (Z.ai)", "MiniMax", "Scale AI"))
print(f"Identified debt/non-VC capital across universe (ex IPO proceeds, ex Meta-Scale): "
      f"${debt:,.1f}M")
