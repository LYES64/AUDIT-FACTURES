import json,re,csv
def sn(c): return re.split(r'[ ]',(c or "").strip())[0].upper().replace(",","")

mail=json.load(open("mail_orders.json"))["mail"]   # ref -> [client,dep,date]
crm=json.load(open("crm_rows.json"))[2:]
tab=json.load(open("tab_items.json"))
fdoss=list(csv.DictReader(open("base_dossiers_fichiers.csv")))
alldata=json.load(open("all_data.json"))

# ---- Registre des FACTURES IRSH (source: Suivi Factures + onglets + mails) ----
registre=[
 # num, date, montant, etat(mail/fichier), note
 ["F1225-01-IRSH","2026-01-15","2840","ANNULÉE (DARMENDRAIL) → 200€ résiduel repris en F2026-15","Mail 28/04: 'la facture F1225-01 annulée'"],
 ["F1225-02-IRSH","2026-01-15","4800→révisée","Payée (08/05)","SURFACTURATION: facturé 3250/4800 mais DIA PERRIERE 2065 → révisée (mail 23-24/04)"],
 ["F1225-03..13-IRSH","2026-01-15","~","Payées","Lot janvier"],
 ["F1225-14-IRSH","2026-02-11","3914,66","Payée (08/05)","Détail virement 18/05"],
 ["F1225-15REV","2026-02-11","3355","Payée (30/04)","Révisée (dossier MANEVIT)"],
 ["F1225-16-IRSH","2026-02-11","4260","Payée (08/05)",""],
 ["F1225-17-IRSH","2026-02-11","4360","Payée (17/04)","Virement 7280 avec F2026-09"],
 ["F1225-18-IRSH","2026-02-11","4255","Payée","Impayée relancée 19/05 puis payée"],
 ["F2026-01..07-IRSH","2026-02/03","~","Payées",""],
 ["F2026-03REV","2026-03-09","2980","Payée (29/05)","Virement 1012.75 = 2980 - AV14 1967.25"],
 ["F2026-08-IRSH","2026-04-08","5130","Payée","Débloquée 21/05"],
 ["F2026-09-IRSH","2026-04-08","2920","Payée (17/04)","Virement 7280"],
 ["F2026-10-IRSH","2026-04-08","3835","Payée","Débloquée 21/05"],
 ["F2026-11REV","2026-04-08","3220","Payée (30/04)","Révisée"],
 ["F2026-12/13/14-IRSH","2026-04","~","Payées",""],
 ["F2026-15","2026-05","200","NON PAYÉE — à corriger à 100€","DARMENDRAIL DIAP133037: 100€ déjà payé sur F1225-01 (mail 18/06 & 09/07)"],
 ["F2026-16","2026-06-10","2460","Envoyée 10/06 — MOMAS(IP)+COLAS(solde)","Numéro EFFACÉ du suivi. Payée? F16 en attente"],
 ["F2026-17","2026-06-10","2100","Envoyée — DOUBLON de numéro signalé par compta","'j'ai deux factures avec le numéro F2026-17' (compta 10/06)"],
 ["F2026-18","2026-06-10","5010","Au paiement 10/07","MANSUY(IP)+BOUEILH. TISSAIRE 1930→avoir (BE 1390)"],
 ["F2026-19","2026-06-10","2450","Au paiement 10/07","HERREYRE+PANTANI+LARREDE (attente CRI/solde)"],
 ["F2026-20","2026-06-10","1500HT/1800TTC","—","LE FRANCOIS + FAUCONNIER (dépose-repose, TVA 20%)"],
 ["F2026-21","2026-06-10","3300","—","CHARLES+PONTE+DA SILVA (soldes non reçus)"],
 ["F2026-22","2026-06-10","2950","—","DISSAUX(-150)+HERVE(-100)+PEZOT(-250)"],
 ["F2026-23","2026-06-15","4850","NON PAYÉE (attente IP + solde)","Fichier indique 4890 → écart. Réel=4850 (mail 09/07). PELUHET+TISSAIRE+SUBERCAZE"],
 ["F2026-24","2026-06-15","2700","Soldes non reçus","CLAUDON+VENTURINI+BENEDE"],
 ["AV06","2026-04-24","-413,60","Payé (30/04)",""],
 ["AV07","2026-04-24","-1020","Payé — SUPERCHI ARLETTE","Réclamation assurance"],
 ["AV08..AV13","2026-04-28","~","Payés",""],
 ["AV14","2026-05-22","-1967,25","Payé — SUPERCHI ARLETTE (2e réclamation)","Compensé sur F2026-03REV"],
]

