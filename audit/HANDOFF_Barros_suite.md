# Note de passation — Poursuite de l'audit (volet BARROS) dans une nouvelle conversation

> À coller au démarrage de la nouvelle conversation Claude Code, **après avoir connecté la boîte mail utilisée pour Barros**. Ce document résume tout le travail déjà fait pour que la reprise soit immédiate.

## 0. Contexte de la mission
Audit de reconstitution de la facturation **2026** d'ETS OUHADDAD (gérant : Lyes OUHADDAD ; assistante : Silya OUARAB). L'ancienne personne en charge de la facturation est partie en mauvais termes ; suspicion de factures non créées, commandes oubliées, factures supprimées du suivi. **Règle d'or : la boîte mail est la source de vérité ; les fichiers de suivi Excel sont des sources secondaires non fiables.** Périmètre temporel : **à partir du 01/01/2026 inclus**.

## 1. Ce qui est DÉJÀ fait — volet IRSH (terminé)
- Boîte `ets.lyessanitaire@gmail.com` dépouillée (≈201 fils 2026 ; ≈159 DIA).
- Fichier `Suivi_IRSH_2026.xlsx` analysé (onglets Suivi Poses / SAV / Factures + onglets factures F2026-16→24 + « Copie de non facturé »).
- Extract CRM IRSH 07/07/2026 analysé.
- Livrables produits : `Rapport_Audit_IRSH_2026.md`, `Audit_IRSH_outil.html` (outil local), `IRSH_Interventions_a_facturer.xlsx`, `Audit_Factures_2026.xlsx`, `master.json`.
- Constats clés IRSH : F2026-16→24 réellement émises mais **numéros effacés du suivi** ; **doublon F2026-17** ; **surfacturation vs DIA** (PERRIERE) ; **PINCON SERGE réalisé mais non facturé** ; F2026-15 à corriger à 100 € ; écart F2026-23 (4850 vs 4890) ; avoirs SUPERCHI (AV07+AV14).

## 2. Ce qui RESTE à faire — volet BARROS
Le fichier `Suivi_Barros_2026.xlsx` est déjà disponible dans le repo, mais **l'historique mail de Barros est sur une autre boîte** (à connecter). Objectif : refaire pour Barros exactement la même démarche que pour IRSH.

### 2.1 Structure du fichier de suivi Barros (déjà connue)
- Onglets : `Suivi Poses`, `Suivi SAV`, `Suivi Factures`, + onglets factures `F2026-B01`, `F2026-B09`, `F2026-B10`, `F2026-B11`, `F2026-B12`, `Copy` (modèle B00).
- **Référence commande = « Bon de Travail »** au format `CO-000xxx` (ou `N°2025-xxxx`), **PAS** de DIA.
- Colonnes Poses (⚠️ **colonne A vide en tête → décalage de 1**) : A vide, B Client, C BT, D CP, E Date Pose, F Montant, G Posé?, H Photos, I CRI, J Validé Lyes, K « Dépose bidet 50€ », L Nouveau Montant, M Facturé?, N Nº Facture.
- Numérotation factures : `F2026-Bxx`. Séquence suivi B01→B10. **Anomalies déjà repérées dans le fichier** (à confirmer par les mails) :
  - Onglets **F2026-B11 (4 750 €) et F2026-B12 (brouillon, 0 €) ABSENTS du Suivi Factures**.
  - Ligne à **7 600 € sans numéro** dans le Suivi Factures.
  - **B11 et B12 affichent tous deux « F2026-B10 »** en cellule « Facture N° » (copier-coller → risque doublon).
  - Écart onglet/suivi **F2026-B01** : 13 580 € (onglet) vs 13 850 € (suivi).
  - Factures 2025 (F0925…F122025) datées 13/01/2026 (antidatage possible).

