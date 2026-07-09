import json,re
d=json.load(open("all_data.json"))
def parse_amt(s):
    try: return float(s)
    except: return None
for label in ("IRSH","BARROS"):
    fac2026=av=blank=old=0.0
    ncount=0
    for r in d[label]["Suivi Factures"]:
        num=(r[3] if len(r)>3 else "").strip()
        date=(r[4] if len(r)>4 else "")
        amt=parse_amt(r[5] if len(r)>5 else "")
        if amt is None or "Total" in " ".join(r): continue
        y2026 = date.startswith("2026")
        if num.startswith("AV") or (amt<0): av+=amt
        elif not num:
            blank+=amt; ncount+=1
        elif y2026: fac2026+=amt
        else: old+=amt
    print(f"{label}: factures2026(num,>=2026)={fac2026:.0f}  avoirs={av:.0f}  lignes_sans_num={blank:.0f}({ncount})  factures_datées_2025={old:.0f}")
# non facturé IRSH total
print("IRSH non-facturé sheet total affiché: 30170 HT (+13430 col adj)")
