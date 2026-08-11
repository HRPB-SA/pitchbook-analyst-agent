#!/usr/bin/env bash
# Environment setup for the report engine. Run once per fresh session/container
# before stage 6 (BUILD). Safe to re-run; every step is idempotent.
set -e
pip install -q python-docx matplotlib openpyxl
python3 -c "import docx, matplotlib, openpyxl" && echo "python deps ok"
if ! soffice --version 2>/dev/null | grep -q LibreOffice || ! which pdftotext >/dev/null 2>&1; then
    apt-get update -q >/dev/null 2>&1 || sudo apt-get update -q >/dev/null 2>&1 || true
    apt-get install -y -q libreoffice-writer poppler-utils >/dev/null 2>&1 \
        || sudo apt-get install -y -q libreoffice-writer poppler-utils >/dev/null 2>&1 \
        || echo "WARN: could not install libreoffice-writer/poppler-utils; build will produce docx only (no pdf, no measured TOC). Flag this in the validation log."
fi
soffice --version 2>/dev/null | head -1 || true
which pdftotext || true
echo "setup complete"
