import json,csv,re
d=json.load(open("all_data.json"))
dossiers=list(csv.DictReader(open("base_dossiers_fichiers.csv")))

# invoice date/amount lookups
inv_meta={}  # num -> (date, amount, etat)
def load_suivi(label):
    for r in d[label]["Suivi Factures"]:
        num=(r[3] if len(r)>3 else "").strip()
        if num and num not in ("Nº Facture","Total") and "Suivi" not in num:
            inv_meta[num.replace(" ","")]=(r[4][:10] if len(r)>4 else "",r[5] if len(r)>5 else "",r[6] if len(r)>6 else "")
load_suivi("IRSH"); load_suivi("BARROS")
# tab dates
tab_date={}
for label in ("IRSH","BARROS"):
    for sh in d[label]:
        rows=d[label][sh]
        if rows and len(rows[0])>4 and rows[0][4]=="Facture N°":
            num=(rows[0][5] if len(rows[0])>5 else "").strip()
            date=(rows[1][5][:10] if len(rows)>1 and len(rows[1])>5 else "")
            if num: tab_date[num]=date

def map_status(r):
    s=r["statut_fichiers"]; conf="Moyen"; mail="À vérifier (Gmail indisponible)"
    if s=="Facturée (num dans suivi)": st="Facturée";conf="Élevé"
    elif s=="Facturée (onglet, num ABSENT du suivi)": st="Anomalie détectée — facture émise mais N° retiré du suivi";conf="Élevé"
    elif s=="Posé, NON facturé": st="À facturer (pose réalisée, aucune facture dans les fichiers)";conf="Moyen"
    else: st="À vérifier (commande/SAV sans facture identifiée)";conf="Faible"
    return st,conf,mail

out=[]
for r in dossiers:
    inv=r["num_fac_suivi"] if r["num_fac_suivi"] not in ("","OUI","NON") else r["invoice_tab"]
    inv_clean=re.split(r'\(',inv)[0].strip() if inv else ""
    date_fac=tab_date.get(inv_clean,"") or inv_meta.get(inv_clean.replace(" ",""),("","",""))[0]
    fac_retrouvee="Oui" if (r["num_fac_suivi"] not in ("","OUI","NON") or r["invoice_tab"]) else "Non"
    st,conf,mail=map_status(r)
    dia=r["ref"] if r["prescripteur"]=="IRSH" else ""
    cmd=r["ref"] if r["prescripteur"]=="BARROS" else ""
    preuve=r["source"]
    out.append([dia,cmd,r["client"],r["date_pose"][:10],date_fac,inv,r["montant"],
                fac_retrouvee,"Oui",mail,preuve,r["prescripteur"],st,conf])

cols=["Référence DIA","Référence commande","Client","Date de commande/pose","Date de facture",
      "Numéro de facture","Montant (HT/nouveau montant)","Facture retrouvée","Présente fichiers suivi",
      "Présente dans les mails","Preuve retrouvée (fichiers)","Prescripteur","Statut","Niveau de confiance"]
with open("Audit_Factures_2026_Synthese.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(cols)
    for o in sorted(out,key=lambda x:(x[11],x[0]+x[1])): w.writerow(o)
print("CSV écrit:",len(out),"dossiers")
print("Colonnes:",cols)
