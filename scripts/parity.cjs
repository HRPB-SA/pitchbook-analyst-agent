/* CONTEXT: ANTHROPIC INTELLIGENCE DESK — engine parity test. The financial model exists twice: scripts/model.py (writes data/model.json)
   and computeModel() in assets/app.js (recomputes live when a reader moves a slider). This extracts the JS function, feeds it the assumptions stored
   in data/model.json and compares every row and valuation field with the Python outputs. Exit 1 on any mismatch beyond 1e-6 relative.
   Run: node scripts/parity.cjs [path/to/model.json] */
const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(ROOT, 'assets', 'app.js'), 'utf8');
const a = src.indexOf('function lerp('), b = src.indexOf('function computeModel(');
const end = src.indexOf('\n}\n', b) + 3;
if (a < 0 || b < 0 || end < 3) { console.error('could not locate lerp/computeModel in assets/app.js'); process.exit(2); }
const computeModel = new Function(src.slice(a, end) + '\nreturn computeModel;')();
const M = JSON.parse(fs.readFileSync(process.argv[2] || path.join(ROOT, 'data', 'model.json'), 'utf8'));
let bad = 0, checked = 0;
const close = (x, y) => (x == null && y == null) || (Number.isFinite(x) && Number.isFinite(y) && Math.abs(x - y) <= 1e-6 * Math.max(1, Math.abs(x), Math.abs(y)));
for (const [scen, A] of Object.entries(M.assumptions || {})) {
  const py = M.outputs?.[scen]; if (!py) { console.log(`missing python outputs for ${scen}`); bad++; continue; }
  const A2 = JSON.parse(JSON.stringify(A)); if (!A2.years) A2.years = [2024, 2025, 2026, 2027, 2028, 2029, 2030];
  const js = computeModel(A2);
  for (const [k, byYear] of Object.entries(py.rows)) for (const [y, v] of Object.entries(byYear)) { checked++; if (!close(js.rows[k]?.[y], v)) { bad++; if (bad < 12) console.log(`${scen} ${k} ${y}: js=${js.rows[k]?.[y]} py=${v}`); } }
  for (const k of ['dcf_ev', 'pv_fcf', 'pv_tv']) { checked++; if (!close(js.valuation[k], py.valuation[k])) { bad++; console.log(`${scen} valuation.${k}: js=${js.valuation[k]} py=${py.valuation[k]}`); } }
  for (const m of py.valuation.marks) {
    const j = js.valuation.marks.find(x => x.key === m.key);
    for (const k of ['ev', 'ev_rev_2026', 'ev_rev_2027', 'ev_net_2026', 'ev_net_2027', 'req2030rev', 'req_cagr', 'vs_dcf']) { checked++; if (!close(j?.[k], m[k])) { bad++; console.log(`${scen} mark ${m.key}.${k}: js=${j?.[k]} py=${m[k]}`); } }
  }
}
console.log(bad ? `PARITY FAIL: ${bad} of ${checked} values differ` : `parity ok: ${checked} values match across ${Object.keys(M.assumptions || {}).length} scenarios`);
process.exit(bad ? 1 : 0);
