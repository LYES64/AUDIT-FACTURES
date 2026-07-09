# Rapport d'audit — Facturation 2026
**Entreprise : ETS OUHADDAD** — Prescripteurs *IRSH* et *BARROS ECO*
Période auditée : **01/01/2026 → 09/07/2026**
Date du rapport : 09/07/2026

---

## ⚠️ Avertissement méthodologique majeur — à lire en premier

La consigne d'audit désigne **la boîte mail professionnelle comme source de vérité principale**, les fichiers Excel n'étant que des sources secondaires non fiables.

**À ce jour, l'accès à la boîte mail (connecteur Gmail) est indisponible : le jeton d'autorisation a expiré et ne peut pas être renouvelé dans cette session automatisée.**

**Conséquence :** le présent rapport a été produit **uniquement à partir des deux fichiers de suivi Excel**. Il constitue donc :
- une **cartographie complète et un contrôle de cohérence interne** des fichiers (Étape 4) ;
- une **détection d'anomalies** internes et inter-fichiers (Étape 5) ;
- une **base de dossiers** consolidée (Étape 2) servant de socle au recoupement mail.

Il **ne peut pas encore** :
- confirmer/infirmer l'existence réelle des factures via les mails ;
- détecter les commandes présentes *uniquement* dans les mails (jamais reportées dans les fichiers) — c'est-à-dire précisément la fraude la plus probable ;
- valider les envois, relances, validations client et paiements.

➡️ **Pour finaliser l'audit (Étapes 1, 3, 5-mails, 6, 8-complet), il faut reconnecter Gmail** (voir la fin du rapport), puis relancer l'analyse. Toutes les conclusions ci-dessous restent donc **provisoires** et sont marquées « à vérifier par les mails ».

---

## 1. Chiffres clés (fichiers de suivi, activité 2026)

| Indicateur | IRSH | BARROS | Total |
|---|---:|---:|---:|
| Dossiers uniques identifiés (DIA / Bon de travail) | 69 | 56 | **125** |
| Factures avec numéro (datées 2026) | ~35 | ~21 | ~56 |
| Factures avec montant mais **N° effacé/absent** | **9** | **1** (7 600€) | **10** |
| Factures existantes en onglet mais **hors suivi** | — | **2** (B11, B12) | **2** |
| Avoirs 2026 | 9 (AV06→AV14) | 0 | 9 |
| Poses réalisées **non rattachées à une facture** | 21 | (voir §5) | ≥21 |
| CA facturé 2026 (N° présents, ≥2026) | ≈ 115 900 € | ≈ 95 655 € | **≈ 211 555 €** |
| Total avoirs 2026 | −8 575 € | 0 € | **−8 575 €** |
| Factures « fantômes » (montant sans N°) | 27 660 € | 7 600 € | **≈ 35 260 €** |
| Liste « non facturé » IRSH (onglet dédié) | 30 170 € HT | — | **30 170 €** |

> Les montants « facturés » mélangent HT et « nouveau montant » selon les lignes ; ils sont indicatifs et devront être recalés sur les factures réelles.

---

## 2. Répartition des 125 dossiers par statut (fichiers)

| Statut (déduit des fichiers) | Nb | Commentaire |
|---|---:|---|
| Facturée — N° présent dans le suivi | 42 | Cas nominal (surtout BARROS B02–B08) |
| **Facturée en onglet mais N° ABSENT du suivi** | 45 | **Anomalie** — factures existantes dont le n° a disparu du tableau de suivi |
| Posé, **non facturé** (aucune facture dans les fichiers) | 21 | À facturer OU facture émise mais non tracée → **mails requis** |
| Commande / SAV **sans facture identifiée** | 17 | À qualifier |

---

## 3. Anomalies détectées (détail dans l'onglet « Anomalies » du fichier Excel)

### 🔴 CRITIQUE
1. **IRSH — 9 numéros de facture effacés du « Suivi Factures ».** Les lignes 47 à 55 portent des montants (2 460 / 2 100 / 5 010 / 2 450 / 1 800 / 3 300 / 2 950 / 4 890 / 2 700 €) **sans aucun numéro**, alors que les onglets `F2026-16` à `F2026-24` (datés des 10–12/06/2026) existent avec **exactement ces montants**. → Les numéros ont été **retirés du suivi** tandis que les factures existent. C'est la signature typique d'un masquage.

