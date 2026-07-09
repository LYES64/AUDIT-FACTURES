import json,re,csv
d=json.load(open("all_data.json"))

DIA_RE=re.compile(r'DIA\s?[A-Z]?\d{4,7}')
BT_RE=re.compile(r'(?:CO-\d{4,6}|N°2025-\d{3,5})')
def norm_dia(s): return s.replace(" ","") if s else s

# ---------- 1. Invoice tabs -> line items (ref -> invoice num) ----------
tab_items=[]  # dict
def parse_irsh_tab(label,sh,invnum):
    for r in d[label][sh]:
        line=" ".join(r)
        m=DIA_RE.search(line)
        # client is col0 if looks like name and there's an amount
        if m and r[0] and 'Total' not in line and 'Discription' not in line:
            # amount = last numeric-ish cell
            amt=""
            for c in reversed(r):
                cc=c.replace(".0","")
                if re.fullmatch(r'\d{2,6}(\.\d+)?',c or ""): amt=c;break
            tab_items.append({"src":label+"/"+sh,"inv":invnum,"ref":norm_dia(m.group()),
                              "client":r[0].strip(),"amount":amt})
def parse_barros_tab(label,sh,invnum):
    for r in d[label][sh]:
        line=" ".join(r)
        m=BT_RE.search(line)
        if m and r[0] and 'Total' not in line and r[0]!='Client ':
            amt=""
            for c in reversed(r):
                if re.fullmatch(r'\d{2,6}(\.\d+)?',c or ""): amt=c;break
            tab_items.append({"src":label+"/"+sh,"inv":invnum,"ref":m.group(),
                              "client":r[0].strip(),"amount":amt})

irsh_tabs={'F2026-16':'F2026-16','F2026-17':'F2026-17','F2026-18':'F2026-18','F2026-19':'F2026-19',
 'F2026-20':'F2026-20','F2026-21':'F2026-21','F2026-22':'F2026-22','F2026-23':'F2026-23','F2026-24':'F2026-24'}
for sh,n in irsh_tabs.items(): parse_irsh_tab("IRSH",sh,n)
barros_tabs={'F2026-B01 ':'F2026-B01','F2026-B09':'F2026-B09','F2026-B10':'F2026-B10',
 'F2026-B11':'F2026-B11(brouillon,onglet=B10)','F2026-B12':'F2026-B12(brouillon,onglet=B10,0€)'}
for sh,n in barros_tabs.items(): parse_barros_tab("BARROS",sh,n)

print("=== LIGNES DE FACTURES (onglets individuels) ===")
for it in tab_items: print(f"{it['inv']:35} {it['ref']:12} {it['client'][:30]:30} {it['amount']}")
print("total lignes:",len(tab_items))

json.dump(tab_items,open("tab_items.json","w"),ensure_ascii=False)
