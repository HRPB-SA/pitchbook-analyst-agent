# xcheck_formulas.py: evaluate both workbooks with the `formulas` library and compare key cells with the LibreOffice cached values.
import warnings, json, sys, time; warnings.filterwarnings("ignore")
from openpyxl import load_workbook
import formulas
KEYS = {
 "../entry-fee-v5.xlsx": ["01_Data!D5","02_Revenue!D38","02_Revenue!M54","02_Revenue!M55","02_Revenue!M56","02_Revenue!M57","02_Revenue!M66","02_Revenue!J75","02_Revenue!K75",
   "05_Cash_Fund!D17","05_Cash_Fund!J17","05_Cash_Fund!E44","05_Cash_Fund!E45","05_Cash_Fund!G44","05_Cash_Fund!H44","06_Valuation!D9","06_Valuation!D10","06_Valuation!D12","06_Valuation!D13",
   "06_Valuation!C26","06_Valuation!E26","06_Valuation!F26","09_Obligations!B18","09_Obligations!B19","09_Obligations!B20","09_Obligations!B38","09_Obligations!B39","09_Obligations!B46",
   "09_Obligations!G64","09_Obligations!H64","09_Obligations!I64","09_Obligations!J64","09_Obligations!K64","09_Obligations!H68","09_Obligations!I82","09_Obligations!I83","09_Obligations!I88","09_Obligations!I89",
   "09_Obligations!AM99","09_Obligations!AM101","11_AIBQ!F10","11_AIBQ!D17","11_AIBQ!D24","11_AIBQ!D31","03_Costs!G49","03_Costs!D54","03_Costs!E54","07_Sensitivity!G40","10_Financing!B18","13_OutsideView!D29","08_Output!D45","08_Output!D142"],
 "../greenfield-entry-cost.xlsx": ["09_Output!C4","09_Output!D4","09_Output!E4","09_Output!C7","09_Output!D7","09_Output!E7","09_Output!C9","09_Output!D9","09_Output!E9","09_Output!C12","09_Output!D12","09_Output!E12","09_Output!C36","09_Output!C40","05_Inference!D5","05_Inference!D7","05_Inference!D8","09_Output!C26","09_Output!C27","09_Output!C28"],
}
out = {}
for path, keys in KEYS.items():
    t0 = time.time()
    cached = load_workbook(path, data_only=True)
    xl = formulas.ExcelModel().loads(path).finish(); sol = xl.calculate()
    book = path.split("/")[-1]
    res = []
    for k in keys:
        sh, cell = k.split("!")
        v = sol.get(f"'[{book}]{sh.upper()}'!{cell.upper()}")
        val = v.value if hasattr(v, "value") else v
        try:
            val = val.tolist()
            while isinstance(val, list): val = val[0]
        except Exception: pass
        c = cached[sh][cell].value
        ok = (abs(float(val) - float(c)) < 1e-6 * max(1, abs(float(c)))) if isinstance(c, (int, float)) and isinstance(val, (int, float)) else (str(val) == str(c))
        res.append({"cell": k, "libreoffice": c, "formulas": val, "match": bool(ok)})
    out[path] = {"seconds": round(time.time() - t0), "cells": res, "mismatches": sum(1 for r in res if not r["match"])}
    print(path, "seconds", out[path]["seconds"], "mismatches", out[path]["mismatches"], flush=True)
json.dump(out, open("xcheck_formulas.json", "w"), indent=1, default=str)
for path, o in out.items():
    for r in o["cells"]:
        print(("OK " if r["match"] else "XX "), r["cell"], r["libreoffice"], r["formulas"])
