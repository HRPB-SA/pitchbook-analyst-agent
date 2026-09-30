/* CONTEXT: ANTHROPIC INTELLIGENCE DESK — single-page app.
   Reads data/*.json (produced by scripts/merge.py, model.py and the analysis wave) and renders
   nine desks. No framework; D3 for scales, axes, force layout. Every value shown traces to an
   event id or a sourced table row. */
(() => {
'use strict';

/* ---------------- utils ---------------- */
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
function el(tag, attrs = {}, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v == null || v === false) continue;
    if (k === 'class') n.className = v;
    else if (k === 'text') n.textContent = v;
    else if (k === 'html') n.innerHTML = v; // only for trusted static markup (icons)
    else if (k.startsWith('on')) n.addEventListener(k.slice(2), v);
    else if (k === 'style' && typeof v === 'object') Object.assign(n.style, v);
    else n.setAttribute(k, v === true ? '' : v);
  }
  for (const c of kids.flat()) {
    if (c == null || c === false) continue;
    n.append(c.nodeType ? c : document.createTextNode(String(c)));
  }
  return n;
}
const fmt = {
  usd(m, d) { // m in $M
    if (m == null || isNaN(m)) return '—';
    const a = Math.abs(m), s = m < 0 ? '−' : '';
    if (a >= 1e6) return `${s}$${(a / 1e6).toFixed(d ?? (a / 1e6 >= 10 ? 1 : 2))}T`;
    if (a >= 1e3) return `${s}$${(a / 1e3).toFixed(d ?? (a / 1e3 >= 100 ? 0 : 1))}B`;
    if (a >= 1) return `${s}$${a.toFixed(d ?? 0)}M`;
    return `${s}$${(a * 1000).toFixed(0)}K`;
  },
  pct(x, d = 0) { return x == null || isNaN(x) ? '—' : `${(x * 100).toFixed(d)}%`; },
  num(x) { return x == null || isNaN(x) ? '—' : Number(x).toLocaleString('en-US'); },
  date(s) { if (!s) return '—'; const d = new Date(s + (s.length === 10 ? 'T00:00:00Z' : '')); if (isNaN(d)) return s; return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', timeZone: 'UTC' }); },
  mdate(s) { if (!s) return '—'; const d = new Date(s + 'T00:00:00Z'); return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', timeZone: 'UTC' }); },
  dmy(s) { if (!s) return '—'; const d = new Date(s + 'T00:00:00Z'); return d.toLocaleDateString('en-US', { month: 'short', day: '2-digit', timeZone: 'UTC' }); },
  time(iso) { const d = new Date(iso); return isNaN(d) ? '' : d.toISOString().slice(11, 19); },
  gw(x) { return x == null ? '—' : `${Number(x).toLocaleString('en-US', { maximumFractionDigits: 2 })} GW`; },
  domain(u) { try { return new URL(u).hostname.replace(/^www\./, ''); } catch { return u || ''; } },
};
const CAT_ORDER = ['funding','valuation','ipo','revenue','financials','compute','product','model','pricing','governance','safety','policy','government','legal','regulatory','security','people','partnership','customer','acquisition','investment','international','research','competition','debt','secondary','other'];
const SERIES = ['var(--s1)','var(--s2)','var(--s3)','var(--s4)','var(--s5)','var(--s6)','var(--s7)','var(--s8)'];
const AGENT_COLORS = { scout: 'var(--s1)', desk: 'var(--s2)', verify: 'var(--s3)', analysis: 'var(--s7)', model: 'var(--s4)', thesis: 'var(--s5)', certify: 'var(--s6)', orchestrator: 'var(--ink)' };
const ICONS = {
  overview: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>',
  timeline: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h10M4 18h13"/><circle cx="19" cy="12" r="1.5" fill="currentColor"/></svg>',
  topics: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h16v4H4zM4 15h16v4H4zM8 9v6M16 9v6"/></svg>',
  model: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19V5M4 19h16"/><path d="M7 15l4-5 3 3 5-7"/></svg>',
  compute: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 9h6v6H9zM3 10h2M3 14h2M19 10h2M19 14h2M10 3v2M14 3v2M10 19v2M14 19v2"/></svg>',
  thesis: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 4v16M4 9l8-5 8 5M6 9l-3 6h6l-3-6zM18 9l-3 6h6l-3-6z"/></svg>',
  network: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="2.5"/><circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="5" cy="18" r="2"/><circle cx="19" cy="18" r="2"/><path d="M6.5 7.5l4 3M17.5 7.5l-4 3M6.5 16.5l4-3M17.5 16.5l-4-3"/></svg>',
  agents: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3 2.5-5 5-5s5 2 5 5M13 19c0-2.5 2-4 4-4s4 1.5 4 4"/><path d="M14 3l2 3-2 1" /></svg>',
  sources: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3h9l5 5v13H6z"/><path d="M14 3v6h6M9 13h6M9 17h6"/></svg>',
};
const TABS = [
  ['overview', 'Overview'], ['timeline', 'Timeline'], ['topics', 'Topics'], ['model', 'Financial model'],
  ['compute', 'Compute'], ['thesis', 'Bull / Bear'], ['network', 'Network'], ['agents', 'Agents floor'], ['sources', 'Sources & ledger'],
];
const state = { data: {}, tab: 'overview', evIndex: new Map(), rendered: {}, floor: null };

/* ---------------- theme ---------------- */
function initTheme() {
  const root = document.documentElement, lbl = $('#themeLabel');
  let pref = null; try { pref = localStorage.getItem('aid-theme'); } catch {}
  const apply = () => { if (pref) root.setAttribute('data-theme', pref); else root.removeAttribute('data-theme'); lbl.textContent = `Theme: ${pref || 'system'}`; };
  apply();
  $('#themeToggle').addEventListener('click', () => {
    pref = pref === 'dark' ? 'light' : pref === 'light' ? null : 'dark';
    try { pref ? localStorage.setItem('aid-theme', pref) : localStorage.removeItem('aid-theme'); } catch {}
    apply(); rerenderCharts();
  });
}
function rerenderCharts() { state.rendered = {}; showTab(state.tab, true); }

/* ---------------- data ---------------- */
async function loadAll() {
  const files = ['events','metrics','entities','topics','model','compute','thesis','agent_log','ledger','audit','health','certify'];
  const res = await Promise.all(files.map(async f => {
    try { const r = await fetch(`data/${f}.json`, { cache: 'no-store' }); if (!r.ok) throw new Error(`${r.status}`); return [f, await r.json()]; }
    catch (e) { return [f, null, e]; }
  }));
  const missing = [];
  for (const [f, d, e] of res) { state.data[f] = d; if (!d && !['audit', 'health', 'certify'].includes(f)) missing.push(f); }
  if (!state.data.events) throw new Error(`Could not load data/events.json (${missing.join(', ')} missing). Run scripts/merge.py first.`);
  for (const e of state.data.events) { state.evIndex.set(e.id, e); for (const m of e.merged_ids || []) if (!state.evIndex.has(m)) state.evIndex.set(m, e); }
  return missing;
}

/* ---------------- routing ---------------- */
function renderNav() {
  const nav = $('#nav');
  for (const [id, label] of TABS) {
    const b = el('button', { role: 'tab', id: `tab-${id}`, 'aria-selected': 'false', 'aria-controls': `panel-${id}`, onclick: () => showTab(id) },
      el('span', { class: 'ico', html: ICONS[id] }), el('span', { class: 't', text: label }));
    nav.append(b);
  }
}
function showTab(id, force) {
  if (!TABS.some(t => t[0] === id)) id = 'overview';
  state.tab = id;
  $$('#nav button').forEach(b => b.setAttribute('aria-selected', String(b.id === `tab-${id}`)));
  $$('.panel').forEach(p => p.classList.toggle('active', p.id === `panel-${id}`));
  $('#pageTitle').textContent = TABS.find(t => t[0] === id)[1];
  try { if (location.hash !== `#${id}`) history.replaceState(null, '', `#${id}`); } catch { /* sandboxed frames may refuse history updates */ }
  if (!state.rendered[id] || force) { RENDER[id]($(`#panel-${id}`)); state.rendered[id] = true; }
  if (id === 'agents' && state.floor) state.floor.onShow();
}

/* ---------------- tooltip ---------------- */
const tip = $('#tooltip');
function showTip(x, y, node) { tip.replaceChildren(node); tip.hidden = false; const r = tip.getBoundingClientRect(); const px = Math.min(x + 14, window.innerWidth - r.width - 8), py = Math.min(y + 14, window.innerHeight - r.height - 8); tip.style.left = px + 'px'; tip.style.top = py + 'px'; }
function hideTip() { tip.hidden = true; }
function tipRows(title, rows) { const n = el('div'); n.append(el('div', { class: 't', text: title })); for (const r of rows) n.append(el('div', { class: 'row' }, el('span', {}, el('i', { style: { background: r.color || 'transparent' } }), r.label), el('b', { text: r.value }))); return n; }

/* ---------------- charts ---------------- */
function chartFrame(container, w, h, m) {
  container.replaceChildren();
  const svg = d3.select(container).append('svg').attr('viewBox', `0 0 ${w} ${h}`).attr('role', 'img');
  const g = svg.append('g').attr('transform', `translate(${m.l},${m.t})`);
  return { svg, g, iw: w - m.l - m.r, ih: h - m.t - m.b };
}
function yGrid(g, y, iw, ticks) {
  g.append('g').attr('class', 'grid').selectAll('line').data(y.ticks(ticks)).join('line').attr('x1', 0).attr('x2', iw).attr('y1', d => y(d)).attr('y2', d => y(d));
}
function axisY(g, y, fmtFn, ticks) { g.append('g').attr('class', 'axis').call(d3.axisLeft(y).ticks(ticks).tickSize(0).tickPadding(6).tickFormat(fmtFn)).call(a => a.select('.domain').remove()); }
function axisX(g, x, ih, fmtFn, ticks) { g.append('g').attr('class', 'axis').attr('transform', `translate(0,${ih})`).call(d3.axisBottom(x).ticks(ticks).tickSize(0).tickPadding(8).tickFormat(fmtFn)).call(a => a.select('.domain').attr('class', 'baseline')); }

// Line chart: series = [{name, color, points:[{x:Date, y:number, label?, ref?}]}]
function lineChart(container, { series, yFmt = v => fmt.usd(v), log = false, h = 260, endLabels = true, xTicks = 6, yTicks = 5, onPoint, xFmt }) {
  const w = 720, m = { t: 14, r: 96, b: 28, l: 54 };
  const { svg, g, iw, ih } = chartFrame(container, w, h, m);
  const all = series.flatMap(s => s.points);
  if (!all.length) { container.replaceChildren(el('div', { class: 'empty', text: 'No data' })); return; }
  const x = d3.scaleUtc().domain(d3.extent(all, d => d.x)).range([0, iw]);
  const ymax = d3.max(all, d => d.y), ymin = d3.min(all, d => d.y);
  const y = log ? d3.scaleLog().domain([Math.max(ymin * 0.8, 1), ymax * 1.4]).range([ih, 0]) : d3.scaleLinear().domain([Math.min(0, ymin), ymax * 1.12]).nice().range([ih, 0]);
  if (log) {
    const [lo, hi] = y.domain(); const tv = []; for (let p = Math.floor(Math.log10(lo)); p <= Math.ceil(Math.log10(hi)); p++) for (const k of [1, 3]) { const v = k * Math.pow(10, p); if (v >= lo && v <= hi) tv.push(v); }
    g.append('g').attr('class', 'grid').selectAll('line').data(tv).join('line').attr('x1', 0).attr('x2', iw).attr('y1', d => y(d)).attr('y2', d => y(d));
    g.append('g').attr('class', 'axis').call(d3.axisLeft(y).tickValues(tv).tickSize(0).tickPadding(6).tickFormat(yFmt)).call(a => a.select('.domain').remove());
  } else { yGrid(g, y, iw, yTicks); axisY(g, y, yFmt, yTicks); }
  axisX(g, x, ih, xFmt || d3.utcFormat('%b %Y'), xTicks);
  const line = d3.line().x(d => x(d.x)).y(d => y(d.y)).curve(d3.curveMonotoneX);
  series.forEach((s, i) => {
    g.append('path').datum(s.points).attr('d', line).attr('fill', 'none').attr('stroke', s.color || SERIES[i]).attr('stroke-width', 2).attr('stroke-linejoin', 'round').attr('stroke-linecap', 'round');
    g.selectAll(null).data(s.points).join('circle').attr('cx', d => x(d.x)).attr('cy', d => y(d.y)).attr('r', 4).attr('fill', s.color || SERIES[i]).attr('stroke', 'var(--chart-surface)').attr('stroke-width', 2);
    if (endLabels) { const last = s.points[s.points.length - 1]; g.append('text').attr('class', 'dl').attr('x', x(last.x) + 8).attr('y', y(last.y) + 4).text(`${series.length > 1 ? s.name + ' ' : ''}${yFmt(last.y)}`); }
  });
  // hover: nearest x
  const hair = g.append('line').attr('class', 'baseline').attr('y1', 0).attr('y2', ih).attr('stroke-dasharray', null).style('opacity', 0);
  const bisect = d3.bisector(d => d.x).center;
  svg.append('rect').attr('x', m.l).attr('y', m.t).attr('width', iw).attr('height', ih).attr('fill', 'transparent')
    .on('pointermove', ev => {
      const [px] = d3.pointer(ev, g.node()); const xd = x.invert(px);
      const rows = series.map((s, i) => { const k = bisect(s.points, xd); const p = s.points[Math.max(0, Math.min(k, s.points.length - 1))]; return { p, s, i }; }).filter(r => r.p);
      if (!rows.length) return;
      const near = rows.reduce((a, b) => Math.abs(b.p.x - xd) < Math.abs(a.p.x - xd) ? b : a);
      hair.attr('x1', x(near.p.x)).attr('x2', x(near.p.x)).style('opacity', 1);
      showTip(ev.clientX, ev.clientY, tipRows(near.p.label ? `${fmt.date(near.p.date)} · ${near.p.label}` : fmt.date(near.p.date), rows.map(r => ({ label: r.s.name, value: yFmt(r.p.y), color: r.s.color || SERIES[r.i] }))));
    }).on('pointerleave', () => { hair.style('opacity', 0); hideTip(); })
    .on('click', ev => { if (!onPoint) return; const [px] = d3.pointer(ev, g.node()); const xd = x.invert(px); const s = series[0]; const k = bisect(s.points, xd); onPoint(s.points[Math.max(0, Math.min(k, s.points.length - 1))]); });
}
// Column chart: data = [{label, values:[{name, value, color}]}] (stacked when >1 value)
function columnChart(container, { data, yFmt = v => fmt.usd(v), h = 240, stacked = true, labelTop = true, negOK = false, onBar }) {
  const w = 720, m = { t: 18, r: 12, b: 30, l: 54 };
  const { svg, g, iw, ih } = chartFrame(container, w, h, m);
  if (!data.length) { container.replaceChildren(el('div', { class: 'empty', text: 'No data' })); return; }
  const x = d3.scaleBand().domain(data.map(d => d.label)).range([0, iw]).paddingInner(0.35).paddingOuter(0.15);
  const totals = data.map(d => stacked ? d3.sum(d.values, v => Math.max(0, v.value)) : d3.max(d.values, v => v.value));
  const mins = negOK ? data.map(d => d3.min(d.values, v => Math.min(0, v.value))) : [0];
  const y = d3.scaleLinear().domain([Math.min(0, d3.min(mins)), d3.max(totals) * 1.1 || 1]).nice().range([ih, 0]);
  yGrid(g, y, iw, 5); axisY(g, y, yFmt, 5);
  g.append('line').attr('class', 'baseline').attr('x1', 0).attr('x2', iw).attr('y1', y(0)).attr('y2', y(0));
  const bw = Math.min(x.bandwidth(), 26);
  data.forEach(d => {
    let acc = 0, accNeg = 0;
    const gx = x(d.label) + (x.bandwidth() - bw) / 2;
    d.values.forEach((v, vi) => {
      if (v.value == null) return;
      const neg = v.value < 0;
      const y0 = stacked ? (neg ? accNeg : acc) : 0, y1 = y0 + v.value;
      const top = y(Math.max(y0, y1)), hgt = Math.max(0, Math.abs(y(y0) - y(y1)) - (stacked && vi > 0 ? 2 : 0));
      g.append('rect').attr('x', gx).attr('y', top + (stacked && vi > 0 && !neg ? 2 : 0)).attr('width', bw).attr('height', hgt).attr('rx', 3).attr('fill', v.color || SERIES[vi]).attr('opacity', v.est ? .55 : 1)
        .style('cursor', onBar ? 'pointer' : 'default')
        .on('pointermove', ev => showTip(ev.clientX, ev.clientY, tipRows(d.label, d.values.map((vv, i) => ({ label: vv.name, value: yFmt(vv.value), color: vv.color || SERIES[i] })))))
        .on('pointerleave', hideTip).on('click', () => onBar && onBar(d, v));
      if (stacked) { if (neg) accNeg = y1; else acc = y1; }
    });
    if (labelTop) { const t = stacked ? acc : d3.max(d.values, v => v.value); g.append('text').attr('class', 'dl').attr('x', gx + bw / 2).attr('y', y(t) - 5).attr('text-anchor', 'middle').text(yFmt(t)); }
  });
  g.append('g').attr('class', 'axis').attr('transform', `translate(0,${ih})`).call(d3.axisBottom(x).tickSize(0).tickPadding(8)).call(a => a.select('.domain').remove());
}
// Horizontal bars: data=[{label, value, color, sub, value2?}]
function barChartH(container, { data, xFmt = v => fmt.usd(v), rowH = 26, onBar, secondary }) {
  const w = 720, m = { t: 6, r: 90, b: 6, l: 150 }, h = m.t + m.b + data.length * rowH;
  const { svg, g, iw } = chartFrame(container, w, h, m);
  if (!data.length) { container.replaceChildren(el('div', { class: 'empty', text: 'No data' })); return; }
  const x = d3.scaleLinear().domain([0, d3.max(data, d => Math.max(d.value || 0, d.value2 || 0)) * 1.05 || 1]).range([0, iw]);
  data.forEach((d, i) => {
    const y = i * rowH + 4;
    g.append('text').attr('class', 'dl sub').attr('x', -8).attr('y', y + 13).attr('text-anchor', 'end').text(d.label.length > 24 ? d.label.slice(0, 23) + '…' : d.label);
    if (d.value2 != null) g.append('rect').attr('x', 0).attr('y', y).attr('width', x(d.value2)).attr('height', rowH - 8).attr('rx', 3).attr('fill', d.color || SERIES[0]).attr('opacity', .3);
    g.append('rect').attr('x', 0).attr('y', y).attr('width', x(d.value || 0)).attr('height', rowH - 8).attr('rx', 3).attr('fill', d.color || SERIES[0]).style('cursor', onBar ? 'pointer' : 'default')
      .on('pointermove', ev => showTip(ev.clientX, ev.clientY, tipRows(d.label, [{ label: secondary ? secondary[0] : 'Value', value: xFmt(d.value), color: d.color || SERIES[0] }, ...(d.value2 != null ? [{ label: secondary ? secondary[1] : 'Upper', value: xFmt(d.value2) }] : []), ...(d.sub ? [{ label: d.sub, value: '' }] : [])])))
      .on('pointerleave', hideTip).on('click', () => onBar && onBar(d));
    g.append('text').attr('class', 'dl').attr('x', x(Math.max(d.value || 0, d.value2 || 0)) + 6).attr('y', y + 13).text(d.tag || (xFmt(d.value) + (d.value2 != null ? ` / ${xFmt(d.value2)}` : '')));
  });
}
function waterfall(container, { steps, yFmt = v => fmt.pct(v), rowH = 38 }) {
  // horizontal waterfall: nine long labels do not fit under vertical bars, so each step is a row
  const w = 720, m = { t: 6, r: 64, b: 26, l: 250 }, h = steps.length * rowH + m.t + m.b;
  const { g, iw, ih } = chartFrame(container, w, h, m);
  let run = 0; const bars = steps.map((st, i) => { const start = st.total ? 0 : run; const end = st.total ? st.value : run + st.value; run = end; return { ...st, start, end, i }; });
  const lo = Math.min(0, d3.min(bars, b => Math.min(b.start, b.end))), hi = d3.max(bars, b => Math.max(b.start, b.end));
  const x = d3.scaleLinear().domain([lo, hi * 1.06]).nice().range([0, iw]);
  const y = d3.scaleBand().domain(bars.map(b => b.i)).range([0, ih]).paddingInner(0.3);
  g.append('g').attr('class', 'grid').selectAll('line').data(x.ticks(5)).join('line').attr('x1', d => x(d)).attr('x2', d => x(d)).attr('y1', 0).attr('y2', ih);
  g.append('g').attr('class', 'axis').attr('transform', `translate(0,${ih})`).call(d3.axisBottom(x).ticks(5).tickSize(0).tickPadding(8).tickFormat(yFmt)).call(a => a.select('.domain').remove());
  const wrap = t => { const words = String(t).split(/\s+/), lines = []; let cur = ''; for (const wd of words) { if ((cur + ' ' + wd).trim().length > 36 && cur) { lines.push(cur); cur = wd; } else cur = (cur + ' ' + wd).trim(); } if (cur) lines.push(cur); return lines.slice(0, 2).map((l, i, arr) => i === 1 && lines.length > 2 ? l + '…' : l); };
  bars.forEach(bd => {
    const yy = y(bd.i), bh = y.bandwidth(), x0 = Math.min(x(bd.start), x(bd.end)), bw = Math.max(1.5, Math.abs(x(bd.end) - x(bd.start)));
    const tx = g.append('text').attr('class', 'dl sub').attr('x', -10).attr('text-anchor', 'end').attr('y', yy + bh / 2);
    const ls = wrap(bd.label); ls.forEach((l, i) => tx.append('tspan').attr('x', -10).attr('dy', i === 0 ? (ls.length === 1 ? '0.35em' : '-0.2em') : '1.15em').text(l));
    g.append('rect').attr('x', x0).attr('y', yy).attr('width', bw).attr('height', bh).attr('rx', 3)
      .attr('fill', bd.total ? 'var(--ink-2)' : (bd.value < 0 ? 'var(--s8)' : 'var(--s3)'))
      .on('pointermove', ev => showTip(ev.clientX, ev.clientY, tipRows(bd.label, [{ label: bd.total ? 'Level' : 'Change', value: yFmt(bd.value) }, ...(bd.range ? [{ label: 'Range', value: `${yFmt(bd.range[0])} to ${yFmt(bd.range[1])}` }] : []), ...(bd.note ? [{ label: bd.note.slice(0, 220), value: '' }] : [])]))).on('pointerleave', hideTip);
    g.append('text').attr('class', 'dl').attr('x', Math.max(x(bd.start), x(bd.end)) + 6).attr('y', yy + bh / 2).attr('dy', '0.35em').text(yFmt(bd.value));
  });
}
function wrapText(sel, width) {
  sel.each(function () { const t = d3.select(this), words = t.text().split(/\s+/); let line = [], lineNo = 0; const y = t.attr('y'), dy = 0.9; let tspan = t.text(null).append('tspan').attr('x', 0).attr('y', y).attr('dy', dy + 'em'); for (const w of words) { line.push(w); tspan.text(line.join(' ')); if (tspan.node().getComputedTextLength() > width && line.length > 1) { line.pop(); tspan.text(line.join(' ')); line = [w]; tspan = t.append('tspan').attr('x', 0).attr('y', y).attr('dy', ++lineNo * 1.1 + dy + 'em').text(w); } } });
}
function sparkline(container, points, color = 'var(--s1)') {
  const w = 78, h = 30; container.replaceChildren();
  if (!points || points.length < 2) return;
  const svg = d3.select(container).append('svg').attr('viewBox', `0 0 ${w} ${h}`);
  const x = d3.scaleLinear().domain([0, points.length - 1]).range([2, w - 2]), y = d3.scaleLinear().domain(d3.extent(points)).range([h - 3, 3]);
  const line = d3.line().x((d, i) => x(i)).y(d => y(d)).curve(d3.curveMonotoneX);
  svg.append('path').datum(points).attr('d', line).attr('fill', 'none').attr('stroke', 'var(--line-2)').attr('stroke-width', 1.5);
  svg.append('circle').attr('cx', x(points.length - 1)).attr('cy', y(points[points.length - 1])).attr('r', 3).attr('fill', color);
}
function legend(items) { const n = el('div', { class: 'legend' }); items.forEach(it => n.append(el('span', { class: 'k' }, el('i', { class: it.rect ? 'rect' : '', style: { background: it.color } }), it.name))); return n; }
function tableView(container, headers, rows) {
  const btn = el('button', { class: 'tablebtn', type: 'button', text: 'Table view' });
  const wrap = el('div', { class: 'tablewrap', hidden: true }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, ...headers.map(h => el('th', { text: h })))), el('tbody', {}, ...rows.map(r => el('tr', {}, ...r.map((c, i) => el('td', { class: i > 0 ? 'num' : '', text: c })))))));
  btn.addEventListener('click', () => { wrap.hidden = !wrap.hidden; btn.textContent = wrap.hidden ? 'Table view' : 'Hide table'; });
  container.append(btn, wrap);
}

