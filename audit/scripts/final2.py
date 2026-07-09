import json,re,csv
crm=json.load(open("crm_rows.json"))[2:]
data=json.load(open("all_data.json"))
tab=json.load(open("tab_items.json"))
def sn(c): return re.split(r'[ ]',c.strip())[0].upper().replace(",","")

# montant réel depuis 'Copie de non facturé' : cellule montant = après 'POSE DOUCHE'/'Dépose'
nonfact={}
for row in data["IRSH"]["Copie de non facturé"]:
    line=" ".join(row)
    m=re.search(r'DIA\s?[A-Z]?\d{4,7}',line)
    if m and row[0] and ('POSE' in line or 'Dépose' in line):
        cp=row[2] if len(row)>2 else ""
        amt=""
        for c in row[3:]:
            c=(c or "").strip()
            if re.fullmatch(r'\d{3,4}(\.\d+)?',c) and c!=cp: amt=c;break
        nonfact[sn(row[0])]=(m.group().replace(" ",""),amt)

invoiced=set()
for it in tab:
    if not it['ref'].startswith(("CO","N")): invoiced.add(sn(it['client']))
invoiced.update(["MOUHEL","ROLLAND","VEUILLAULT","FRIMAS","CORVISIER","WORMSER","DARMENDRAIL",
 "MOMAS","COLAS","SAINT","DESLUX","HOSPITAL","MANSUY","BOUEILH","TISSAIRE","HERREYRE","PANTANI",
 "LARREDE","LEFRANCOIS","FAUCONNIER","CHARLES","PONTE","DA","DISSAUX","HERVE","PEZOT","PELUHET",
 "SUBERCAZE","CLAUDON","VENTURINI","BENEDE","PERRIERE","MOYA"])

done=[(r+[""]*10)[:10] for r in crm if len(r)>5 and r[5]=="Posée/Effectuée"]
rows=[]
for dia,typ,pri,denv,drdv,stat,cli,cp,ville,prod in done:
    s=sn(cli); y="2026" in drdv; inv=s in invoiced
    nf=nonfact.get(s,("",""))
    if typ=="POSE":
        cat="1. POSE réalisée NON facturée" if not inv else None
    elif typ in ("REWORK","SAV"):
        cat="2. Reprise/SAV réalisée — à facturer si prestation à charge"
    else: # VISAP
        cat="3. Visite SAP réalisée — à qualifier (rarement facturable)"
    if cat is None: continue
    if not y: cat="4. Intervention ANTÉRIEURE à 2026 (hors périmètre — à vérifier séparément)"
    rows.append([cat,dia,typ,cli,cp or ville,drdv,nf[1],"Non trouvée",])
rows.sort(key=lambda x:x[0])
cols=["Catégorie","DIA","Type","Client","CP/Ville","Date intervention","Montant (si connu)","Facture"]
with open("IRSH_Interventions_a_facturer.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(cols)
    for r in rows: w.writerow(r)
cur=None
for r in rows:
    if r[0]!=cur: cur=r[0]; print("\n### ",cur)
    mt=f"  ~{r[6]}€" if r[6] else ""
    print(f"   {r[1]:11} {r[2]:6} {r[3][:30]:30} {r[5]}{mt}")
