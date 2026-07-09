import json,re,csv
crm=json.load(open("crm_rows.json"))[2:]
tab=json.load(open("tab_items.json"))
def sn(c): return re.split(r'[ ]',c.strip())[0].upper().replace(",","")

# --- Ensemble des CLIENTS facturés (preuves) ---
invoiced={}  # surname -> preuve
# 1) onglets de factures F2026-16..24
for it in tab:
    if not it['ref'].startswith(("CO","N")):
        invoiced[sn(it['client'])]=f"Onglet {it['inv']}"
# 2) Suivi Poses avec Nº facture (F2026-01/02) + clients facturés connus
poses_fact={"MOUHEL":"F2026-01","ROLLAND":"F2026-01","VEUILLAULT":"F2026-01",
            "FRIMAS":"F2026-02","CORVISIER":"F2026-02","WORMSER":"F2026-02"}
invoiced.update(poses_fact)
# 3) Factures confirmées par mails IRSH (point compta 18/06 & 09/07 + onglets 17/20/22)
mail_fact={
 "DARMENDRAIL":"F2026-15 (200€, à corriger 100€)","MOMAS":"F2026-16","COLAS":"F2026-16",
 "SAINT":"F2026-17","DESLUX":"F2026-17","HOSPITAL":"F2026-17",
 "MANSUY":"F2026-18","BOUEILH":"F2026-18","TISSAIRE":"F2026-18/23 (+avoir)",
 "HERREYRE":"F2026-19","PANTANI":"F2026-19","LARREDE":"F2026-19",
 "LEFRANCOIS":"F2026-20","FAUCONNIER":"F2026-20",
 "CHARLES":"F2026-21","PONTE":"F2026-21","DA":"F2026-21 (DA SILVA)",
 "DISSAUX":"F2026-22","HERVE":"F2026-22","PEZOT":"F2026-22",
 "PELUHET":"F2026-23","SUBERCAZE":"F2026-23","CLAUDON":"F2026-24","VENTURINI":"F2026-24","BENEDE":"F2026-24",
 "PERRIERE":"F1225-02 (litige)","MOYA":"F2026-16",
}
invoiced.update(mail_fact)

print("=== 18 INTERVENTIONS 'Posée/Effectuée' (CRM) — statut facturation ===\n")
done=[r for r in crm if len(r)>5 and r[5]=="Posée/Effectuée"]
for r in done:
    r=(r+[""]*10)[:10]
    dia,typ,denv,drdv,stat,cli,cp=r[0],r[1],r[3],r[4],r[5],r[6],r[7]
    s=sn(cli)
    fac=invoiced.get(s)
    y2026 = ("2026" in drdv)
    tag = "✅ FACTURÉE: "+fac if fac else "🔴 AUCUNE FACTURE TROUVÉE"
    scope = "" if y2026 else "  [hors 2026 / ancienne]"
    print(f"{dia:11}|{typ:6}|RDV {drdv:10}|{cli[:30]:30}| {tag}{scope}")
