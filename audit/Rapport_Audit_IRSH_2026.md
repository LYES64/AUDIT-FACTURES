# Rapport d'audit — Facturation 2026 — Volet IRSH
**ETS OUHADDAD** · Prescripteur **IRSH / Indépendance Royale**
Période : 01/01/2026 → 09/07/2026 · Rapport du 09/07/2026
Sources : (1) boîte mail `ets.lyessanitaire@gmail.com` — *source de vérité*, (2) fichier `Suivi_IRSH_2026.xlsx`, (3) extract CRM IRSH du 07/07/2026.

> ⚠️ Ce volet couvre **IRSH uniquement**. Le volet **BARROS** est à traiter séparément : l'essentiel des informations est sur **une autre boîte mail** (voir note de passation `HANDOFF_Barros_suite.md`).

---

## 1. Comment fonctionne la facturation IRSH (compris via les mails)

- Chaque intervention démarre par une **DIA** envoyée par mail (`information@independanceroyale.com`, objet « Votre DIA … / DIAxxxxx CLIENT DEPT »). C'est le **bon de commande**.
- Types de DIA : `DIAP…` (pose), `DIAR…` (rework/reprise), `DIAV…` (visite SAV/SAP), `DIA1…` (SAV).
- Après pose, ETS OUHADDAD édite une facture (`F2026-xx-IRSH`) envoyée à `compta@independanceroyale.com` (interlocutrice : **Camille BUSTREAU**, compta).
- IRSH ne met en paiement qu'après réception du **solde client** (chèque récupéré le jour de la pose) et résolution des **IP** (incidents/anomalies pose), et validation du **BE** (bureau d'études) sur les montants.
- Auto-liquidation de TVA (sauf dépose-repose facturée avec TVA 20 %).

---

## 1bis. Rapprochement DIA → chantier → facture (re-traité 11/07/2026, base = MAILS)

