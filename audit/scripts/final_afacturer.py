import json,re,csv
crm=json.load(open("crm_rows.json"))[2:]
data=json.load(open("all_data.json"))
tab=json.load(open("tab_items.json"))
def sn(c): return re.split(r'[ ]',c.strip())[0].upper().replace(",","")

# montants depuis l'onglet "Copie de non facturé" (par nom)
nonfact={}
for row in data["IRSH"]["Copie de non facturé"]:
    m=re.search(r'DIA\s?[A-Z]?\d{4,7}'," ".join(row))
    if m and row[0]:
        amt=""
        for c in row:
            if re.fullmatch(r'\d{3,5}(\.\d+)?',c or ""): amt=c;break
        nonfact[sn(row[0])]=(m.group().replace(" ",""),amt)

# clients facturés (preuve) — repris de l'analyse précédente
invoiced=set()
for it in tab:
    if not it['ref'].startswith(("CO","N")): invoiced.add(sn(it['client']))
invoiced.update(["MOUHEL","ROLLAND","VEUILLAULT","FRIMAS","CORVISIER","WORMSER",
 "DARMENDRAIL","MOMAS","COLAS","SAINT","DESLUX","HOSPITAL","MANSUY","BOUEILH","TISSAIRE",
 "HERREYRE","PANTANI","LARREDE","LEFRANCOIS","FAUCONNIER","CHARLES","PONTE","DA","DISSAUX",
 "HERVE","PEZOT","PELUHET","SUBERCAZE","CLAUDON","VENTURINI","BENEDE","PERRIERE","MOYA"])

done=[r for r in crm if len(r)>5 and r[5]=="Posée/Effectuée"]
out=[]
for r in done:
    r=(r+[""]*10)[:10]
    dia,typ,denv,drdv,stat,cli,cp,ville=r[0],r[1],r[3],r[4],r[5],r[6],r[7],r[8]
    s=sn(cli)
    y2026="2026" in drdv
    inv = s in invoiced
    nf=nonfact.get(s,("",""))
    montant = nf[1] if nf[1] else ""
    if typ in ("VISAP","SAV") and not montant:
        billable="À vérifier (SAV/visite — facturable seulement si prestation à charge client)"
    else:
        billable="OUI — pose/reprise réalisée, aucune facture retrouvée"
    if inv and typ in ("POSE",):
        continue  # pose déjà facturée
    statut = "DÉJÀ FACTURÉ (pose) — reprise/visite postérieure à qualifier" if inv else ("À FACTURER" if y2026 else "À FACTURER (intervention antérieure à 2026 — hors périmètre, à vérifier)")
    out.append([dia,typ,cli,cp,ville,drdv,montant,statut,billable])

cols=["DIA","Type","Client","CP","Ville","Date intervention","Montant estimé (fichier non facturé)","Statut","À facturer ?"]
with open("IRSH_Interventions_a_facturer.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(cols)
    for o in out: w.writerow(o)

print("== INTERVENTIONS RÉALISÉES À FACTURER (IRSH, source CRM 07/07/2026) ==\n")
for o in out:
    print(f"{o[0]:11}|{o[1]:6}|{o[2][:28]:28}|{o[5]:10}|{('montant '+o[6]) if o[6] else '':13}| {o[7]}")
print("\nTotal lignes:",len(out))
