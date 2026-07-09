import json,re
d=json.load(open("all_data.json"))
def suivi_factures(label):
    out=[]
    for r in d[label]["Suivi Factures"]:
        # find the Nº facture col: for IRSH col3, BARROS col3
        num=r[3] if len(r)>3 else ""
        date=r[4] if len(r)>4 else ""
        amt=r[5] if len(r)>5 else ""
        etat=r[6] if len(r)>6 else ""
        regl=r[7] if len(r)>7 else ""
        if (num and num not in ("Nº Facture",) and "Suivi" not in num and num!="Total") or (not num and amt and re.match(r'-?\d',amt) and "Total" not in " ".join(r)):
            out.append((num,date,amt,etat,regl))
    return out
for label in ("IRSH","BARROS"):
    print("="*60,"\nSUIVI FACTURES",label)
    tot=0
    for num,date,amt,etat,regl in suivi_factures(label):
        flag="  <<< NUMERO MANQUANT" if not num.strip() else ""
        print(f"  {num:20} {date[:10]:10} {amt:10} {etat:20}{flag}")
