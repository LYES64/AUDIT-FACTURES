import openpyxl, json
def dump_sheet(f, sheet, maxr=None):
    wb = openpyxl.load_workbook(f, data_only=True)
    ws = wb[sheet]
    rows=[]
    for r in ws.iter_rows(values_only=True):
        # keep row if any cell non-empty
        if any(c is not None and str(c).strip()!="" for c in r):
            rows.append([("" if c is None else str(c)) for c in r])
    return rows

f_irsh="/root/.claude/uploads/7767e6b5-de9b-5631-a5c3-b77beef4874c/b7dfb6a3-Suivi_IRSH_2026.xlsx"
for sh in ['Suivi Factures']:
    print("###### IRSH /",sh)
    for i,row in enumerate(dump_sheet(f_irsh,sh)):
        print(i, "|".join(row))
