#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""master2.json + export COMPIEXE à jour (11/07) -> master4.json
   Règle demandée : dès que la DATE RDV (pose) est passée, l'intervention est
   considérée RÉALISÉE (les statuts de l'export ne sont pas à jour).
   Sources = boîtes mail + CRM InterFast/Compiexe (PAS le fichier de suivi).
"""
import json, re, datetime, zipfile
from xml.etree import ElementTree as ET
from collections import Counter

TODAY = datetime.date(2026, 7, 11)

# ---------------------------------------------------------------------------
# 0) Lecture export COMPIEXE à jour (XML brut, openpyxl plante sur les fills)
# ---------------------------------------------------------------------------
def read_compiexe(path):
    z = zipfile.ZipFile(path)
    ns = {'a': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    ss = []
    if 'xl/sharedStrings.xml' in z.namelist():
        t = ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in t.findall('a:si', ns):
            ss.append(''.join(x.text or '' for x in si.iter() if x.tag.endswith('}t')))
    t = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    def celltext(c):
        typ = c.get('t')
        if typ == 'inlineStr':
            return ''.join(x.text or '' for x in c.iter() if x.tag.endswith('}t'))
        v = c.find('a:v', ns)
        if v is None: return ''
        if typ == 's': return ss[int(v.text)]
        return v.text or ''
    colof = lambda ref: re.match(r'[A-Z]+', ref).group()
    out = []
    for r in t.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
        d = {}
        for c in r.findall('a:c', ns):
            d[colof(c.get('r'))] = celltext(c)
        out.append(d)
    return out

def pdate(s):
    try:
        d, m, y = s.strip().split('/'); return datetime.date(int(y), int(m), int(d))
    except Exception:
        return None

norm = lambda s: re.sub(r'\s+', '', (s or '').upper())

rows = read_compiexe("audit/sources/CRM_IRSH_2026-07-11.xlsx")
CRM = {}   # DIA -> dict
for r in rows[2:]:
    dia = r.get('A', '').strip()
    if not dia.upper().startswith('DIA'):
        continue
    CRM[norm(dia)] = {
        "dia": dia, "type": r.get('B', '').strip(), "envoi": r.get('D', '').strip(),
        "rdv": r.get('E', '').strip(), "rdv_d": pdate(r.get('E', '')),
        "statut": r.get('F', '').strip(), "client": r.get('G', '').strip(),
        "cp": r.get('H', '').strip(), "ville": r.get('I', '').strip(),
    }

# ---------------------------------------------------------------------------
# 1) Base dossiers (master2) + mapping facture->chantier (mails IRSH)
# ---------------------------------------------------------------------------
m = json.load(open("audit/data/master2.json", encoding="utf-8"))
D = m["dossiers"]

INVOICE_MAP = [
    ("F1225-02", ["PERRIERE"]), ("F1225-08", ["RAINAUD"]), ("F1225-10", ["DARMENDRAIL"]),
    ("F1225-14", ["PARPAILLON"]), ("F1225-15", ["MANEVIT"]), ("F1225-16", ["JEANJEAN", "VERRIER"]),
    ("F1225-18", ["BAUER"]),
    ("F2026-01", ["MOUHEL", "ROLLAND PHILIPPE", "VEUILLAULT"]),
    ("F2026-02", ["FRIMAS", "CORVISIER", "WORMSER"]),
    ("F2026-03", ["LECOQ", "CHAMPENOIS"]), ("F2026-08", ["GRIN NATHALIE"]),
    ("F2026-10", ["COMMANDEUR"]), ("F2026-11", ["PASTORINO"]), ("F2026-12", ["ATZORI"]),
    ("F2026-13", ["CABRIERE"]), ("F2026-14", ["PERRIN SOPHIE"]), ("F2026-15", ["DARMENDRAIL"]),
    ("F2026-16", ["MOMAS", "COLAS GUY", "MOYA"]),
    ("F2026-17", ["SAINT MARTIN", "SAINT-MARTIN", "DESLUX", "HOSPITAL"]),
    ("F2026-18", ["MANSUY", "BOUEILH"]), ("F2026-19", ["HERREYRE", "LARREDE", "PANTANI"]),
    ("F2026-20", ["LE FRANCOIS", "FAUCONNIER"]), ("F2026-21", ["CHARLES ALAIN", "PONTE", "DA SILVA"]),
    ("F2026-22", ["DISSAUX", "HERVE JOSYANE", "PEZOT"]), ("F2026-23", ["PELUHET", "SUBERCAZE"]),
    ("F2026-24", ["CLAUDON", "VENTURINI", "BENEDE"]),
]
SPECIAL = {"TISSAIRE": "F2026-18 / F2026-23"}
def match_invoice(client):
    c = client.upper()
    for k, ref in SPECIAL.items():
        if k in c: return ref
    seen = []
    for inv, frags in INVOICE_MAP:
        if any(f in c for f in frags) and inv not in seen:
            seen.append(inv)
    return " / ".join(seen)

POSE_SIGNALEE = ["MINGAM", "RANDRIAMANANA", "MONTEAU", "PERBOST", "VERNER ELIANE",
                 "BOURCEAU", "MAYZAUD", "BOUCHERARA", "DALBO MARC", "DAL BO MARC"]

def dossier_rdv(r):
    """Retourne (rdv_str, rdv_date, statut_frais, type_frais) le plus pertinent :
       priorité à l'export à jour ; sinon date CRM historique du master2."""
    best_str, best_d, stat, typ = "", None, r.get("crm_status", ""), r.get("crm_type", "")
    for x in r.get("dia", []):
        c = CRM.get(norm(x))
        if c:
            stat, typ = c["statut"], c["type"]
            if c["rdv_d"] and (best_d is None or c["rdv_d"] > best_d):
                best_d, best_str = c["rdv_d"], c["rdv"]
    if best_d is None:  # pas dans l'export à jour -> date CRM historique
        d = pdate(r.get("crm_date", ""))
        if d: best_d, best_str = d, r.get("crm_date", "")
    return best_str, best_d, stat, typ

added_inv = 0
for r in D:
    if not r.get("invoice", "").strip():
        inv = match_invoice(r["client"])
        if inv:
            r["invoice"] = inv; added_inv += 1
    facture = bool(r.get("invoice", "").strip())

    rdv_str, rdv_d, stat, typ = dossier_rdv(r)
    if stat: r["crm_status"] = stat
    if typ: r["crm_type"] = typ
    r["rdv"] = rdv_str

    client_up = r["client"].upper()
    realized = (
        (rdv_d is not None and rdv_d < TODAY) or           # RÈGLE : RDV passé = réalisé
        (r.get("crm_status") == "Posée/Effectuée") or
        any(f in client_up for f in POSE_SIGNALEE) or
        (r.get("a_facturer") == "OUI")
    )
    future_rdv = (rdv_d is not None and rdv_d >= TODAY)

    enc = bool(future_rdv or r.get("crm_status") in {"A Planifier", "RDV à confirmer", "Client Repousse", "Stand by", "En attente matériel", "Planifiée"} or r.get("status", "").startswith("Commande en cours"))
    r["future"] = bool(future_rdv)
    r["enc"] = enc
    if facture:
        r["fstat"] = "Facturé"
    elif realized:
        r["fstat"] = "Réalisée — NON facturée"
    elif enc:
        r["fstat"] = "En cours — pas encore posée"
    else:
        r["fstat"] = "Commande reçue — à vérifier"

    r["pose"] = "Oui" if (realized or facture) else ("À vérifier" if r["fstat"].startswith("Commande") else "Non")
    src = []
    if rdv_d is not None and rdv_d < TODAY: src.append("RDV pose passé (" + rdv_str + ")")
    if r.get("crm_status") == "Posée/Effectuée": src.append("CRM Compiexe : Posée/Effectuée")
    if any(f in client_up for f in POSE_SIGNALEE): src.append("mail/brouillon 06-2026")
    r["pose_src"] = " · ".join(dict.fromkeys(src))

# --- Corrections client (11/07) : factures créées dans InterFast, invisibles dans Gmail ---
MANUAL_FACTURE_FULL = ["BARTH", "BOUCHERARA", "ANORGA", "DRAMCOURT", "NOBLET", "JACQUEMIN"]
MANUAL_FACTURE_DIAV = ["PINCON", "MAILLON"]   # seule la DIAV/SAV a été facturée
for r in D:
    cu = r["client"].upper()
    if any(f in cu for f in MANUAL_FACTURE_FULL):
        if not r.get("invoice", "").strip():
            r["invoice"] = "Facturée (InterFast)"
        r["fstat"] = "Facturé"; r["pose"] = "Oui"
        r["pose_src"] = (r.get("pose_src", "") + " · facture créée dans InterFast").strip(" ·")
    elif any(f in cu for f in MANUAL_FACTURE_DIAV):
        r["pose_src"] = (r.get("pose_src", "") + " · DIAV/SAV facturée dans InterFast (poses à facturer)").strip(" ·")

# ---------------------------------------------------------------------------
# 2) Ajout DIA de l'export à jour absentes des dossiers + BARRERE
# ---------------------------------------------------------------------------
present = set()
for r in D:
    for x in r.get("dia", []): present.add(norm(x))

for k, c in CRM.items():
    if k in present: continue
    facture = bool(match_invoice(c["client"]))
    rdv_d = c["rdv_d"]
    realized = (rdv_d is not None and rdv_d < TODAY) or c["statut"] == "Posée/Effectuée"
    fstat = ("Facturé" if facture else "Réalisée — NON facturée" if realized
             else "En cours — pas encore posée" if (rdv_d and rdv_d >= TODAY) or c["statut"] in {"A Planifier", "Planifiée", "Client Repousse", "Stand by", "RDV à confirmer"}
             else "Commande reçue — à vérifier")
    fut = bool(rdv_d and rdv_d >= TODAY)
    enc = bool(fut or c["statut"] in {"A Planifier", "Planifiée", "Client Repousse", "Stand by", "RDV à confirmer"})
    D.append({
        "surname": c["client"].split()[0] if c["client"] else k, "client": c["client"] or k,
        "cp": c["cp"], "dia": [c["dia"]], "order_date": "", "crm_type": c["type"],
        "crm_status": c["statut"], "crm_date": c["rdv"], "pose_date": "", "montant": "",
        "invoice": match_invoice(c["client"]), "in_files": False, "in_mail": False, "in_crm": True,
        "status": "CRM " + c["statut"], "a_facturer": "", "evidence": [], "rdv": c["rdv"],
        "future": fut, "enc": enc,
        "fstat": fstat, "pose": "Oui" if realized else ("Non" if fut else "À vérifier"),
        "pose_src": ("RDV pose passé (" + c["rdv"] + ")") if (rdv_d and rdv_d < TODAY) else ("CRM Posée/Effectuée" if c["statut"] == "Posée/Effectuée" else ""),
    })

NEW = [("BARRERE MARIE JEANINE", "40", "DIAP135671", "2026-07-10")]
present = {norm(x) for r in D for x in r.get("dia", [])}
for client, cp, dia, od in NEW:
    if norm(dia) not in present:
        D.append({"surname": client.split()[0], "client": client, "cp": cp, "dia": [dia],
                  "order_date": od, "crm_type": "", "crm_status": "", "crm_date": "", "pose_date": "",
                  "montant": "", "invoice": "", "in_files": False, "in_mail": True, "in_crm": False,
                  "status": "Commande reçue (mail)", "a_facturer": "À vérifier", "evidence": [],
                  "rdv": "", "future": False, "enc": True,
                  "fstat": "En cours — pas encore posée", "pose": "Non", "pose_src": ""})

# ---------------------------------------------------------------------------
# 3) PREUVES (mails réellement lus) reliées aux factures, avec lien Gmail
# ---------------------------------------------------------------------------
GM = "https://mail.google.com/mail/u/0/#all/"
PROOFS = [
 {"id": "p-0417",
  "date": "17/04/2026", "from": "camille.bustreau@independanceroyale.com (compta IRSH)",
  "subj": "Point factures restantes à payer",
  "gmail": GM + "19d9bbef868ee2bb",
  "covers": ["F1225-02","F1225-08","F1225-10","F1225-14","F1225-15","F1225-16","F1225-18",
             "F2026-03","F2026-08","F2026-10","F2026-11","F2026-12","F2026-13","F2026-14"],
  "body": ("Point compta IRSH — chaque facture est rattachée à son dossier + DIA :\n\n"
    "F1225-02 · Dossier PERRIERE MARIE CLAUDE - DIAP133217 (DIA à 2 065€)\n"
    "F1225-15 · Dossier MANEVIT JACQUES - DIAP130013 (déjà facturée sur 10002025)\n"
    "F1225-10 · Dossier DARMENDRAIL ISABELLE - DIAP133037 (déjà sur F1225-01)\n"
    "F1225-16 · JEANJEAN GENEVIEVE - DIAP132112 ; VERRIER RENE - DIAP133216 (avoir 1 250€)\n"
    "F1225-08 · RAINAUD SYLVIE - DIAP132481 (avoir 100€)\n"
    "F2026-03 · LECOQ ANNICK - DIAP133783 (IP) ; CHAMPENOIS FRANCOISE - DIAP133777 (avoir 100€)\n"
    "F1225-18 · BAUER BERNARD - DIAP130563 (solde client non reçu)\n"
    "F1225-14 · PARPAILLON PIERRETTE - DIAP133556 (avoir 150€)\n"
    "F2026-10 · COMMANDEUR COLETTE ET JEAN - DIAP134443 (IP)\n"
    "F2026-08 · GRIN NATHALIE ET LIONEL - DIAP133101 (IP)\n"
    "F2026-13 · CABRIERE MARIE ET DANIEL - DIAP133362 (SAV en cours)\n"
    "F2026-12 · ATZORI OLIVIER - DIAP133662 (photo WC manquante)\n"
    "F2026-14 · PERRIN SOPHIE - DIAP134059 (avoir 250€)\n"
    "F2026-11 · PASTORINO ALEXIS - DIAP134565 (avoir 100€)\n\n"
    "Avoirs demandés : DUGUET MURIEL ET LE BORGNE YVES 413,60€ ; SUPERCHI ARLETTE 1 020€.\n"
    "Nouvelle adresse de facturation : IRSH, 7 Allée Loewy, 87068 LIMOGES.")},
 {"id": "p-0618",
  "date": "18/06/2026 (repris le 09/07/2026)", "from": "camille.bustreau@independanceroyale.com (compta IRSH)",
  "subj": "Factures restantes à payer",
  "gmail": GM + "19eda2c536ba8317",
  "covers": ["F2026-15","F2026-16","F2026-18","F2026-19","F2026-21","F2026-23","F2026-24"],
  "body": ("Point compta IRSH — dossiers rattachés à chaque facture :\n\n"
    "F-2026-15 · DARMENDRAIL ISABELLE - DIAP133037 (facture attendue 100€)\n"
    "F2026-23 · SUBERCAZE JEAN - DIAP134675 (IP + solde client)\n"
    "F2026-24 · CLAUDON NICOLE - DIAP135020 ; VENTURINI JEAN - DIAP134394 ; BENEDE CATHERINE - DIAP135237\n"
    "F2026-19 · HERREYRE MARIETHERESE - DIAP135008 ; PANTANI ANTOINE - DIAP134837\n"
    "F2026-16 · MOMAS MICHEL - DIAP134529 (IP) ; COLAS GUY - DIAP134518 (solde)\n"
    "F2026-18 · MANSUY OLIVIER - DIAP134403 (IP) ; BOUEILH PASCAL - DIAP135040 (solde)\n"
    "F2026-21 · CHARLES ALAIN - DIAP134952 ; PONTE CATHERINE - DIAP135307 ; DA SILVA SILVINO - DIAP134483\n\n"
    "09/07 : « Les factures F2026-18 et F2026-19 seront au paiement demain. »")},
 {"id": "p-0309",
  "date": "09/03 → 13/04/2026", "from": "ets.lyessanitaire@gmail.com (envoyé à compta IRSH)",
  "subj": "Factures des douche posées-2026",
  "gmail": GM + "19ccff61f0774be9",
  "covers": ["F2026-04","F2026-05","F2026-06","F2026-07","F2026-09"],
  "body": ("Fil d'envoi des factures (PDF joints) : F2026-03, 04, 05, 06, 07 le 09/03 ; "
    "puis F2026-08, 09, 10, 11 le 08/04 ; F2026-12, 13 le 08/04 ; F2026-14 le 13/04.\n"
    "« Ci-joint les factures correspondant aux douches installées à ce jour. »\n"
    "→ Les chantiers de F2026-04/05/06/07/09 sont dans les PDF (poses de février), "
    "à confirmer sur les PDF ; sans incidence sur la liste des non-facturés.")},
]
# map facture -> proof id
fac_proof = {}
for p in PROOFS:
    for f in p["covers"]:
        fac_proof.setdefault(f, p["id"])
m["proofs"] = PROOFS
m["fac_proof"] = fac_proof

# rattacher une preuve à chaque dossier via sa 1re facture
def first_inv(inv):
    return re.split(r"\s*/\s*", inv)[0].strip() if inv else ""
for r in D:
    key = first_inv(r.get("invoice", "")).replace("-IRSH", "").strip()
    r["proof"] = fac_proof.get(key, "")

# ---------------------------------------------------------------------------
m["dossiers"] = D
m["generated"] = TODAY.isoformat()
m["crm_asof"] = "2026-07-11"
m["fstat_counts"] = dict(Counter(r["fstat"] for r in D))
json.dump(m, open("audit/data/master4.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("invoices ajoutées:", added_inv, "| total dossiers:", len(D))
print("répartition fstat:", m["fstat_counts"])
print("\n== RÉALISÉES NON FACTURÉES (", sum(1 for r in D if r['fstat'].startswith('Réalisée')), ") ==")
for r in sorted((r for r in D if r["fstat"].startswith("Réalisée")), key=lambda x: x["client"]):
    print(" ", r["client"].ljust(34), "|", (";".join(r["dia"]))[:40].ljust(40), "|", r["pose_src"])