# ---- Événements / preuves mail (keyés par mots-clés client) ----
evidence=[
 {"date":"2026-06-10","from":"ets.lyessanitaire→compta@independanceroyale.com","subj":"Factures des douche posées-2026",
  "detail":"Envoi des factures des douches installées (lot F2026-16 et suivantes). PREUVE que ces factures existent et ont été transmises à IRSH.","tags":["F2026-16","F2026-17","F2026-18","F2026-19","F2026-20","F2026-21","F2026-22"]},
 {"date":"2026-06-10","from":"compta@independanceroyale.com","subj":"RE: Factures des douche posées-2026",
  "detail":"IRSH: refaire avec adresse IRSH Limoges + « j'ai DEUX factures avec le numéro F2026-17 » → DOUBLON de numérotation confirmé par le client.","tags":["F2026-17","DOUBLON"]},
 {"date":"2026-06-10","from":"ets.lyessanitaire","subj":"Re: Factures rectifiées",
  "detail":"Montants ajustés à la baisse: DA SILVA DIAP134483 -250€ (WC japonais compté 2x), DISSAUX DIAP134682 -150€ (pompe relevage non posée), HERVE DIAP134950 -100€ (entretoise non réalisée), PEZOT DIAP134873 -250€ (WC non installé).","tags":["DA","DISSAUX","HERVE","PEZOT"]},
 {"date":"2026-06-15","from":"ets.lyessanitaire","subj":"Re: … F2026-23 et F2026-24","detail":"Envoi de F2026-23 et F2026-24 à la compta IRSH.","tags":["F2026-23","F2026-24"]},
 {"date":"2026-06-12→16","from":"camille.bustreau ↔ ets","subj":"Facture F2026-18",
  "detail":"TISSAIRE DIAP134429 facturé 1930€; le BE valide 1390€ (700 forfait +200 meuble +490). Lyes ajoute 100€ évacuation. Corentin (R&D) valide. Lyes envoie un AVOIR le 16/06.","tags":["TISSAIRE","F2026-18","AVOIR"]},
 {"date":"2026-05-21→22","from":"camille.bustreau ↔ ets","subj":"Dossier SUPERCHI ARLETTE – 06",
  "detail":"IRSH demande un avoir de 1967,25€ (réclamation assurance/expertise). Lyes rappelle qu'un avoir AV07=1020€ existe déjà pour le même dossier. Nouvel avoir AV14 émis.","tags":["SUPERCHI","AV14","AV07"]},
 {"date":"2026-04-23→24","from":"alima.ihrab / camille.bustreau","subj":"paiement facture / Point factures",
  "detail":"IRSH bloque des paiements: montants DIA ne correspondent pas. Ex: F1225-02 PERRIERE MARIE CLAUDE DIAP133217 facturé 3250€ mais DIA=2065€ → refaire. SURFACTURATION.","tags":["PERRIERE","F1225-02","SURFACTURATION"]},
 {"date":"2026-04-28","from":"ets.lyessanitaire","subj":"Re: Point factures",
  "detail":"DARMENDRAIL ISABELLE: F1225-01 ANNULÉE; 200€ restent à régler → donneront F2026-15 (que la compta veut ramener à 100€ car 100€ déjà payés).","tags":["DARMENDRAIL","F1225-01","F2026-15"]},
 {"date":"2026-04-24","from":"sebastien.brionnaud","subj":"RE: Point factures",
  "detail":"COMMANDEUR COLETTE ET JEAN: WC en double commande (n'ont que des WC chasse ECO).","tags":["COMMANDEUR"]},
 {"date":"2026-06-09→07-06","from":"camille.bustreau (relances)","subj":"Dossiers … solde client non reçu",
  "detail":"Relances soldes clients non reçus (bloque la mise en paiement des factures): BOUEILH DIAP135040, HERREYRE DIAP135008, VENTURINI DIAP134394, COLAS DIAR86229, PONTE DIAP135307, CHARLES DIAP134952, PANTANI DIAP134837, PERBOST DIAP134422, DAL BO MARC DIAP134852, PINCON SERGE DIAP135287.","tags":["BOUEILH","HERREYRE","VENTURINI","COLAS","PONTE","CHARLES","PANTANI","PERBOST","DAL","PINCON"]},
 {"date":"2026-07-09","from":"camille.bustreau","subj":"RE: Factures restantes à payer",
  "detail":"Dernier état: restent F2026-15 (200€→100 DARMENDRAIL) et F2026-23 (4850€ SUBERCAZE, attente IP+solde). F2026-18 et F2026-19 au paiement le 10/07.","tags":["F2026-15","F2026-23","SUBERCAZE","DARMENDRAIL"]},
 {"date":"2026-07-02 / 06-10","from":"stephanie.bustreau","subj":"Annulations",
  "detail":"Dossiers ANNULÉS: DUBOUE GILLES _WS3515128 (02/07) et VERSAILLES ROSANNE ET ROGER _WS3501021 (10/06), tous deux 'de CORDINA FABRICE'.","tags":["DUBOUE","VERSAILLES","ANNULATION"]},
 {"date":"2026-07-07","from":"sebastien.brionnaud","subj":"pose PERRIN Sophie",
  "detail":"Litige technique: douche posée avec chaudière gaz dans le local — IRSH n'aurait pas validé. Rework DIAR134867 planifié.","tags":["PERRIN"]},
 {"date":"2026-03-23","from":"lesly@asheurope.com","subj":"Dossier FATIMA ABDOU ABDALLAH",
  "detail":"[Réseau ASH Europe, hors IRSH] Avoir 200€ demandé (SAV repris par un autre poseur). Avoir émis.","tags":["FATIMA","ASH","AVOIR"]},
]

