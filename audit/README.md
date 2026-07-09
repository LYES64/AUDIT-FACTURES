# Audit Facturation 2026 — ETS OUHADDAD

Reconstitution de la facturation 2026 à partir de la **boîte mail** (source de vérité), des **fichiers de suivi** Excel et de l'**extract CRM IRSH** (07/07/2026).

## Volet IRSH — terminé
- **`Rapport_Audit_IRSH_2026.md`** — rapport d'audit (constats + preuves mail/CRM).
- **`Audit_IRSH_outil.html`** — outil local interactif (ouvrir dans un navigateur, aucune installation) : 146 dossiers, filtres, preuves par dossier, registre des factures, anomalies, export CSV des décisions.
- **`IRSH_Interventions_a_facturer.xlsx` / `.csv`** — interventions réalisées (CRM) à facturer.
- **`Audit_Factures_2026.xlsx`** + `..._Synthese.csv` — base issue des fichiers de suivi + anomalies (1ʳᵉ passe).
- `Rapport_Audit_2026.md` — 1ʳᵉ note (analyse fichiers seuls, avant accès mail).

## Volet BARROS — à faire
- **`HANDOFF_Barros_suite.md`** — note de passation pour poursuivre l'audit Barros dans une nouvelle conversation, avec l'autre boîte mail. À lire en premier pour la suite.

## Dossiers
- `data/` — données consolidées et intermédiaires (`master.json` = données de l'outil).
- `scripts/` — scripts Python d'extraction / consolidation / génération.
- `sources/` — fichiers fournis (suivis IRSH & Barros, CRM IRSH).

## Méthode (résumé)
Commande (DIA / bon de travail) → intervention réalisée (CRM) → facture émise (mail) → facture payée (virement) → éventuel avoir. Chaque information conserve sa source (date + expéditeur + citation).