/* ---------------- shared bits ---------------- */
function chip(text, cls) { return el('span', { class: `chip ${cls || ''}`, text }); }
function tierChip(t) { return el('span', { class: `chip tier ${t}`, text: t }); }
function confChip(c) { return el('span', { class: `chip conf ${c}`, text: c }); }
function evLink(id, text) { const e = state.evIndex.get(id); if (!e) return el('span', { class: 'muted small', text: id }); return el('a', { href: '#timeline', class: 'evl', onclick: ev => { ev.preventDefault(); openEvent(id); } }, el('span', { class: 'd' }, e.date), text || e.headline); }
function sourceLine(src) { if (!src?.url) return el('span', { class: 'muted', text: 'no URL' }); if (src.url.startsWith('pitchbook:')) return el('span', { class: 'muted', title: 'Licensed PitchBook field; no public link', text: `${src.publisher || 'PitchBook'} · licensed field, no public link` }); return el('a', { href: src.url, target: '_blank', rel: 'noopener', text: `${src.publisher || fmt.domain(src.url)}${src.title ? ' · ' + src.title.slice(0, 70) : ''}` }); }
function extractChips(ex, e) {
  const out = [];
  if (!ex) return out;
  const o = ex.other || {}, upTo = e && /\bup to\b/i.test(e.headline || '');
  if (ex.amount_usd_m) out.push(chip(`${upTo ? 'up to ' : ''}${fmt.usd(ex.amount_usd_m)}`, 'num'));
  if (o.amount_target_usd_m) out.push(chip(`target or cap ${fmt.usd(o.amount_target_usd_m)}`, 'num'));
  if (ex.valuation_post_usd_m) out.push(chip(`post ${fmt.usd(ex.valuation_post_usd_m)}`, 'num'));
  if (o.valuation_reference_usd_m) out.push(chip(`reference mark ${fmt.usd(o.valuation_reference_usd_m)}`, 'num'));
  if (ex.revenue_run_rate_usd_m) out.push(chip(`run-rate ${fmt.usd(ex.revenue_run_rate_usd_m)}`, 'num'));
  if (o.projected_run_rate_usd_m) out.push(chip(`projected run-rate ${fmt.usd(o.projected_run_rate_usd_m)}`, 'num'));
  if (ex.revenue_period_usd_m) out.push(chip(`${ex.revenue_period || 'rev'} ${fmt.usd(ex.revenue_period_usd_m)}`, 'num'));
  if (ex.margin_pct != null) out.push(chip(`${ex.margin_type || 'margin'} ${ex.margin_pct}%`, 'num'));
  if (ex.compute?.usd_m) out.push(chip(`compute ${fmt.usd(ex.compute.usd_m)}${ex.compute.gw ? ' · ' + ex.compute.gw + ' GW' : ''}`, 'num'));
  else if (ex.compute?.gw) out.push(chip(`${ex.compute.gw} GW`, 'num'));
  if (ex.product?.price_in_per_mtok != null) out.push(chip(`$${ex.product.price_in_per_mtok}/$${ex.product.price_out_per_mtok} per Mtok`, 'num'));
  if (ex.headcount) out.push(chip(`${fmt.num(ex.headcount)} staff`, 'num'));
  return out;
}
function evRefs(ids) { return (ids || []).filter(id => state.evIndex.has(id)).slice(0, 4).map(id => { const e = state.evIndex.get(id); return el('a', { class: 'evref', href: '#timeline', title: e.headline, onclick: ev => { ev.preventDefault(); openEvent(id); }, text: e.date.slice(0, 7) }); }); }
function threeBeat(obj) {
  const n = el('div', { class: 'beat' });
  const rows = [['What happened', obj.what], ['What it means', obj.means], ['Implications', obj.implications]];
  for (const [l, b] of rows) { if (!b || (Array.isArray(b) && !b.length)) continue; n.append(el('div', { class: 'l', text: l }), el('div', { class: 'b' }, ...(Array.isArray(b) ? b : [b]).map(p => typeof p === 'string' ? el('p', { text: p }) : el('p', {}, p.t || '', ...evRefs(p.e))))); }
  return n;
}

/* ---------------- drawer ---------------- */
function openDrawer(node) { $('#drawerBody').replaceChildren(node); $('#drawer').classList.add('open'); $('#drawer').setAttribute('aria-hidden', 'false'); $('#scrim').classList.add('open'); }
function closeDrawer() { $('#drawer').classList.remove('open'); $('#drawer').setAttribute('aria-hidden', 'true'); $('#scrim').classList.remove('open'); }
function openEvent(id) {
  const e = state.evIndex.get(id); if (!e) return;
  const ex = e.extracted || {};
  const kv = el('dl', { class: 'kv' });
  const add = (k, v) => { if (v == null || v === '' || (Array.isArray(v) && !v.length)) return; kv.append(el('dt', { text: k }), el('dd', {}, v.nodeType ? v : String(v))); };
  add('Date', `${fmt.date(e.date)}${e.date_precision && e.date_precision !== 'day' ? ` (${e.date_precision} precision)` : ''}`);
  add('Categories', el('div', { class: 'meta', style: { display: 'flex', gap: '4px', flexWrap: 'wrap' } }, ...e.category.map(c => chip(c, 'cat'))));
  add('Source', el('div', {}, sourceLine(e.source), ' ', tierChip(e.source.tier), e.source.opened === false ? ' (not opened)' : ''));
  if (e.distinct_outlets) add('Distinct outlets', `${e.distinct_outlets}${e.single_chain_suspected ? ': likely one reporting chain (leak, scoop or official relayed by the others); count as one confirmation' : ''}`);
  if (e.confidence_note) add('Confidence note', e.confidence_note);
  if (e.corroboration?.length) add('Corroboration', el('div', {}, ...e.corroboration.map(c => el('div', {}, el('a', { href: c.url, target: '_blank', rel: 'noopener', text: `${c.publisher || fmt.domain(c.url)}` }), ' ', c.tier ? tierChip(c.tier) : ''))));
  add('Confidence', confChip(e.confidence));
  if (ex.amount_usd_m) add('Amount', `${/\bup to\b/i.test(e.headline) ? 'up to ' : ''}${fmt.usd(ex.amount_usd_m)}`);
  if (ex.other?.amount_target_usd_m) add('Target or cap (not a closed amount)', fmt.usd(ex.other.amount_target_usd_m));
  if (ex.valuation_post_usd_m) add('Post-money', fmt.usd(ex.valuation_post_usd_m));
  if (ex.other?.valuation_reference_usd_m) add('Reference mark (not a priced round)', fmt.usd(ex.other.valuation_reference_usd_m));
  if (ex.other?.projected_run_rate_usd_m) add('Projected run-rate (not reported)', fmt.usd(ex.other.projected_run_rate_usd_m));
  if (ex.valuation_pre_usd_m) add('Pre-money', fmt.usd(ex.valuation_pre_usd_m));
  if (ex.revenue_run_rate_usd_m) add('Run-rate', fmt.usd(ex.revenue_run_rate_usd_m));
  if (ex.revenue_period_usd_m) add('Period revenue', `${fmt.usd(ex.revenue_period_usd_m)} (${ex.revenue_period || 'period n/a'})`);
  if (ex.margin_pct != null) add('Margin', `${ex.margin_pct}% (${ex.margin_type || 'type n/a'})`);
  const cp = ex.compute || {}; if (cp.partner || cp.usd_m || cp.gw) add('Compute', `${cp.partner || ''} · ${cp.chips || ''} · ${cp.usd_m ? fmt.usd(cp.usd_m) : ''} ${cp.gw ? cp.gw + ' GW' : ''} ${cp.term || ''}`.replace(/\s+·\s+·/g, ' ·'));
  const pr = ex.product || {}; if (pr.name) add('Product', `${pr.name}${pr.type ? ' (' + pr.type + ')' : ''}${pr.price_in_per_mtok != null ? ` · $${pr.price_in_per_mtok} in / $${pr.price_out_per_mtok} out per Mtok` : ''}${pr.context_window ? ' · ' + fmt.num(pr.context_window) + ' ctx' : ''}`);
  if (ex.governance) add('Governance', ex.governance);
  if (ex.moat) add('Moat', ex.moat);
  if (ex.strategy) add('Strategy', ex.strategy);
  if (ex.people?.length) add('People', ex.people.map(p => `${p.name} · ${p.role || ''} (${p.move || ''})`).join('; '));
  if (ex.entities?.length) add('Entities', el('div', { style: { display: 'flex', gap: '4px', flexWrap: 'wrap' } }, ...ex.entities.map(x => chip(`${x.name}${x.ticker ? ' · ' + x.ticker : ''}${x.type ? ' · ' + x.type : ''}`))));
  if (ex.headcount) add('Headcount', fmt.num(ex.headcount));
  if (ex.customers) add('Customers', String(ex.customers));
  if (ex.other && Object.keys(ex.other).length) add('Other', el('pre', { class: 'small mono', style: { whiteSpace: 'pre-wrap', margin: 0 }, text: JSON.stringify(ex.other, null, 1).slice(0, 1200) }));
  if (e.notes) add('Notes', e.notes);
  if (e.audit) add('Independent audit', el('div', {}, el('span', { class: 'chip ' + ({ SUPPORTED: 'ok', PARTLY: 'warn', UNOPENABLE: '' }[e.audit.verdict] || 'bad'), text: e.audit.verdict }), ' ', el('span', { class: 'small', text: e.audit.note || '' }),
    ...(e.audit.figure_issues || []).map(f => el('div', { class: 'small muted', text: `${f.field}: claimed ${f.claimed}; page says ${f.page_says}${f.basis_note ? ' (' + f.basis_note + ')' : ''}` }))));
  if (e.corrections?.length) add('Corrected after audit', el('div', {}, ...e.corrections.map(c => el('div', { class: 'small', style: { marginBottom: '4px' } }, el('b', { text: `${c.id} (audit ${c.audit_id}): ` }), c.reason, ...Object.entries(c.changed || {}).filter(([k]) => k !== 'summary').map(([k, v]) => el('div', { class: 'mono small muted', text: `${k.replace('extracted.', '')}: ${JSON.stringify(v.was)} → ${JSON.stringify(v.now)}` })), c.changed?.summary ? el('div', { class: 'mono small muted', text: 'summary text corrected' }) : ''))));
  add('Found by', (e.agents || [e.agent]).join(', '));
  add('Event id', el('code', { text: e.id }));
  openDrawer(el('div', {}, el('div', { class: 'eyebrow', text: fmt.date(e.date) }), el('h2', { text: e.headline, style: { margin: '6px 0 8px' } }), el('p', { class: 'ink2', text: e.summary, style: { marginBottom: '14px' } }), kv));
}

