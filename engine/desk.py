"""Desk dashboard: renders the whole fact store as one self-contained page.

`python3 -m engine dashboard` reads companies/universe.json, every
companies/<slug>/store/profile.json and its conflicts, and writes a single
HTML file with the data baked in. No server, no network, no build step: open
it locally or publish it as an artifact.

Three panels:
  COVERAGE   every company, how much is known, how stale it is, what fired
  COMPANY    every stored fact by category, with tier, vintage and source
  REQUEST    compose a report request against the selected company

Regenerate after every tracker refresh; the page is a view, never a source.
"""
import datetime as _dt
import html
import json
import os

from . import schema, store

OUT_DEFAULT = os.path.join(store.REPO, "Report Automation", "dashboard", "desk.html")

TEMPLATES = [
    ("vertical_analyst_note", "Vertical analyst note", "Default. 4-10pp, master format."),
    ("company_update", "Company update", "6-10pp. What changed since the last note."),
    ("initiation_note", "Initiation note", "30-40pp. First full coverage."),
    ("rush_note", "Rush note", "4-8pp. One dated event, fast."),
    ("earnings_note", "Earnings note", "4-8pp. Against a print."),
    ("one_pager", "One-pager", "1-2pp. Thesis, risk, verdict."),
    ("sector_overview", "Sector overview", "10-16pp. Across companies."),
]


# ----------------------------------------------------------------- collection

def _fact_row(cat, path, f, today):
    """Flatten one Fact into the shape the page renders."""
    stale = schema.fact_is_stale(f, cat, today)
    return {
        "cat": cat,
        "field": path,
        "value": f.get("value"),
        "as_of": f.get("as_of"),
        "age": schema.fact_age_days(f, today),
        "tier": f.get("tier"),
        "decay": f.get("decay") or schema.CATEGORIES[cat][1],
        "source": f.get("source"),
        "flags": f.get("flags") or [],
        "note": f.get("note"),
        "stale": bool(stale),
    }


def _triggers(profile):
    """Named triggers carry their state inside the Fact value."""
    out = []
    block = profile.get("triggers")
    if not isinstance(block, dict):
        return out
    for item in block.get("named") or []:
        if not schema.is_fact(item):
            continue
        v = item.get("value")
        if not isinstance(v, dict):
            continue
        out.append({
            "condition": v.get("condition", ""),
            "status": (v.get("status") or "armed").lower(),
            "fired_on": v.get("fired_on"),
            "as_of": item.get("as_of"),
            "source": item.get("source"),
            "note": item.get("note"),
        })
    return out


def _headline(profile):
    """A few figures worth showing on the overview card, if present."""
    def latest(cat, field):
        blk = profile.get(cat)
        if not isinstance(blk, dict):
            return None
        v = blk.get(field)
        if isinstance(v, list) and v:
            v = v[-1]
        return v if schema.is_fact(v) else None

    out = {}
    for label, cat, fields in (
        ("valuation_bn", "valuation",
         ("pb_last_known_valuation_bn", "post_money_bn", "valuation_ladder_bn")),
        ("run_rate_bn", "financials", ("run_rate_ladder_bn", "run_rate_bn")),
        ("growth_pct", "financials", ("growth_yoy_pct_ladder", "growth_yoy_pct")),
        ("employees", "headcount", ("employees_ladder", "employees")),
        ("raised_bn", "financing", ("equity_raised_bn", "total_raised_bn")),
    ):
        for f in fields:
            got = latest(cat, f)
            if got is not None:
                out[label] = {"value": got.get("value"), "as_of": got.get("as_of"),
                              "tier": got.get("tier")}
                break
    return out


