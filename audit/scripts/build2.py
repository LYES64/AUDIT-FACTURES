import json
m=json.load(open("master.json"))  # dossiers IRSH + evidence IRSH + anomalies IRSH

# ===== REGISTRE FACTURES IRSH (num, date, montant, paiement, source/detail) =====
# paiement: Payée / Non payée / Partielle / Avoir
reg_irsh=[
["F092025","2025-10-07","13100","Payée","Réglée 19/01/2026 (avec AV01/AV02, reçu 12111,04€) — fichier"],
["AV01 / AV02","2025-11","-988,96","Avoir","Réglés 19/01/2026 — fichier"],
["F1225-01→13-IRSH","2026-01-15","~46k","Payée","Réglées janv.→mai (fichier). Sauf F1225-01 ANNULÉE (DARMENDRAIL)"],
["F1225-02-IRSH","2026-01-15","4800→révisée","Payée","Virement 08/05 (détail Camille 18/05). SURFACTURATION corrigée (DIA PERRIERE 2065)"],
["F1225-14-IRSH","2026-02-11","3914,66","Payée","Virement 08/05 (19179,66€)"],
["F1225-15REV","2026-02-11","3355","Payée","Mise en paiement 28/04"],
["F1225-16-IRSH","2026-02-11","4260","Payée","Virement 08/05"],
["F1225-17-IRSH","2026-02-11","4360","Payée","Virement 7280€ le 17/04 (avec F2026-09)"],
["F1225-18-IRSH","2026-02-11","4255","Payée","Mise en paiement 19/05"],
["F2026-01→07-IRSH","2026-02/03","~","Payée","Réglées (fichier: avr.)"],
["F2026-03REV","2026-03-09","2980","Payée","Virement 1012,75€ le 29/05 (= 2980 − AV14 1967,25)"],
["F2026-08-IRSH","2026-04-08","5130","Payée","Débloquée/mise en paiement 21/05"],
["F2026-09-IRSH","2026-04-08","2920","Payée","Virement 7280€ 17/04"],
["F2026-10-IRSH","2026-04-08","3835","Payée","Mise en paiement 21/05"],
["F2026-11REV","2026-04-08","3220","Payée","Mise en paiement 28/04"],
["F2026-12/13-IRSH","2026-04-08","2830/5185","Payée","Mises en paiement 19/05"],
["F2026-14-IRSH","2026-04-13","3140","Payée","Fichier: réglée 08/05"],
["F2026-15","2026-05","200","Non payée","BLOQUÉE: à rééditer à 100€ (DARMENDRAIL, 100€ déjà payés) — mail 09/07"],
["F2026-16","2026-06-10","2460","Non payée","MOMAS(IP)+COLAS(solde). N° effacé du suivi. Mail 09/07: encore due"],
["F2026-17","2026-06-10","2100","Payée","Fichier: réglée 15/06. ⚠ DOUBLON de n° signalé par compta"],
["F2026-18","2026-06-10","5010","Payée (10/07)","Au paiement le 10/07 (mail 09/07). N° effacé du suivi"],
["F2026-19","2026-06-10","2450","Payée (10/07)","Au paiement le 10/07 (mail 09/07)"],
["F2026-20","2026-06-10","1800 TTC","Payée","Fichier: réglée 15/06 (dépose-repose, TVA 20%)"],
["F2026-21","2026-06-10","3300","Non payée","Soldes non reçus CHARLES+PONTE+DA SILVA (mail)"],
["F2026-22","2026-06-10","2950","Payée","Fichier: réglée 15/06"],
["F2026-23","2026-06-15","4850","Non payée","Attente IP + solde SUBERCAZE (mail 09/07). ⚠ fichier=4890, réel=4850"],
["F2026-24","2026-06-15","2700","Non payée","Soldes non reçus CLAUDON+VENTURINI+BENEDE (mail 09/07)"],
["AV06→AV14","2026-04/05","≈ −8575","Avoir","Réglés avr./mai. AV07 & AV14 = SUPERCHI ARLETTE"],
]

