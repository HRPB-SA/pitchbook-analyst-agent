/* CONTEXT: ANTHROPIC INTELLIGENCE DESK — headless QA: serves the repo, opens every tab at desktop and phone
   widths in light and dark, records console errors, saves screenshots. Run: NODE_PATH=$(npm root -g) node scripts/shot.cjs [outdir] */
const { chromium } = require('playwright');
const http = require('http'); const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..'); const OUT = process.argv[2] || path.join(ROOT, 'dist', 'qa'); fs.mkdirSync(OUT, { recursive: true });
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.svg': 'image/svg+xml' };
const srv = http.createServer((req, res) => { let p = decodeURIComponent(req.url.split('?')[0].split('#')[0]); if (p === '/') p = '/index.html'; const f = path.join(ROOT, p); fs.readFile(f, (e, d) => { if (e) { res.writeHead(404); return res.end('nf'); } res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' }); res.end(d); }); });
(async () => {
  await new Promise(r => srv.listen(0, r)); const port = srv.address().port;
  const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
  const errors = [];
  const tabs = ['overview', 'timeline', 'topics', 'model', 'compute', 'thesis', 'network', 'agents', 'sources'];
  for (const [w, h, name] of [[1440, 1000, 'desk'], [400, 860, 'phone']]) {
    for (const theme of ['light', 'dark']) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, colorScheme: theme, deviceScaleFactor: 1, ignoreHTTPSErrors: true });
      const page = await ctx.newPage();
      page.on('console', m => { if (m.type() !== 'error') return; const u = (m.location() && m.location().url) || ''; if (/fonts\.(googleapis|gstatic)\.com/.test(u)) return; /* sandbox has no route to Google Fonts; the page falls back to system fonts */ errors.push(`[${name}/${theme}] console: ${m.text()} ${u.replace(/^https?:\/\/[^/]+/, '')}`.trim()); });
      page.on('pageerror', e => errors.push(`[${name}/${theme}] pageerror: ${e.message}`));
      await page.goto(`http://127.0.0.1:${port}/index.html#overview`, { waitUntil: 'networkidle' });
      await page.waitForTimeout(800);
      for (const t of tabs) {
        await page.evaluate(id => { location.hash = '#' + id; }, t); await page.waitForTimeout(t === 'network' ? 1800 : 500);
        if (t === 'agents') { const btn = await page.$('.floor-ctl .btn.primary'); if (btn) { await btn.click(); await page.waitForTimeout(2500); } }
        const sw = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
        if (sw) errors.push(`[${name}/${theme}/${t}] horizontal overflow`);
        if (theme === 'light' || t === 'overview' || t === 'agents') await page.screenshot({ path: path.join(OUT, `${name}-${theme}-${t}.png`), fullPage: name === 'desk' && t !== 'timeline' });
      }
      await ctx.close();
    }
  }
  await browser.close(); srv.close();
  fs.writeFileSync(path.join(OUT, 'errors.txt'), errors.join('\n'));
  console.log(errors.length ? `ERRORS (${errors.length}):\n` + errors.slice(0, 40).join('\n') : 'no console/page errors, no overflow');
})();
