import json
d=json.load(open("all_data.json"))
def total_and_num(label,sh):
    rows=d[label][sh]
    num=rows[0][4] if len(rows[0])>4 else ""
    date=rows[1][4] if len(rows)>1 and len(rows[1])>4 else ""
    clients=[]
    tot=""
    for r in rows:
        if len(r)>3 and r[3]=="Total":
            tot=r[5] if len(r)>5 else ""
        # client line: first cell nonempty, has amount at end, not header
    return num,date,tot
for sh in ['F2026-16','F2026-17','F2026-18','F2026-19','F2026-20','F2026-21','F2026-22','F2026-23','F2026-24']:
    print("IRSH",sh, total_and_num("IRSH",sh))
for sh in ['F2026-B01 ','F2026-B09','F2026-B10','F2026-B11','F2026-B12']:
    print("BARROS",sh, total_and_num("BARROS",sh))
print("\n--- B11 full ---")
for i,r in enumerate(d["BARROS"]["F2026-B11"]): print(i,"|".join(r))
print("\n--- B12 full ---")
for i,r in enumerate(d["BARROS"]["F2026-B12"]): print(i,"|".join(r))
