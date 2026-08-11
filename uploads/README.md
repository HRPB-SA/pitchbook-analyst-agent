# Uploads

General drop zone for research input that is not yet sorted by company.

- `documents/` any file: PDFs, filings, spreadsheets, decks, exports.
- `links.md` paste URLs (one per line, optional note after a dash).

Every research pass reads this folder first, ingests what is relevant, tiers
it like any other source (a document does not outrank EDGAR just because it
was uploaded), cites it properly, and files company-specific material into
the right `companies/<slug>/<category>/` folder so it is findable next time.
If you know the company, dropping material straight into its folder is
better; this folder is for everything else.
