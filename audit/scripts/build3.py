#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enrichit master2.json -> master3.json :
   - Complète le mapping FACTURE -> CHANTIER (source = MAILS IRSH : registre compta
     Camille Bustreau 18/06+09/07, point compta 17/04, envois de factures).
   - Ajoute un statut de facturation clair par dossier (fstat) et le n° de facture rattaché.
   - Clé de rapprochement : nom de chantier (principale) + n° DIA (secondaire).
   NB: on NE se fie PAS au fichier Suivi IRSH (incomplet). Sources = boîte mail + CRM InterFast.
"""
import json, re, datetime

m = json.load(open("audit/data/master2.json", encoding="utf-8"))
D = m["dossiers"]

# ---------------------------------------------------------------------------
# 1) MAPPING FACTURE -> CHANTIER, confirmé par les MAILS d'IRSH (pas le fichier)
#    (invoice, [fragments de nom de chantier trouvés sur la facture / le registre])
# ---------------------------------------------------------------------------
INVOICE_MAP = [
    # --- Séries 2025 facturées début 2026 (registre compta IRSH 17/04) ---
    ("F1225-02", ["PERRIERE"]),
    ("F1225-08", ["RAINAUD"]),
    ("F1225-10", ["DARMENDRAIL"]),
    ("F1225-14", ["PARPAILLON"]),
    ("F1225-15", ["MANEVIT"]),
    ("F1225-16", ["JEANJEAN", "VERRIER"]),
    ("F1225-18", ["BAUER"]),
    # --- F2026-01..14 ---
    ("F2026-01", ["MOUHEL", "ROLLAND PHILIPPE", "VEUILLAULT"]),
    ("F2026-02", ["FRIMAS", "CORVISIER", "WORMSER"]),
    ("F2026-03", ["LECOQ", "CHAMPENOIS"]),
    ("F2026-08", ["GRIN NATHALIE"]),
    ("F2026-10", ["COMMANDEUR"]),
    ("F2026-11", ["PASTORINO"]),
    ("F2026-12", ["ATZORI"]),
    ("F2026-13", ["CABRIERE"]),
    ("F2026-14", ["PERRIN SOPHIE"]),
    ("F2026-15", ["DARMENDRAIL"]),          # complément 100€
    # --- F2026-16..24 (registre Camille 18/06 + onglets, corroborés par mail) ---
    ("F2026-16", ["MOMAS", "COLAS GUY", "MOYA"]),
    ("F2026-17", ["SAINT MARTIN", "SAINT-MARTIN", "DESLUX", "HOSPITAL"]),
    ("F2026-18", ["MANSUY", "BOUEILH"]),
    ("F2026-19", ["HERREYRE", "LARREDE", "PANTANI"]),
    ("F2026-20", ["LE FRANCOIS", "FAUCONNIER"]),
    ("F2026-21", ["CHARLES ALAIN", "PONTE", "DA SILVA"]),
    ("F2026-22", ["DISSAUX", "HERVE JOSYANE", "PEZOT"]),
    ("F2026-23", ["PELUHET", "SUBERCAZE"]),
    ("F2026-24", ["CLAUDON", "VENTURINI", "BENEDE"]),
]
# TISSAIRE = 2 poses : DIAP134429 (F2026-18) et DIAP134414 (F2026-23)
SPECIAL = {"TISSAIRE": "F2026-18 / F2026-23"}

def match_invoice(client):
    c = client.upper()
    for key, ref in SPECIAL.items():
        if key in c:
            return ref
    hits = []
    for inv, frags in INVOICE_MAP:
        for f in frags:
            if f in c:
                hits.append(inv); break
    # dédup en gardant l'ordre
    seen = []
    for h in hits:
        if h not in seen:
            seen.append(h)
    return " / ".join(seen) if seen else ""

# ---------------------------------------------------------------------------
# 2) Poses réalisées NON facturées :
#    - confirmé CRM InterFast (crm_status == "Posée/Effectuée") sans facture
#    - + poses signalées dans les mails/brouillon de juin (à finaliser -> F2026-25+)
# ---------------------------------------------------------------------------
POSE_SIGNALEE = ["MINGAM", "RANDRIAMANANA", "MONTEAU", "PERBOST", "VERNER ELIANE",
                 "BOURCEAU", "MAYZAUD", "BOUCHERARA", "DALBO MARC", "DAL BO MARC"]

EN_COURS_CRM = {"Planifiée", "A Planifier", "En attente matériel",
                "Client Repousse", "Stand by"}

def norm(s): return re.sub(r"\s+", "", (s or "").upper())

added = 0
for r in D:
    inv = r.get("invoice", "").strip()
    if not inv:
        inv = match_invoice(r["client"])
        if inv:
            r["invoice"] = inv
            added += 1
    facture = bool(r.get("invoice", "").strip())
    crm = r.get("crm_status", "")
    client_up = r["client"].upper()
    pose_signalee = any(f in client_up for f in POSE_SIGNALEE)
    pose_crm = (crm == "Posée/Effectuée")

    if facture:
        r["fstat"] = "Facturé"
    elif pose_crm or pose_signalee:
        r["fstat"] = "Réalisée — NON facturée"
    elif crm in EN_COURS_CRM or r.get("status", "").startswith("Commande en cours"):
        r["fstat"] = "En cours — pas encore posée"
    else:
        r["fstat"] = "Commande reçue — à vérifier"

    # drapeau pose (pour filtres)
    r["pose"] = "Oui" if (pose_crm or pose_signalee or facture) else ("À vérifier" if r["fstat"].startswith("Commande") else "Non")
    # source de la pose
    src = []
    if pose_crm: src.append("CRM InterFast")
    if pose_signalee: src.append("mail/brouillon 06-2026")
    r["pose_src"] = ", ".join(src)

# ---------------------------------------------------------------------------
# 3) Ajout DIA récentes vues en mail et absentes (ex: BARRERE DIAP135671)
# ---------------------------------------------------------------------------
present = set()
for r in D:
    for x in r.get("dia", []):
        present.add(norm(x))

NEW = [
    # (client, cp, dia, order_date)
    ("BARRERE MARIE JEANINE", "40", "DIAP135671", "2026-07-10"),
]
for client, cp, dia, od in NEW:
    if norm(dia) not in present:
        D.append({
            "surname": client.split()[0], "client": client, "cp": cp,
            "dia": [dia], "order_date": od, "crm_type": "", "crm_status": "",
            "crm_date": "", "pose_date": "", "montant": "", "invoice": "",
            "in_files": False, "in_mail": True, "in_crm": False,
            "status": "Commande reçue (mail) — non suivie",
            "a_facturer": "À vérifier", "evidence": [],
            "fstat": "Commande reçue — à vérifier", "pose": "À vérifier", "pose_src": "",
        })

# ---------------------------------------------------------------------------
# 4) Récap
# ---------------------------------------------------------------------------
from collections import Counter
m["dossiers"] = D
m["generated"] = datetime.date.today().isoformat()
m["fstat_counts"] = dict(Counter(r["fstat"] for r in D))
json.dump(m, open("audit/data/master3.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

print("invoices ajoutées par rapprochement mail:", added)
print("total dossiers:", len(D))
print("répartition fstat:", m["fstat_counts"])
print("\n== RÉALISÉES NON FACTURÉES ==")
for r in D:
    if r["fstat"].startswith("Réalisée"):
        print(" ", r["client"], "|", ";".join(r["dia"]), "|", r["pose_src"])
