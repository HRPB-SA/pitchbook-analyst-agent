const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, PageNumber, Footer, TabStopType, ShadingType, ImageRun
} = require('docx');

const SRC = process.argv[2] || '/home/user/pitchbook-analyst-agent/templates/q2_2026_report.md';
const OUT = process.argv[3] || '/home/user/pitchbook-analyst-agent/templates/q2_2026_report.docx';
const IMGDIR = '/home/user/pitchbook-analyst-agent/templates/';

const NAVY = '1A2744', INK = '1F2733', SLATE = '55637A', RULE = 'C9D2E0';


const RED = 'C00000';
function bodyRuns(text) {
  const runs = [];
  const parts = text.split('**');
  parts.forEach((seg, i) => {
    if (!seg) return;
    if (i % 2 === 1) runs.push(new TextRun({ text: seg, bold: true, color: RED, size: 21, font: 'Georgia' }));
    else runs.push(new TextRun({ text: seg, size: 21, color: INK, font: 'Georgia' }));
  });
  return runs;
}

const lines = fs.readFileSync(SRC, 'utf8').split('\n');
const blocks = [];
let buf = [];
const flush = () => { if (buf.length) { blocks.push({ t: 'p', text: buf.join(' ').replace(/\s+/g,' ').trim() }); buf = []; } };
for (const raw of lines) {
  const line = raw.replace(/\s+$/,'');
  if (line.startsWith('# '))       { flush(); blocks.push({ t: 'title', text: line.slice(2).trim() }); }
  else if (line.startsWith('## ')) { flush(); blocks.push({ t: 'h1', text: line.slice(3).trim() }); }
  else if (line.startsWith('### ')){ flush(); blocks.push({ t: 'h2', text: line.slice(4).trim() }); }
  else if (line.startsWith('CHART:')) { flush(); blocks.push({ t: 'chart', file: line.slice(6).trim() }); }
  else if (line.startsWith('- ')) { flush(); blocks.push({ t: 'p', text: line.trim() }); }
  else if (line.trim() === '---' || line.trim() === '') { flush(); }
  else buf.push(line.trim());
}
flush();

const children = [];
for (const b of blocks) {
  if (b.t === 'title') {
    children.push(new Paragraph({ spacing: { after: 40 },
      children: [ new TextRun({ text: b.text, bold: true, size: 34, color: NAVY, font: 'Arial' }) ] }));
  } else if (b.t === 'p' && b.text.startsWith('Late-Stage Company Research')) {
    children.push(new Paragraph({ spacing: { after: 200 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: NAVY, space: 8 } },
      children: [ new TextRun({ text: b.text, size: 20, color: SLATE, font: 'Arial' }) ] }));
  } else if (b.t === 'p' && b.text.startsWith('Primary basis:')) {
    children.push(new Paragraph({ spacing: { before: 40, after: 200, line: 264 },
      shading: { type: ShadingType.CLEAR, fill: 'F3F6FB', color: 'auto' },
      border: {
        top: { style: BorderStyle.SINGLE, size: 2, color: RULE, space: 6 },
        bottom: { style: BorderStyle.SINGLE, size: 2, color: RULE, space: 6 },
        left: { style: BorderStyle.SINGLE, size: 2, color: RULE, space: 8 },
        right: { style: BorderStyle.SINGLE, size: 2, color: RULE, space: 8 } },
      children: b.text.split('**').filter(s => s).map((seg, i, arr) =>
        new TextRun({ text: seg, italics: true, size: 18, font: 'Georgia',
          bold: b.text.startsWith('**') ? i % 2 === 0 : i % 2 === 1,
          color: (b.text.startsWith('**') ? i % 2 === 0 : i % 2 === 1) ? RED : SLATE })) }));
  } else if (b.t === 'p' && b.text.startsWith('Source:')) {
    children.push(new Paragraph({ spacing: { before: 360, after: 0 },
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 8 } },
      children: [ new TextRun({ text: b.text, size: 16, italics: true, color: SLATE, font: 'Georgia' }) ] }));
  } else if (b.t === 'h1') {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_1,
      spacing: { before: 320, after: 140 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 6 } },
      children: [ new TextRun({ text: b.text, bold: true, size: 26, color: NAVY, font: 'Arial' }) ] }));
  } else if (b.t === 'h2') {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_2,
      spacing: { before: 220, after: 70 },
      children: [ new TextRun({ text: b.text, bold: true, size: 21, color: NAVY, font: 'Arial' }) ] }));
  } else if (b.t === 'chart') {
    const img = fs.readFileSync(IMGDIR + b.file);
    children.push(new Paragraph({ alignment: AlignmentType.CENTER,
      spacing: { before: 120, after: 160 },
      children: [ new ImageRun({ type: 'png', data: img, transformation: { width: 620, height: 380 } }) ] }));
  } else if (b.t === 'p' && b.text.startsWith('- ')) {
    children.push(new Paragraph({ spacing: { after: 100, line: 276 }, bullet: { level: 0 },
      children: bodyRuns(b.text.slice(2)) }));
  } else if (b.t === 'p') {
    children.push(new Paragraph({ spacing: { after: 160, line: 276 },
      children: bodyRuns(b.text) }));
  }
}

const doc = new Document({
  creator: 'Late-Stage Company Research',
  title: 'Global Unicorn Tracker - Q2 2026',
  styles: { default: { document: { run: { font: 'Georgia', size: 21, color: INK } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: 'Arial', size: 26, bold: true, color: NAVY } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: 'Arial', size: 21, bold: true, color: NAVY } } ] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 },
      margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [ new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 6 } },
      children: [ new TextRun({ text: 'Global Unicorn Tracker  |  Q2 2026', size: 16, color: SLATE, font: 'Arial' }),
                  new TextRun({ text: '\t', size: 16 }),
                  new TextRun({ children: [ PageNumber.CURRENT ], size: 16, color: SLATE, font: 'Arial' }) ] }) ] }) },
    children }],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log('wrote', OUT, buf.length, 'bytes'); });