# ---- Construire dossiers consolidés (par surname) ----
doss={}
def get(s):
    return doss.setdefault(s,{"surname":s,"client":"","cp":"","dia":set(),"order_date":"","crm_type":"","crm_status":"",
      "crm_date":"","pose_date":"","montant":"","invoice":"","in_files":False,"in_mail":False,"in_crm":False,
      "status":"","a_facturer":"","evidence":[]})
# mail orders
for ref,(cli,dep,dt) in mail.items():
    r=get(sn(cli)); r["client"]=r["client"] or cli; r["dia"].add(ref); r["cp"]=r["cp"] or dep
    if not r["order_date"] or dt<r["order_date"]: r["order_date"]=dt
    r["in_mail"]=True
# files
for fr in fdoss:
    if fr["prescripteur"]!="IRSH": continue
    r=get(sn(fr["client"])); r["client"]=r["client"] or fr["client"]; 
    if fr["ref"]: r["dia"].add(fr["ref"])
    r["cp"]=r["cp"] or fr["cp"]; r["pose_date"]=r["pose_date"] or fr["date_pose"][:10]
    r["montant"]=r["montant"] or fr["montant"]; r["in_files"]=True
    if fr["invoice_tab"]: r["invoice"]=r["invoice"] or fr["invoice_tab"]
    if fr["num_fac_suivi"] not in ("","OUI","NON"): r["invoice"]=r["invoice"] or fr["num_fac_suivi"]
# crm
for row in crm:
    row=(row+[""]*10)[:10]
    dia,typ,pri,denv,drdv,stat,cli,cp,ville,prod=row
    if not cli: continue
    r=get(sn(cli)); r["client"]=r["client"] or cli; r["dia"].add(dia); r["cp"]=r["cp"] or cp
    r["crm_type"]=typ; r["crm_status"]=stat; r["crm_date"]=drdv; r["in_crm"]=True
# attach evidence by tag(surname or invoice)
for e in evidence:
    for r in doss.values():
        if r["surname"] in e["tags"] or any(t in r["invoice"] for t in e["tags"] if t.startswith("F")):
            r["evidence"].append({"date":e["date"],"from":e["from"],"subj":e["subj"],"detail":e["detail"]})
# statut synthèse
for r in doss.values():
    inv=bool(r["invoice"])
    if inv: r["status"]="Facturée"; r["a_facturer"]="Non (facturée)"
    elif r["in_crm"] and r["crm_status"]=="Posée/Effectuée":
        r["status"]="Réalisée NON facturée"; r["a_facturer"]="OUI"
    elif r["in_crm"] and r["crm_status"] in ("Planifiée","A Planifier","En attente matériel","Client Repousse","Stand by"):
        r["status"]="Commande en cours ("+r["crm_status"]+")"; r["a_facturer"]="Pas encore"
    elif r["in_mail"] and not r["in_files"]:
        r["status"]="Commande reçue (mail) — non suivie"; r["a_facturer"]="À vérifier"
    else: r["status"]="À vérifier"; r["a_facturer"]="À vérifier"
    r["dia"]=sorted(r["dia"])

master={"generated":"2026-07-09","perimetre":"IRSH / Indépendance Royale — 2026",
        "dossiers":sorted(doss.values(),key=lambda x:x["client"]),
        "registre_factures":registre,"evidence":evidence}
json.dump(master,open("master.json","w"),ensure_ascii=False)
from collections import Counter
print("Dossiers consolidés:",len(master["dossiers"]))
print(Counter(d["status"] for d in master["dossiers"]))
print("Factures au registre:",len(registre),"| Événements-preuves:",len(evidence))
