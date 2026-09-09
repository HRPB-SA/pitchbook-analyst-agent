# verify.py: post-recalculation checks for a workbook (used for both A and B).
#   1. cached-value error scan (openpyxl data_only)
#   2. formulas-library cross-check of named cells (loads the requoted file)
#   3. numeric-constant audit: every typed number outside the allowed input tabs
#   4. embargo grep of the saved XML ("correl", "-0.99", "r=") and em-dash / en-dash scan
# Usage: python3 verify.py <file> [--allowed 00_Assumptions,01_Data] [--check-keys key=Sheet!Cell,...]
import sys, re, zipfile, json, warnings, argparse
warnings.filterwarnings("ignore")
from openpyxl import load_workbook

ERR = {"#REF!", "#NAME?", "#DIV/0!", "#VALUE!", "#N/A", "#NUM!", "#NULL!"}


def cached_errors(path):
    wb = load_workbook(path, data_only=True)
    errs, nf, nv = [], 0, 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.value is None:
                    continue
                nv += 1
                if isinstance(c.value, str) and c.value.strip() in ERR:
                    errs.append(f"{ws.title}!{c.coordinate}={c.value}")
    return errs, nv


def formula_cells(path):
    wb = load_workbook(path)
    out = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    out[f"{ws.title}!{c.coordinate}"] = c.value
    return out, wb


def constants_audit(path, allowed):
    """Numeric constants typed as cell VALUES (not formulas) outside the allowed tabs, plus numeric literals inside formulas."""
    wb = load_workbook(path)
    typed, literals = [], {}
    for ws in wb.worksheets:
        if ws.title in allowed:
            continue
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    typed.append(f"{ws.title}!{c.coordinate}={v}")
                elif isinstance(v, str) and v.startswith("="):
                    f = re.sub(r'"[^"]*"', '""', v)          # strip string literals
                    f = re.sub(r"'[^']*'!", "!", f)            # strip sheet names
                    f = re.sub(r"\$?[A-Z]{1,3}\$?\d+", "", f)   # strip cell refs
                    f = re.sub(r"[A-Za-z_][A-Za-z0-9_\.]*", "", f)  # strip names / functions
                    for m in re.findall(r"(?<![\w.])\d+(?:\.\d+)?", f):
                        literals.setdefault(m, []).append(f"{ws.title}!{c.coordinate}")
    return typed, literals


def xml_scans(path):
    hits = {"correl": [], "-0.99": [], "r=": [], "emdash": [], "endash": []}
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            if not n.endswith(".xml"):
                continue
            s = z.read(n).decode("utf-8", "ignore")
            low = s.lower()
            if "correl" in low:
                hits["correl"].append(n)
            if "-0.99" in s or "−0.99" in s:
                hits["-0.99"].append(n)
            if re.search(r"\br=", s):
                hits["r="].append(n)
            if "—" in s:
                hits["emdash"].append(n)
            if "–" in s:
                hits["endash"].append(n)
    return hits


def formulas_lib(path, keys):
    """Evaluate with the formulas library and return values for the requested Sheet!Cell keys (uppercase)."""
    import formulas
    xl = formulas.ExcelModel().loads(path).finish()
    sol = xl.calculate()
    book = path.split("/")[-1]
    out = {}
    for k in keys:
        sheet, cell = k.split("!")
        ref = f"'[{book}]{sheet.upper()}'!{cell.upper()}"
        v = sol.get(ref)
        if v is None:
            out[k] = None
        else:
            val = v.value if hasattr(v, "value") else v
            try:
                val = val.tolist()
                while isinstance(val, list):
                    val = val[0]
            except Exception:
                pass
            out[k] = val
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--allowed", default="00_Assumptions,01_Data"); ap.add_argument("--formulas", default="")
    a = ap.parse_args()
    errs, nv = cached_errors(a.file)
    print(json.dumps({"cached_error_cells": len(errs), "nonempty_cells": nv, "first_errors": errs[:20]}))
    typed, lits = constants_audit(a.file, set(a.allowed.split(",")))
    print("typed numeric constants outside allowed tabs:", len(typed))
    for t in typed[:200]:
        print("  ", t)
    print("numeric literals inside formulas (value: count, first cells):")
    for k, v in sorted(lits.items(), key=lambda kv: -len(kv[1])):
        print(f"   {k}: {len(v)} e.g. {v[:4]}")
    print("xml scans:", json.dumps(xml_scans(a.file)))
    if a.formulas:
        keys = a.formulas.split(",")
        print("formulas-lib:", json.dumps(formulas_lib(a.file, keys), default=str))
