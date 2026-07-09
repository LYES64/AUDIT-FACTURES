# Note de passation — Poursuite de l'audit (volet BARROS / ECO SHOWER)

> À coller au démarrage de la nouvelle conversation Claude Code, **après avoir connecté la boîte mail utilisée pour Barros / Eco Shower**. Résume tout le travail déjà fait pour une reprise immédiate.

## 0. Contexte de la mission
Audit de reconstitution de la facturation **2026** d'ETS OUHADDAD (gérant : Lyes OUHADDAD ; assistante : Silya OUARAB). L'ancienne personne en charge de la facturation est partie en mauvais termes ; suspicion de factures non créées, commandes oubliées, factures supprimées du suivi. **Règle d'or : la boîte mail est la source de vérité ; les fichiers de suivi Excel sont des sources secondaires non fiables.** Périmètre temporel : **à partir du 01/01/2026 inclus**.

## 1. Ce qui est DÉJÀ fait — volet IRSH (terminé)
- Boîte `ets.lyessanitaire@gmail.com` dépouillée (≈201 fils 2026 ; ≈159 DIA).
- Fichier `Suivi_IRSH_2026.xlsx` + extract CRM IRSH 07/07/2026 analysés.
- Livrables : `Rapport_Audit_IRSH_2026.md`, `Audit_IRSH_outil.html` (outil local), `IRSH_Interventions_a_facturer.xlsx`, `Audit_Factures_2026.xlsx`, `data/master.json`.
- Constats clés IRSH : F2026-16→24 réellement émises mais **numéros effacés du suivi** ; **doublon F2026-17** ; **surfacturation vs DIA** (PERRIERE) ; **PINCON SERGE réalisé non facturé** ; F2026-15 à corriger à 100 € ; écart F2026-23 (4850/4890) ; avoirs SUPERCHI (AV07+AV14).

## 2. Ce qui RESTE à faire — volet BARROS = **ECO SHOWER** (confirmé)

### 2.0 Faits confirmés par le client
- **Barros = Eco Shower** — interlocutrice connue : **`carolina.silva@ecoshower.fr`** (domaine `ecoshower.fr`).
- **Pas de CRM Eco Shower** (contrairement à IRSH). ⚠️ Conséquence méthodo : pas de référentiel externe des « interventions réalisées ». Il faut donc reconstituer « intervention réalisée » à partir de :
  1. la boîte mail Eco Shower (confirmations de pose, envoi de **CRI/photos**, demandes de **solde client**, accusés, plannings) ;
  2. la colonne **`Posé? = OUI`** + **CRI/Photos** du `Suivi_Barros_2026.xlsx` ;
  3. à défaut, demander à l'utilisateur un état, même sommaire, des poses réalisées.