/* ---------------- OVERVIEW ---------------- */
function latest(arr, pick) { if (!arr?.length) return null; const s = [...arr].filter(r => r && (pick ? pick(r) : true)).sort((a, b) => String(a.date || '').localeCompare(String(b.date || ''))); return s[s.length - 1] || null; }
function renderOverview(root) {
  const { metrics: M = {}, thesis: T, ledger: L, agent_log: A, model: MD, compute: C } = state.data;
  root.replaceChildren();
  const tiles = el('div', { class: 'grid cols-4' });
  const roundPts = (M.rounds || []).filter(r => r.post_usd_m > 0 && r.status !== 'talks' && r.additive !== false).map(r => ({ date: r.date, usd_m: r.post_usd_m, label: `${r.round}: ${fmt.usd(r.size_usd_m)} raised${r.press_post_usd_m && r.press_post_usd_m !== r.post_usd_m ? ` (press reported ${fmt.usd(r.press_post_usd_m)} post)` : ''}`, event_id: r.event_id, tier: r.tier || 'T2', confidence: ((r.press_post_usd_m && r.press_post_usd_m !== r.post_usd_m) || (r.press_size_usd_m && r.press_size_usd_m !== r.size_usd_m)) ? 'DISPUTED' : (r.confidence || 'HIGH') }));
  const valSeries = roundPts.length >= 5 ? roundPts : (M.valuation || []);
  const val = latest(valSeries, r => r.usd_m);
  const rr = latest(M.run_rate_desk?.length ? M.run_rate_desk.map(r => ({ ...r, usd_m: r.run_rate_usd_m })) : M.run_rate, r => r.usd_m);
  const q = (M.period_revenue || []).filter(r => /Q[1-4]\s*20\d\d/.test(r.period || '') && /actual|prelim/i.test(r.kind || '')).sort((a, b) => a.period.replace(/(Q\d)\s*(\d{4})/, '$2$1').localeCompare(b.period.replace(/(Q\d)\s*(\d{4})/, '$2$1'))).pop();
  const cs = M.capital_summary || {};
  const ct = C?.totals || M.compute_totals || {};   // same source and labels as the Compute tab
  const hcAll = (M.headcount_desk?.length ? M.headcount_desk : M.headcount || []).map(r => ({ ...r, date: /^\d{4}-\d{2}-\d{2}/.test(String(r.date)) ? String(r.date).slice(0, 10) : /^\d{4}-\d{2}/.test(String(r.date)) ? String(r.date).slice(0, 7) + '-01' : r.date }));
  const hc = latest(hcAll.filter(r => /^T[123]$/.test(r.tier || 'T3')), r => r.headcount) || latest(hcAll, r => r.headcount);   // a headline KPI rests on T1-T3 only
  const hcLater = hc ? hcAll.filter(r => r.date > hc.date && r.headcount && Math.abs(r.headcount - hc.headcount) / hc.headcount > 0.2) : [];
  const os = M.offering_structure || {};
  const tile = (label, value, sub, opts = {}) => { const t = el('div', { class: 'tile' }, el('div', { class: 'label', text: label }), el('div', { class: 'value', text: value }), el('div', { class: 'sub' }, ...sub.map(x => typeof x === 'string' ? (x ? el('span', { text: x }) : '') : x))); if (opts.spark) { const s = el('div', { class: 'spark' }); t.append(s); sparkline(s, opts.spark); } if (opts.onclick) { t.style.cursor = 'pointer'; t.addEventListener('click', opts.onclick); } return t; };
  tiles.append(
    tile('Last post-money valuation', val ? fmt.usd(val.usd_m) : '—', val ? [fmt.date(val.date), tierChip(val.tier), confChip(val.confidence)] : ['no data'], { onclick: val ? () => openEvent(val.event_id) : null, spark: valSeries.map(r => Math.log10(r.usd_m)) }),
    tile('Annualized run-rate revenue', rr ? fmt.usd(rr.usd_m) : '—', rr ? [fmt.date(rr.date), rr.tier ? tierChip(rr.tier) : '', rr.confidence ? confChip(rr.confidence) : '', rr.basis ? Object.assign(chip(String(rr.basis).slice(0, 44) + (String(rr.basis).length > 44 ? '…' : '')), { title: rr.basis }) : ''] : ['no data'], { onclick: rr?.event_id ? () => openEvent(rr.event_id) : null, spark: (M.run_rate_desk?.length ? M.run_rate_desk.map(r => r.run_rate_usd_m) : (M.run_rate || []).map(r => r.usd_m)) }),
    tile(q ? `${q.period} revenue (${q.kind})` : 'Latest quarterly revenue', q ? fmt.usd(q.usd_m) : '—', q ? [q.basis ? Object.assign(chip(String(q.basis).slice(0, 44) + (String(q.basis).length > 44 ? '…' : '')), { title: q.basis }) : '', q.tier ? tierChip(q.tier) : '', q.confidence ? confChip(q.confidence) : ''] : ['no data'], { onclick: () => (q?.event_id && state.evIndex.has(q.event_id)) ? openEvent(q.event_id) : showTab('topics') }),
    tile('Equity raised (ex-debt)', cs.equity_only_usd_m ? fmt.usd(cs.equity_only_usd_m) : '—', [cs.debt_usd_m ? `+ ${fmt.usd(cs.debt_usd_m)} debt` : '', (() => { const cv = (M.rounds || []).filter(r => /convertible/i.test(r.round) && r.size_usd_m).reduce((a, r) => a + r.size_usd_m, 0); return cv ? chip(`incl. ${fmt.usd(cv)} convertible notes`) : ''; })(), (() => {
      const cl = (L?.claims || []).find(c => c.kind === 'total' && c.verdict === 'MISMATCH'); if (!cl) return cs.basis_note ? chip('basis noted') : '';
      const ro = cl.rederived_obj || {}, x = ro.equity_only_usd_m, lo = ro.equity_only_range_usd_m?.low;
      return el('span', { class: 'chip conf DISPUTED', title: 'Independent re-derivation disagrees with the PitchBook ledger total (whether April hyperscaler tranches sit inside Series H); see Sources > re-derivation ledger', text: x ? `disputed: independent check ${fmt.usd(lo && lo < x ? lo : x)} to ${fmt.usd(x)}` : 'disputed in re-derivation' });
    })()], { onclick: () => showTab('sources') }),
    tile('Compute commitments (announced)', ct.usd_m_announced ? fmt.usd(ct.usd_m_announced) : '—', [ct.usd_m_up_to ? `incl. ${fmt.usd(ct.usd_m_up_to)} up to and ${fmt.usd(ct.usd_m_reported_unconfirmed || 0)} unconfirmed` : '', ct.usd_m_contracted ? `${fmt.usd(ct.usd_m_contracted)} contracted or disclosed` : '', ct.usd_m_contracted_t1_t2_documented ? `${fmt.usd(ct.usd_m_contracted_t1_t2_documented)} on T1/T2 documents` : '', ct.gw_announced ? fmt.gw(ct.gw_announced) : ''], { onclick: () => showTab('compute') }),
    tile('Headcount', hc ? fmt.num(hc.headcount) : '—', hc ? [fmt.date(hc.date), hc.tier ? tierChip(hc.tier) : '', hcLater.length ? el('span', { class: 'chip conf DISPUTED', title: 'Later figures differ by more than 20%; all are T4 estimates', text: `disputed: ${hcLater.map(r => fmt.num(r.headcount)).join(' / ')} (T4)` }) : ''] : ['no data'], { onclick: () => showTab('topics') }),
    tile('IPO', 'Confidential S-1', [/dispute/i.test(os.timing || '') ? el('span', { class: 'chip conf DISPUTED', title: os.timing, text: 'timing disputed: Oct vs Nov' }) : '', os.exchange || '', os.target_valuation_usd_m ? `target ${fmt.usd(os.target_valuation_usd_m)} (reported)` : '', os.target_raise_usd_m ? `raise up to ${fmt.usd(os.target_raise_usd_m)} (WSJ)` : ''], { onclick: () => state.evIndex.has('evt-20260601-confidential-draft-s1') ? openEvent('evt-20260601-confidential-draft-s1') : showTab('topics') }),
    tile('Record', `${fmt.num((state.data.events || []).length)} events`, [L ? `${fmt.num(L.raw_events)} raw · ${Object.keys(A?.agents || {}).length} agents` : '', L ? chip(`${((L.opened_share || 0) * 100).toFixed(1)}% opened`) : ''], { onclick: () => showTab('sources') }),
  );
  root.append(tiles);
  if (T?.verdict) {
    const v = T.verdict; const cls = /bull/i.test(v.call) ? 'bull' : /bear/i.test(v.call) ? 'bear' : 'lean';
    root.append(el('div', { class: 'section' }, el('div', { class: 'verdict' }, el('div', { class: `badge ${cls}`, text: v.call }), el('div', {}, el('div', { style: { fontWeight: 600, fontSize: '15px' }, text: v.one_liner }), v.by_mark?.length ? el('div', { style: { display: 'flex', gap: '8px', flexWrap: 'wrap', margin: '8px 0 4px' } }, ...v.by_mark.map(m => el('span', { class: `chip ${/BEAR/.test(m.call) ? 'conf DISPUTED' : /BULL/.test(m.call) ? 'conf HIGH' : 'conf MEDIUM'}`, title: m.why, text: `${fmt.usd(m.ev_usd_m)} ${({ series_h: 'Series H', secondary: 'Secondary mark', ipo_target: 'IPO target' })[m.mark] || m.mark}: ${m.call}` }))) : '', el('div', { class: 'ink2', style: { marginTop: '4px' }, text: (v.rationale || [])[0] || '' }), el('button', { class: 'tablebtn', type: 'button', text: 'Read the full case →', onclick: () => showTab('thesis') })))));
  }
  const g = el('div', { class: 'grid cols-2 section' });
  const c1 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Post-money valuation by round' }), el('span', { class: 'small muted', text: 'log scale' })));
  const c1c = el('div', { class: 'chart' }); c1.append(c1c);
  const vpts = valSeries.filter(r => r.usd_m > 0).map(r => ({ x: new Date(r.date), y: r.usd_m, date: r.date, label: r.label, ref: r.event_id }));
  lineChart(c1c, { series: [{ name: 'Post-money', color: 'var(--s1)', points: vpts }], log: true, yFmt: v => fmt.usd(v), onPoint: p => p.ref && openEvent(p.ref) });
  tableView(c1, ['Date', 'Post-money', 'Round'], vpts.map(p => [fmt.date(p.date), fmt.usd(p.y), p.label]));
  const c2 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Annualized run-rate revenue' }), el('span', { class: 'small muted', text: 'gross basis unless noted' })));
  const c2c = el('div', { class: 'chart' }); c2.append(c2c);
  const rpts = (M.run_rate_desk?.length ? M.run_rate_desk.map(r => ({ date: r.date, y: r.run_rate_usd_m, ref: r.event_id })) : (M.run_rate || []).map(r => ({ date: r.date, y: r.usd_m, ref: r.event_id }))).filter(r => r.y > 0 && r.date).map(r => ({ ...r, x: new Date(r.date) })).sort((a, b) => a.x - b.x);
  lineChart(c2c, { series: [{ name: 'Run-rate', color: 'var(--s2)', points: rpts }], yFmt: v => fmt.usd(v), onPoint: p => p.ref && openEvent(p.ref) });
  tableView(c2, ['Date', 'Run-rate'], rpts.map(p => [fmt.date(p.date), fmt.usd(p.y)]));
  g.append(c1, c2);
  const c3 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Quarterly revenue' }), el('span', { class: 'small muted', text: 'actual / preliminary; model estimates faded' })));
  const c3c = el('div', { class: 'chart' }); c3.append(c3c);
  const qs = (M.period_revenue || []).filter(r => /Q[1-4]\s*20\d\d/.test(r.period || '')).map(r => ({ key: r.period.replace(/(Q\d)\s*(\d{4})/, '$2$1'), label: r.period.replace(/\s+/, ' '), value: r.usd_m, kind: r.kind })).sort((a, b) => a.key.localeCompare(b.key));
  const seen = new Set(); const qd = qs.filter(r => { if (seen.has(r.key)) return false; seen.add(r.key); return true; });
  columnChart(c3c, { data: qd.map(r => ({ label: r.label, values: [{ name: r.kind || 'revenue', value: r.value, color: 'var(--s1)', est: /proj|est|guid/i.test(r.kind || '') }] })), yFmt: v => fmt.usd(v) });
  const c4 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Capital raised by year' }), el('span', { class: 'small muted', text: 'closed rounds at PitchBook sizes (incl. converted notes); excludes secondaries and "up to" commitments' })));
  const c4c = el('div', { class: 'chart' }); c4.append(c4c);
  const byY = {};
  if ((M.rounds || []).length >= 5) for (const r of M.rounds) { if (r.additive === false || r.status !== 'closed' || !r.size_usd_m || !r.date) continue; const y = r.date.slice(0, 4); byY[y] = byY[y] || { equity: 0, debt: 0 }; byY[y][/revolv|credit facility|bond|loan/i.test(r.round) ? 'debt' : 'equity'] += r.size_usd_m; }
  else for (const r of (M.capital || [])) { const y = r.date.slice(0, 4); byY[y] = byY[y] || { equity: 0, debt: 0 }; byY[y][r.kind] += r.usd_m; }
  columnChart(c4c, { data: Object.keys(byY).sort().map(y => ({ label: y, values: [{ name: 'Equity', value: byY[y].equity, color: 'var(--s1)' }, { name: 'Debt', value: byY[y].debt, color: 'var(--s2)' }] })), yFmt: v => fmt.usd(v) });
  c4.append(legend([{ name: 'Equity', color: 'var(--s1)', rect: true }, { name: 'Debt', color: 'var(--s2)', rect: true }]));
  g.append(c3, c4);
  root.append(g);
  // flags + recent
  const g2 = el('div', { class: 'grid cols-2 section' });
  const flags = (A?.log || []).filter(r => r.type === 'flag').slice(-8).reverse();
  const fl = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Signs raised by the desk' }), el('button', { class: 'tablebtn', type: 'button', text: 'Agents floor →', onclick: () => showTab('agents') })), el('div', { class: 'flags-list' }, ...(flags.length ? flags.map(f => el('div', { class: 'f' }, el('div', { class: 'who', text: `${A.agents[f.agent]?.name || f.agent} · ${fmt.time(f.t)}` }), el('div', {}, f.text, f.event_id && state.evIndex.has(f.event_id) ? el('span', {}, ' ', evLink(f.event_id, '↗')) : ''))) : [el('div', { class: 'empty', text: 'No flags yet' })])));
  const recent = [...(state.data.events || [])].sort((a, b) => b.date.localeCompare(a.date)).slice(0, 12);
  const rc = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Most recent events' }), el('button', { class: 'tablebtn', type: 'button', text: 'Full timeline →', onclick: () => showTab('timeline') })), el('div', { class: 'evlist' }, ...recent.map(e => evLink(e.id))));
  g2.append(fl, rc); root.append(g2);
}

/* ---------------- TIMELINE ---------------- */
const tl = { q: '', years: new Set(), cats: new Set(), tier: '', conf: '', sort: 'desc' };
function renderTimeline(root) {
  root.replaceChildren();
  const E = state.data.events || [];
  const years = [...new Set(E.map(e => e.date.slice(0, 4)))].sort();
  const cats = CAT_ORDER.filter(c => E.some(e => e.category.includes(c)));
  const f = el('div', { class: 'filters' });
  const search = el('input', { class: 'input', type: 'search', placeholder: 'Search the record…', id: 'tlSearch', value: tl.q, style: { minWidth: '220px' } });
  search.addEventListener('input', () => { tl.q = search.value.trim().toLowerCase(); list(); });
  f.append(search, el('span', { class: 'sep' }));
  const yg = el('div', { class: 'grp' }); years.forEach(y => { const b = el('button', { class: 'pill-btn', type: 'button', 'aria-pressed': String(tl.years.has(y)), text: y }); b.addEventListener('click', () => { tl.years.has(y) ? tl.years.delete(y) : tl.years.add(y); b.setAttribute('aria-pressed', String(tl.years.has(y))); list(); }); yg.append(b); });
  f.append(yg, el('span', { class: 'sep' }));
  const cg = el('div', { class: 'grp' }); cats.forEach(c => { const b = el('button', { class: 'pill-btn', type: 'button', 'aria-pressed': String(tl.cats.has(c)), text: c }); b.addEventListener('click', () => { tl.cats.has(c) ? tl.cats.delete(c) : tl.cats.add(c); b.setAttribute('aria-pressed', String(tl.cats.has(c))); list(); }); cg.append(b); });
  f.append(cg, el('span', { class: 'sep' }));
  const tsel = el('select', { class: 'input', id: 'tlTier' }, el('option', { value: '', text: 'Any tier' }), ...['T1', 'T2', 'T3', 'T4', 'T5'].map(t => el('option', { value: t, text: `≤ ${t}` })));
  tsel.value = tl.tier; tsel.addEventListener('change', () => { tl.tier = tsel.value; list(); });
  const csel = el('select', { class: 'input', id: 'tlConf' }, el('option', { value: '', text: 'Any confidence' }), ...['CANONICAL', 'HIGH', 'MEDIUM', 'LOW', 'VERIFY', 'DISPUTED'].map(t => el('option', { value: t, text: t })));
  csel.value = tl.conf; csel.addEventListener('change', () => { tl.conf = csel.value; list(); });
  const sortb = el('button', { class: 'pill-btn', type: 'button', text: tl.sort === 'desc' ? 'Newest first' : 'Oldest first' }); sortb.addEventListener('click', () => { tl.sort = tl.sort === 'desc' ? 'asc' : 'desc'; sortb.textContent = tl.sort === 'desc' ? 'Newest first' : 'Oldest first'; list(); });
  const clr = el('button', { class: 'pill-btn', type: 'button', text: 'Clear' }); clr.addEventListener('click', () => { tl.q = ''; tl.years.clear(); tl.cats.clear(); tl.tier = ''; tl.conf = ''; renderTimeline(root); });
  f.append(tsel, csel, sortb, clr);
  root.append(f);
  const count = el('div', { class: 'small muted', style: { marginBottom: '6px' } }); root.append(count);
  const listEl = el('div'); root.append(listEl);
  function list() {
    const TR = { T1: 1, T2: 2, T3: 3, T4: 4, T5: 5 };
    let rows = E.filter(e => (!tl.years.size || tl.years.has(e.date.slice(0, 4))) && (!tl.cats.size || e.category.some(c => tl.cats.has(c))) && (!tl.tier || TR[e.source.tier] <= TR[tl.tier]) && (!tl.conf || e.confidence === tl.conf)
      && (!tl.q || `${e.headline} ${e.summary} ${e.notes || ''} ${e.source.publisher || ''} ${(e.extracted?.entities || []).map(x => x.name).join(' ')}`.toLowerCase().includes(tl.q)));
    rows.sort((a, b) => tl.sort === 'desc' ? b.date.localeCompare(a.date) : a.date.localeCompare(b.date));
    count.textContent = `${rows.length.toLocaleString()} of ${E.length.toLocaleString()} events · ${rows.filter(r => r.confidence === 'DISPUTED').length} disputed · ${rows.filter(r => r.source.tier === 'T1').length} primary-sourced`;
    listEl.replaceChildren();
    let month = '';
    const frag = document.createDocumentFragment();
    tl.shown = tl.shown || 150;
    for (const e of rows.slice(0, tl.shown)) {
      const m = e.date.slice(0, 7);
      if (m !== month) { month = m; frag.append(el('div', { class: 'tl-month', text: fmt.mdate(e.date.slice(0, 7) + '-01') })); }
      frag.append(el('div', { class: 'evt', role: 'button', tabindex: '0', onclick: () => openEvent(e.id), onkeydown: ev => { if (ev.key === 'Enter') openEvent(e.id); } },
        el('div', { class: 'd', text: fmt.dmy(e.date) }),
        el('div', {}, el('div', { class: 'h', text: e.headline }), el('div', { class: 's', text: e.summary }),
          el('div', { class: 'meta' }, ...e.category.slice(0, 4).map(c => chip(c, 'cat')), ...extractChips(e.extracted, e), e.single_chain_suspected ? chip('likely one reporting chain', 'conf VERIFY') : ''),
          el('div', { class: 'src' }, sourceLine(e.source), e.corroboration?.length ? ` · +${e.corroboration.length} corroborating` : '')),
        el('div', { class: 'right' }, tierChip(e.source.tier), confChip(e.confidence), e.audit ? el('span', { class: 'chip ' + ({ SUPPORTED: 'ok', PARTLY: 'warn', UNOPENABLE: '' }[e.audit.verdict] || 'bad'), title: 'Independent audit: ' + (e.audit.note || ''), text: 'audit ' + e.audit.verdict.toLowerCase().replace('_', ' ') }) : '')));
    }
    if (rows.length > tl.shown) frag.append(el('button', { class: 'btn showmore', type: 'button', text: `Show ${Math.min(200, rows.length - tl.shown)} more (${tl.shown} of ${rows.length} shown)`, onclick: () => { tl.shown += 200; list(true); } }));
    if (!rows.length) frag.append(el('div', { class: 'empty', text: 'Nothing matches these filters.' }));
    listEl.append(frag);
  }
  const listReset = list; list = function (keep) { if (!keep) tl.shown = 150; listReset(); };
  list();
}