**Méthode (à la demande) :** on ne se fie **plus au fichier `Suivi_IRSH_2026.xlsx`** (incomplet : DIA et factures manquantes). La comparaison est reconstruite **entièrement depuis Gmail** :
- **Côté DIA** : toutes les DIA reçues depuis le 01/01/2026 (`information@independanceroyale.com`, objet « Votre DIA … / DIA[P/R/V]xxxxx CLIENT »).
- **Côté factures** : correspondance **facture → chantier → DIA** confirmée par les mails de la **compta IRSH** (Camille BUSTREAU : point 18/06 + 09/07, point compta du **17/04** qui détaille chaque F1225-xx et F2026-03→14 par dossier/DIA) + envois de factures.
- **Clé de rapprochement** : le **nom de chantier** (clé principale, car le n° DIA n'est pas toujours porté sur la facture) **et** le **n° DIA** (clé secondaire).
- **Preuve de pose** (facturable) : **CRM InterFast** (`Posée/Effectuée`) + poses signalées dans les mails/brouillon de juin.

**Résultat (147 dossiers) :**
| Statut de facturation | Nb |
|---|---:|
| ✅ **Facturé** (n° de facture rattaché, corroboré mail) | **43** |
| 🔴 **Réalisé (posé) mais NON facturé** → à facturer | **23** |
| 🔵 En cours — pas encore posé | 27 |
| 🟠 Commande reçue — à vérifier | 54 |

➡️ Voir l'onglet **« ⚠️ Non facturés »** de `Audit_Factures_outil.html` et le fichier **`IRSH_Non_factures_2026.csv`**. Mapping complet dans **`IRSH_DIA_chantier_facture_2026.csv`**.

### Les 23 dossiers posés NON facturés (à reprendre à partir de F2026-25)
Confirmés **CRM InterFast** : BARTH JANINE, BONETTO STEPHANE, CARRE LUCIE, DAL BO MARC, DRAMCOURT JOCELYNE ET FABRICE, DUGUET MURIEL ET LE BORGNE YVES, HARCAUT ODETTE, LEVY RENE, MAILLON EDDY, MEOULE FABIENNE ET ROLAND, PATIES MARIE-AGNES ET GILBERT, PECQUERY THERESE ET GILES, PINCON SERGE, SALLENAVE CHRISTIANE.
Signalés **poses juin (mails/brouillon)** : BOUCHERARA NADIA, BOURCEAU RICHARD, DALBO MARC, MAYZAUD PATRICK, MINGAM BERTRAND ET FRANCIS, MONTEAU ODETTE, PERBOST JEAN-CLAUDE, RANDRIAMANANA MARTINE, VERNER ELIANE.

### Factures ↔ chantiers confirmés par mail (extrait)
- **F1225-02** PERRIERE · **F1225-08** RAINAUD · **F1225-10** DARMENDRAIL · **F1225-14** PARPAILLON · **F1225-15** MANEVIT · **F1225-16** JEANJEAN + VERRIER · **F1225-18** BAUER.
- **F2026-03** LECOQ + CHAMPENOIS · **F2026-08** GRIN · **F2026-10** COMMANDEUR · **F2026-11** PASTORINO · **F2026-12** ATZORI · **F2026-13** CABRIERE · **F2026-14** PERRIN · **F2026-15** DARMENDRAIL (compl.).
- **F2026-16** MOMAS/COLAS/MOYA · **F2026-17** SAINT-MARTIN/DESLUX/HOSPITAL · **F2026-18** MANSUY/TISSAIRE/BOUEILH · **F2026-19** HERREYRE/LARREDE/PANTANI · **F2026-20** LE FRANCOIS/FAUCONNIER · **F2026-21** CHARLES/PONTE/DA SILVA · **F2026-22** DISSAUX/HERVE/PEZOT · **F2026-23** PELUHET/TISSAIRE/SUBERCAZE · **F2026-24** CLAUDON/VENTURINI/BENEDE.
- **F2026-04/05/06/07** : factures émises le 09/03 (PDF), chantiers = poses de février (à confirmer sur PDF ; sans incidence sur les non-facturés).

---

## 2. Chiffres clés IRSH 2026 (croisés mail + fichier + CRM)

| Indicateur | Valeur |
|---|---:|
| Dossiers IRSH identifiés (clients uniques) | **146** |
| Commandes DIA reçues par mail (réf. uniques) | **159** |
| Factures/avoirs au registre reconstruit | **29 lots** |
| Dossiers facturés (preuve) | 31 |
| Interventions **réalisées non facturées** (CRM 07/07) | 14 |
| Commandes en cours (planifiées / attente matériel…) | 34 |
| CA facturé 2026 estimé (num. + F16-24) | ≈ **143 000 €** |
| Avoirs 2026 (AV06→AV14) | ≈ **−8 575 €** |

---

## 3. Constats majeurs et preuves

### 🔴 3.1 — Les 9 factures « à numéro effacé » existent réellement (F2026-16 → F2026-24)
- **Fichier** : dans « Suivi Factures », lignes 47-55, des montants (2 460 / 2 100 / 5 010 / 2 450 / 1 800 / 3 300 / 2 950 / 4 890 / 2 700 €) **sans numéro** ; les onglets `F2026-16`…`F2026-24` existent pourtant avec ces montants.
- **Preuve mail décisive** : le 10/06/2026, envoi à `compta@independanceroyale.com` — objet *« Factures des douche posées-2026 »* : « Ci-joint les factures correspondant aux douches installées à ce jour. » Puis 15/06 : envoi de F2026-23 et F2026-24.
- **Confirmation IRSH** : point compta du 18/06 et du **09/07** listant nommément F2026-15/16/18/19/21/23/24 avec leurs montants et l'état de paiement.
- **Conclusion** : ce ne sont **pas** des factures manquantes — elles sont émises et suivies par IRSH. En revanche, **leurs numéros ont été retirés du fichier de suivi interne** *a posteriori*. → **manipulation du fichier de suivi**, pas de perte de CA sur ces lignes.

### 🔴 3.2 — Doublon de numéro F2026-17 (confirmé par le client)
- **Preuve** : réponse compta IRSH du 10/06 : « et **j'ai deux factures avec le numéro F2026-17** ». Deux factures distinctes ont porté le même numéro → risque comptable.

### 🟠 3.3 — Surfacturation par rapport au montant DIA
- **Preuve** : 23/04, Camille BUSTREAU : « F1225-02 — PERRIERE MARIE CLAUDE — DIAP133217 : vous facturez 3 250 € mais la DIA est à 2 065 € ». Facture révisée demandée.
- Autres ajustements à la baisse reconnus par ETS le 10/06 : DA SILVA −250 € (WC compté 2×), DISSAUX −150 € (pompe non posée), HERVE −100 € (entretoise non faite), PEZOT −250 € (WC non installé).
- → vérifier systématiquement l'écart **montant facturé ↔ montant DIA validé**.

### 🟠 3.4 — PINCON SERGE : très actif, aucune facture retrouvée
- Nombreux DIA/rework/visap (DIAP135285, DIAP135287, DIAR86325, DIAR86336, DIAV11424, DIAV11425…). CRM : reworks et visites **« Posée/Effectuée »**. Relance solde par IRSH (DIAP135287, 22/06). Pose au « non facturé » ~1 790 €.
- **Aucune facture** dans les onglets, le suivi, ni les mails de paiement. → **à facturer / vérifier en priorité.**

### 🟠 3.5 — F2026-15 (DARMENDRAIL ISABELLE) : mauvais montant, bloquée
- F1225-01 **annulée** ; 100 € déjà réglés → la compta demande une facture de **100 €** et non 200 €. Toujours en attente au 09/07.

### 🟡 3.6 — Écart fichier ↔ réalité : F2026-23 = 4 850 € (mail) vs 4 890 € (fichier).
### 🟡 3.7 — Double avoir SUPERCHI ARLETTE : AV07 (1 020 €) puis AV14 (1 967,25 €) — réclamations assurance successives.
### 🟡 3.8 — Dossiers annulés après lancement (« de CORDINA FABRICE ») : VERSAILLES ROSANNE _WS3501021 (10/06), DUBOUE GILLES _WS3515128 (02/07). Vérifier récupération matériel / non-facturation.

---

## 4. Interventions réalisées À FACTURER (CRM 07/07 croisé factures)

Interventions au statut **« Posée/Effectuée »** sans facture retrouvée (détail dans `IRSH_Interventions_a_facturer.xlsx` et dans l'outil) :

- **Pose non facturée (2026)** : **LEVY RENE** (DIAP135331).
- **Reprises/SAV réalisés à facturer si prestation à charge** : PINCON SERGE (DIAR86325), DAL BO MARC (DIAR135504 + pose DIAP134852 ~1 300 €), DRAMCOURT (DIAR86327), PATIES MARIE-AGNES (DIA113690).
- **Visites SAP à qualifier** : PINCON (DIAV11424/11425), MAILLON EDDY (DIAV11427).
- **Interventions antérieures à 2026 (hors périmètre, à régulariser si jamais facturées)** : MEOULE, SALLENAVE, BONETTO, HARCAUT, DUGUET, PECQUERY, CARRE, BARTH.

> Note : le gros du retard a déjà été rattrapé par F2026-16→24. La liste restante est courte.

---

## 5. Périmètre plus large que prévu (à ne pas oublier)
La boîte mail révèle d'autres donneurs d'ordre facturés en 2026, **hors des 2 fichiers de suivi** : **ASH Europe** (projets `PROJ…`, réseaux HAMARIS/ERILIA/Haute-Savoie Habitat, SAV DOHEN…), **Halpades** (bons de commande, plateforme de dépôt de factures), **Ecoshower** (lié à Barros), **SEM4V / LT Showertec** (AO France Loire, « Le Cèdre »). Ces flux mériteront un audit dédié.

---

## 6. Livrables de ce volet
- `Audit_IRSH_outil.html` — outil local interactif (dossiers, preuves, registre, anomalies, export décisions).
- `IRSH_Interventions_a_facturer.xlsx` / `.csv` — liste à facturer (CRM croisé factures).
- `Audit_Factures_2026.xlsx` — base fichiers + anomalies (1ʳᵉ passe).
- `master.json` — base consolidée (données de l'outil).
- `Rapport_Audit_IRSH_2026.md` — le présent rapport.