### 2.1 Structure du fichier de suivi Barros (déjà connue)
- Onglets : `Suivi Poses`, `Suivi SAV`, `Suivi Factures`, + onglets factures `F2026-B01`, `F2026-B09`, `F2026-B10`, `F2026-B11`, `F2026-B12`, `Copy` (modèle B00).
- **Référence commande = « Bon de Travail »** au format `CO-000xxx` (ou `N°2025-xxxx`), **pas de DIA**.
- Colonnes Poses (⚠️ **colonne A vide en tête → décalage de 1**) : A vide, B Client, C BT, D CP, E Date Pose, F Montant, G Posé?, H Photos, I CRI, J Validé Lyes, K « Dépose bidet 50€ », L Nouveau Montant, M Facturé?, N Nº Facture.
- Numérotation factures `F2026-Bxx`. **Anomalies déjà repérées dans le fichier** (à confirmer par les mails) :
  - Onglets **F2026-B11 (4 750 €) et F2026-B12 (brouillon, 0 €) ABSENTS du Suivi Factures** (qui s'arrête à B10).
  - Ligne à **7 600 € sans numéro** dans le Suivi Factures.
  - **B11 et B12 affichent tous deux « F2026-B10 »** en cellule « Facture N° » (copier-coller → risque doublon).
  - Écart onglet/suivi **F2026-B01** : 13 580 € (onglet) vs 13 850 € (suivi).
  - Factures 2025 (F0925…F122025) datées 13/01/2026 (antidatage possible).

### 2.2 Clients Barros/Eco Shower déjà repérés (dans le fichier de suivi)
BOULAY Denis, ECHEVERRIA, DOYHAMBOURE, DEL HIERRO, BRINDET, ZANARDI, GOUIN, DEBAIGT, EYHARABIDE, LLOPIS, DUVAL, DE ALMEIDA, MARTINEZ, SALESSES, BARRAU, MELIN, SALABERRY, LACARRIEU, MERINO, CASTAGNOS, ETCHEGARAY, LETEINTURIER, DEBAS, CALDUGARAY, LAYAN, DOYHENARD, ETCHEGORRY, URRUTIA, BELLIARD, DUVERGER, LOPEZ, LABARRERE, LOSADA, POPLEWSKI, JACQUES, QUESADA, DEL COTTO, CATHERINE SUZANNE, DUBOURG, LEFILLIATRE, CLAIN, OLMEDO, MONTAGUT, FOURLOUBEY, RONTEIX, ZITOUNI, VENTURA, PERVIEUX, SERGE CLEE, BRAJOT, TOULOUSE, LABOUYSSARIE, DEBRAY, PETEL, RICHERT, GAUDOUT, EL BAZ, MANSEUR, VALENTIN, MOREAU.
Bons de commande signalés manquants côté Ecoshower en janvier 2026 (mail `carolina.silva@ecoshower.fr`) : LARRABURU, LARTIGAU, DARRACQ, CONAN, OBERTO, AGUERRE, NAVARRET, FRUCTUOSO, WIEDERKEHR, BROCHOT, MATTEI, GABARROT, COUTHENX, BEHRO, GARCIA — **à retrouver en priorité dans la boîte Eco Shower**.

### 2.3 Marche à suivre pour Barros (méthode IRSH adaptée — sans CRM)
1. **Connecter la boîte mail Eco Shower** (Réglages → Connecteurs → Gmail → reconnecter ; idéalement nouvelle session).
2. Requêtes Gmail utiles :
   - `from:ecoshower.fr after:2026/01/01`
   - `after:2026/01/01 (facture OR avoir OR "bon de commande" OR "bon de travail" OR CO-000)`
   - `after:2026/01/01 (paiement OR virement OR relance OR solde OR annulation)`
   - rechercher les n° `F2026-B01`…`F2026-B12`, la ligne à **7 600 €**, et les bons `CO-000xxx`.
3. Établir la liste des **bons de travail reçus** (commandes) et des **poses confirmées** (mails + colonne Posé? du fichier), faute de CRM.
4. Croiser : bons reçus ↔ Suivi Poses ↔ onglets factures ↔ Suivi Factures ↔ virements/relances.
5. Élucider les anomalies fichier (B11/B12 hors suivi, ligne 7 600 €, doublon « B10 », écart B01).
6. Produire les mêmes livrables (rapport Barros, liste « à facturer », onglet Barros dans l'outil).

### 2.4 À demander à l'utilisateur au démarrage
- Confirmer l'adresse exacte de la boîte Eco Shower et le fournisseur (Gmail grand public ou Workspace).
- À défaut de CRM, un **état des poses réalisées Eco Shower** (même sommaire) est-il disponible ?

## 3. Où sont les données / scripts (repo `LYES64/AUDIT-FACTURES`, dossier `audit/`)
- `audit/data/master.json` — base consolidée IRSH. · `audit/Audit_IRSH_outil.html` — outil local.
- `audit/Rapport_Audit_IRSH_2026.md`, `audit/IRSH_Interventions_a_facturer.csv/xlsx`.
- `audit/scripts/` — scripts Python (extraction, consolidation `build_master.py`, génération outil `gen_html.py`).
- `audit/sources/` — `Suivi_IRSH_2026.xlsx`, `Suivi_Barros_2026.xlsx`, `CRM_IRSH_2026-07-07.xlsx`.
- Astuce technique : certains `.xlsx` cassent openpyxl (`Fill() takes no arguments`) → les lire via le XML brut du zip (cf. `audit/scripts/crm3.py`).

## 4. Rappels méthodo (à conserver pour Barros)
- Ne jamais conclure « facture inexistante » sans avoir cherché dans les mails **et** vérifié le statut réel (souvent : facture émise mais paiement bloqué faute de solde client/CRI).
- Distinguer **commande reçue** (bon de travail) / **intervention réalisée** (mail+fichier, pas de CRM ici) / **facture émise** (mail) / **facture payée** (virement) / **avoir**.
- Conserver la **source de chaque information** (date + expéditeur + citation).
- Statuts : Facturée / À facturer / Facture envoyée non retrouvée / Introuvable / En attente d'infos / Annulée / Avoir émis / À vérifier / Anomalie.