### 🟠 ÉLEVÉE
2. **IRSH — avoirs AV03, AV04, AV05 manquants** (la séquence saute de AV02 à AV06). 3 avoirs potentiellement supprimés ou jamais tracés.
3. **IRSH — 21 poses réalisées et validées sans numéro de facture** (Suivi Poses, lignes 9 à 35). Poses faites mais non rattachées à une facture dans les fichiers.
4. **IRSH — onglet « Copie de non facturé » = 30 170 € HT** de poses listées comme non facturées (36 dossiers DIA).
5. **BARROS — onglets `F2026-B11` (4 750 €) et `F2026-B12` (brouillon, 0 €) absents du « Suivi Factures »** (qui s'arrête à B10).
6. **BARROS — ligne à 7 600 € sans numéro** dans le suivi, ne correspondant ni à B11 ni à B12.

### 🟡 MOYENNE
7. **BARROS — B11 et B12 affichent tous deux « F2026-B10 »** en cellule « Facture N° » (copier-coller non mis à jour → risque de doublon).
8. **Écarts de montants facture ↔ suivi** : `F2026-23` (4 850 € vs 4 890 €, Δ+40) ; `F2026-B01` (13 580 € vs 13 850 €, Δ+270).
9. **`F2026-15` orpheline** : 200 €, sans date, sans état, sans règlement.
10. **Numérotation 2025 datée janvier 2026** (BARROS `F0925`→`F122025` au 13/01/2026 ; IRSH `F1225-xx` au 15/01/2026) — antidatage possible à clarifier.

---

## 4. Ce que les fichiers **ne peuvent pas** révéler (nécessite les mails)

C'est le cœur du risque de fraude évoqué (personne partie en mauvais termes) :

- **Commandes reçues par mail et jamais reportées** dans aucun fichier → invisibles ici par construction.
- **Factures annoncées « envoyées » au client** mais jamais créées.
- Distinguer, parmi les 21 poses « non facturées », celles **réellement jamais facturées** de celles simplement **non ré-annotées** (le suivi ne détaille pas les lignes des factures F2026-03 à F2026-14).
- Les **relances, avoirs demandés, modifications** et **paiements** échangés par mail.

---

## 5. Dossiers nécessitant une vérification humaine prioritaire

1. Les **9 factures IRSH à numéro effacé** (F2026-16→24) : confirmer émission, envoi client, encaissement.
2. Les **avoirs AV03/AV04/AV05** : ont-ils existé ? Pour qui ? Pour quel montant ?
3. Les **30 170 € HT** de la liste « non facturé » IRSH : facturer ou justifier l'abandon.
4. Les **factures BARROS B11/B12** hors suivi + la **ligne 7 600 €**.
5. Les **21 poses IRSH sans facture** (dont PERRIN SOPHIE 5 790 €, ATZORI, GRIN, etc.).

---

## 6. Livrables produits

- `Audit_Factures_2026.xlsx` — onglet **Synthèse Dossiers 2026** (125 dossiers, colonnes Étape 7 + niveau de confiance) et onglet **Anomalies**.
- `Audit_Factures_2026_Synthese.csv` — même table au format CSV.
- `Rapport_Audit_2026.md` — le présent rapport.

Colonne **« Présente dans les mails »** = *« À vérifier (Gmail indisponible) »* pour tous les dossiers, en attente de reconnexion.

---

## 7. Étape suivante indispensable — reconnexion de la boîte mail

Pour compléter l'audit selon le périmètre demandé (source de vérité = mails) :

1. Ouvrir une session **interactive** de l'outil et lancer `/mcp` (ou reconfigurer le connecteur Gmail via les réglages des connecteurs claude.ai) afin de **ré-autoriser le serveur Gmail**.
2. Me redonner la main : je reprendrai alors **la base des 125 dossiers ci-dessus comme socle**, je parcourrai les mails 2026 (mots-clés *facture, avoir, bon de commande, DIA…* + analyse des objets, corps, pièces jointes), et je produirai la version **finale** avec la colonne « Présente dans les mails » renseignée, la chronologie par dossier (Étape 3), la 2ᵉ passe (Étape 6) et le rapport complet (Étape 8).

**Aucune conclusion de fraude ne doit être arrêtée avant ce recoupement mail.** Les anomalies ci-dessus sont des *signaux* solides, pas des preuves définitives.