# ===== REGISTRE FACTURES BARROS (source: fichier + détail virements Marina 19/05) =====
reg_barros=[
["F082025","2025-08-16","6540","Non payée","Impayée (fichier) — antérieure 2026"],
["F0925","2026-01-13*","800","Payée","Virement 800€ 29/04 (Marina). *datée 09/01"],
["F1025-01 (10 25-1)","2026-01-09*","800","Payée","Virement 800€ 29/04 (Marina)"],
["F1025-02 (10 25-2)","2026-01-09*","4200","Payée","Inclus virement 25k€ 20/04"],
["F1025-03 (10 25-3)","2026-01-09*","2600","Payée","Inclus virement 25k€ 20/04"],
["F1025-04 (10 25-4)","2026-01-09*","4200","Payée","Inclus virement 25k€ 20/04"],
["F1125-01 (11 25-01)","2025-12-31*","4250","Payée","1300€ (20/04) + 2950€ (29/04) = soldée"],
["F1125-02 (11 25-02)","2025-12-31*","4050","Payée","Inclus virement 25k€ 20/04"],
["F1125-03","2026-01-13*","4200","Payée","Fichier: réglée 19/05"],
["F1125-04","2026-01-13*","2450","Payée","Fichier: réglée 19/05"],
["F1225","2026-01-13*","850","Payée","Fichier: réglée 19/05"],
["F122025","2026-01-13*","16740","Payée","Fichier: réglée 23/04"],
["F2026-B01","2026-06-08","13850","Non payée","Fichier: Pas Payée. ⚠ onglet=13580 (écart 270€)"],
["F2026-B02","2026-03-08","4250","Payée","Virement 20/04 (Marina)"],
["F2026-B03","2026-03-23","4100","Payée","Fichier"],
["F2026-B04","2026-03-08","4400","Payée","Virement 20/04 (Marina)"],
["F2026-B05","2026-03-23","3400","Non payée","Fichier: Pas Payée"],
["F2026-B06","2026-04-08","3600","Non payée","Fichier: Pas Payée"],
["F2026-B07","2026-04-08","2700","Payée","Fichier"],
["F2026-B08","2026-04-08","3200","Payée","Fichier"],
["F2026-B09","2026-06-15","4750","Non payée","Fichier: Pas Payée"],
["F2026-B10","2026-06-15","6265","Non payée","Fichier: Pas Payée"],
["(sans numéro)","—","7600","À finaliser","⚠ AUCUN mail: jamais transmise à Eco Shower. Montant interne = poses à facturer (brouillon)."],
["F2026-B11 (brouillon)","2026-06","4750","À finaliser","Brouillon (affiche 'B10'), JAMAIS envoyé par mail. À finaliser en vraie F2026-B11."],
["F2026-B12 (brouillon)","2026-06","0","À finaliser","Brouillon 0€, jamais transmis. Dernière facture ENVOYÉE = B10 (15/06)."],
]

reprise={
 "IRSH":{"derniere":"F2026-24-IRSH (15/06/2026, 2700€)","repartir":"F2026-25-IRSH",
   "avoir":"dernier avoir AV14 → prochain AV15",
   "note":"Séquence F2026 complète de 01 à 24 (numéros 16→24 avaient été effacés du suivi mais existent). Reprendre à 25."},
 "BARROS":{"derniere":"F2026-B10 (15/06/2026) — dernière facture RÉELLEMENT envoyée à Eco Shower (confirmé par mail du 15/06).",
   "repartir":"F2026-B11",
   "avoir":"aucun avoir Barros identifié en 2026",
   "note":"CONFIRMÉ: B11 (4750€), B12 (0€) et la ligne 7600€ n'ont JAMAIS été transmises (aucun mail) — ce sont des brouillons/poses à facturer. Repartir à F2026-B11 en finalisant ces brouillons. Le virement de 10 000€ du 07/07 n'est pas encore ventilé par Eco Shower (accès InterFast demandé le 09/07)."},
}