/* ---------------- TOPICS ---------------- */
function metricTile(k) {
  const linked = k.event_id && state.evIndex.has(k.event_id);
  const body = [el('div', { class: 'l', text: k.label }), el('div', { class: 'v', text: String(k.value ?? '') }), k.note ? el('div', { class: 's', text: k.note }) : ''];
  return linked ? el('a', { class: 'mt link', href: '#timeline', title: 'Open the source event', onclick: ev => { ev.preventDefault(); openEvent(k.event_id); } }, ...body) : el('div', { class: 'mt' }, ...body);
}
function renderTopics(root) {
  root.replaceChildren();
  const T = state.data.topics?.topics || [];
  if (!T.length) { root.append(el('div', { class: 'empty', text: 'Topic analyses not generated yet (data/topics.json).' })); return; }
  const grid = el('div', { class: 'grid cols-2' });
  const detail = el('div', { class: 'section' });
  T.forEach((t, i) => {
    const card = el('div', { class: 'card topic-card', role: 'button', tabindex: '0' }, el('div', { class: 'n', text: String(i + 1).padStart(2, '0') }), el('h3', { text: t.title }), el('div', { class: 'ol', text: t.one_liner }),
      el('div', { class: 'km' }, ...(t.key_metrics || []).slice(0, 3).map(k => el('div', { class: 'ml' }, el('b', { text: k.label + ': ' }), String(k.value ?? '')))));
    const open = () => { $$('.topic-card', grid).forEach(c => c.style.borderColor = ''); card.style.borderColor = 'var(--accent)'; showTopic(t); detail.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
    card.addEventListener('click', open); card.addEventListener('keydown', ev => { if (ev.key === 'Enter') open(); });
    grid.append(card);
  });
  root.append(grid, detail);
  function showTopic(t) {
    detail.replaceChildren(el('div', { class: 'card' },
      el('div', { class: 'eyebrow', text: 'Topic' }), el('h2', { text: t.title, style: { margin: '4px 0 6px' } }), el('p', { class: 'ink2', text: t.one_liner, style: { marginBottom: '14px' } }),
      el('div', { class: 'metric-grid' }, ...(t.key_metrics || []).map(metricTile)),
      threeBeat(t),
      t.second_order?.length ? el('div', { class: 'section' }, el('div', { class: 'eyebrow', text: 'Second-order' }), el('ul', { style: { margin: '6px 0 0 18px', padding: 0 } }, ...t.second_order.map(s => el('li', { text: s })))) : '',
      t.watch?.length ? el('div', { class: 'section' }, el('div', { class: 'eyebrow', text: 'What to watch' }), el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Item' }), el('th', { text: 'Threshold' }), el('th', { text: 'Observable by' }))), el('tbody', {}, ...t.watch.map(w => el('tr', {}, el('td', { text: w.item }), el('td', { class: 'small', text: w.threshold || '' }), el('td', { class: 'mono', text: w.by || '—' }))))))) : '',
      t.uncertainties?.length ? el('div', { class: 'section' }, el('div', { class: 'eyebrow', text: 'What is not known' }), ...t.uncertainties.map(u => el('div', { class: 'unc' }, el('div', { class: 'ty', text: u.type }), el('div', {}, u.note, u.what_would_change_it ? el('div', { class: 'small muted', text: `Would change if: ${u.what_would_change_it}` }) : '')))) : '',
      t.house_view ? el('div', { class: 'section' }, el('div', { class: 'eyebrow', text: 'House-view check' }), el('p', { text: t.house_view })) : '',
      el('div', { class: 'section' }, el('div', { class: 'eyebrow', text: `Evidence (${(t.evidence || []).length})` }), el('div', { class: 'evlist' }, ...(t.evidence || []).map(id => evLink(id))))));
  }
  if (T[0]) showTopic(T[0]);
}

/* ---------------- MODEL ---------------- */
function lerp(a, b, t) { return a + (b - a) * t; }
function computeModel(A) {
  const years = A.years; const out = { years, rows: {}, valuation: {} };
  const R = {}, seg = {};
  const segs = Object.keys(A.mix_2026);
  years.forEach((y, i) => {
    if (A.actuals[y]?.revenue != null) R[y] = A.actuals[y].revenue;
    else if (y === 2026) R[y] = A.revenue_2026;
    else R[y] = R[y - 1] * (1 + (A.growth[y] ?? 0));
    const t = Math.min(1, Math.max(0, (y - 2026) / 4));
    seg[y] = {}; segs.forEach(s => { seg[y][s] = R[y] * lerp(A.mix_2026[s], A.mix_2030[s], t); });
  });
  const rows = {};
  const put = (k, y, v) => { (rows[k] = rows[k] || {})[y] = v; };
  years.forEach(y => {
    const rev = R[y]; put('revenue', y, rev);
    segs.forEach(s => put(`seg_${s}`, y, seg[y][s]));
    put('revenue_net', y, rev * (1 - A.equalization_haircut));
    const gm = A.actuals[y]?.gross_margin ?? A.gross_margin[y]; put('gross_margin', y, gm);
    const gp = rev * gm; put('gross_profit', y, gp); put('cogs', y, rev - gp);
    const infer = A.actuals[y]?.inference_share ?? A.inference_share_of_cogs; put('cogs_inference', y, (rev - gp) * infer); put('cogs_other', y, (rev - gp) * (1 - infer));
    const rnd = rev * (A.opex.rnd[y] ?? 0), sm = rev * (A.opex.sm[y] ?? 0), ga = rev * (A.opex.ga[y] ?? 0), sbc = rev * (A.sbc_pct[y] ?? 0);
    const train = (A.training_usd_m || {})[y] != null ? A.training_usd_m[y] : rev * ((A.training_pct || {})[y] ?? 0);
    put('rnd', y, rnd); put('sm', y, sm); put('ga', y, ga); put('sbc', y, sbc); put('training', y, train);
    const opex = rnd + sm + ga + sbc; put('opex', y, opex);
    const oi_ex = gp - opex; put('op_income_ex_training', y, oi_ex); put('om_ex_training', y, rev ? oi_ex / rev : 0);
    const oi = oi_ex - (A.expense_training ? train : 0); const oiAll = gp - opex - train;
    put('op_income', y, oi); put('op_income_incl_training', y, oiAll); put('om', y, rev ? oi / rev : 0);
    const tax = oiAll > 0 ? oiAll * A.tax_rate : 0; put('tax', y, tax);
    const capex = A.capex_usd_m[y] ?? 0; put('capex', y, capex);
    const fcf = oiAll - tax + sbc - capex + (A.expense_training ? 0 : 0); put('fcf', y, fcf); put('fcf_margin', y, rev ? fcf / rev : 0);
  });
  let cum = 0; years.forEach(y => { if (y >= 2024) cum += rows.fcf[y]; put('cum_fcf', y, cum); });
  out.rows = rows;
  // valuation
  const r = A.discount_rate, base = 2025; const pv = {}; let pvSum = 0;
  years.filter(y => y >= 2026).forEach(y => { pv[y] = rows.fcf[y] / Math.pow(1 + r, y - base); if (y < 2030) pvSum += pv[y]; });
  const tv = rows.fcf[2030] * A.terminal_multiple_fcf; const pvTv = tv / Math.pow(1 + r, 2030 - base);
  out.valuation.dcf_ev = pvSum + pv[2030] + pvTv; out.valuation.pv_fcf = pvSum + pv[2030]; out.valuation.pv_tv = pvTv;
  out.valuation.marks = Object.entries(A.marks).map(([k, ev]) => {
    const req2030fcf = (ev - pvSum) * Math.pow(1 + r, 2030 - base) / (A.terminal_multiple_fcf + 1);
    const req2030rev = rows.fcf_margin[2030] > 0 ? req2030fcf / rows.fcf_margin[2030] : null;
    const cagr = req2030rev ? Math.pow(req2030rev / R[2026], 1 / 4) - 1 : null;
    return { key: k, label: A.mark_labels?.[k] || k, ev, ev_rev_2026: ev / R[2026], ev_rev_2027: ev / R[2027], ev_net_2026: ev / rows.revenue_net[2026], ev_net_2027: ev / rows.revenue_net[2027], req2030rev, req_cagr: cagr, vs_dcf: ev / out.valuation.dcf_ev - 1 };
  });
  return out;
}
const MODEL_ROWS = [
  ['revenue', 'Revenue (gross basis)', 'grp'], ['seg_*', null, 'sub'], ['revenue_net', 'Revenue, equalized net basis', 'sub'],
  ['cogs', 'Cost of revenue', 'grp'], ['cogs_inference', 'of which inference compute', 'sub'], ['cogs_other', 'of which other cost of revenue (partner share sits in S&M per the prospectus)', 'sub'],
  ['gross_profit', 'Gross profit', 'tot'], ['gross_margin', 'Gross margin', 'pct'],
  ['rnd', 'R&D (ex-training)', 'sub'], ['sm', 'Sales & marketing', 'sub'], ['ga', 'G&A', 'sub'], ['sbc', 'Stock-based comp', 'sub'], ['opex', 'Operating expenses', 'tot'],
  ['op_income_ex_training', 'Operating income, ex-training', 'tot'], ['om_ex_training', 'Margin, ex-training', 'pct'],
  ['training', 'Training compute', 'sub'], ['op_income_incl_training', 'Operating income, incl. training', 'tot'],
  ['tax', 'Cash taxes', 'sub'], ['capex', 'Compute capex / prepayments', 'sub'], ['fcf', 'Free cash flow', 'tot'], ['fcf_margin', 'FCF margin', 'pct'], ['cum_fcf', 'Cumulative FCF from 2024', 'sub'],
];
function renderModel(root) {
  root.replaceChildren();
  const MD = state.data.model;
  if (!MD?.assumptions) { root.append(el('div', { class: 'empty', text: 'Model not generated yet (data/model.json).' })); return; }
  let scen = MD.default_scenario || 'base';
  let A = JSON.parse(JSON.stringify(MD.assumptions[scen]));
  const layout = el('div', { class: 'model-layout' });
  const side = el('div', { class: 'card assump' }), main = el('div');
  layout.append(side, main); root.append(layout);
  function buildSide() {
    side.replaceChildren(el('div', { class: 'card-h' }, el('h3', { text: 'Assumptions' }), el('span', { class: 'small muted', text: 'live' })));
    const segc = el('div', { class: 'seg', role: 'group' }); ['bear', 'base', 'bull'].forEach(s => { if (!MD.assumptions[s]) return; const b = el('button', { type: 'button', 'aria-pressed': String(s === scen), text: s[0].toUpperCase() + s.slice(1) }); b.addEventListener('click', () => { scen = s; A = JSON.parse(JSON.stringify(MD.assumptions[s])); buildSide(); draw(); }); segc.append(b); });
    side.append(segc);
    const basis = el('div', { class: 'ctl', style: { marginTop: '10px' } }, el('label', { text: 'Expense training compute in operating income' }), (() => { const c = el('input', { type: 'checkbox', id: 'mExp' }); c.checked = !!A.expense_training; c.addEventListener('change', () => { A.expense_training = c.checked; draw(); }); return c; })());
    side.append(basis);
    const sl = (label, get, set, min, max, step, fmtF, src) => {
      const inp = el('input', { type: 'range', min, max, step, id: 'sl-' + label.replace(/\W+/g, '-') }); inp.value = get();
      const out = el('output', { text: fmtF(get()) });
      inp.addEventListener('input', () => { set(parseFloat(inp.value)); out.textContent = fmtF(parseFloat(inp.value)); draw(); });
      side.append(el('div', { class: 'ctl' }, el('label', { text: label }), out, inp, src ? el('details', { class: 'src' }, el('summary', { text: 'source and basis' }), el('div', { text: src })) : ''));
    };
    const S = MD.sources || {};
    side.append(el('h4', { text: 'Revenue' }));
    sl('FY2026 revenue ($B, gross)', () => A.revenue_2026 / 1000, v => A.revenue_2026 = v * 1000, 30, 90, 1, v => `$${v}B`, S.revenue_2026);
    [2027, 2028, 2029, 2030].forEach(y => sl(`${y} growth`, () => A.growth[y], v => A.growth[y] = v, -0.2, 2, 0.01, v => fmt.pct(v), y === 2027 ? S.growth : null));
    sl('Gross→net equalization haircut', () => A.equalization_haircut, v => A.equalization_haircut = v, 0, 0.6, 0.0025, v => fmt.pct(v, 1), S.equalization);
    {
      // the desk's canonical haircut and what the record's own evidence implies are both offered; neither is chosen silently
      const alt = MD.assumptions?.[scen]?.equalization_alt || MD.assumptions?.base?.equalization_alt, canon = MD.assumptions?.[scen]?.equalization_haircut ?? 0.3975;
      if (alt?.platform_fee_pct_fy2025 != null) {
        const slider = side.querySelector('#sl-Gross-net-equalization-haircut'), outEl = slider?.previousElementSibling;
        const setH = v => { A.equalization_haircut = v; if (slider) { slider.value = v; outEl.textContent = fmt.pct(v, 1); } draw(); };
        side.append(el('div', { class: 'ctl', style: { display: 'block' } }, el('div', { class: 'small muted', text: 'Two bases for the same haircut (conflict kept open):' }),
          el('div', { style: { display: 'flex', gap: '6px', flexWrap: 'wrap', marginTop: '4px' } },
            el('button', { class: 'btn', type: 'button', text: `Desk canonical ${fmt.pct(canon, 2)}`, onclick: () => setH(canon) }),
            el('button', { class: 'btn', type: 'button', text: `Record evidence ${fmt.pct(alt.platform_fee_pct_fy2025, 1)} (platform fees)`, onclick: () => setH(alt.platform_fee_pct_fy2025) })),
          alt.note ? el('div', { class: 'src', text: alt.note }) : ''));
      }
    }
    side.append(el('h4', { text: 'Margins' }));
    [2026, 2027, 2028, 2029, 2030].forEach(y => sl(`${y} gross margin`, () => A.gross_margin[y], v => A.gross_margin[y] = v, -0.5, 0.9, 0.01, v => fmt.pct(v), y === 2026 ? S.gross_margin : null));
    sl('Inference share of cost of revenue', () => A.inference_share_of_cogs, v => A.inference_share_of_cogs = v, 0.3, 0.95, 0.01, v => fmt.pct(v), S.inference_share);
    side.append(el('h4', { text: 'Opex & compute' }));
    [2026, 2028, 2030].forEach(y => sl(`${y} R&D % rev`, () => A.opex.rnd[y], v => { A.opex.rnd[y] = v; if (y === 2026) A.opex.rnd[2027] = (v + A.opex.rnd[2028]) / 2; if (y === 2028) { A.opex.rnd[2027] = (A.opex.rnd[2026] + v) / 2; A.opex.rnd[2029] = (v + A.opex.rnd[2030]) / 2; } if (y === 2030) A.opex.rnd[2029] = (A.opex.rnd[2028] + v) / 2; }, 0.02, 0.6, 0.01, v => fmt.pct(v), y === 2026 ? S.opex : null));
    [2026, 2028, 2030].forEach(y => sl(`${y} S&M + G&A % rev`, () => A.opex.sm[y] + A.opex.ga[y], v => { const r = A.opex.sm[y] / (A.opex.sm[y] + A.opex.ga[y] || 1); A.opex.sm[y] = v * r; A.opex.ga[y] = v * (1 - r); const ys = [2026, 2027, 2028, 2029, 2030]; [2027, 2029].forEach(yy => { A.opex.sm[yy] = (A.opex.sm[yy - 1] + A.opex.sm[yy + 1]) / 2; A.opex.ga[yy] = (A.opex.ga[yy - 1] + A.opex.ga[yy + 1]) / 2; }); }, 0.02, 0.4, 0.01, v => fmt.pct(v)));
    [2026, 2027, 2028, 2029, 2030].forEach(y => sl(`${y} training compute ($B)`, () => (A.training_usd_m[y] ?? 0) / 1000, v => A.training_usd_m[y] = v * 1000, 0, 80, 0.5, v => `$${v}B`, y === 2026 ? S.training : null));
    [2026, 2027, 2028, 2029, 2030].forEach(y => sl(`${y} compute capex / prepay ($B)`, () => (A.capex_usd_m[y] ?? 0) / 1000, v => A.capex_usd_m[y] = v * 1000, 0, 120, 1, v => `$${v}B`, y === 2026 ? S.capex : null));
    side.append(el('h4', { text: 'Valuation' }));
    sl('Discount rate', () => A.discount_rate, v => A.discount_rate = v, 0.07, 0.2, 0.005, v => fmt.pct(v, 1));
    sl('Terminal EV / 2030 FCF', () => A.terminal_multiple_fcf, v => A.terminal_multiple_fcf = v, 8, 50, 1, v => `${v}x`, S.terminal);
    sl('Tax rate', () => A.tax_rate, v => A.tax_rate = v, 0, 0.3, 0.01, v => fmt.pct(v));
    const reset = el('button', { class: 'btn', type: 'button', text: 'Reset scenario', style: { marginTop: '10px', width: '100%' } }); reset.addEventListener('click', () => { A = JSON.parse(JSON.stringify(MD.assumptions[scen])); buildSide(); draw(); }); side.append(reset);
    if (MD.notes?.length) side.append(el('div', { class: 'small muted', style: { marginTop: '12px' } }, ...MD.notes.map(n => el('p', { text: n, style: { marginBottom: '6px' } }))));
  }
  function draw() {
    const O = computeModel(A); const Y = O.years, R = O.rows;
    main.replaceChildren();
    const isA = y => A.actuals[y]?.revenue != null;
    const yl = y => isA(y) ? `${y}*` : `${y}E`;   // * = revenue and operating loss press-reported from a leaked draft prospectus (no public S-1); the rest of the column is the model's own split
    const SRC = new Set(['revenue', 'op_income_incl_training', 'gross_margin', 'gross_profit', 'cogs']);
    const modeled = (key, y) => isA(y) && !SRC.has(key);
    const k = el('div', { class: 'grid cols-4' });
    const kt = (l, v, s) => el('div', { class: 'tile' }, el('div', { class: 'label', text: l }), el('div', { class: 'value', text: v }), el('div', { class: 'sub', text: s || '' }));
    k.append(kt('2026E revenue', fmt.usd(R.revenue[2026]), `${fmt.pct(R.gross_margin[2026])} GM · ${scen}`), kt('2028E revenue', fmt.usd(R.revenue[2028]), `${fmt.pct(R.fcf_margin[2028])} FCF margin`), kt('2030E revenue', fmt.usd(R.revenue[2030]), `${fmt.pct(R.fcf_margin[2030])} FCF margin`), kt('DCF enterprise value', fmt.usd(O.valuation.dcf_ev), `${fmt.pct(O.valuation.pv_tv / O.valuation.dcf_ev)} from terminal`));
    const base25 = R.cum_fcf[2025], c26 = y => R.cum_fcf[y] - base25, Yf = Y.filter(y => y >= 2026);   // the trough is measured from 2026: FY2024-25 FCF is a model estimate, not reported cash burn
    const trough = Yf.reduce((a, y) => c26(y) < c26(a) ? y : a, Yf[0]);
    k.append(kt('Cumulative FCF trough (from 2026)', fmt.usd(c26(trough)), `in ${trough} · incl. modelled FY2024-25: ${fmt.usd(Math.min(...Y.map(y => R.cum_fcf[y])))}`), kt('Ex-training breakeven', String(Y.find(y => R.op_income_ex_training[y] > 0) || 'beyond 2030'), 'first positive year'), kt('Incl-training breakeven', String(Y.find(y => R.op_income_incl_training[y] > 0) || 'beyond 2030'), 'first positive year'), kt('2027E EV/revenue at $965B', `${(965000 / R.revenue[2027]).toFixed(1)}x`, `${(965000 / R.revenue_net[2027]).toFixed(1)}x net at a ${fmt.pct(A.equalization_haircut, 2)} haircut${A.equalization_alt?.platform_fee_pct_fy2025 != null && Math.abs(A.equalization_alt.platform_fee_pct_fy2025 - A.equalization_haircut) > 0.001 ? ` · ${(965000 / (R.revenue[2027] * (1 - A.equalization_alt.platform_fee_pct_fy2025))).toFixed(1)}x at ${fmt.pct(A.equalization_alt.platform_fee_pct_fy2025, 1)}` : ''}`));
    main.append(k);
    const g = el('div', { class: 'grid cols-2 section' });
    const segs = Object.keys(A.mix_2026); const segLabels = A.segment_labels || {};
    const c1 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Revenue build by segment' }), el('span', { class: 'small muted', text: '* = revenue press-reported (leaked draft, no public S-1), no segment split reported; E = estimate' }))); const c1c = el('div', { class: 'chart' }); c1.append(c1c);
    columnChart(c1c, { data: Y.map(y => ({ label: yl(y), values: isA(y) ? [{ name: 'Revenue, press-reported (no segment split)', value: R.revenue[y], color: 'var(--muted)' }] : segs.map((s, i) => ({ name: segLabels[s] || s, value: R[`seg_${s}`][y], color: SERIES[i] })) })), yFmt: v => fmt.usd(v) });
    c1.append(legend([{ name: 'Reported revenue, no split', color: 'var(--muted)', rect: true }, ...segs.map((s, i) => ({ name: segLabels[s] || s, color: SERIES[i], rect: true }))]));
    const c2 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Margin path, 2026E–2030E' }), el('span', { class: 'small muted', text: 'gross, operating (ex/incl training), FCF · 2024A–2025A in the table' }))); const c2c = el('div', { class: 'chart' }); c2.append(c2c);
    const YF = Y.filter(y => y >= 2026);   // 2024A-2025A margins (down to -800%) stay in the table: on one axis they flatten every forward line
    const pts = key => YF.map(y => ({ x: new Date(`${y}-07-01`), y: R[key][y], date: `${y}` }));
    lineChart(c2c, { series: [{ name: 'Gross', color: 'var(--s1)', points: pts('gross_margin') }, { name: 'Op ex-training', color: 'var(--s3)', points: pts('om_ex_training') }, { name: 'Op incl-training', color: 'var(--s2)', points: YF.map(y => ({ x: new Date(`${y}-07-01`), y: R.revenue[y] ? R.op_income_incl_training[y] / R.revenue[y] : 0, date: `${y}` })) }, { name: 'FCF', color: 'var(--s7)', points: pts('fcf_margin') }], yFmt: v => fmt.pct(v), xTicks: 5, xFmt: d3.utcFormat('%Y') });
    c2.append(legend([{ name: 'Gross margin', color: 'var(--s1)' }, { name: 'Operating, ex-training', color: 'var(--s3)' }, { name: 'Operating, incl. training', color: 'var(--s2)' }, { name: 'FCF margin', color: 'var(--s7)' }]));
    g.append(c1, c2); main.append(g);
    const g2 = el('div', { class: 'grid section' });
    const c3 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Free cash flow and cumulative' }))); const c3c = el('div', { class: 'chart' }); c3.append(c3c);
    columnChart(c3c, { data: Y.map(y => ({ label: isA(y) ? `${y} (model)` : `${y}E`, values: [{ name: 'FCF', value: R.fcf[y], color: R.fcf[y] < 0 ? 'var(--s8)' : 'var(--s3)' }] })), yFmt: v => fmt.usd(v), stacked: false, negOK: true, labelTop: false });
    c3.append(el('div', { class: 'chart-foot' }, el('span', { text: `Cumulative FCF 2024–2030: ${fmt.usd(R.cum_fcf[2030])} · trough ${fmt.usd(R.cum_fcf[trough])} (${trough})` })));
    const c4 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'What each mark requires' }), el('span', { class: 'small muted', text: 'reverse DCF at the sliders above' })));
    const mt = el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Mark' }), el('th', { class: 'num', text: 'EV' }), el('th', { class: 'num', text: 'EV/2026E rev' }), el('th', { class: 'num', text: 'EV/2027E rev' }), el('th', { class: 'num', text: 'EV/2027E net' }), el('th', { class: 'num', text: 'Req. 2030 rev' }), el('th', { class: 'num', text: '2026→30 CAGR' }), el('th', { class: 'num', text: 'vs DCF' }))),
      el('tbody', {}, ...O.valuation.marks.map(m => el('tr', {}, el('td', { text: m.label }), el('td', { class: 'num', text: fmt.usd(m.ev) }), el('td', { class: 'num', text: m.ev_rev_2026.toFixed(1) + 'x' }), el('td', { class: 'num', text: m.ev_rev_2027.toFixed(1) + 'x' }), el('td', { class: 'num', text: m.ev_net_2027.toFixed(1) + 'x' }), el('td', { class: 'num', text: m.req2030rev ? fmt.usd(m.req2030rev) : 'n/a (FCF ≤ 0)' }), el('td', { class: 'num', text: m.req_cagr != null ? fmt.pct(m.req_cagr) : '—' }), el('td', { class: `num ${m.vs_dcf < 0 ? '' : 'neg'}`, text: (m.vs_dcf >= 0 ? '+' : '') + fmt.pct(m.vs_dcf) })))));
    c4.append(el('div', { class: 'tablewrap' }, mt), el('div', { class: 'small muted', style: { marginTop: '6px' }, text: 'Required 2030 revenue solves EV = PV(FCF 2026–2029) + PV(2030 FCF × (1 + terminal multiple)) at the model FCF margin. EV treated as equity value (net cash ignored).' }));
    g2.append(c3); main.append(g2); c4.classList.add('section'); main.append(c4);
    // P&L table
    const tbl = el('table', { class: 'data model' }); const th = el('tr', {}, el('th', { text: '$M' }), ...Y.map(y => el('th', { class: 'num', text: yl(y), title: isA(y) ? 'Revenue and operating loss: press-reported from a leaked draft prospectus (no public S-1). Other cells in this column are the model\'s own split.' : 'Estimate' }))); tbl.append(el('thead', {}, th));
    const tb = el('tbody'); const cell = (v, kind, key, y) => el('td', { class: `num ${v < 0 ? 'neg' : ''} ${modeled(key, y) ? 'modeled' : ''}`, title: modeled(key, y) ? 'Model split, tuned to reproduce the reported operating loss; not reported' : '', text: kind === 'pct' ? fmt.pct(v) : fmt.usd(v) });
    for (const [key, label, kind] of MODEL_ROWS) {
      if (key === 'seg_*') { segs.forEach(s => tb.append(el('tr', {}, el('td', { class: 'sub', text: segLabels[s] || s }), ...Y.map(y => isA(y) ? el('td', { class: 'num modeled', title: 'No segment split is reported', text: '—' }) : cell(R[`seg_${s}`][y], 'usd', `seg_${s}`, y))))); continue; }
      tb.append(el('tr', {}, el('td', { class: kind === 'pct' ? 'sub' : kind, text: label }), ...Y.map(y => cell(R[key][y], kind, key, y))));
    }
    tbl.append(tb);
    main.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Income statement and cash flow build' }), el('span', { class: 'small muted', text: `${scen} scenario · gross revenue basis · * = revenue and operating loss press-reported from a leaked draft (no public S-1); italic grey = model split, not reported` })), el('div', { class: 'tablewrap' }, tbl)));
    // sensitivity
    const revs = [0.6, 0.8, 1, 1.25, 1.5].map(f => R.revenue[2030] * f), mults = [12, 18, 25, 32, 40];
    const st = el('table', { class: 'data sens' }, el('thead', {}, el('tr', {}, el('th', { text: '2030 revenue ↓ · terminal EV/FCF →' }), ...mults.map(m => el('th', { class: 'num', text: `${m}x` })))));
    const stb = el('tbody');
    for (const rv of revs) { const tr = el('tr', {}, el('td', { class: 'num', text: fmt.usd(rv) })); for (const m of mults) { const fcf30 = rv * R.fcf_margin[2030]; const pvFixed = O.valuation.pv_fcf - R.fcf[2030] / Math.pow(1 + A.discount_rate, 5); const ev = pvFixed + (fcf30 * (1 + m)) / Math.pow(1 + A.discount_rate, 5); const hit = Math.abs(ev - 965000) < 965000 * 0.12 ? 'hit' : ''; tr.append(el('td', { class: `num ${hit}`, text: fmt.usd(ev), title: hit ? 'within ±12% of the $965B Series H mark' : '' })); } stb.append(tr); }
    st.append(stb);
    main.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Sensitivity: implied EV today' }), el('span', { class: 'small muted', text: 'highlight = within ±12% of the $965B Series H mark' })), el('div', { class: 'tablewrap' }, st)));
    if (MD.comps?.length) {
      const ct = el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Comparable' }), el('th', { class: 'num', text: 'Valuation' }), el('th', { class: 'num', text: 'Revenue / run-rate' }), el('th', { text: 'Basis' }), el('th', { class: 'num', text: 'Multiple' }), el('th', { text: 'Source' }))), el('tbody', {}, ...MD.comps.map(c => el('tr', {}, el('td', { text: c.name }), el('td', { class: 'num', text: fmt.usd(c.valuation_usd_m) }), el('td', { class: 'num', text: fmt.usd(c.revenue_usd_m) }), el('td', { text: c.basis || '' }), el('td', { class: 'num', text: c.revenue_usd_m ? (c.valuation_usd_m / c.revenue_usd_m).toFixed(1) + 'x' : '—' }), el('td', {}, c.source_url ? el('a', { href: c.source_url, target: '_blank', rel: 'noopener', text: c.source_label || fmt.domain(c.source_url) }) : (c.source_label || ''), ' ', c.tier ? tierChip(c.tier) : '')))));
      main.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Frontier comparables' }), el('span', { class: 'small muted', text: 'never compare gross to net raw' })), el('div', { class: 'tablewrap' }, ct)));
    }
  }
  buildSide(); draw();
}

