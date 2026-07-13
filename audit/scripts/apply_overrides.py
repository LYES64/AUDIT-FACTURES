#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fusionne les saisies manuelles du client (user_overrides.json) dans master4.json,
   en RECALCULANT le statut de facturation avec la même logique que l'outil.
   -> ces choix deviennent la base officielle (visibles même sans localStorage)."""
import json
m = json.load(open("audit/data/master4.json", encoding="utf-8"))
ovr = json.load(open("audit/data/user_overrides.json", encoding="utf-8"))
POSE, FAC, AF = ovr.get("pose", {}), ovr.get("fac", {}), ovr.get("afac", {})
by = {}
for r in m["dossiers"]:
    if r.get("dia"): by.setdefault(r["dia"][0], r)

def recomp(r):
    if r.get("invoice", "").strip(): return "Facturé"
    if r.get("afac_def", "Oui") == "Non": return "Hors facturation"
    if r["pose"] == "Oui": return "Réalisée — NON facturée"
    if r["pose"] == "Non": return "En cours — pas encore posée" if (r.get("future") or r.get("enc")) else "Commande reçue — à vérifier"
    return "Commande reçue — à vérifier"

changes = []
def touch(k):
    r = by.get(k)
    return r

for k, v in POSE.items():
    r = touch(k)
    if r: r["pose"] = v; r.setdefault("_um", []).append("Posé="+v)
for k, v in FAC.items():
    r = touch(k)
    if r and v == "oui" and not r.get("invoice", "").strip():
        r["invoice"] = "Facturé (saisie manuelle)"; r.setdefault("_um", []).append("Facturée=oui")
    elif r and v == "non":
        r["invoice"] = ""; r.setdefault("_um", []).append("Facturée=non")
for k, v in AF.items():
    r = touch(k)
    if r: r["afac_def"] = v; r.setdefault("_um", []).append("Àfacturer="+v)

for r in m["dossiers"]:
    if r.get("_um"):
        old = r["fstat"]; r["fstat"] = recomp(r)
        note = "Saisie manuelle client (" + ", ".join(r["_um"]) + ")"
        r["pose_src"] = (r.get("pose_src", "") + (" · " if r.get("pose_src") else "") + note)
        r["um"] = True
        changes.append((r["client"], r["dia"][0], old, r["fstat"]))
        del r["_um"]

json.dump(m, open("audit/data/master4.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("=== dossiers modifiés par vos saisies (", len(changes), ") ===")
for c in sorted(changes, key=lambda x: x[3]):
    print(f"  {c[0][:32]:32} {c[1]:12}  {c[2]:28} -> {c[3]}")
print("\n=== nouvelle répartition ===")
for k, v in Counter(r["fstat"] for r in m["dossiers"]).items():
    print(f"  {k}: {v}")