m["anomalies"] = [
 {"sev":"CRITIQUE","titre":"IRSH — Numéros F2026-16 à F2026-24 effacés du fichier de suivi",
  "preuve":"Suivi Factures lignes 47-55: montants sans numéro; onglets F2026-16..24 existent; envoi confirmé à compta IRSH le 10/06 et 15/06.",
  "constat":"Factures émises mais numéros retirés du suivi a posteriori. Manipulation du fichier, pas perte de CA."},
 {"sev":"CRITIQUE","titre":"IRSH — Doublon de numéro F2026-17",
  "preuve":"Mail compta IRSH 10/06: « j'ai deux factures avec le numéro F2026-17 ».",
  "constat":"Deux factures avec le même numéro → risque comptable."},
 {"sev":"ÉLEVÉE","titre":"IRSH — Surfacturation vs DIA (F1225-02 PERRIERE)",
  "preuve":"Mail 23/04: F1225-02 PERRIERE DIAP133217 facturé 3250€ mais DIA=2065€.",
  "constat":"Facturation supérieure au barème DIA; révision demandée."},
 {"sev":"ÉLEVÉE","titre":"IRSH — PINCON SERGE réalisé mais non facturé",
  "preuve":"Nombreux DIA/rework/visap CRM 'Posée/Effectuée'; pose au 'non facturé' ~1790€; aucune facture retrouvée.",
  "constat":"À facturer/vérifier en priorité."},
 {"sev":"ÉLEVÉE","titre":"IRSH — F2026-15 (DARMENDRAIL) mauvais montant, non payée",
  "preuve":"Mails 18/06 & 09/07: F1225-01 annulée, 100€ déjà payés → F2026-15 doit être 100€.",
  "constat":"Facture bloquée, à rééditer à 100€."},
 {"sev":"MOYENNE","titre":"IRSH — Écart F2026-23 (fichier 4890 / réel 4850)","preuve":"Mail compta 09/07 = 4850€.","constat":"Fichier divergent de 40€."},
 {"sev":"MOYENNE","titre":"IRSH — Double avoir SUPERCHI (AV07+AV14)","preuve":"Mails 21-22/05.","constat":"Deux avoirs même dossier (assurance)."},
]
m["anomalies"] += [
 {"sev":"CRITIQUE","titre":"BARROS — Antidatage des factures (demandé par Eco Shower)",
  "preuve":"Mails 19-20/01/2026 Carolina Silva: « il faudrait toutes les factures avec la date de 2025 et pas 2026 ». Compta Marina 19/05 référence F11 25-01/02 datées 31/12/2025 et F10 25-x datées 09/01/2026.",
  "constat":"Factures de poses oct./nov. 2025 datées fin 2025-début 2026 à la demande du donneur d'ordre. À faire valider par l'expert-comptable (exercice/TVA)."},
 {"sev":"ÉLEVÉE","titre":"BARROS — B11/B12 hors suivi, ligne 7600€, doublon 'B10'",
  "preuve":"Fichier Suivi Factures Barros s'arrête à B10; onglets B11 (4750€) et B12 (0€) présents; ligne 7600€ sans n°; B11 et B12 affichent 'F2026-B10'.",
  "constat":"Numérotation Barros non maîtrisée en fin de séquence. Risque de doublon/omission. À régulariser avant toute nouvelle facture."},
 {"sev":"ÉLEVÉE","titre":"BARROS — Soldes clients manquants + client hors fichier (HARTMANN)",
  "preuve":"Mail Marina 02/04: BOULAY 8400€, ECHEVERRA 11925€, DOYHAMBOURRE 3850,01€, HARTMANN Henri 1500€ espèces.",
  "constat":"HARTMANN Henri absent du fichier de suivi → dossier potentiellement non tracé. Soldes clients à recouvrer/remonter."},
 {"sev":"MOYENNE","titre":"BARROS — Encours 31k€ puis virement 10k€ (07/07) à imputer",
  "preuve":"Mail ETS 19/05 (encours ~31000€); notif Qonto 07/07 (virement 10000€ de BARROS ECO).",
  "constat":"Rapprochement à finaliser: imputer le 10k€ sur B01/B05/B06/B09/B10."},
]
# evidence Barros
m["evidence"] += [
 {"date":"2026-05-19","from":"marina.delage@ecoshower.fr","subj":"Détail des factures réglées",
  "detail":"Détail: 25k€ (20/04)=F10 25-2/3/4 + F11 25-01(acompte1300)/02 + B02 + B04 ; 800+800+2950 (29/04)= F0925 + F10 25-1 + solde F11 25-01. Confirme le fichier.","tags":["BARROS"]},
 {"date":"2026-04-02","from":"marina.delage@ecoshower.fr","subj":"CLIENTS EN ATTENTE DE PAIEMENTS",
  "detail":"Soldes clients manquants: BOULAY 8400€, HARTMANN Henri 1500€ espèces, ECHEVERRA 11925€, DOYHAMBOURRE 3850,01€.","tags":["BARROS","BOULAY","ECHEVERRIA","DOYHAMBOURE"]},
 {"date":"2026-01-19→21","from":"carolina.silva@ecoshower.fr ↔ ETS","subj":"Factures date 2025",
  "detail":"Eco Shower: « il faudrait toutes les factures avec la date de 2025 et pas 2026 ». ETS renvoie les factures datées 2025. → antidatage assumé.","tags":["BARROS"]},
 {"date":"2026-04-20","from":"carolina.silva@ecoshower.fr (auto)","subj":"Changement d'interlocuteur",
  "detail":"Départ de Carolina Silva d'Ecoshower/Barros Eco au 21/04/2026; Marina Delage reprend.","tags":["BARROS"]},
]

m["reg_irsh"]=reg_irsh
m["reg_barros"]=reg_barros
m["reprise"]=reprise
# retirer l'ancien registre IRSH simple si présent
m.pop("registre_factures",None)
json.dump(m,open("master2.json","w"),ensure_ascii=False)
# stats paiement
def stat(reg):
    from collections import Counter
    return Counter(r[3].split(" ")[0] for r in reg)
print("IRSH:",stat(reg_irsh))
print("BARROS:",stat(reg_barros))
print("OK master2.json")
