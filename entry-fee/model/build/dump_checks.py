# dump_checks.py: print the spec section 9 check table (08_Output rows 45+) and key figures from the recalculated Workbook A.
import sys, warnings, json
warnings.filterwarnings("ignore")
from openpyxl import load_workbook

path = sys.argv[1] if len(sys.argv) > 1 else "../entry-fee-v5.xlsx"
wb = load_workbook(path, data_only=True)
o = wb["08_Output"]
fails = []
rows = []
for r in range(45, 200):
    lab = o[f"A{r}"].value
    if lab is None:
        break
    exp = o[f"B{r}"].value; pf = o[f"D{r}"].value; where = o[f"E{r}"].value
    rows.append((lab, exp, pf, where))
    if not (isinstance(pf, str) and pf.startswith("PASS")):
        fails.append((lab, exp, pf, where))
print(f"checks: {len(rows)}  fails: {len(fails)}")
for lab, exp, pf, where in rows:
    print(f"  {str(pf):<28} | {lab:<62} | exp {exp} | {where}")
print("FAILCOUNT cell:", o[f"D{45+len(rows)}"].value)


def g(sheet, cell):
    return wb[sheet][cell].value


keys = {
    "FY26A live (02 M54)": ("02_Revenue", "M54"), "FY26 at 100k (M55)": ("02_Revenue", "M55"), "FY26 at 120k (M56)": ("02_Revenue", "M56"), "FY26 flat (M57)": ("02_Revenue", "M57"),
    "FY26O live (M64)": ("02_Revenue", "M64"), "OpenAI 0/10/20 (M65:M67)": ("02_Revenue", "M65"),
    "Anthropic rev 2027-2030 (H71:K71)": ("02_Revenue", "H71"), "REV 2029": ("02_Revenue", "J71"), "REV 2030": ("02_Revenue", "K71"),
    "Priced run A 2026-2030 (09 G64:K64)": ("09_Obligations", "G64"), "2027": ("09_Obligations", "H64"), "2028": ("09_Obligations", "I64"), "2029": ("09_Obligations", "J64"), "2030": ("09_Obligations", "K64"),
    "Priced run O 2027 (H68)": ("09_Obligations", "H68"), "DOC_A (B18)": ("09_Obligations", "B18"), "DOC_A_SPV (B19)": ("09_Obligations", "B19"), "REP_A (B20)": ("09_Obligations", "B20"), "CANC_A (E18)": ("09_Obligations", "E18"),
    "DOC_O (B38)": ("09_Obligations", "B38"), "REC_O (B39)": ("09_Obligations", "B39"), "Gap 2028 lo/hi (I88:I89)": ("09_Obligations", "I88"), "gap hi": ("09_Obligations", "I89"), "Gap 2027 lo": ("09_Obligations", "H88"),
    "Env plan 2028 lo/hi": ("09_Obligations", "I82"), "env hi": ("09_Obligations", "I83"), "Env live 2028 (I84)": ("09_Obligations", "I84"),
    "CE A live (05 E43)": ("05_Cash_Fund", "E43"), "CE O live (G43)": ("05_Cash_Fund", "G43"), "ratio (H43)": ("05_Cash_Fund", "H43"),
    "Mult A live (06 D8)": ("06_Valuation", "D8"), "Mult O (D11)": ("06_Valuation", "D11"), "PPT A (C26)": ("06_Valuation", "C26"), "PPT O (E26)": ("06_Valuation", "E26"), "spread (F26)": ("06_Valuation", "F26"),
    "Burn plug (05 D61)": ("05_Cash_Fund", "D61"), "A 2026 result (D66)": ("05_Cash_Fund", "D66"),
    "Grid c base (07 C51)": ("07_Sensitivity", "C51"), "Grid b P1 (200k,77%) (07 D28)": ("07_Sensitivity", "D28"),
    "03 Anthropic COGS 2026-2028 (G8:I8)": ("03_Costs", "G8"), "COGS 2027": ("03_Costs", "H8"), "COGS 2028": ("03_Costs", "I8"), "L5 A 2026 (G16)": ("03_Costs", "G16"), "OpenAI L5 2027 (H35)": ("03_Costs", "H35"),
    "04 A op incl training 2026-2030 (G13:K13)": ("04_PL", "G13"), "2027": ("04_PL", "H13"), "2028": ("04_PL", "I13"), "2030": ("04_PL", "K13"),
    "04 O op incl training 2026 (G29)": ("04_PL", "G29"), "2030 (K29)": ("04_PL", "K29"),
    "A19 flag (03 E59)": ("03_Costs", "E59"), "GM grid D54/E54": ("03_Costs", "D54"),
}
for k, (s, c) in keys.items():
    print(f"  {k:<44} {s}!{c} = {g(s, c)}")
