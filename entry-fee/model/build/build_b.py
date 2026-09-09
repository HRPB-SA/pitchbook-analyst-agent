# build_b.py: builds Workbook B (greenfield-entry-cost.xlsx) with openpyxl from the Analyst's model spec section 7.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from xlhelp import Sh, REG
import tabs_b

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "greenfield-entry-cost.xlsx")
TABS = ["00_Assumptions", "01_Data", "02_Compute", "03_Facility", "04_Training", "05_Inference", "06_People_Other", "07_Cash", "08_Reference", "09_Output"]
W = {"A": 70, "B": 12, "C": 40, "D": 14, "E": 14, "F": 14, "G": 14, "H": 14, "I": 14, "J": 40}
WIDTHS = {
    "00_Assumptions": {"A": 78, "B": 12, "C": 52, "D": 13, "E": 13, "F": 13, "G": 13, "H": 12, "I": 12, "J": 50},
    "01_Data": {"A": 16, "B": 62, "C": 46, "D": 14, "E": 14, "F": 16, "G": 40, "H": 14, "I": 10, "J": 12, "K": 18, "L": 18, "M": 30},
    "07_Cash": W, "08_Reference": {"A": 32, "B": 18, "C": 60, "D": 14, "E": 14, "F": 30, "G": 34, "H": 70},
    "09_Output": {"A": 78, "B": 10, "C": 44, "D": 44, "E": 44, "F": 20, "G": 44},
}


def build():
    wb = Workbook(); wb.remove(wb.active)
    sheets = {t: Sh(wb, t, WIDTHS.get(t, W)) for t in TABS}
    tabs_b.build_b01(sheets["01_Data"])
    tabs_b.build_b00(sheets["00_Assumptions"])
    tabs_b.build_b02(sheets["02_Compute"])
    tabs_b.build_b03(sheets["03_Facility"])
    tabs_b.build_b05(sheets["05_Inference"])
    tabs_b.build_b04(sheets["04_Training"])
    tabs_b.build_b06(sheets["06_People_Other"])
    tabs_b.build_b07(sheets["07_Cash"])
    tabs_b.build_b08(sheets["08_Reference"])
    tabs_b.build_b09(sheets["09_Output"])
    for ws in wb.worksheets:
        ws.sheet_properties.tabColor = "1F3864" if ws.title in ("00_Assumptions", "01_Data") else "548235"
    wb.save(OUT)
    n = sum(1 for ws in wb.worksheets for row in ws.iter_rows() for c in row if isinstance(c.value, str) and c.value.startswith("="))
    print("saved", OUT, "formulas:", n, "names:", len(wb.defined_names))


if __name__ == "__main__":
    build()