### 2.2 Indices sur le donneur d'ordre Barros (depuis la boîte IRSH)
- « BARROS ECO », adresse **14 Rue de la Poudrière, Lot B11, 33700 MERIGNAC**.
- Interlocuteur probable : **Ecoshower** — `carolina.silva@ecoshower.fr` (échanges « Bons de commande manquants », listes de clients DIA). À confirmer dans la nouvelle boîte.
- Bons de travail `CO-000xxx`. Clients Barros vus : BOULAY Denis, ECHEVERRIA, DOYHAMBOURE, DEL HIERRO, BRINDET, ZANARDI, GOUIN, DEBAIGT, EYHARABIDE, LLOPIS, DUVAL, DE ALMEIDA, MARTINEZ, SALESSES, BARRAU, MELIN, SALABERRY, LACARRIEU, MERINO, CASTAGNOS, ETCHEGARAY, LETEINTURIER, DEBAS, CALDUGARAY, LAYAN, DOYHENARD, ETCHEGORRY, URRUTIA, BELLIARD, DUVERGER, LOPEZ, LABARRERE, LOSADA, POPLEWSKI, JACQUES, QUESADA, DEL COTTO, CATHERINE SUZANNE, DUBOURG, LEFILLIATRE, CLAIN, OLMEDO, MONTAGUT, FOURLOUBEY, RONTEIX, ZITOUNI, VENTURA, PERVIEUX, SERGE CLEE, BRAJOT, TOULOUSE, LABOUYSSARIE, DEBRAY, PETEL, RICHERT, GAUDOUT, EL BAZ, MANSEUR, VALENTIN, MOREAU.

### 2.3 Marche à suivre pour Barros (répéter la méthode IRSH)
1. **Connecter la boîte mail Barros** (option A : Réglages → Connecteurs → Gmail → reconnecter avec le compte Barros ; idéalement nouvelle session).
2. Requêtes Gmail utiles (adapter l'expéditeur au réseau Barros/Ecoshower) :
   - `after:2026/01/01 (facture OR avoir OR "bon de commande" OR "bon de travail" OR CO-000 OR barros OR ecoshower)`
   - `from:ecoshower.fr after:2026/01/01`
   - `after:2026/01/01 (paiement OR virement OR relance OR annulation)`
   - rechercher les n° `F2026-B01`…`F2026-B12` et la ligne à **7 600 €**.
3. Croiser : bons de travail reçus (mail) ↔ Suivi Poses Barros ↔ onglets factures ↔ Suivi Factures.
4. Rechercher un **extract CRM Ecoshower/Barros** équivalent (interventions réalisées) — demander à l'utilisateur s'il peut le fournir (comme le CRM IRSH).
5. Produire les mêmes livrables (rapport Barros, liste « à facturer », onglet outil).

### 2.4 Questions à poser à l'utilisateur au démarrage
- Adresse exacte de la boîte Barros et fournisseur (Gmail grand public ou Workspace) ?
- Existe-t-il un **extract CRM Ecoshower** (interventions réalisées) comme pour IRSH ?
- Barros = bien Ecoshower (`ecoshower.fr`) ? Autre interlocuteur ?

## 3. Où sont les données / scripts (repo)
Tous les livrables et scripts d'analyse sont commités dans le repo `lyes64/audit-factures` (dossier `audit/`). Fichiers clés :
- `audit/master.json` — base consolidée IRSH (données de l'outil).
- `audit/Audit_IRSH_outil.html` — outil local.
- `audit/Rapport_Audit_IRSH_2026.md`, `audit/IRSH_Interventions_a_facturer.csv/xlsx`.
- `audit/scripts/` — scripts Python (extraction xlsx, consolidation, génération outil).
- Fichiers de suivi source dans le repo / uploads : `Suivi_IRSH_2026.xlsx`, `Suivi_Barros_2026.xlsx`, CRM IRSH.

## 4. Rappels méthodo (à conserver pour Barros)
- Ne jamais conclure « facture inexistante » sans avoir cherché dans les mails **et** vérifié le statut réel (souvent : facture émise mais paiement bloqué faute de solde client/CRI/IP).
- Distinguer **commande reçue** (bon de travail) / **intervention réalisée** (CRM) / **facture émise** (mail) / **facture payée** (virement) / **avoir**.
- Conserver la **source de chaque information** (date + expéditeur + citation).
- Statuts à utiliser : Facturée / À facturer / Facture envoyée non retrouvée / Introuvable / En attente d'infos / Annulée / Avoir émis / À vérifier / Anomalie.