/* ---------------- COMPUTE ---------------- */
function renderCompute(root) {
  root.replaceChildren();
  const C = state.data.compute, M = state.data.metrics || {};
  const rows = C?.commitments || M.compute || [];
  if (!rows.length) { root.append(el('div', { class: 'empty', text: 'Compute ledger not generated yet.' })); return; }
  const tot = C?.totals || M.compute_totals || {};
  const k = el('div', { class: 'grid cols-4' });
  const kt = (l, v, s) => el('div', { class: 'tile' }, el('div', { class: 'label', text: l }), el('div', { class: 'value', text: v }), el('div', { class: 'sub', text: s || '' }));
  k.append(kt('Announced, all bases', fmt.usd(tot.usd_m_announced), tot.usd_m_up_to != null ? `incl. ${fmt.usd(tot.usd_m_up_to)} "up to" and ${fmt.usd(tot.usd_m_reported_unconfirmed || 0)} reported, unconfirmed` : 'sum of headline figures, "up to" included'), kt('Contracted or disclosed', fmt.usd(tot.usd_m_contracted), tot.usd_m_contracted_t1_t2_documented != null ? `${fmt.usd(tot.usd_m_contracted_t1_t2_documented)} on T1/T2 documents + ${fmt.usd(tot.usd_m_contracted_s1_coverage || 0)} from S-1 press coverage (T3)` : 'contract-level or filing-level figures'), kt('Power announced', fmt.gw(tot.gw_announced), tot.gw_up_to_ceiling != null ? `${tot.gw_up_to_ceiling} GW are "up to" ceilings` : 'gigawatts across partners'), tot.s1_non_cancelable_share != null ? kt('S-1 plan, non-cancelable', fmt.pct(tot.s1_non_cancelable_share, 1), `${fmt.usd(tot.usd_m_s1_non_cancelable_lines)} of ${fmt.usd(tot.usd_m_s1_reference)} over ten years (press-reported)`) : kt('Partners', String(new Set(rows.map(r => r.partner)).size), 'cloud, chip, neocloud, data-center'));
  root.append(k);
  const g = el('div', { class: 'grid cols-2 section' });
  const byP = {}; rows.forEach(r => { const p = r.partner || 'Other'; byP[p] = byP[p] || { a: 0, c: 0, gw: 0 }; byP[p].a += r.usd_m || 0; if ((r.usd_basis || '').match(/contract|filing|disclosed/i)) byP[p].c += r.usd_m || 0; byP[p].gw += r.gw || 0; });
  const c1 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Dollar commitments by partner' }), el('span', { class: 'small muted', text: 'solid = contracted basis, faded = announced/up to' }))); const c1c = el('div', { class: 'chart' }); c1.append(c1c);
  barChartH(c1c, { data: Object.entries(byP).sort((a, b) => b[1].a - a[1].a).map(([p, v], i) => ({ label: p, value: v.c, value2: v.a, color: 'var(--s2)', tag: v.c ? `${fmt.usd(v.c)} contracted / ${fmt.usd(v.a)} announced` : `${fmt.usd(v.a)} up to or unconfirmed` })), secondary: ['Contracted', 'Announced'] });
  const c2 = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Power by partner' }), el('span', { class: 'small muted', text: 'GW, where stated' }))); const c2c = el('div', { class: 'chart' }); c2.append(c2c);
  barChartH(c2c, { data: Object.entries(byP).filter(([, v]) => v.gw > 0).sort((a, b) => b[1].gw - a[1].gw).map(([p, v]) => ({ label: p, value: v.gw, color: 'var(--s4)' })), xFmt: v => fmt.gw(v) });
  g.append(c1, c2); root.append(g);
  // table
  const t = el('table', { class: 'data' }, el('thead', {}, el('tr', {}, ...['Partner', 'Chips', '$ (M)', 'Basis', 'GW', 'Term', 'Status', 'Financing', 'Source'].map(h => el('th', { class: /\$|GW/.test(h) ? 'num' : '', text: h })))),
    el('tbody', {}, ...rows.sort((a, b) => (b.usd_m || 0) - (a.usd_m || 0)).map(r => el('tr', {}, el('td', { text: r.partner }), el('td', { text: r.chips || '—' }), el('td', { class: 'num', text: fmt.usd(r.usd_m) }), el('td', {}, chip(r.usd_basis || '—')), el('td', { class: 'num', text: r.gw != null ? String(r.gw) : '—' }), el('td', { class: 'mono small', text: r.term || '—' }), el('td', {}, chip(r.status || '—')), el('td', { class: 'small', text: r.financing || '—' }), el('td', {}, r.event_id && state.evIndex.has(r.event_id) ? evLink(r.event_id, 'event') : (r.source_url ? el('a', { href: r.source_url, target: '_blank', rel: 'noopener', text: fmt.domain(r.source_url) }) : '—'))))));
  root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Commitment ledger' })), el('div', { class: 'tablewrap' }, t)));
  if (C?.gross_margin_bridge?.length) {
    const c = el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: C.gross_margin_bridge_title || 'From list price to gross margin' }), el('span', { class: 'small muted', text: 'every bar per $1 of list price; margins on realized revenue (list less discounts, 0.90) read higher' }))); const cc = el('div', { class: 'chart' }); c.append(cc);
    waterfall(cc, { steps: C.gross_margin_bridge, yFmt: v => fmt.pct(v) });
    if (C.gross_margin_bridge_note) c.append(el('div', { class: 'small muted', style: { marginTop: '6px' }, text: C.gross_margin_bridge_note }));
    root.append(c);
  }
  if (C?.unit_economics) {
    const u = C.unit_economics; const ut = el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Metric' }), el('th', { class: 'num', text: 'Value' }), el('th', { text: 'Basis / source' }))), el('tbody', {}, ...(u.rows || []).map(r => el('tr', {}, el('td', { text: r.metric }), el('td', { class: 'num', text: r.value }), el('td', { class: 'small' }, r.basis || '', r.source_url ? el('a', { href: r.source_url, target: '_blank', rel: 'noopener', text: ' ' + fmt.domain(r.source_url) }) : '', ' ', r.tier ? tierChip(r.tier) : '')))));
    root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Unit economics' }), el('span', { class: 'small muted', text: u.note || '' })), el('div', { class: 'tablewrap' }, ut)));
  }
  if (C?.circularity?.length) {
    const c = el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Vendor financing loop' }), el('span', { class: 'small muted', text: 'money in as investment vs money out as compute' }))); const cc = el('div', { class: 'chart' }); c.append(cc);
    const w = 720, h = 40 + C.circularity.length * 30, m = { t: 8, r: 20, b: 8, l: 140 }; const { g: gg, iw } = chartFrame(cc, w, h, m);
    const x = d3.scaleLinear().domain([0, d3.max(C.circularity, d => Math.max(d.invested_usd_m || 0, d.compute_usd_m || 0)) * 1.05]).range([0, iw]);
    C.circularity.forEach((d, i) => { const y = i * 30; gg.append('text').attr('class', 'dl sub').attr('x', -8).attr('y', y + 16).attr('text-anchor', 'end').text(d.partner); gg.append('rect').attr('x', 0).attr('y', y + 2).attr('width', x(d.invested_usd_m || 0)).attr('height', 9).attr('rx', 2).attr('fill', 'var(--s1)'); gg.append('rect').attr('x', 0).attr('y', y + 13).attr('width', x(d.compute_usd_m || 0)).attr('height', 9).attr('rx', 2).attr('fill', 'var(--s2)'); gg.append('text').attr('class', 'dl').attr('x', x(Math.max(d.invested_usd_m || 0, d.compute_usd_m || 0)) + 6).attr('y', y + 16).text(`${fmt.usd(d.invested_usd_m)} in · ${fmt.usd(d.compute_usd_m)} out`); });
    c.append(legend([{ name: 'Invested in Anthropic', color: 'var(--s1)', rect: true }, { name: 'Compute committed to partner', color: 'var(--s2)', rect: true }]));
    if (C.circularity_note) c.append(el('p', { class: 'small muted', style: { marginTop: '8px' }, text: C.circularity_note }));
    root.append(c);
  }
  if (C?.narrative) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Strategy read' })), threeBeat(C.narrative)));
  if (C?.cost_datapoints?.length || M.compute_costs?.length) {
    const cd = C?.cost_datapoints || M.compute_costs; root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Reported cost and margin datapoints' })), el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Metric' }), el('th', { text: 'Value' }), el('th', { text: 'Basis' }), el('th', { text: 'Source' }))), el('tbody', {}, ...cd.map(r => el('tr', {}, el('td', { text: r.metric }), el('td', { class: 'mono', text: String(r.value) }), el('td', { class: 'small', text: r.basis || '' }), el('td', {}, r.source_url ? el('a', { href: r.source_url, target: '_blank', rel: 'noopener', text: fmt.domain(r.source_url) }) : '', ' ', r.tier ? tierChip(r.tier) : ''))))))));
  }
}

