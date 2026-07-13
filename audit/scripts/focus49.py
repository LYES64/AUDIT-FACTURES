#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Focus sur les dossiers 'Commande reçue — à vérifier' :
   applique les verdicts issus des MAILS (soldes clients, poses, plannings, annulations)
   -> reclasse en Facturé ceux dont la pose est prouvée par mail, note les autres.
"""
import json, csv

m = json.load(open("audit/data/master4.json", encoding="utf-8"))
D = m["dossiers"]

# fragment de nom (MAJ) -> (verdict, note preuve mail)
# verdict: FACTURE (pose prouvée par mail -> facturée série F), PROBABLE (activité mail), CONFIRMER (dormant)
EVID = {
 # --- Posé prouvé par mail (date d'intervention citée par la compta IRSH) => facturé série F ---
 "BONJEAN":            ("FACTURE", "Posé 31/01/2026 — solde client suivi par IRSH"),
 "BIBE":               ("FACTURE", "Posé 02/02/2026 — solde client suivi par IRSH"),
 "BOUCHER GILBERT":    ("FACTURE", "Posé 16/02/2026 — solde client suivi par IRSH"),
 "CLOUET":             ("FACTURE", "Posé 18/02/2026 — solde 4 784€ suivi par IRSH"),
 "SCORDO":             ("FACTURE", "Posé 09/02/2026 — solde 5 250€ suivi par IRSH"),
 "GUIGO":              ("FACTURE", "Posé 23/02/2026 — solde 5 345€ suivi par IRSH"),
 "VANDURME":           ("FACTURE", "Posé 24/02/2026 — solde 4 450€ suivi par IRSH"),
 "PEROTTINO":          ("FACTURE", "Posé 17/02/2026 — CRI fourni (Julien Brisset)"),
 "MANAS":              ("FACTURE", "Posé 05/03/2026 — solde 4 549€ suivi par IRSH"),
 "MAILLARD":           ("FACTURE", "Posé 11/03/2026 — solde 3 920€ suivi par IRSH"),
 "DAL-BO CLEMENTINE":  ("FACTURE", "Posé 16/03 + 05/05/2026 — soldes suivis par IRSH"),
 "BURTON":             ("FACTURE", "Posé 19/11/2025 — solde suivi par IRSH"),
 "LARROUCAU":          ("FACTURE", "Posé 17/12/2025 — solde suivi par IRSH"),
 "DUPLE":              ("FACTURE", "Posé 29/12/2025 — solde suivi par IRSH"),
 "JAILLON":            ("FACTURE", "Installé — avis client transmis 06/03/2026"),
 # --- Pose très probable (activité mail : matériel livré / modif DIAP / CRI) ---
 "KABANTCHENKO":       ("PROBABLE", "Matériel livré 06/02 + travaux supp. — pose probable"),
 "JACOMINO":           ("PROBABLE", "Modif DIAP (pompe non posée) — pose faite"),
 "BERTHELOT":          ("PROBABLE", "Matériel livré 16/02 (GEODIS)"),
 "LHERITIER":          ("PROBABLE", "Modif DIAP +100€ (saignée évacuation)"),
 "LASSUS":             ("PROBABLE", "Modif DIAP +200€ FHS"),
 "DEBLONDE":           ("PROBABLE", "Modif DIAP +150€ FHS"),
 "KLELIFA":            ("PROBABLE", "Intervention 15/04/2026 (SAV/rework) — CRI demandé"),
 # --- Poses vues côté planning/fichier mais SANS preuve mail directe -> à confirmer sur PDF F04-07 ---
 "IGLESIAS":           ("CONFIRMER", "Pose de février probable (série F04-07) — à confirmer sur PDF"),
 "CASTEJON":           ("CONFIRMER", "Pose de février probable (série F04-07) — à confirmer sur PDF"),
 "ZIOLKOWSKI":         ("CONFIRMER", "Pose de février probable (série F04-07) — à confirmer sur PDF"),
 "FROMONT":            ("CONFIRMER", "Pose de février probable (série F04-07) — à confirmer sur PDF"),
 "CHAMAK":             ("CONFIRMER", "Pose de février probable (série F04-07) — à confirmer sur PDF"),
 "VERGE BRIGITTE":     ("CONFIRMER", "Pose ~30/03 probable — à confirmer sur PDF"),
 "ZUBIETA":            ("CONFIRMER", "Pose ~30/03 probable — à confirmer sur PDF"),
 "WEBER RAYMOND":      ("CONFIRMER", "Pose ~31/03 probable — à confirmer sur PDF"),
 "JUZANS":             ("CONFIRMER", "Pose du 12/02 REPORTÉE — statut à confirmer"),
 # --- Dormant : seule la DIA reçue, aucune autre trace (probable non-abouti / annulé) ---
 "ARBERET":            ("CONFIRMER", "DIA reçue 03/02, aucune autre trace"),
 "ARMAND LAURENT":     ("CONFIRMER", "DIA reçue 13/05, aucune autre trace (récent)"),
 "BOCHATEY":           ("CONFIRMER", "DIA reçue 13/02, aucune autre trace"),
 "CASERIO":            ("CONFIRMER", "DIA reçue 15/04, aucune autre trace"),
 "COSTA FRANCE":       ("CONFIRMER", "DIA reçue 13/05, aucune autre trace (récent)"),
 "DARMAGNAC":          ("CONFIRMER", "DIA redemandée 27/01, pas de pose tracée"),
 "DUNKLEY":            ("CONFIRMER", "DIA reçue 20/03, aucune autre trace"),
 "GOUDARD":            ("CONFIRMER", "DIA reçue (2 réf.), aucune pose tracée"),
 "GRAS ESTELLE":       ("CONFIRMER", "DIA reçue 13/05, aucune autre trace (récent)"),
 "GUDE":               ("CONFIRMER", "DIA reçue 23/04, aucune autre trace"),
 "HADJ CHIKH":         ("CONFIRMER", "DIA reçue 20/02, aucune autre trace"),
 "LUPFER":             ("CONFIRMER", "DIA reçue 27/01, aucune autre trace"),
 "MATHEU":             ("CONFIRMER", "DIA reçue 05/01, aucune autre trace"),
 "MICHEL FRANCISCO":   ("CONFIRMER", "DIA reçue 13/05, aucune autre trace (récent)"),
 "RAMBAUD":            ("CONFIRMER", "DIA/DIAV reçue 22/04, aucune pose tracée"),
 "RUGGERI":            ("CONFIRMER", "DIA redemandée 19/01, pas de pose tracée"),
 "SAUTIER":            ("CONFIRMER", "DIA reçue 13/03, aucune autre trace"),
 "SOLER":              ("CONFIRMER", "DIA reçue 20/04, aucune autre trace"),
}

def find(cu):
    for frag, v in EVID.items():
        if frag in cu:
            return v
    return None

# --- Annulations confirmées par mail (Stéphanie Bustreau) ---
CANCELLED = {"DUBOUE": "Annulé par IRSH (mail Stéphanie 02/07/2026)"}
for r in D:
    cu = r["client"].upper()
    for frag, note in CANCELLED.items():
        if frag in cu:
            r["fstat"] = "Hors facturation"; r["pose"] = "Non"
            r["invoice"] = ""
            r["pose_src"] = note
            r["focus"] = "ANNULE"

focus_rows = []
n_fac = n_prob = n_conf = 0
for r in D:
    if r["fstat"] != "Commande reçue — à vérifier":
        continue
    cu = r["client"].upper()
    v = find(cu)
    if not v:
        v = ("CONFIRMER", "Aucune trace au-delà de la DIA reçue")
    verdict, note = v
    if verdict == "FACTURE":
        r["invoice"] = r.get("invoice") or "Facturé (série F 2026)"
        r["fstat"] = "Facturé"; r["pose"] = "Oui"
        n_fac += 1
    elif verdict == "PROBABLE":
        # posé + très probablement déjà facturé (série début 2026) -> Facturé, note "probable"
        r["invoice"] = r.get("invoice") or "Facturé (probable, à confirmer)"
        r["fstat"] = "Facturé"; r["pose"] = "Oui"
        n_prob += 1
    else:
        n_conf += 1
    r["focus"] = verdict
    r["pose_src"] = (r.get("pose_src", "") + (" · " if r.get("pose_src") else "") + note)
    focus_rows.append((r["client"], " ; ".join(r["dia"]),
                       {"FACTURE": "Facturé (posé, prouvé mail)",
                        "PROBABLE": "Posé probable (à confirmer)",
                        "CONFIRMER": "À confirmer / non abouti"}[verdict], note))

json.dump(m, open("audit/data/master4.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

with open("audit/IRSH_Focus_commandes_a_verifier.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Nom de chantier", "N° DIA", "Verdict", "Preuve / note (source: mails IRSH)"])
    for row in sorted(focus_rows, key=lambda x: (x[2], x[0])):
        w.writerow(row)

print(f"Focus 49 dossiers : Facturé(prouvé)={n_fac}  Posé probable={n_prob}  À confirmer={n_conf}")
print("Nouvelle répartition fstat:")
from collections import Counter
for k, v in Counter(r["fstat"] for r in D).items():
    print(f"  {k}: {v}")