def collect(today=None):
    """Read the whole store into one JSON-serializable structure."""
    today = today or _dt.date.today()
    uni = store.universe()
    entries = uni.get("companies", uni if isinstance(uni, list) else [])
    companies = []

    for ent in entries:
        slug = ent.get("slug")
        if not slug:
            continue
        try:
            profile = store.load_profile(slug)
        except Exception:
            profile = {}
        conflicts = []
        try:
            raw = store.load_conflicts(slug)
            conflicts = raw if isinstance(raw, list) else raw.get("conflicts", [])
        except Exception:
            pass

        facts, cats = [], {}
        for cat, path, f in schema.walk_facts(profile):
            row = _fact_row(cat, path, f, today)
            facts.append(row)
            cats.setdefault(cat, 0)
            cats[cat] += 1

        # Only the newest print of a ladder counts toward staleness.
        last_idx = {}
        for r in facts:
            if "[" in r["field"]:
                base, idx = r["field"].rsplit("[", 1)
                idx = int(idx.rstrip("]"))
                last_idx[(r["cat"], base)] = max(last_idx.get((r["cat"], base), -1), idx)
        stale = 0
        for r in facts:
            if "[" in r["field"]:
                base, idx = r["field"].rsplit("[", 1)
                if int(idx.rstrip("]")) < last_idx[(r["cat"], base)]:
                    r["stale"] = False
                    continue
            if r["stale"]:
                stale += 1

        trigs = _triggers(profile)
        flagged = [r for r in facts
                   if any(fl in ("DISPUTED", "VERIFY") for fl in r["flags"])]

        try:
            snaps = store.snapshots(slug)
        except Exception:
            snaps = []

        companies.append({
            "slug": slug,
            "name": ent.get("name", slug),
            "group": ent.get("group", "coverage"),
            "sector": ent.get("sector"),
            "pbid": ent.get("pb_entity_id"),
            "updated": profile.get("_updated"),
            "facts": facts,
            "cats": cats,
            "n_facts": len(facts),
            "n_cats": len(cats),
            "n_stale": stale,
            "n_flagged": len(flagged),
            "n_conflicts": len(conflicts),
            "conflicts": conflicts,
            "triggers": trigs,
            "n_armed": sum(1 for t in trigs if t["status"] == "armed"),
            "n_fired": sum(1 for t in trigs if t["status"] == "fired"),
            "headline": _headline(profile),
            "snapshots": [str(s) for s in snaps],
        })

    companies.sort(key=lambda c: (c["group"] != "frontier_five", -c["n_facts"]))
    return {
        "generated": today.isoformat(),
        "categories": list(schema.CATEGORIES),
        "templates": [{"id": i, "name": n, "blurb": b} for i, n, b in TEMPLATES],
        "companies": companies,
    }


# --------------------------------------------------------------------- render

def render(data):
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("</", "<\\/")
    n_co = len(data["companies"])
    n_facts = sum(c["n_facts"] for c in data["companies"])
    n_stale = sum(c["n_stale"] for c in data["companies"])
    n_armed = sum(c["n_armed"] for c in data["companies"])
    n_thin = sum(1 for c in data["companies"] if c["n_cats"] <= 2)
    return _PAGE.replace("__DATA__", payload).replace("__GEN__", html.escape(data["generated"])) \
        .replace("__NCO__", str(n_co)).replace("__NFACTS__", str(n_facts)) \
        .replace("__NSTALE__", str(n_stale)).replace("__NARMED__", str(n_armed)) \
        .replace("__NTHIN__", str(n_thin))


def build(out=None, today=None):
    out = out or OUT_DEFAULT
    data = collect(today)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render(data))
    return out, data