/* ---------------- THESIS ---------------- */
function renderThesis(root) {
  root.replaceChildren();
  const T = state.data.thesis;
  if (!T || (!T.verdict && !(T.bull?.length || T.bear?.length))) { root.append(el('div', { class: 'empty', text: 'Thesis not generated yet.' })); return; }
  const v = T.verdict || { call: 'Verdict pending', one_liner: "The Judge has not filed a verdict yet. The two cases below were written independently under the same standard and are not weighed.", rationale: [], what_flips: [], by_mark: [] };
  const cls = !T.verdict ? 'lean' : /bull/i.test(v.call) ? 'bull' : /bear/i.test(v.call) ? 'bear' : 'lean';
  const MARK_SHORT = { series_h: 'Series H', secondary: 'Secondary mark', ipo_target: 'IPO target' };
  const callCls = c => /BEAR/.test(c) ? 'conf DISPUTED' : /BULL/.test(c) ? 'conf HIGH' : 'conf MEDIUM';
  root.append(el('div', { class: 'verdict' }, el('div', { class: `badge ${cls}`, text: v.call }), el('div', {}, el('div', { style: { fontWeight: 600, fontSize: '16px' }, text: v.one_liner }), el('div', { class: 'small muted', style: { marginTop: '4px' }, text: v.horizon ? `Horizon: ${v.horizon}` : '' }),
    v.by_mark?.length ? el('div', { style: { display: 'flex', gap: '8px', flexWrap: 'wrap', marginTop: '10px' } }, ...v.by_mark.map(m => el('span', { class: `chip ${callCls(m.call)}`, title: m.why, text: `${fmt.usd(m.ev_usd_m)} ${MARK_SHORT[m.mark] || m.mark}: ${m.call}` }))) : '',
    el('div', { class: 'small muted', style: { marginTop: '8px' }, text: 'Decision support, not investment advice. The desk\'s model portfolio is overweight Anthropic (6%) and underweight OpenAI (2%) per project context dated Feb 27 2026, not re-verified; the call does not depend on it.' }))));
  const g = el('div', { class: 'grid cols-2 section' });
  const col = (title, args, color) => { const c = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: title }), el('span', { class: 'small muted', text: `${args.length} arguments` }))); args.forEach(a => c.append(el('div', { class: 'arg' }, el('div', { class: 'c' }, a.claim, el('span', { class: 'strength', title: `strength ${a.strength}/5` }, el('i', { style: { width: `${(a.strength || 3) * 20}%`, background: color } }))), el('div', { class: 'e', text: a.evidence }), a.defense ? el('details', { class: 'small', style: { margin: '4px 0' } }, el('summary', { text: 'best attack and the answer', style: { cursor: 'pointer', color: 'var(--ink-2)' } }), el('div', { text: a.defense, style: { marginTop: '4px' } })) : '', el('div', { class: 'ev' }, ...(a.event_ids || []).filter(id => state.evIndex.has(id)).map(id => el('a', { href: '#timeline', onclick: ev => { ev.preventDefault(); openEvent(id); }, text: state.evIndex.get(id).date, title: state.evIndex.get(id).headline })))))); return c; };
  g.append(col('The bull case', T.bull || [], 'var(--s3)'), col('The bear case', T.bear || [], 'var(--s8)'));
  root.append(g);
  const MARK_LABEL = { series_h: 'Series H post-money (May 2026)', secondary: 'Secondary-market mark (reported)', ipo_target: 'Reported IPO target' };
  if ((T.bull_at_price || []).length || (T.bear_at_price || []).length) {
    const pick = (arr, k) => (arr || []).find(x => x.mark === k);
    root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'What each side says must be true at each price' }), el('span', { class: 'small muted', text: 'each uses the model reverse-DCF' })),
      el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Mark' }), el('th', { class: 'num', text: 'EV' }), el('th', { text: 'Bull' }), el('th', { text: 'Bear' }))),
        el('tbody', {}, ...['series_h', 'secondary', 'ipo_target'].map(k => { const b = pick(T.bull_at_price, k), r = pick(T.bear_at_price, k); return el('tr', {}, el('td', { text: MARK_LABEL[k] }), el('td', { class: 'num', text: fmt.usd((b || r || {}).ev_usd_m) }), el('td', { class: 'small', text: b?.argument || '' }), el('td', { class: 'small', text: r?.argument || '' })); }))))));
  }
  if (T.bull_outside_view || T.bear_outside_view) {
    const ov = o => o ? el('div', { class: 'small' }, el('p', {}, el('b', { text: 'Reference class: ' }), o.reference_class || ''), el('p', {}, el('b', { text: 'Base rate: ' }), o.base_rate || ''), el('p', {}, el('b', { text: 'What is different here: ' }), o.what_is_different || ''), o.source ? el('p', { class: 'muted', text: `Source: ${o.source}` }) : '') : '';
    root.append(el('div', { class: 'grid cols-2 section' }, el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Outside view, bull framing' })), ov(T.bull_outside_view)), el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Outside view, bear framing' })), ov(T.bear_outside_view))));
  }
  if (T.bull_concedes || T.bear_concedes) root.append(el('div', { class: 'grid cols-2 section' }, el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'The bull concedes' })), el('p', { text: T.bull_concedes || '' })), el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'The bear concedes' })), el('p', { text: T.bear_concedes || '' }))));
  const r = el('div', { class: 'grid cols-2 section' });
  r.append(el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Why the verdict lands where it does' })), el('ol', { style: { margin: '0 0 0 18px', padding: 0 } }, ...(v.rationale || []).map(x => el('li', { text: x, style: { marginBottom: '6px' } })))),
    el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'What would flip it' })), el('ul', { style: { margin: '0 0 0 18px', padding: 0 } }, ...(v.what_flips || []).map(x => el('li', { text: x, style: { marginBottom: '6px' } })))));
  root.append(r);
  if (v.by_mark?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'The call at each price' }), el('span', { class: 'small muted', text: 'from the model reverse-DCF; reference prices are reported marks' })),
    el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Mark' }), el('th', { class: 'num', text: 'EV' }), el('th', { text: 'Call' }), el('th', { text: 'Why' }))),
      el('tbody', {}, ...v.by_mark.map(m => el('tr', {}, el('td', { text: (({ series_h: 'Series H post-money (May 2026)', secondary: 'Secondary-market mark (reported)', ipo_target: 'Reported IPO target' })[m.mark]) || m.mark }), el('td', { class: 'num', text: fmt.usd(m.ev_usd_m) }), el('td', {}, chip(m.call, /BULL/.test(m.call) ? 'conf HIGH' : /BEAR/.test(m.call) ? 'conf DISPUTED' : 'conf MEDIUM')), el('td', { class: 'small', text: m.why }))))))));
  if (v.position_check?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Consistency with the standing position' }), el('span', { class: 'small muted', text: 'a check for the decision-maker, not evidence for the call; position per project context dated Feb 27 2026, not re-verified' })),
    el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Mark' }), el('th', { text: 'Relation' }), el('th', { text: 'Note' }))), el('tbody', {}, ...v.position_check.map(p => el('tr', {}, el('td', { text: MARK_LABEL[p.mark] || p.mark }), el('td', {}, chip(p.relation, p.relation === 'supports' ? 'conf HIGH' : p.relation === 'challenges' ? 'conf DISPUTED' : 'conf MEDIUM')), el('td', { class: 'small', text: p.note || '' }))))))));
  if (T.scorecard?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Scorecard' }), el('span', { class: 'small muted', text: 'strength of each side by dimension, 1 to 5' })),
    el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Dimension' }), el('th', { class: 'num', text: 'Bull' }), el('th', { class: 'num', text: 'Bear' }), el('th', { text: 'Edge' }), el('th', { text: 'Note' }))),
      el('tbody', {}, ...T.scorecard.map(s => el('tr', {}, el('td', { text: s.dimension }), el('td', { class: 'num', text: String(s.bull) }), el('td', { class: 'num', text: String(s.bear) }), el('td', {}, chip(s.edge, s.edge === 'bull' ? 'conf HIGH' : s.edge === 'bear' ? 'conf DISPUTED' : 'conf MEDIUM')), el('td', { class: 'small', text: s.note || '' }))))))));
  if (T.thesis_breakers?.length) {
    const tb = el('table', { class: 'data' }, el('thead', {}, el('tr', {}, ...['Metric', 'Threshold', 'Observable by', 'Current reading', 'Status', 'Evidence'].map(h => el('th', { text: h })))), el('tbody', {}, ...T.thesis_breakers.map(b => el('tr', {}, el('td', { text: b.metric }), el('td', { class: 'mono', text: b.threshold }), el('td', { class: 'mono', text: b.observable_by }), el('td', { text: b.current }), el('td', {}, chip(b.status || 'open', /breach|fail/i.test(b.status || '') ? 'conf DISPUTED' : /hold|intact/i.test(b.status || '') ? 'conf HIGH' : 'conf MEDIUM')), el('td', {}, b.event_id && state.evIndex.has(b.event_id) ? evLink(b.event_id, '↗') : '')))));
    root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Thesis-breakers' }), el('span', { class: 'small muted', text: 'the observation, the threshold, and when it becomes observable' })), el('div', { class: 'tablewrap' }, tb)));
  }
  if (v.house_view_check?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'House-view check' })), el('ul', { style: { margin: '0 0 0 18px', padding: 0 } }, ...v.house_view_check.map(x => el('li', { text: x, style: { marginBottom: '6px' } })))));
  if (T.unresolved?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Still open in the record' }), el('span', { class: 'small muted', text: 'could change the call' })), el('ul', { style: { margin: '0 0 0 18px', padding: 0 } }, ...T.unresolved.map(x => el('li', { text: x, style: { marginBottom: '6px' } })))));
  if (T.consensus) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Where this differs from consensus' })), el('p', { text: T.consensus })));
}

