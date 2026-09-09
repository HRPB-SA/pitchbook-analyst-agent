// Build entry-fee-v5.docx from entry-fee-v5.md using the docx npm package (run from report/build/).
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, PageBreak, TableOfContents, Footer, Header, PageNumber, LevelFormat, BorderStyle,
  TableLayoutType, VerticalAlign,
} = require('docx');

const MD = path.resolve(__dirname, '..', 'entry-fee-v5.md');
const OUT = path.resolve(__dirname, '..', 'entry-fee-v5.docx');
const FONT = 'Arial';
const TEXT_WIDTH = 9360; // 6.5in
const PL_WIDTHS = [1600, 850, 850, 850, 1000, 1000, 1000, 1000, 1210];

const src = fs.readFileSync(MD, 'utf8');
if (/[–—]/.test(src)) { throw new Error('em/en dash found in source'); }
const lines = src.split('\n');

// ---------- inline parsing (**bold** only) ----------
function runs(text, opts = {}) {
  const out = [];
  const parts = text.split('**');
  parts.forEach((p, i) => {
    if (!p) return;
    out.push(new TextRun({ text: p, bold: i % 2 === 1 ? true : (opts.bold || false), italics: opts.italics || false,
      size: opts.size || 21, font: FONT, color: opts.color }));
  });
  return out;
}
function para(text, o = {}) {
  return new Paragraph({ children: runs(text, o), alignment: o.align || AlignmentType.LEFT,
    spacing: { after: o.after == null ? 140 : o.after, before: o.before || 0, line: o.line || 276 }, keepNext: o.keepNext || false });
}

// ---------- table widths ----------
function colWidths(rows) {
  const n = rows[0].length;
  const isYearTable = n === 9 && rows[0].slice(1).every(h => /^20\d\d[AE]$/.test(h.trim()));
  if (isYearTable) return PL_WIDTHS.slice(); // P&L-style layer x year tables use the mandated widths
  const w = new Array(n).fill(0);
  rows.forEach(r => r.forEach((c, i) => { w[i] = Math.max(w[i], Math.min(c.length, 40)); }));
  const weights = w.map((x, i) => Math.max(x, 8) * (i === 0 ? 1.1 : 1));
  const total = weights.reduce((a, b) => a + b, 0);
  let widths = weights.map(x => Math.max(900, Math.round(TEXT_WIDTH * x / total)));
  let sum = widths.reduce((a, b) => a + b, 0);
  // rebalance to exactly TEXT_WIDTH
  const scale = TEXT_WIDTH / sum;
  widths = widths.map(x => Math.round(x * scale));
  sum = widths.reduce((a, b) => a + b, 0);
  widths[widths.length - 1] += TEXT_WIDTH - sum;
  return widths;
}
function makeTable(rows) {
  const widths = colWidths(rows);
  const n = widths.length;
  const fsz = n >= 7 ? 15 : (n >= 5 ? 16 : 18); // half-points: 7.5 / 8 / 9 pt
  const border = { style: BorderStyle.SINGLE, size: 4, color: 'A6A6A6' };
  const trows = rows.map((cells, ri) => {
    const c = cells.slice(0, n);
    while (c.length < n) c.push('');
    if (cells.length !== n) console.warn('row cell count fixed:', cells.length, '->', n, '|', cells[0].slice(0, 40));
    const isHeader = ri === 0;
    const isPanel = /^Panel \d/.test(c[0]);
    return new TableRow({ tableHeader: isHeader, cantSplit: true, children: c.map((txt, ci) => new TableCell({
      width: { size: widths[ci], type: WidthType.DXA },
      shading: isHeader ? { fill: 'D9E2F3', type: ShadingType.CLEAR, color: 'auto' } : (isPanel ? { fill: 'F2F2F2', type: ShadingType.CLEAR, color: 'auto' } : undefined),
      margins: { top: 40, bottom: 40, left: 60, right: 60 },
      verticalAlign: VerticalAlign.TOP,
      borders: { top: border, bottom: border, left: border, right: border },
      children: [new Paragraph({ children: runs(txt, { size: fsz, bold: isHeader || isPanel }), spacing: { after: 0, line: 240 } })],
    })) });
  });
  return new Table({ width: { size: TEXT_WIDTH, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows: trows });
}
function parseRow(l) {
  let s = l.trim();
  if (s.startsWith('|')) s = s.slice(1);
  if (s.endsWith('|')) s = s.slice(0, -1);
  return s.split('|').map(x => x.trim());
}
function boxTable(text) {
  const border = { style: BorderStyle.SINGLE, size: 8, color: '1F3864' };
  return new Table({ width: { size: TEXT_WIDTH, type: WidthType.DXA }, columnWidths: [TEXT_WIDTH], layout: TableLayoutType.FIXED, rows: [
    new TableRow({ children: [new TableCell({ width: { size: TEXT_WIDTH, type: WidthType.DXA },
      shading: { fill: 'EDF1F7', type: ShadingType.CLEAR, color: 'auto' }, margins: { top: 120, bottom: 120, left: 160, right: 160 },
      borders: { top: border, bottom: border, left: border, right: border },
      children: [new Paragraph({ children: runs(text, { size: 18 }), spacing: { after: 0, line: 260 } })] })] }) ] });
}

// ---------- parse document ----------
const children = [];
let i = 0;
// cover block: up to first <<<PAGEBREAK>>>
const cover = [];
while (i < lines.length && lines[i].trim() !== '<<<PAGEBREAK>>>') { if (lines[i].trim()) cover.push(lines[i].trim()); i++; }
i++; // skip pagebreak marker
const title = cover[0].replace(/^#\s*/, '');
const subtitle = cover[1].replace(/^##\s*/, '');
children.push(new Paragraph({ spacing: { before: 2400, after: 200 }, children: [new TextRun({ text: 'PitchBook', font: FONT, size: 24, bold: true, color: '1F3864' })] }));
children.push(new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: title, font: FONT, size: 52, bold: true, color: '1F3864' })] }));
children.push(new Paragraph({ spacing: { after: 600 }, children: [new TextRun({ text: subtitle, font: FONT, size: 30, color: '404040' })] }));
cover.slice(2).forEach(l => children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: l, font: FONT, size: 22 })] })));
children.push(new Paragraph({ spacing: { before: 600 }, children: [new TextRun({ text: 'Anthropic and OpenAI on the 5-Layer Cost Stack, 2023A-2030E, with a greenfield entry-cost section. Institutional research; figures carry ledger row references (L-xxx) and tiers throughout.', font: FONT, size: 18, italics: true, color: '595959' })] }));
children.push(new Paragraph({ children: [new PageBreak()] }));
// TOC
children.push(new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: 'Contents', font: FONT, size: 30, bold: true, color: '1F3864' })] }));
children.push(new TableOfContents('Contents', { hyperlink: true, headingStyleRange: '1-1' }));
children.push(new Paragraph({ children: [new PageBreak()] }));

