# requote.py: LibreOffice strips the quotes around sheet names that begin with a digit ('01_Data'! -> 01_Data!)
# when it re-saves an .xlsx after recalculation. Excel and the `formulas` library expect the quotes.
# This patches the saved XML in place (cell <f> texts and <definedName> texts) without touching cached values.
import zipfile, re, sys, os

PAT = re.compile(r"(?<![A-Za-z0-9_'\.\[\]])(\d[A-Za-z0-9_]*)!")


def _fix(m):
    return m.group(1) + PAT.sub(lambda mm: "'" + mm.group(1) + "'!", m.group(2)) + m.group(3)


def requote(path):
    tmp = path + ".tmp"
    n = 0
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "xl/workbook.xml" or (item.filename.startswith("xl/worksheets/") and item.filename.endswith(".xml")):
                s = data.decode("utf-8")
                s2 = re.sub(r"(<f[^>]*>)([^<]*)(</f>)", _fix, s)
                s2 = re.sub(r"(<definedName[^>]*>)([^<]*)(</definedName>)", _fix, s2)
                if s2 != s:
                    n += 1
                data = s2.encode("utf-8")
            zout.writestr(item, data)
    os.replace(tmp, path)
    return n


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print("requoted", p, "parts changed:", requote(p))