/* ---------------- NETWORK ---------------- */
const TYPE_COLOR = { investor: 'var(--s1)', cloud: 'var(--s2)', chip: 'var(--s4)', customer: 'var(--s3)', distribution: 'var(--s3)', competitor: 'var(--s8)', portfolio: 'var(--s7)', acquired: 'var(--s7)', government: 'var(--s5)', regulator: 'var(--s5)', court: 'var(--s5)' };
const TYPE_LABEL = { investor: 'Investor', cloud: 'Cloud partner', chip: 'Chip supplier', customer: 'Customer / distribution', competitor: 'Competitor', portfolio: 'Portfolio / acquired', government: 'Government / regulator / court', other: 'Adviser / other' };
function primaryType(e) { const t = e.types || []; for (const k of ['investor', 'cloud', 'chip', 'competitor', 'portfolio', 'acquired', 'customer', 'distribution', 'government', 'regulator', 'court']) if (t.includes(k)) return k === 'acquired' ? 'portfolio' : (k === 'distribution' ? 'customer' : (k === 'regulator' || k === 'court') ? 'government' : k); return 'other'; }
function renderNetwork(root) {
  root.replaceChildren();
  const ENT = state.data.entities || [];
  if (!ENT.length) { root.append(el('div', { class: 'empty', text: 'Entity graph not generated yet.' })); return; }
  const active = new Set(Object.keys(TYPE_LABEL));
  const f = el('div', { class: 'filters' });
  Object.entries(TYPE_LABEL).forEach(([k, l]) => { const b = el('button', { class: 'pill-btn', type: 'button', 'aria-pressed': 'true' }, el('span', { class: 'sw', style: { display: 'inline-block', width: '8px', height: '8px', borderRadius: '2px', background: TYPE_COLOR[k] || 'var(--muted)', marginRight: '6px' } }), l); b.addEventListener('click', () => { active.has(k) ? active.delete(k) : active.add(k); b.setAttribute('aria-pressed', String(active.has(k))); draw(); }); f.append(b); });
  const lim = el('select', { class: 'input' }, ...[60, 100, 160, 250].map(n => el('option', { value: n, text: `Top ${n} by connections` }))); lim.value = '100'; lim.addEventListener('change', draw); f.append(el('span', { class: 'sep' }), lim);
  root.append(f);
  const lay = el('div', { class: 'net-layout' }); const netEl = el('div', { class: 'net' }); const side = el('div', { class: 'card' }); lay.append(netEl, side); root.append(lay);
  function draw() {
    const nodes = ENT.filter(e => active.has(primaryType(e))).slice(0, +lim.value).map(e => ({ id: e.name, e, r: 4 + Math.min(14, Math.sqrt(e.degree || 1) * 2.2), type: primaryType(e) }));
    nodes.unshift({ id: 'Anthropic', hub: true, r: 26, type: 'hub' });
    const links = nodes.filter(n => !n.hub).map(n => ({ source: 'Anthropic', target: n.id, w: 0.5 + Math.min(3, Math.log1p(n.e.degree || 1)) }));
    netEl.replaceChildren();
    const W = 900, H = 620; const svg = d3.select(netEl).append('svg').attr('viewBox', `0 0 ${W} ${H}`);
    const zoomG = svg.append('g'); svg.call(d3.zoom().scaleExtent([0.5, 3]).on('zoom', ev => zoomG.attr('transform', ev.transform)));
    const link = zoomG.append('g').selectAll('line').data(links).join('line').attr('class', 'link').attr('stroke-width', d => d.w);
    const node = zoomG.append('g').selectAll('g').data(nodes).join('g').attr('class', d => `node${d.hub ? ' hub' : ''}`);
    node.append('circle').attr('r', d => d.r).attr('fill', d => d.hub ? 'var(--ink)' : (TYPE_COLOR[d.type] || 'var(--muted)'))
      .on('pointermove', (ev, d) => { if (d.hub) return; showTip(ev.clientX, ev.clientY, tipRows(d.id, [{ label: TYPE_LABEL[d.type] || d.type, value: d.e.public ? (d.e.ticker || 'public') : 'private' }, { label: 'Linked events', value: String(d.e.degree || 0) }, ...(d.e.amount_usd_m ? [{ label: 'Amount', value: fmt.usd(d.e.amount_usd_m) }] : [])])); })
      .on('pointerleave', hideTip).on('click', (ev, d) => { if (!d.hub) showEntity(d.e); });
    node.filter(d => d.hub || d.r >= 8).append('text').attr('dy', d => d.r + 11).attr('text-anchor', 'middle').text(d => d.id.length > 22 ? d.id.slice(0, 21) + '…' : d.id).attr('fill', 'var(--ink)').attr('font-size', d => d.hub ? 13 : 10.5).attr('font-weight', d => d.hub ? 700 : 400);
    const sim = d3.forceSimulation(nodes).force('link', d3.forceLink(links).id(d => d.id).distance(d => 120 + 160 / (d.w || 1))).force('charge', d3.forceManyBody().strength(-60)).force('center', d3.forceCenter(W / 2, H / 2)).force('collide', d3.forceCollide(d => d.r + 6));
    sim.on('tick', () => { link.attr('x1', d => d.source.x).attr('y1', d => d.source.y).attr('x2', d => d.target.x).attr('y2', d => d.target.y); node.attr('transform', d => `translate(${d.x},${d.y})`); });
    node.call(d3.drag().on('start', (ev, d) => { if (!ev.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; }).on('drag', (ev, d) => { d.fx = ev.x; d.fy = ev.y; }).on('end', (ev, d) => { if (!ev.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));
    // side: public companies
    const pub = ENT.filter(e => e.public && e.ticker).sort((a, b) => (b.degree || 0) - (a.degree || 0));
    side.replaceChildren(el('div', { class: 'card-h' }, el('h3', { text: 'Public companies attached' }), el('span', { class: 'small muted', text: `${pub.length}` })),
      el('div', { class: 'tablewrap', style: { maxHeight: '540px', overflow: 'auto' } }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Ticker' }), el('th', { text: 'Company' }), el('th', { text: 'Role' }), el('th', { class: 'num', text: 'Events' }))), el('tbody', {}, ...pub.map(e => el('tr', { style: { cursor: 'pointer' }, onclick: () => showEntity(e) }, el('td', { class: 'mono', text: e.ticker }), el('td', { text: e.name }), el('td', { class: 'small', text: (e.types || []).slice(0, 3).join(', ') }), el('td', { class: 'num', text: String(e.degree || 0) })))))));
  }
  function showEntity(e) {
    const evs = (e.event_ids || []).map(id => state.evIndex.get(id)).filter(Boolean).sort((a, b) => a.date.localeCompare(b.date));
    openDrawer(el('div', {}, el('div', { class: 'eyebrow', text: (e.types || []).join(' · ') }), el('h2', { text: `${e.name}${e.ticker ? ' (' + e.ticker + ')' : ''}`, style: { margin: '4px 0 8px' } }),
      el('div', { style: { display: 'flex', gap: '6px', flexWrap: 'wrap', marginBottom: '10px' } }, chip(e.public ? 'public' : 'private'), e.amount_usd_m ? chip(fmt.usd(e.amount_usd_m), 'num') : '', e.first_date ? chip(`since ${fmt.date(e.first_date)}`) : '', e.tier ? tierChip(e.tier) : ''),
      ...(e.notes || []).map(n => el('p', { class: 'ink2', text: n, style: { marginBottom: '6px' } })),
      e.sources?.length ? el('div', { class: 'small', style: { margin: '8px 0' } }, ...e.sources.map(s => el('a', { href: s, target: '_blank', rel: 'noopener', text: fmt.domain(s), style: { marginRight: '8px' } }))) : '',
      el('div', { class: 'eyebrow', style: { marginTop: '12px' }, text: `Linked events (${evs.length})` }), el('div', { class: 'evlist' }, ...evs.map(x => evLink(x.id)))));
  }
  draw();
}

/* ---------------- AGENTS FLOOR ---------------- */
class Floor {
  constructor(root, data) {
    this.root = root; this.data = data; this.log = data.log || []; this.agents = data.agents || {};
    this.i = 0; this.playing = false; this.vt = 0; this.speed = 90; this.live = false; this.pollTimer = null; this.raf = null; this.lastReal = 0;
    this.t0 = this.log.length ? Date.parse(this.log[0].t) : Date.now(); this.t1 = this.log.length ? Date.parse(this.log[this.log.length - 1].t) : this.t0 + 1;
    this.state = {}; this.counts = { search: 0, open: 0, found: 0, flag: 0, message: 0 };
    this.build();
  }
  layout() {
    const waves = [['orchestrator', 'orchestrator'], ['scouts', 'scout'], ['desks', 'desk'], ['verification', 'verify'], ['topic analysts', 'analysis'], ['model & compute', 'model'], ['bull / bear / judge', 'thesis'], ['certify', 'certify']];
    const rows = [];
    for (const [label, w] of waves) {
      const ids = w === 'orchestrator' ? ['orchestrator'] : Object.keys(this.agents).filter(a => this.agents[a].wave === w);
      for (let i = 0; i < ids.length; i += 8) rows.push([i ? `${label} (cont.)` : label, ids.slice(i, i + 8)]);
    }
    const W = 1000, dw = 108, dh = 78, gap = 10; let y = 50; const pos = {}; const rowMeta = [];
    for (const [name, ids] of rows) { const total = ids.length * dw + (ids.length - 1) * gap; let x = (W - total) / 2; rowMeta.push({ name, y }); for (const id of ids) { pos[id] = { x, y, w: dw, h: dh }; x += dw + gap; } y += dh + 62; }
    return { W, H: y - 34, pos, rowMeta, dw, dh };
  }
  build() {
    const L = this.layout(); this.L = L;
    this.root.replaceChildren();
    const ctl = el('div', { class: 'floor-ctl' });
    this.playBtn = el('button', { class: 'btn primary', type: 'button', text: 'Play' }); this.playBtn.addEventListener('click', () => this.toggle());
    this.scrub = el('input', { type: 'range', min: 0, max: 1000, value: 0, 'aria-label': 'Scrub replay' }); this.scrub.addEventListener('input', () => this.seek(+this.scrub.value / 1000));
    this.clock = el('span', { class: 'clock', text: '—' });
    const sp = el('select', { class: 'input' }, el('option', { value: 30, text: 'Replay in 30 s' }), el('option', { value: 90, text: 'Replay in 90 s' }), el('option', { value: 300, text: 'Replay in 5 min' }), el('option', { value: 0, text: 'Real time' })); sp.value = '90'; sp.addEventListener('change', () => { this.speed = +sp.value; });
    this.liveBtn = el('button', { class: 'live pill-btn', type: 'button' }, el('i'), 'Live'); this.liveBtn.addEventListener('click', () => this.toggleLive());
    ctl.append(this.playBtn, this.scrub, this.clock, sp, this.liveBtn);
    this.counters = el('div', { class: 'counters' });
    const lay = el('div', { class: 'floor-layout' });
    const floor = el('div', { class: 'floor' }); this.svg = d3.select(floor).append('svg').attr('viewBox', `0 0 ${L.W} ${L.H}`).attr('role', 'img').attr('aria-label', 'The agents at their desks; raised signs mark new or conflicting information');
    const lg = el('div', { class: 'floor-legend' }, ...[['scout', 'Timeline scouts'], ['desk', 'Research desks'], ['verify', 'Re-derivers'], ['analysis', 'Topic analysts'], ['model', 'Model & compute'], ['thesis', 'Bull / bear / judge'], ['certify', 'Certifier']].map(([w, l]) => el('span', { class: 'k' }, el('i', { style: { background: AGENT_COLORS[w] } }), l)),
      el('span', { class: 'k sym' }, 'sign = a desk flagged new or conflicting information'), el('span', { class: 'k sym' }, 'NEW = first desk to file an event'), el('span', { class: 'k sym' }, 'CONFIRMS = another desk corroborated it'), el('span', { class: 'k sym' }, 'envelope = message between desks'));
    floor.append(lg);
    const side = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Desk chatter' }), el('span', { class: 'small muted', text: 'the real log' }))); this.feed = el('div', { class: 'feed' }); side.append(this.feed);
    lay.append(floor, side);
    this.root.append(ctl, this.counters, lay);
    this.flagsCard = el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Signs raised' }), el('span', { class: 'small muted', text: 'new or conflicting information' }))); this.flagsList = el('div', { class: 'flags-list' }); this.flagsCard.append(this.flagsList); this.root.append(this.flagsCard);
    this.rosterCard = el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Roster' }))); this.root.append(this.rosterCard); this.renderRoster();
    // draw rows and desks
    const g = this.svg.append('g');
    L.rowMeta.forEach(r => g.append('text').attr('class', 'row-l').attr('x', 12).attr('y', r.y - 8).text(r.name));
    this.desks = {};
    for (const [id, p] of Object.entries(L.pos)) {
      const a = this.agents[id] || { name: 'Orchestrator', wave: 'orchestrator' };
      const col = AGENT_COLORS[a.wave] || 'var(--ink)';
      const d = this.svg.append('g').attr('class', 'desk').attr('transform', `translate(${p.x},${p.y})`).attr('tabindex', 0).attr('role', 'button').attr('aria-label', `${a.name}: open activity`)
        .style('cursor', 'pointer').on('click', () => this.showAgent(id)).on('keydown', ev => { if (ev.key === 'Enter') this.showAgent(id); });
      d.append('rect').attr('class', 'd').attr('width', p.w).attr('height', p.h);
      d.append('circle').attr('class', 'ring').attr('cx', 24).attr('cy', 22).attr('r', 15);
      const mon = d.append('g').attr('class', 'mon').attr('transform', 'translate(64,16)');
      mon.append('rect').attr('class', 'scr').attr('width', 34).attr('height', 22).attr('rx', 3);
      [[5, 22], [10.5, 15], [16, 19]].forEach(([yy, ww], i) => mon.append('rect').attr('class', 'ln').attr('x', 5).attr('y', yy).attr('width', ww).attr('height', 2.4).attr('rx', 1.2).style('animation-delay', `${i * 0.22}s`));
      mon.append('line').attr('class', 'stand').attr('x1', 17).attr('x2', 17).attr('y1', 22).attr('y2', 28);
      d.append('line').attr('class', 'top').attr('x1', 8).attr('x2', p.w - 8).attr('y1', 44).attr('y2', 44);
      const fig = d.append('g').attr('class', 'fig').attr('transform', 'translate(24,0)');
      fig.append('path').attr('class', 'body').attr('d', 'M-14,44 C-14,33 -8,29 0,29 C8,29 14,33 14,44 Z').attr('fill', col);
      fig.append('circle').attr('class', 'head').attr('cx', 0).attr('cy', 20).attr('r', 8);
      fig.append('g').attr('class', 'arm').attr('transform', 'translate(10,35) rotate(-30)').append('line').attr('x1', 0).attr('y1', 0).attr('x2', 0).attr('y2', 11).attr('stroke', col);
      d.append('text').attr('class', 'st').attr('x', 8).attr('y', 11).text('idle');
      d.append('text').attr('class', 'n').attr('x', 8).attr('y', 58).text(shortName(a.name, id));
      d.append('text').attr('class', 'r').attr('x', 8).attr('y', 70).text(a.wave === 'orchestrator' ? 'dispatch & merge' : a.wave);
      d.append('text').attr('class', 'cnt').attr('x', p.w - 8).attr('y', 70).attr('text-anchor', 'end').text('');
      const fb = d.append('g').attr('class', 'flagbadge').attr('transform', `translate(${p.w - 10},8)`).style('display', 'none');
      fb.append('circle').attr('r', 7); fb.append('text').attr('text-anchor', 'middle').attr('dy', '0.35em').text('0');
      this.desks[id] = d; this.state[id] = { status: 'idle', searches: 0, pages: 0, events: 0, flags: 0, lastFloat: 0 };
    }
    this.msgLayer = this.svg.append('g'); this.flagLayer = this.svg.append('g'); this.floatLayer = this.svg.append('g');
    this.renderCounters(); this.updateClock();
    // key handling
    this.root.addEventListener('keydown', ev => { if (ev.key === ' ' && ev.target === this.root) { ev.preventDefault(); this.toggle(); } });
  }
  renderRoster() {
    const rows = Object.values(this.agents).sort((a, b) => (a.planned ? 1 : 0) - (b.planned ? 1 : 0) || String(a.started).localeCompare(String(b.started)));
    this.rosterCard.replaceChildren(el('div', { class: 'card-h' }, el('h3', { text: 'Roster' }), el('span', { class: 'small muted', text: `${rows.length} agents` })),
      el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, ...['Agent', 'Wave', 'Started', 'Finished', 'Searches', 'Pages', 'Events', 'Flags', 'Conflicts', 'Open'].map(h => el('th', { class: /Searches|Pages|Events|Flags|Conflicts|Open/.test(h) ? 'num' : '', text: h })))),
        el('tbody', {}, ...rows.map(a => el('tr', { style: { cursor: 'pointer' }, onclick: () => this.showAgent(a.id) }, el('td', {}, el('span', { class: 'sw', style: { display: 'inline-block', width: '8px', height: '8px', borderRadius: '50%', background: AGENT_COLORS[a.wave], marginRight: '6px' } }), a.name), el('td', { text: a.wave }), el('td', { class: 'mono small', text: a.planned ? 'queued' : fmt.time(a.started) }), el('td', { class: 'mono small', text: a.planned ? '' : fmt.time(a.finished) }), el('td', { class: 'num', text: String(a.stats?.searches ?? '—') }), el('td', { class: 'num', text: String(a.stats?.pages_opened ?? '—') }), el('td', { class: 'num', text: String(a.events ?? '—') }), el('td', { class: 'num', text: String(a.stats?.flags ?? '—') }), el('td', { class: 'num', text: String(a.conflicts ?? '—') }), el('td', { class: 'num', text: String(a.open_items ?? '—') })))))));
  }
  showAgent(id) {
    const a = this.agents[id] || { name: 'Orchestrator', wave: 'orchestrator' };
    const entries = this.log.filter(r => r.agent === id || r.to === id);
    openDrawer(el('div', {}, el('div', { class: 'eyebrow', text: a.wave }), el('h2', { text: a.name, style: { margin: '4px 0 8px' } }),
      el('div', { style: { display: 'flex', gap: '6px', flexWrap: 'wrap', marginBottom: '10px' } }, chip(`${a.stats?.searches ?? 0} searches`), chip(`${a.stats?.pages_opened ?? 0} pages`), chip(`${a.events ?? 0} events`), chip(`${a.stats?.flags ?? 0} flags`), chip(`${a.conflicts ?? 0} conflicts`)),
      el('div', { class: 'feed', style: { height: 'auto', maxHeight: '70vh' } }, ...entries.slice(0, 400).map(r => this.feedRow(r, true)))));
  }
  feedRow(r, full) {
    const who = this.agents[r.agent]?.name || (r.agent === 'orchestrator' ? 'Orchestrator' : r.agent); const wave = this.agents[r.agent]?.wave || 'orchestrator';
    const to = r.to ? ` → ${this.agents[r.to]?.name || r.to}` : '';
    return el('div', { class: `li ${r.type}` }, el('div', { class: 't', text: fmt.time(r.t) }), el('div', {}, el('div', { class: 'who' }, el('i', { style: { background: AGENT_COLORS[wave] } }), `${who}${to}`, ' ', el('span', { class: 'muted', style: { fontWeight: 400 }, text: r.type })), el('div', { class: 'tx' }, r.text, r.url && (full || r.type === 'open') ? el('span', {}, ' ', el('a', { href: r.url, target: '_blank', rel: 'noopener', text: fmt.domain(r.url) })) : '', r.event_id && state.evIndex.has(r.event_id) ? el('span', {}, ' ', evLink(r.event_id, '↗')) : '')));
  }
  renderCounters() {
    const c = this.counts; this.counters.replaceChildren(...[['Searches', c.search], ['Pages opened', c.open], ['Events extracted', c.found], ['Signs raised', c.flag], ['Messages', c.message]].map(([l, v]) => el('div', { class: 'c' }, el('div', { class: 'v', text: String(v) }), el('div', { class: 'l', text: l }))));
  }
  updateClock() { const t = this.t0 + this.vt; this.clock.textContent = this.log.length ? `${new Date(t).toISOString().slice(11, 19)} UTC · ${this.i}/${this.log.length}` : 'no log'; this.scrub.value = Math.round(1000 * this.vt / Math.max(1, this.t1 - this.t0)); }
  setStatus(id, text, cls) { const d = this.desks[id]; if (!d) return; d.select('text.st').text(text.length > 18 ? text.slice(0, 17) + '…' : text); d.attr('class', `desk ${cls || ''}`); }
  updateDesk(id) { const d = this.desks[id], st = this.state[id]; if (!d || !st) return; d.select('text.cnt').text(st.events ? `${st.events} ev` : ''); const fb = d.select('g.flagbadge'); fb.style('display', st.flags ? null : 'none'); fb.select('text').text(st.flags > 9 ? '9+' : String(st.flags)); }
  apply(r, animate) {
    const id = r.agent; const st = this.state[id] || (this.state[id] = { status: 'idle', searches: 0, pages: 0, events: 0, flags: 0, lastFloat: 0 });
    this.counts[r.type] = (this.counts[r.type] || 0) + (['search', 'open', 'found', 'flag', 'message'].includes(r.type) ? 1 : 0);
    switch (r.type) {
      case 'dispatch': this.setStatus(r.to, 'briefed', 'working'); if (animate) this.sendDot('orchestrator', r.to); break;
      case 'search': st.searches++; this.setStatus(id, 'searching', 'working'); break;
      case 'open': st.pages++; this.setStatus(id, `reading ${fmt.domain(r.url || '')}`, 'working'); break;
      case 'found': st.events++; this.setStatus(id, r.new === false ? 'confirming' : 'new event', 'working'); this.updateDesk(id); if (animate) this.floatTag(id, r.new === false ? 'CONFIRMS' : 'NEW', r.new === false ? 'conf' : 'new'); break;
      case 'verify': this.setStatus(id, 'cross-checking', 'working'); break;
      case 'note': this.setStatus(id, 'noting', 'working'); break;
      case 'flag': st.flags++; this.setStatus(id, 'sign raised', 'working'); this.updateDesk(id); this.raiseSign(id, r, animate); this.flagsList.prepend(el('div', { class: 'f' }, el('div', { class: 'who', text: `${this.agents[id]?.name || id} · ${fmt.time(r.t)}` }), el('div', {}, r.text, r.event_id && state.evIndex.has(r.event_id) ? el('span', {}, ' ', evLink(r.event_id, '↗')) : ''))); while (this.flagsList.children.length > 60) this.flagsList.lastChild.remove(); break;
      case 'message': this.setStatus(id, `msg → ${shortName(this.agents[r.to]?.name || r.to || '', r.to)}`, 'working'); if (animate && r.to) this.sendDot(id, r.to); break;
      case 'done': this.setStatus(id, 'done', 'done'); break;
    }
    this.feed.append(this.feedRow(r)); while (this.feed.children.length > 300) this.feed.firstChild.remove(); this.feed.scrollTop = this.feed.scrollHeight;
  }
  center(id) { const p = this.L.pos[id]; if (!p) return null; return { x: p.x + p.w / 2, y: p.y + p.h / 2 }; }
  sendDot(from, to) {
    const a = this.center(from), b = this.center(to); if (!a || !b) return;
    const mid = { x: (a.x + b.x) / 2, y: Math.min(a.y, b.y) - 30 };
    const path = this.msgLayer.append('path').attr('class', 'msgline').attr('d', `M${a.x},${a.y} Q${mid.x},${mid.y} ${b.x},${b.y}`);
    const env = this.msgLayer.append('g').attr('class', 'msgenv'); env.append('rect').attr('x', -6).attr('y', -4).attr('width', 12).attr('height', 8).attr('rx', 1.5); env.append('path').attr('d', 'M-6,-4 L0,1 L6,-4');
    const node = path.node(), len = node.getTotalLength();
    env.transition().duration(1000).ease(d3.easeCubicInOut).attrTween('transform', () => t => { const p = node.getPointAtLength(t * len); return `translate(${p.x},${p.y})`; }).on('end', () => { env.remove(); path.transition().duration(500).style('opacity', 0).remove(); });
  }
  floatTag(id, text, cls) {
    const p = this.L.pos[id]; if (!p) return; const st = this.state[id]; const now = performance.now(); if (now - (st.lastFloat || 0) < 450) return; st.lastFloat = now;
    const t = this.floatLayer.append('text').attr('class', `float ${cls}`).attr('x', p.x + 34).attr('y', p.y + 2).attr('text-anchor', 'middle').text(text).style('opacity', 0);
    t.transition().duration(180).style('opacity', 1).attr('y', p.y - 6).transition().delay(450).duration(450).style('opacity', 0).attr('y', p.y - 18).remove();
  }
  raiseSign(id, r, animate) {
    const p = this.L.pos[id]; if (!p) return; const d = this.desks[id];
    d.select('g.arm').transition().duration(280).attr('transform', 'translate(10,35) rotate(165)');
    const label = (r.text || '').replace(/\s+/g, ' ').trim();
    const per = 17, lines = []; for (let i = 0; i < 3; i++) lines.push(label.slice(i * per, (i + 1) * per)); if (label.length > per * 3) lines[2] = lines[2].slice(0, per - 1) + '…';
    const used = lines.filter(Boolean), h = 10 + used.length * 11.5, w = p.w, hx = 34;
    const g = this.flagLayer.append('g').attr('class', 'flagpin').attr('transform', `translate(${p.x},${p.y + 10})`).style('opacity', 0);
    g.append('line').attr('class', 'stick').attr('x1', hx).attr('y1', 0).attr('x2', hx).attr('y2', -8);
    g.append('rect').attr('class', 'board').attr('x', 0).attr('y', -8 - h).attr('width', w).attr('height', h).attr('rx', 4);
    g.append('circle').attr('class', 'bang').attr('cx', 11).attr('cy', -8 - h + 12).attr('r', 6.5);
    g.append('text').attr('class', 'bangt').attr('x', 11).attr('y', -8 - h + 12).attr('text-anchor', 'middle').attr('dy', '0.36em').text('!');
    used.forEach((ln, i) => g.append('text').attr('class', 't').attr('x', i === 0 ? 22 : 8).attr('y', -8 - h + 14 + i * 11.5).text(ln));
    g.transition().duration(200).style('opacity', 1);
    const hold = animate ? 4200 : 900;
    g.transition().delay(hold).duration(500).style('opacity', 0).remove().on('end', () => { d.select('g.arm').transition().duration(250).attr('transform', 'translate(10,35) rotate(-30)'); });
  }
  toggle() { this.playing ? this.pause() : this.play(); }
  play() { if (!this.log.length) return; if (this.i >= this.log.length && !this.live) this.reset(); this.playing = true; this.playBtn.textContent = 'Pause'; this.lastReal = performance.now(); this.tick(); }
  pause() { this.playing = false; this.playBtn.textContent = 'Play'; if (this.raf) cancelAnimationFrame(this.raf); }
  reset() { this.i = 0; this.vt = 0; this.counts = { search: 0, open: 0, found: 0, flag: 0, message: 0 }; this.feed.replaceChildren(); this.flagsList.replaceChildren(); this.msgLayer.selectAll('*').interrupt().remove(); this.flagLayer.selectAll('*').interrupt().remove(); this.floatLayer.selectAll('*').interrupt().remove(); for (const id of Object.keys(this.desks)) { this.setStatus(id, 'idle', ''); this.state[id] = { status: 'idle', searches: 0, pages: 0, events: 0, flags: 0, lastFloat: 0 }; this.desks[id].select('g.arm').interrupt().attr('transform', 'translate(10,35) rotate(-30)'); this.updateDesk(id); } this.renderCounters(); this.updateClock(); }
  tick() {
    if (!this.playing) return;
    const now = performance.now(); const dReal = now - this.lastReal; this.lastReal = now;
    const span = Math.max(1, this.t1 - this.t0); const rate = this.speed ? span / (this.speed * 1000) : 1;
    this.vt += dReal * rate;
    let n = 0;
    while (this.i < this.log.length && Date.parse(this.log[this.i].t) - this.t0 <= this.vt && n < 40) { this.apply(this.log[this.i], true); this.i++; n++; }
    if (n) this.renderCounters();
    this.updateClock();
    if (this.i >= this.log.length && !this.live) { this.vt = span; this.updateClock(); this.pause(); this.playBtn.textContent = 'Replay'; return; }
    this.raf = requestAnimationFrame(() => this.tick());
  }
  seek(frac) {
    const target = frac * (this.t1 - this.t0); const wasPlaying = this.playing; this.pause();
    if (target < this.vt) this.reset();
    while (this.i < this.log.length && Date.parse(this.log[this.i].t) - this.t0 <= target) { this.apply(this.log[this.i], false); this.i++; }
    this.vt = target; this.renderCounters(); this.updateClock(); if (wasPlaying) this.play();
  }
  toggleLive() {
    this.live = !this.live; this.liveBtn.classList.toggle('on', this.live);
    if (this.live) { this.seek(1); this.speed = 0; this.pollTimer = setInterval(() => this.poll(), 15000); this.play(); }
    else { clearInterval(this.pollTimer); this.pollTimer = null; }
  }
  async poll() {
    try { const r = await fetch('data/agent_log.json', { cache: 'no-store' }); if (!r.ok) return; const d = await r.json(); if ((d.log || []).length > this.log.length) { const fresh = d.log.slice(this.log.length); this.log = d.log; this.agents = d.agents || this.agents; this.t1 = Date.parse(this.log[this.log.length - 1].t); for (const id of Object.keys(this.agents)) if (!this.desks[id]) { /* new agent: rebuild floor */ this.build(); this.seek(1); return; } this.renderRoster(); } } catch {}
  }
  onShow() { /* nothing; replay is user-initiated */ }
}
function initials(n) { return (n || '?').replace(/[·—-]/g, ' ').split(/\s+/).filter(Boolean).slice(0, 2).map(w => w[0]).join('').toUpperCase(); }
const SHORT = {
  'scout-2021-2022': 'Scout 2021–22', 'scout-2023': 'Scout 2023', 'scout-2024': 'Scout 2024', 'scout-2025h1': 'Scout 2025 H1', 'scout-2025h2': 'Scout 2025 H2', 'scout-2026q1': 'Scout 2026 Q1', 'scout-2026q2': 'Scout 2026 Q2', 'scout-2026q3': 'Scout 2026 Q3',
  'desk-deals': 'Deal Desk', 'desk-compute': 'Compute Desk', 'desk-product': 'Product Desk', 'desk-revenue': 'Revenue Desk', 'desk-governance': 'Governance', 'desk-legal': 'Legal & Reg.', 'desk-ecosystem': 'Ecosystem', 'desk-s1': 'Prospectus',
  'verify-capital': 'Re-derive Cap.', 'verify-operating': 'Re-derive Ops', 'verify-prospectus': 'Re-derive Prosp.', 'verify-compute': 'Re-derive Comp.', 'verify-audit-1': 'Auditor 1', 'verify-audit-2': 'Auditor 2',
  'analyst-topic-capital': 'Capital Analyst', 'analyst-topic-revenue': 'Revenue Analyst', 'analyst-topic-compute': 'Compute Analyst', 'analyst-topic-product': 'Product Analyst', 'analyst-topic-moat': 'Moat Analyst',
  'analyst-topic-governance': 'Gov. Analyst', 'analyst-topic-legal': 'Legal Analyst', 'analyst-topic-government': 'Policy Analyst', 'analyst-topic-people': 'People Analyst', 'analyst-topic-ecosystem': 'Ecosys. Analyst',
  'analyst-model': 'Modeler', 'analyst-compute': 'Compute Econ.', 'analyst-bull': 'Bull Analyst', 'analyst-bear': 'Bear Analyst', 'analyst-judge': 'Judge', 'certifier': 'Certifier', 'orchestrator': 'Orchestrator' };
function shortName(n, id) { if (id && SHORT[id]) return SHORT[id]; const s = (n || '').replace('Timeline Scout · ', 'Scout ').replace('Source Re-deriver · ', 'Re-derive ').replace('Analyst · ', 'Analyst ').replace(' Desk', '').replace(' & People', '').replace(' & Regulatory', ''); return s.length > 16 ? s.slice(0, 15) + '…' : s; }
function renderAgents(root) {
  root.replaceChildren();
  const A = state.data.agent_log;
  if (!A?.log?.length) { root.append(el('div', { class: 'empty', text: 'No agent log yet.' })); return; }
  root.append(el('p', { class: 'ink2', style: { marginBottom: '10px' }, text: `${Object.keys(A.agents).length} agents · ${A.log.length.toLocaleString()} logged actions · session ${fmt.date(A.log[0].t.slice(0, 10))} ${fmt.time(A.log[0].t)}–${fmt.time(A.log[A.log.length - 1].t)} UTC. Press Play to replay the desks as they worked. A raised sign is an agent flagging new or conflicting information. NEW means it was the first desk to file that event; CONFIRMS means it corroborated an event another desk had already filed. An envelope is a message between desks. Start and finish times are each agent's own clock readings; actions inside a run are spread evenly between them.` }));
  const host = el('div', { tabindex: '0' }); root.append(host);
  state.floor = new Floor(host, A);
}

/* ---------------- SOURCES & LEDGER ---------------- */
function moreTable(headers, rows, mapRow, limit) {
  const tbody = el('tbody'); let shown = 0;
  const btn = el('button', { class: 'btn showmore', type: 'button' }); btn.addEventListener('click', () => draw(rows.length));
  const draw = n => { const f = document.createDocumentFragment(); rows.slice(shown, n).forEach(r => f.append(mapRow(r))); tbody.append(f); shown = Math.min(n, rows.length); btn.hidden = shown >= rows.length; btn.textContent = `Show all ${rows.length} (${shown} shown)`; };
  draw(limit || 15);
  return el('div', {}, el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, ...headers.map(h => el('th', { text: h })))), tbody)), btn);
}
function compactJson(v) {
  let o = v; if (typeof v === 'string') { try { o = JSON.parse(v); } catch { return v; } }
  if (!o || typeof o !== 'object') return String(o ?? '');
  return Object.entries(o).filter(([, x]) => x != null && x !== '').map(([k, x]) => `${k.replace(/_usd_m$/, '').replace(/_/g, ' ')} ${/_usd_m$/.test(k) && typeof x === 'number' ? fmt.usd(x) : Array.isArray(x) ? x.join('/') : x}`).join(' · ');
}
function renderSources(root) {
  root.replaceChildren();
  const L = state.data.ledger, E = state.data.events || [];
  if (!L) { root.append(el('div', { class: 'empty', text: 'Ledger not generated yet.' })); return; }
  const g = el('div', { class: 'grid cols-3' });
  const bars = (title, obj, order, color) => { const c = el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: title }))); const tot = Object.values(obj).reduce((a, b) => a + b, 0) || 1; (order || Object.keys(obj)).filter(k => obj[k]).forEach(k => c.append(el('div', { class: 'bar-row' }, el('span', { class: 'mono small', text: k }), el('div', { class: 'b' }, el('i', { style: { width: `${100 * obj[k] / tot}%`, background: color } })), el('span', { class: 'num mono small', text: String(obj[k]) })))); return c; };
  g.append(bars('Source tier of primary citation', L.tiers, ['T1', 'T2', 'T3', 'T4', 'T5'], 'var(--s1)'), bars('Confidence', L.confidence, ['CANONICAL', 'HIGH', 'MEDIUM', 'LOW', 'VERIFY', 'DISPUTED'], 'var(--s3)'), bars('Events by year', L.years, null, 'var(--s2)'));
  root.append(g);
  const kt = (l, v, s) => el('div', { class: 'tile' }, el('div', { class: 'label', text: l }), el('div', { class: 'value', text: v }), el('div', { class: 'sub', text: s || '' }));
  root.append(el('div', { class: 'grid cols-4 section' }, kt('Raw findings', fmt.num(L.raw_events), 'before dedupe'), kt('Merged events', fmt.num(L.merged_events), 'in the record'), kt('Pages opened', fmt.pct(L.opened_share, 1), 'primary source actually opened'), kt('Multi-outlet events', fmt.num(E.filter(e => (e.distinct_outlets || e.independent_sources || 1) >= 2).length), `two or more distinct outlets; ${fmt.num(E.filter(e => e.single_chain_suspected).length)} likely one reporting chain`)));
  const AU = state.data.audit, HL = state.data.health;
  if (AU?.n) root.append(el('div', { class: 'grid cols-2 section' },
    el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'Independent audit of the record' }), el('span', { class: 'small muted', text: `${AU.n} events re-checked cold by separate agents` })),
      el('div', { class: 'hero', text: fmt.pct(AU.supported_share) }), el('div', { class: 'small muted', text: `of ${AU.opened} opened sources fully support the summary and figures; ${fmt.pct(AU.supported_or_partly_share)} support the core fact; ${AU.unopenable} could not be opened.` }),
      el('div', { style: { marginTop: '10px' } }, ...Object.entries(AU.verdicts || {}).map(([k, v]) => el('div', { class: 'bar-row' }, el('span', { class: 'mono small', text: k }), el('div', { class: 'b' }, el('i', { style: { width: `${100 * v / AU.n}%`, background: k === 'SUPPORTED' ? 'var(--s3)' : k === 'PARTLY' ? 'var(--s4)' : 'var(--s8)' } })), el('span', { class: 'num mono small', text: String(v) }))))),
    el('div', { class: 'card' }, el('div', { class: 'card-h' }, el('h3', { text: 'What the auditors found wrong' }), el('span', { class: 'small muted', text: 'kept in the open' })),
      el('div', { class: 'flags-list' }, ...((AU.problems || []).slice(0, 12).map(p => el('div', { class: 'f' }, el('div', { class: 'who', text: `${p.verdict} · ${p.tier} · ${p.category}` }), el('div', {}, `${p.headline} — ${p.note || ''}`, p.event_id && state.evIndex.has(p.event_id) ? el('span', {}, ' ', evLink(p.event_id, '↗')) : '')))), ...((AU.problems || []).length ? [] : [el('div', { class: 'empty', text: 'No problems recorded.' })])))));
  if (L.corrections?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: `Corrections applied after the audit (${L.corrections.length})` }), el('span', { class: 'small muted', text: 'unsupported figures removed or relabelled; no facts added; agent outputs untouched' })),
    moreTable(['Event', 'Audit item', 'Fields changed', 'Why'], L.corrections, c => el('tr', {}, el('td', {}, state.evIndex.has(c.event_id) ? evLink(c.event_id, c.headline) : c.headline), el('td', { class: 'mono small', text: c.audit_id || '' }), el('td', { class: 'mono small', text: (c.changed || []).map(x => x.replace('extracted.', '')).join(', ') }), el('td', { class: 'small', text: c.reason || '' })), 8)));
  const CT = state.data.certify;
  if (CT?.gates?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Ship gates' }), el('span', { class: 'small muted', text: `${CT.summary.PASS} pass · ${CT.summary.WARN} warn · ${CT.summary.FAIL} fail · ${CT.summary.PENDING} pending · ${fmt.date(CT.generated.slice(0, 10))} ${fmt.time(CT.generated)} UTC` })),
    el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Gate' }), el('th', { text: 'Status' }), el('th', { text: 'Detail' }))),
      el('tbody', {}, ...CT.gates.map(g => el('tr', {}, el('td', { text: `${g.id} · ${g.name}` }), el('td', {}, el('span', { class: 'chip ' + ({ PASS: 'ok', WARN: 'warn', FAIL: 'bad', PENDING: '' }[g.status] || ''), text: g.status })), el('td', { class: 'small', text: g.detail }))))))));
  if (HL) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Mechanical checks on the record' }), el('span', { class: 'small muted', text: `${HL.fails} fails · ${HL.warns} warnings` })),
    el('div', { class: 'tablewrap' }, el('table', { class: 'data' }, el('thead', {}, el('tr', {}, el('th', { text: 'Check' }), el('th', { class: 'num', text: 'Count' }), el('th', { text: 'Result' }))), el('tbody', {}, ...HL.checks.map(c => el('tr', {}, el('td', { text: c.check }), el('td', { class: 'num', text: String(c.count) }), el('td', {}, chip(c.severity, c.severity === 'OK' ? 'conf HIGH' : c.severity === 'FAIL' ? 'conf DISPUTED' : c.severity === 'WARN' ? 'conf LOW' : 'conf MEDIUM')))))))));
  if (L.claims?.length) {
    const VC = { MATCH: 'ok', PARTIAL: 'warn', NOTED: '', MISMATCH: 'bad', UNTRACEABLE: 'bad' }, cs = L.claims_summary || {};
    root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: `Re-derivation ledger (${L.claims.length} load-bearing claims)` }), el('span', { class: 'small muted', text: `re-derived from source by agents that never saw the draft · ${cs.MATCH ?? 0} match · ${cs.PARTIAL ?? 0} partial · ${cs.NOTED ?? 0} noted (text, side by side) · ${cs.MISMATCH ?? 0} mismatch (frozen) · ${cs.UNTRACEABLE ?? 0} untraceable` })),
      moreTable(['Claim', 'Draft', 'Re-derived', 'Verdict', 'Tier', 'Origins', 'Confidence', 'Note'], L.claims, c => el('tr', {},
        el('td', {}, c.event_id && state.evIndex.has(c.event_id) ? evLink(c.event_id, c.claim) : c.claim), el('td', { class: 'mono small', text: compactJson(c.draft) }),
        el('td', { class: 'mono small' }, compactJson(c.rederived_obj || c.rederived), ...(c.sources || []).slice(0, 2).map(u => el('span', {}, ' ', el('a', { href: u, target: '_blank', rel: 'noopener', text: fmt.domain(u) })))),
        el('td', {}, el('span', { class: 'chip ' + (VC[c.verdict] || ''), text: c.verdict })), el('td', {}, tierChip(c.tier || 'T4')), el('td', { class: 'num', text: String(c.cross_check ?? '') }), el('td', {}, confChip(c.confidence || 'MEDIUM')), el('td', { class: 'small', text: c.red_team || '' })), 20)));
  }
  const conf = [...(L.cross_agent_conflicts || []), ...(L.agent_conflicts || [])];
  if (conf.length) {
    const lk = u => /^https?:/.test(u || '') ? el('a', { href: u, target: '_blank', rel: 'noopener', text: fmt.domain(u) }) : '';
    root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: `Frozen conflicts (${conf.length})` }), el('span', { class: 'small muted', text: 'both values shown, neither chosen' })),
      moreTable(['Topic', 'Value A', 'Value B', 'Note', 'Raised by'], conf, c => el('tr', {}, el('td', { text: c.topic }), el('td', { class: 'small' }, String(c.value_a ?? ''), ' ', lk(c.source_a)), el('td', { class: 'small' }, String(c.value_b ?? ''), ' ', lk(c.source_b)), el('td', { class: 'small', text: c.note || '' }), el('td', { class: 'mono small', text: c.agent || 'merge' })), 10)));
  }
  if (L.open_items?.length) root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: `Open items (${L.open_items.length})` }), el('span', { class: 'small muted', text: 'ships only with the flag visible' })),
    moreTable(['Claim', 'Why unverified', 'Best lead', 'Agent'], L.open_items, o => el('tr', {}, el('td', { text: o.claim }), el('td', { class: 'small', text: o.why_unverified || '' }), el('td', { class: 'small' }, /^https?:/.test(o.best_lead || '') ? el('a', { href: o.best_lead, target: '_blank', rel: 'noopener', text: fmt.domain(o.best_lead) }) : (o.best_lead || '')), el('td', { class: 'mono small', text: o.agent || '' })), 10)));
  root.append(el('div', { class: 'card section' }, el('div', { class: 'card-h' }, el('h3', { text: 'Method and disclosures' })),
    el('div', { class: 'small ink2' }, ...(L.method || [
      'Tier ladder: T1 primary documents (filings, dockets, anthropic.com, partner releases) · T2 Bloomberg/Reuters/WSJ/FT/CNBC and PitchBook fields · T3 single-outlet scoops and PitchBook notes · T4 aggregators · T5 social. An event inherits the tier of its weakest load-bearing source.',
      'Freeze-on-conflict: sources that disagree by more than 10% at comparable tiers are shown as DISPUTED with both values; the desk never picks silently.',
      'Basis discipline: Anthropic reports revenue gross of cloud-partner resale; comparables on a net basis are equalized with a stated haircut, never compared raw. PitchBook TTM revenue fields are forward projections, not current run-rate.',
      'Inputs: public web sources (company posts, filings, dockets, press) and licensed PitchBook Premium content (round sizes, valuations, investors, team data, analyst notes). The PitchBook content is not public: check your licence before sharing this page or its data files.',
      'MNPI screen: the S-1 is confidential. Any figure attributed to a leaked or reported prospectus is press-reported (T2/T3), not confirmed by the company, and is labelled as such where it appears. Nothing here was obtained from an insider. Run your compliance review before acting on reported-prospectus figures.',
      'Conflict of interest: the desk\'s model portfolio (project context dated Feb 27 2026; re-verify before relying on it) is overweight Anthropic (6%) and underweight OpenAI (2%). The analysis does not treat that position as evidence. This page is decision support, not investment advice.',
      'Tools: PitchBook Premium, web page fetches and news-feed queries were the live sources. Bigdata.com was not used (subscription paused in the desk\'s tool registry).',
    ]).map(p => el('p', { text: p, style: { marginBottom: '6px' } })))));
}

