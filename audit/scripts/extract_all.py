import openpyxl, json, os
files={
 "IRSH":"/root/.claude/uploads/7767e6b5-de9b-5631-a5c3-b77beef4874c/b7dfb6a3-Suivi_IRSH_2026.xlsx",
 "BARROS":"/root/.claude/uploads/7767e6b5-de9b-5631-a5c3-b77beef4874c/241efaeb-Suivi_Barros_2026.xlsx",
}
out={}
for label,f in files.items():
    wb=openpyxl.load_workbook(f,data_only=True)
    out[label]={}
    for ws in wb.worksheets:
        rows=[]
        for r in ws.iter_rows(values_only=True):
            if any(c is not None and str(c).strip()!="" for c in r):
                rows.append(["" if c is None else (c.isoformat() if hasattr(c,'isoformat') else str(c)) for c in r])
        out[label][ws.title]=rows
json.dump(out,open("all_data.json","w"),ensure_ascii=False)
# print summary counts
for label in out:
    for sh,rows in out[label].items():
        print(f"{label:7} {sh:25} rows={len(rows)}")