_PAGE = r"""<title>HRPB Research Desk</title>
<style>
  :root {
    --navy:#1F2A44; --slate:#35506E; --green:#1C5D46; --rust:#8F3421;
    --amber:#8A6410; --muted:#63708A; --ink:#232B3A;
    --ground:#FBFBFC; --panel:#F2F5F9; --band:#E9EEF5; --edge:#D5DBE4; --hair:#E4E9F0;
    --rail:#97A3B8; --on:#1F2A44; --on-ink:#FFFFFF;
    --serif:Georgia,"Iowan Old Style","Times New Roman",serif;
    --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
  }
  @media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
    --navy:#C8D4E8; --slate:#9FB3D0; --green:#7FC4A6; --rust:#D89178; --amber:#D6AE5C;
    --muted:#8E9BB2; --ink:#DCE3EF; --ground:#12161F; --panel:#1A202C; --band:#1E2533;
    --edge:#333C4D; --hair:#262E3C; --rail:#5C6880; --on:#C8D4E8; --on-ink:#12161F;}}
  :root[data-theme="dark"]{
    --navy:#C8D4E8; --slate:#9FB3D0; --green:#7FC4A6; --rust:#D89178; --amber:#D6AE5C;
    --muted:#8E9BB2; --ink:#DCE3EF; --ground:#12161F; --panel:#1A202C; --band:#1E2533;
    --edge:#333C4D; --hair:#262E3C; --rail:#5C6880; --on:#C8D4E8; --on-ink:#12161F;}
  *{box-sizing:border-box}
  body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--serif);
       font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
  .mono{font-family:var(--mono)}
  header.top{border-bottom:2px solid var(--navy);padding:1.5rem 1.6rem 1.1rem;
             display:flex;flex-wrap:wrap;gap:.6rem 1.4rem;align-items:baseline}
  .brand{font-size:1.3rem;font-weight:700;color:var(--navy)}
  .brand em{font-style:normal;color:var(--green)}
  .sub{color:var(--muted);font-size:.82rem;font-family:var(--mono)}
  .stats{margin-left:auto;display:flex;gap:.4rem;flex-wrap:wrap}
  .pill{font-family:var(--mono);font-size:.68rem;letter-spacing:.04em;padding:.2rem .55rem;
        border:1px solid var(--edge);border-radius:999px;color:var(--muted);white-space:nowrap}
  .pill b{color:var(--navy);font-weight:700}
  .pill.warn b{color:var(--rust)}
  nav.tabs{display:flex;gap:0;border-bottom:1px solid var(--edge);padding:0 1.6rem;
           background:var(--ground);position:sticky;top:0;z-index:10;overflow-x:auto}
  nav.tabs button{font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;
    text-transform:uppercase;background:none;border:none;border-bottom:2px solid transparent;
    color:var(--muted);padding:.85rem 1rem;cursor:pointer;white-space:nowrap}
  nav.tabs button[aria-selected="true"]{color:var(--navy);border-bottom-color:var(--green)}
  nav.tabs button:focus-visible{outline:2px solid var(--green);outline-offset:-2px}
  main{padding:1.6rem}
  .panel[hidden]{display:none}
  h2{font-size:1.15rem;color:var(--navy);margin:0 0 .3rem}
  .hint{color:var(--muted);font-size:.86rem;margin:0 0 1.1rem;max-width:70ch}

  .scroll{overflow-x:auto}
  table{border-collapse:collapse;width:100%;min-width:820px;font-size:.88rem}
  th{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;
     color:var(--muted);font-weight:400;text-align:left;padding:0 .7rem .5rem 0;
     border-bottom:1px solid var(--navy);white-space:nowrap}
  td{padding:.5rem .7rem .5rem 0;border-bottom:1px solid var(--hair);vertical-align:top}
  th.r,td.r{text-align:right;font-variant-numeric:tabular-nums;font-family:var(--mono);font-size:.82rem}
  tr.co{cursor:pointer}
  tr.co:hover td{background:var(--panel)}
  tr.co:focus-visible{outline:2px solid var(--green);outline-offset:-2px}
  .co-name{color:var(--navy);font-weight:700}
  .co-slug{font-family:var(--mono);font-size:.7rem;color:var(--rail);display:block}
  .grp{font-family:var(--mono);font-size:.6rem;letter-spacing:.08em;text-transform:uppercase;
       padding:.1rem .4rem;border:1px solid var(--edge);border-radius:2px;color:var(--muted)}
  .grp.f5{color:var(--green);border-color:var(--green)}

  .bar{display:inline-block;height:6px;border-radius:1px;background:var(--green);vertical-align:middle}
  .bartrack{display:inline-block;width:70px;height:6px;background:var(--band);border-radius:1px;
            vertical-align:middle;margin-right:.45rem}
  .thin{color:var(--rust);font-weight:700}
  .ok{color:var(--green)}
  .warnv{color:var(--amber)}

  .tier{font-family:var(--mono);font-size:.6rem;padding:.08rem .3rem;border-radius:2px;
        border:1px solid var(--edge);color:var(--muted)}
  .tier.T1{color:var(--green);border-color:var(--green)}
  .tier.T2{color:var(--slate);border-color:var(--slate)}
  .flag{font-family:var(--mono);font-size:.58rem;letter-spacing:.06em;padding:.08rem .3rem;
        border-radius:2px;background:var(--rust);color:var(--ground);margin-left:.25rem}
  .flag.est{background:var(--muted)}
  .stalechip{font-family:var(--mono);font-size:.58rem;color:var(--amber)}

  .cols{display:grid;grid-template-columns:minmax(200px,270px) 1fr;gap:1.6rem;align-items:start}
  @media (max-width:760px){.cols{grid-template-columns:1fr}}
  .colist{display:flex;flex-direction:column;gap:0;border-top:1px solid var(--edge)}
  .colist button{text-align:left;background:none;border:none;border-bottom:1px solid var(--hair);
    padding:.6rem .5rem;cursor:pointer;font-family:var(--serif);font-size:.9rem;color:var(--ink);
    display:flex;justify-content:space-between;gap:.5rem;align-items:baseline}
  .colist button[aria-current="true"]{background:var(--panel);color:var(--navy);font-weight:700;
    box-shadow:inset 2px 0 0 var(--green)}
  .colist button:focus-visible{outline:2px solid var(--green);outline-offset:-2px}
  .colist .n{font-family:var(--mono);font-size:.7rem;color:var(--rail)}

  .cat{margin-bottom:1.5rem}
  .cat h3{font-family:var(--mono);font-size:.66rem;letter-spacing:.13em;text-transform:uppercase;
          color:var(--muted);margin:0 0 .4rem;padding-bottom:.3rem;border-bottom:1px solid var(--edge);
          font-weight:400}
  .frow{display:grid;grid-template-columns:minmax(130px,190px) 1fr;gap:.4rem 1rem;
        padding:.45rem 0;border-bottom:1px solid var(--hair)}
  @media (max-width:620px){.frow{grid-template-columns:1fr;gap:.15rem}}
  .fk{font-family:var(--mono);font-size:.74rem;color:var(--slate);word-break:break-word}
  .fv{min-width:0}
  .fval{color:var(--ink)}
  .fmeta{font-family:var(--mono);font-size:.66rem;color:var(--muted);margin-top:.15rem;
         display:flex;flex-wrap:wrap;gap:.3rem .6rem;align-items:center}
  .fnote{font-size:.8rem;color:var(--muted);font-style:italic;margin-top:.15rem}

  .trig{border-left:2px solid var(--edge);padding:.5rem 0 .5rem .8rem;margin-bottom:.6rem}
  .trig.armed{border-left-color:var(--amber)}
  .trig.fired{border-left-color:var(--green)}
  .trig .st{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase}
  .trig.armed .st{color:var(--amber)} .trig.fired .st{color:var(--green)}

  .empty{background:var(--panel);border:1px dashed var(--edge);padding:1.4rem;
         color:var(--muted);font-size:.9rem;text-align:center}

  label{display:block;font-family:var(--mono);font-size:.64rem;letter-spacing:.1em;
        text-transform:uppercase;color:var(--muted);margin:1.1rem 0 .4rem}
  select,textarea,input[type=text]{width:100%;font:inherit;font-size:.9rem;padding:.5rem .6rem;
    background:var(--ground);color:var(--ink);border:1px solid var(--edge);border-radius:3px}
  textarea{min-height:5.5rem;resize:vertical}
  select:focus,textarea:focus,input:focus,button:focus-visible{outline:2px solid var(--green);outline-offset:1px}
  .tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.5rem}
  .tcard{text-align:left;background:var(--ground);border:1px solid var(--edge);border-radius:3px;
         padding:.6rem .7rem;cursor:pointer;color:var(--ink);font-family:var(--serif)}
  .tcard[aria-pressed="true"]{border-color:var(--green);background:var(--panel);
         box-shadow:inset 0 0 0 1px var(--green)}
  .tcard b{display:block;color:var(--navy);font-size:.88rem}
  .tcard span{font-size:.75rem;color:var(--muted)}
  .row{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:1.2rem}
  button.action{font-family:var(--mono);font-size:.72rem;letter-spacing:.06em;padding:.55rem .9rem;
    border:1px solid var(--edge);background:var(--ground);color:var(--ink);border-radius:3px;cursor:pointer}
  button.action.primary{background:var(--green);border-color:var(--green);color:var(--ground);font-weight:700}
  pre.out{background:var(--panel);border:1px solid var(--edge);border-radius:3px;padding:.9rem;
    font-family:var(--mono);font-size:.74rem;line-height:1.55;white-space:pre-wrap;word-break:break-word;
    max-height:22rem;overflow:auto;margin:.8rem 0 0;color:var(--ink)}
  .steps{counter-reset:s;margin:1.2rem 0 0;padding:0;list-style:none}
  .steps li{counter-increment:s;display:flex;gap:.7rem;padding:.4rem 0;font-size:.87rem;color:var(--ink)}
  .steps li::before{content:counter(s);font-family:var(--mono);font-size:.66rem;color:var(--green);
    border:1px solid var(--green);border-radius:999px;width:1.35rem;height:1.35rem;flex:0 0 auto;
    display:flex;align-items:center;justify-content:center}
  .flash{position:fixed;left:50%;bottom:1.4rem;transform:translateX(-50%);background:var(--navy);
    color:var(--ground);font-family:var(--mono);font-size:.74rem;padding:.5rem .9rem;border-radius:3px;
    opacity:0;pointer-events:none;transition:opacity .18s}
  .flash.show{opacity:1}
  @media (prefers-reduced-motion:reduce){*{transition:none!important}}
  footer{padding:1.4rem 1.6rem 3rem;border-top:1px solid var(--edge);margin-top:2rem;
    font-family:var(--mono);font-size:.7rem;color:var(--muted);line-height:1.7}
</style>

<header class="top">
  <div>
    <div class="brand">HRPB <em>Research Desk</em></div>
    <div class="sub">Fact store view · generated __GEN__</div>
  </div>
  <div class="stats">
    <span class="pill">Companies <b>__NCO__</b></span>
    <span class="pill">Facts <b>__NFACTS__</b></span>
    <span class="pill warn">Thin coverage <b>__NTHIN__</b></span>
    <span class="pill">Stale <b>__NSTALE__</b></span>
    <span class="pill">Triggers armed <b>__NARMED__</b></span>
  </div>
</header>

<nav class="tabs" role="tablist">
  <button role="tab" id="t-cov" aria-selected="true" aria-controls="p-cov">Coverage</button>
  <button role="tab" id="t-co" aria-selected="false" aria-controls="p-co">Company</button>
  <button role="tab" id="t-req" aria-selected="false" aria-controls="p-req">Request a report</button>
</nav>

<main>
  <section class="panel" id="p-cov" role="tabpanel" aria-labelledby="t-cov">
    <h2>Coverage</h2>
    <p class="hint">Every company in the universe, what the store actually holds on each, and
      what is stale or waiting. Click a row to open it. Thin coverage is the gap worth closing
      first — a report can only be as good as the column marked Facts.</p>
    <div class="scroll"><table>
      <thead><tr>
        <th>Company</th><th>Group</th><th class="r">Facts</th><th>Coverage</th>
        <th class="r">Stale</th><th class="r">Flagged</th><th class="r">Conflicts</th>
        <th>Triggers</th><th>Headline</th><th class="r">Updated</th>
      </tr></thead>
      <tbody id="covbody"></tbody>
    </table></div>
  </section>

  <section class="panel" id="p-co" role="tabpanel" aria-labelledby="t-co" hidden>
    <div class="cols">
      <div>
        <h2>Companies</h2>
        <p class="hint" style="margin-bottom:.7rem">Select to inspect.</p>
        <div class="colist" id="colist"></div>
      </div>
      <div id="codetail"></div>
    </div>
  </section>

  <section class="panel" id="p-req" role="tabpanel" aria-labelledby="t-req" hidden>
    <div class="cols">
      <div>
        <h2>Request a report</h2>
        <p class="hint">Composes the request file and the launch prompt. This page cannot run the
          pipeline itself — it hands you the instruction, and the engine does the rest.</p>
        <label for="rq-co">Company</label>
        <select id="rq-co"></select>
        <label>Template</label>
        <div class="tgrid" id="rq-tpl"></div>
        <label for="rq-idea">The question this note answers</label>
        <textarea id="rq-idea" placeholder="What changed, why it matters, and what you want the note to settle."></textarea>
        <label for="rq-rigor">Rigor (1-5)</label>
        <input type="text" id="rq-rigor" value="4" inputmode="numeric">
        <label for="rq-charts">Charts</label>
        <input type="text" id="rq-charts" value="3" inputmode="numeric">
        <label><input type="checkbox" id="rq-model" style="width:auto;margin-right:.4rem">
          <span style="font-family:var(--serif);text-transform:none;letter-spacing:0;font-size:.9rem;color:var(--ink)">Companion operating model (xlsx)</span></label>
        <div class="row">
          <button class="action primary" id="rq-copy" type="button">Copy launch prompt</button>
          <button class="action" id="rq-json" type="button">Copy request JSON</button>
        </div>
      </div>
      <div>
        <h2>What you send</h2>
        <p class="hint">Paste the prompt into a Claude Code session on this repo, or commit the
          JSON to <span class="mono">Report Automation/requests/queue/</span> and let the
          scheduled run pick it up.</p>
        <pre class="out" id="rq-out"></pre>
        <ol class="steps">
          <li>Pick the company and the format.</li>
          <li>Copy the launch prompt.</li>
          <li>Paste it into a session on <span class="mono">pitchbook-analyst-agent</span>.</li>
          <li>The engine runs research, store, trends, compose, charts, build, validate, ship.</li>
        </ol>
      </div>
    </div>
  </section>
</main>

<footer>
  Generated by <span class="mono">python3 -m engine dashboard</span> from companies/*/store/.
  This page is a view, never a source — edit the store, then regenerate.<br>
  Roadmap: Report Automation/docs/AUTOMATION_ROADMAP.md
</footer>

<div class="flash" id="flash"></div>

<script>
const DATA = __DATA__;
const $ = id => document.getElementById(id);
const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c =>
  ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

/* ---------------------------------------------------------------- tabs */
const TABS = [["t-cov","p-cov"],["t-co","p-co"],["t-req","p-req"]];
TABS.forEach(([t,p]) => $(t).onclick = () => {
  TABS.forEach(([tt,pp]) => {
    const on = tt === t;
    $(tt).setAttribute("aria-selected", on ? "true" : "false");
    $(pp).hidden = !on;
  });
});

/* ------------------------------------------------------------ coverage */
function fmtVal(v) {
  if (v == null) return "—";
  if (typeof v === "number") return String(v);
  if (typeof v === "object") return JSON.stringify(v);
  return String(v);
}
function headlineStr(h) {
  const bits = [];
  if (h.valuation_bn != null) bits.push("$" + fmtVal(h.valuation_bn.value) + "B val");
  if (h.run_rate_bn != null) bits.push("$" + fmtVal(h.run_rate_bn.value) + "B run-rate");
  if (h.growth_pct != null) bits.push("+" + fmtVal(h.growth_pct.value) + "%");
  if (h.employees != null) bits.push(fmtVal(h.employees.value) + " staff");
  return bits.length ? bits.join(" · ") : "—";
}
const MAXF = Math.max(...DATA.companies.map(c => c.n_facts), 1);

function renderCoverage() {
  $("covbody").innerHTML = DATA.companies.map(c => {
    const pct = Math.round(100 * c.n_facts / MAXF);
    const thin = c.n_cats <= 2;
    return `<tr class="co" tabindex="0" data-slug="${esc(c.slug)}">
      <td><span class="co-name">${esc(c.name)}</span><span class="co-slug">${esc(c.slug)}</span></td>
      <td><span class="grp ${c.group === "frontier_five" ? "f5" : ""}">${esc(c.group === "frontier_five" ? "Frontier 5" : "Coverage")}</span></td>
      <td class="r ${thin ? "thin" : ""}">${c.n_facts}</td>
      <td><span class="bartrack"><span class="bar" style="width:${pct}%"></span></span>
          <span class="mono" style="font-size:.7rem;color:var(--muted)">${c.n_cats}/${DATA.categories.length} cats</span></td>
      <td class="r ${c.n_stale ? "warnv" : ""}">${c.n_stale || "—"}</td>
      <td class="r ${c.n_flagged ? "warnv" : ""}">${c.n_flagged || "—"}</td>
      <td class="r ${c.n_conflicts ? "thin" : ""}">${c.n_conflicts || "—"}</td>
      <td class="mono" style="font-size:.72rem">${c.n_armed ? c.n_armed + " armed" : ""}${c.n_armed && c.n_fired ? " · " : ""}${c.n_fired ? c.n_fired + " fired" : ""}${!c.n_armed && !c.n_fired ? "—" : ""}</td>
      <td style="font-size:.8rem;color:var(--muted)">${esc(headlineStr(c.headline))}</td>
      <td class="r" style="color:var(--muted)">${esc(c.updated || "—")}</td>
    </tr>`;
  }).join("");
  document.querySelectorAll("tr.co").forEach(tr => {
    const go = () => { selectCompany(tr.dataset.slug); $("t-co").click(); };
    tr.onclick = go;
    tr.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); go(); } };
  });
}

/* ------------------------------------------------------------- company */
let current = DATA.companies.length ? DATA.companies[0].slug : null;

function renderList() {
  $("colist").innerHTML = DATA.companies.map(c =>
    `<button type="button" data-slug="${esc(c.slug)}" aria-current="${c.slug === current}">
       <span>${esc(c.name)}</span><span class="n">${c.n_facts}</span></button>`).join("");
  document.querySelectorAll("#colist button").forEach(b =>
    b.onclick = () => selectCompany(b.dataset.slug));
}

function factRow(f) {
  const flags = f.flags.map(x =>
    `<span class="flag ${x === "est." ? "est" : ""}">${esc(x)}</span>`).join("");
  return `<div class="frow">
    <div class="fk">${esc(f.field)}</div>
    <div class="fv">
      <div class="fval">${esc(fmtVal(f.value))}${flags}</div>
      <div class="fmeta">
        <span class="tier ${esc(f.tier || "")}">${esc(f.tier || "—")}</span>
        <span>${esc(f.as_of || "—")}</span>
        ${f.stale ? `<span class="stalechip">STALE ${f.age}d · ${esc(f.decay)}</span>` : ""}
        <span style="color:var(--rail)">${esc(f.source || "")}</span>
      </div>
      ${f.note ? `<div class="fnote">${esc(f.note)}</div>` : ""}
    </div></div>`;
}

function selectCompany(slug) {
  current = slug;
  renderList();
  const c = DATA.companies.find(x => x.slug === slug);
  if (!c) return;
  const el = $("codetail");

  if (!c.n_facts) {
    el.innerHTML = `<h2>${esc(c.name)}</h2>
      <p class="hint">${esc(c.slug)} · ${esc(c.sector || "")}</p>
      <div class="empty"><b>No facts stored.</b><br>
      This company is in the universe but the store is empty. Run a research pass and snapshot
      before requesting a report on it.</div>`;
    return;
  }

  const byCat = {};
  c.facts.forEach(f => (byCat[f.cat] = byCat[f.cat] || []).push(f));

  let html = `<h2>${esc(c.name)}</h2>
    <p class="hint">${esc(c.slug)}${c.pbid ? " · PitchBook " + esc(c.pbid) : ""}${c.sector ? " · " + esc(c.sector) : ""}
      · ${c.n_facts} facts · updated ${esc(c.updated || "?")}
      ${c.snapshots.length ? " · " + c.snapshots.length + " snapshot(s)" : ""}</p>`;

  if (c.triggers.length) {
    html += `<div class="cat"><h3>Triggers</h3>` + c.triggers.map(t =>
      `<div class="trig ${esc(t.status)}">
         <div class="st">${esc(t.status)}${t.fired_on ? " · " + esc(t.fired_on) : ""}</div>
         <div style="font-size:.88rem">${esc(t.condition)}</div>
         ${t.source ? `<div class="fmeta"><span style="color:var(--rail)">${esc(t.source)}</span></div>` : ""}
       </div>`).join("") + `</div>`;
  }

  if (c.n_conflicts) {
    html += `<div class="cat"><h3>Frozen conflicts</h3>
      <div class="empty" style="text-align:left;border-color:var(--rust);color:var(--ink)">
      ${c.n_conflicts} unresolved conflict(s). Both values ship or neither.
      <pre class="out" style="margin-top:.6rem">${esc(JSON.stringify(c.conflicts, null, 1))}</pre></div></div>`;
  }

  DATA.categories.forEach(cat => {
    const rows = byCat[cat];
    if (!rows || !rows.length || cat === "triggers") return;
    html += `<div class="cat"><h3>${esc(cat.replace(/_/g, " "))} <span style="color:var(--rail)">${rows.length}</span></h3>`
          + rows.map(factRow).join("") + `</div>`;
  });

  el.innerHTML = html;
}

/* ------------------------------------------------------------- request */
const state = { template: "vertical_analyst_note" };

function renderReq() {
  $("rq-co").innerHTML = DATA.companies.map(c =>
    `<option value="${esc(c.slug)}"${c.slug === current ? " selected" : ""}>${esc(c.name)}${c.n_facts ? "" : "  (store empty)"}</option>`).join("");
  $("rq-tpl").innerHTML = DATA.templates.map(t =>
    `<button class="tcard" type="button" data-id="${esc(t.id)}" aria-pressed="${t.id === state.template}">
       <b>${esc(t.name)}</b><span>${esc(t.blurb)}</span></button>`).join("");
  document.querySelectorAll("#rq-tpl .tcard").forEach(b => b.onclick = () => {
    state.template = b.dataset.id; renderReq(); paint();
  });
}

function buildRequest() {
  const slug = $("rq-co").value;
  const today = DATA.generated;
  return {
    id: `${slug}-${state.template.replace(/_/g, "-")}-${today}`,
    submitted: today,
    idea: $("rq-idea").value.trim() || "(state the question this note answers)",
    template: state.template,
    companies: [slug],
    rigor: Number($("rq-rigor").value) || 4,
    deadline: null,
    extras: { charts: Number($("rq-charts").value) || 3, model: $("rq-model").checked },
    source: "desk"
  };
}

function buildPrompt(req) {
  return `Run the report pipeline in CLAUDE.md for this request.\n\n`
    + `Request (write it to "Report Automation/requests/queue/${req.id}.json" first):\n`
    + JSON.stringify(req, null, 2) + `\n\n`
    + `Work all eight stages in order: intake, research, store, trends, compose, charts, build, `
    + `validate, ship. Follow style/STYLE.md and the writing standard in README.md. `
    + `Do not ship until every box in the Report Ship gate is true.`;
}

function paint() { $("rq-out").textContent = buildPrompt(buildRequest()); }

function flash(msg) {
  const f = $("flash"); f.textContent = msg; f.classList.add("show");
  clearTimeout(f._t); f._t = setTimeout(() => f.classList.remove("show"), 1600);
}
async function copy(text, msg) {
  try { await navigator.clipboard.writeText(text); flash(msg); }
  catch { flash("Copy blocked — select the text and copy manually"); }
}
$("rq-copy").onclick = () => copy(buildPrompt(buildRequest()), "Launch prompt copied");
$("rq-json").onclick = () => copy(JSON.stringify(buildRequest(), null, 2) + "\n", "Request JSON copied");
["rq-co","rq-idea","rq-rigor","rq-charts","rq-model"].forEach(id => {
  $(id).addEventListener("input", paint);
  $(id).addEventListener("change", paint);
});

/* --------------------------------------------------------------- boot */
renderCoverage();
renderList();
if (current) selectCompany(current);
renderReq();
paint();
</script>
"""
