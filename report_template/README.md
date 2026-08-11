# Report template

**The master template is `Vertical_Analyst_Note_10.docx`** (analyst-provided,
August 2026): production metadata sheet (data filepath, chart as-of date,
geography, research type, access level, chart/table counts, credits,
contents, landing page block, report picks), then Key takeaways, analytical
sections with charts (captions 30 words or fewer), and numbered References.
Its machine-readable contract is `vertical_analyst_note.json`; the builder
renders it via the `analyst_note` theme (Segoe UI, blue headings, no
header/footer chrome). It is the default template on the dashboard.

The other contracts (one JSON per report type; see TEMPLATE_SPEC.md) cover
the deep-dive and specialty formats. Each template fixes section order and
the binding `required` obligations per section; that is what keeps every
report consistent.

To change or add a template: drop your material here in any form (a marked-up
docx, a PDF of a report whose shape you want, a bullet list of sections) and
ask the desk to translate it into a contract JSON. Custom one-off section
lists in a dashboard request are also legitimate; the engine renders whatever
sections exist.