/* ---------------- boot ---------------- */
const RENDER = { overview: renderOverview, timeline: renderTimeline, topics: renderTopics, model: renderModel, compute: renderCompute, thesis: renderThesis, network: renderNetwork, agents: renderAgents, sources: renderSources };
async function boot() {
  initTheme(); renderNav();
  $('#drawerClose').addEventListener('click', closeDrawer); $('#scrim').addEventListener('click', closeDrawer);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDrawer(); });
  window.addEventListener('hashchange', () => showTab(location.hash.slice(1) || 'overview'));
  try {
    const missing = await loadAll();
    $('#loading').hidden = true;
    const os = state.data.metrics?.offering_structure || {};
    const pill = $('#ipoPill'); pill.replaceChildren(el('span', { class: 'dot' }), el('span', { text: `Private · S-1 confidential (Jun 1 2026) · ${/dispute/i.test(os.timing || '') ? 'listing timing disputed: Oct, then Nov or after the midterms' : (os.timing ? String(os.timing).split(/[·;.]/)[0].trim().slice(0, 48) : 'listing timing per record')}` }));
    const gen = state.data.ledger?.generated || state.data.agent_log?.generated; $('#asof').textContent = `record as of ${gen ? fmt.date(gen.slice(0, 10)) + ' ' + fmt.time(gen) + ' UTC' : '—'}`;
    const E = state.data.events || []; $('#railStats').textContent = `${E.length.toLocaleString()} events · ${E.filter(e => e.source.tier === 'T1').length} primary · ${E.filter(e => e.confidence === 'DISPUTED').length} disputed`;
    if (missing.length) { const w = $('#loadError'); w.hidden = false; w.textContent = `Some data files are missing (${missing.join(', ')}); those desks show an empty state.`; }
    showTab(location.hash.slice(1) || 'overview');
  } catch (e) { $('#loading').hidden = true; const w = $('#loadError'); w.hidden = false; w.textContent = String(e.message || e); }
}
boot();
})();