let listId = 0;
while (i < lines.length) {
  const raw = lines[i]; const s = raw.trim();
  if (!s) { i++; continue; }
  if (s === '<<<PAGEBREAK>>>') { children.push(new Paragraph({ children: [new PageBreak()] })); i++; continue; }
  if (s.startsWith('## ')) { children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 160 }, children: [new TextRun({ text: s.slice(3), font: FONT })] })); i++; continue; }
  if (s.startsWith('### ')) { children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: s.slice(4), font: FONT })] })); i++; continue; }
  if (s.startsWith(':::box')) {
    const buf = []; i++;
    while (i < lines.length && lines[i].trim() !== ':::') { buf.push(lines[i].trim()); i++; }
    i++; children.push(boxTable(buf.join(' '))); children.push(para('', { after: 120 })); continue;
  }
  if (s.startsWith('|')) {
    const rows = [];
    while (i < lines.length && lines[i].trim().startsWith('|')) {
      const r = parseRow(lines[i]);
      if (!r.every(c => /^:?-{2,}:?$/.test(c))) rows.push(r);
      i++;
    }
    children.push(makeTable(rows));
    children.push(para('', { after: 60 }));
    continue;
  }
  if (/^\*\*Exhibit /.test(s) || (/^\*\*.+\*\*$/.test(s))) {
    children.push(new Paragraph({ children: runs(s, { size: 20, color: '1F3864' }), keepNext: true, spacing: { before: 200, after: 80 } })); i++; continue;
  }
  if (s.startsWith('Note:') || s.startsWith('Footnote ')) { children.push(para(s, { size: 17, italics: true, after: 160, color: '404040' })); i++; continue; }
  if (s.startsWith('- ')) {
    children.push(new Paragraph({ numbering: { reference: 'bullets', level: 0 }, children: runs(s.slice(2)), spacing: { after: 100, line: 276 } })); i++; continue;
  }
  if (/^\d+\.\s/.test(s)) {
    // start a fresh numbered list when the previous line was not numbered
    const prev = i > 0 ? lines[i - 1].trim() : '';
    if (!/^\d+\.\s/.test(prev)) listId++;
    children.push(new Paragraph({ numbering: { reference: 'numbers' + Math.min(listId, 6), level: 0 }, children: runs(s.replace(/^\d+\.\s/, '')), spacing: { after: 100, line: 276 } })); i++; continue;
  }
  children.push(para(s)); i++;
}

const headerText = 'The $100 Billion Entry Fee  |  v5.0  |  PitchBook  |  September 9, 2026';
const numberConfigs = [{ reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }];
for (let k = 1; k <= 6; k++) numberConfigs.push({ reference: 'numbers' + k, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] });

const doc = new Document({
  creator: 'Harrison Rolfes, PitchBook', title: 'The $100 Billion Entry Fee', description: 'v5.0, September 9, 2026',
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 30, bold: true, font: FONT, color: '1F3864' }, paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0, keepNext: true } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 24, bold: true, font: FONT, color: '1F3864' }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1, keepNext: true } },
    ],
  },
  numbering: { config: numberConfigs },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: headerText, size: 15, color: '7F7F7F', font: FONT })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'Page ', size: 16, font: FONT, color: '7F7F7F' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, font: FONT, color: '7F7F7F' })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log('wrote', OUT, buf.length, 'bytes; paragraphs/tables:', children.length); });
