import csv
from collections import Counter
rows=list(csv.DictReader(open("base_dossiers_fichiers.csv")))
for presc in ("IRSH","BARROS"):
    print("====",presc)
    c=Counter(r["statut_fichiers"] for r in rows if r["prescripteur"]==presc)
    for k,v in c.most_common(): print(f"  {v:3} {k}")
print("\n-- sample BARROS with num_fac --")
for r in rows:
    if r["prescripteur"]=="BARROS":
        print(f"{r['ref']:14} fac?={r['facture_flag_suivi']:4} num={r['num_fac_suivi']:12} tab={r['invoice_tab']:12} -> {r['statut_fichiers']}")
