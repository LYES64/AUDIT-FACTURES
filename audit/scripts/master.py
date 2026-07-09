import json,re,csv
d=json.load(open("all_data.json"))
tab_items=json.load(open("tab_items.json"))
DIA_RE=re.compile(r'DIA\s?[A-Z]?\d{4,7}')
BT_RE=re.compile(r'(?:CO-\d{4,6}|N°2025-\d{3,5})')
def nd(s): return s.replace(" ","").strip() if s else s

# ref -> invoice(s) from tabs
ref2inv={}
for it in tab_items:
    ref2inv.setdefault(nd(it['ref']),[]).append(it['inv'])

dossiers={}  # key ref -> record
def add(ref,**kw):
    ref=nd(ref)
    r=dossiers.setdefault(ref,{"ref":ref,"prescripteur":"","client":"","cp":"","date_pose":"",
        "montant":"","pose":"","valide":"","facture_flag_suivi":"","num_fac_suivi":"","invoice_tab":"",
        "source":set(),"note":""})
    for k,v in kw.items():
        if k=="source": r["source"].add(v)
        elif v not in (None,"","False") or not r.get(k): 
            if v not in (None,""): r[k]=v
    return r

# IRSH Poses
for row in d["IRSH"]["Suivi Poses"][2:]:
    if len(row)<3: continue
    m=DIA_RE.search(" ".join(row))
    if not m: continue
    ref=nd(m.group())
    add(ref,prescripteur="IRSH",client=row[1] if len(row)>1 else "",cp=row[3] if len(row)>3 else "",
        date_pose=row[4] if len(row)>4 else "",montant=row[5] if len(row)>5 else "",
        pose=row[6] if len(row)>6 else "",valide=row[9] if len(row)>9 else "",
        facture_flag_suivi=row[14] if len(row)>14 else "",num_fac_suivi=row[15] if len(row)>15 else "",
        source="IRSH:Poses")
# IRSH SAV
for row in d["IRSH"]["Suivi SAV"][2:]:
    m=DIA_RE.search(" ".join(row))
    if not m: continue
    add(nd(m.group()),prescripteur="IRSH",client=row[1] if len(row)>1 else "",
        cp=row[3] if len(row)>3 else "",source="IRSH:SAV",note="SAV")
# IRSH non facturé
for row in d["IRSH"]["Copie de non facturé"]:
    m=DIA_RE.search(" ".join(row))
    if not m: continue
    ref=nd(m.group())
    add(ref,prescripteur="IRSH",client=row[0] if row[0] else "",source="IRSH:NonFacture",
        note="liste 'non facturé'")
# BARROS Poses
for row in d["BARROS"]["Suivi Poses"][2:]:
    m=BT_RE.search(" ".join(row))
    if not m: continue
    ref=m.group()
    add(ref,prescripteur="BARROS",client=row[1] if len(row)>1 else "",cp=row[3] if len(row)>3 else "",
        date_pose=row[4] if len(row)>4 else "",montant=row[5] if len(row)>5 else "",
        pose=row[6] if len(row)>6 else "",valide=row[9] if len(row)>9 else "",
        facture_flag_suivi=row[12] if len(row)>12 else "",num_fac_suivi=row[13] if len(row)>13 else "",
        source="BARROS:Poses")
# tab line items -> attach invoice_tab + client fallback
for it in tab_items:
    r=add(it['ref'],source="FactureOnglet:"+it['inv'])
    invs=";".join(sorted(set(ref2inv.get(nd(it['ref']),[]))))
    r["invoice_tab"]=invs
    if not r["client"]: r["client"]=it["client"]
    if not r["prescripteur"]: r["prescripteur"]="BARROS" if it['ref'].startswith(('CO','N°')) else "IRSH"

# finalize status
def status_for(r):
    ns=r["num_fac_suivi"]; it=r["invoice_tab"]; ff=r["facture_flag_suivi"]
    if ns and ns not in ("NON","OUI"): base="Facturée (num dans suivi)"
    elif it: base="Facturée (onglet, num ABSENT du suivi)"
    elif ff=="OUI": base="Marquée facturée mais num manquant"
    elif r.get("pose")=="OUI": base="Posé, NON facturé"
    else: base="Commande/SAV sans facture"
    return base

rows=[]
for ref,r in dossiers.items():
    r["source"]=";".join(sorted(r["source"]))
    r["statut_fichiers"]=status_for(r)
    rows.append(r)
rows.sort(key=lambda x:(x["prescripteur"],x["ref"]))

cols=["ref","prescripteur","client","cp","date_pose","montant","pose","valide",
      "facture_flag_suivi","num_fac_suivi","invoice_tab","statut_fichiers","source","note"]
with open("base_dossiers_fichiers.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(cols)
    for r in rows: w.writerow([r.get(c,"") for c in cols])

# stats
from collections import Counter
print("TOTAL dossiers (DIA/BT uniques):",len(rows))
print("  IRSH:",sum(1 for r in rows if r['prescripteur']=='IRSH'),
      " BARROS:",sum(1 for r in rows if r['prescripteur']=='BARROS'))
c=Counter(r["statut_fichiers"] for r in rows)
for k,v in c.most_common(): print(f"  {v:3}  {k}")
