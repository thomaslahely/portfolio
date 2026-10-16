---
titre: Dépôt GitHub ProjetBDCabinetConseil — Modélisation et conception d'une base de données relationnelle pour un cabinet de conseil MCD, MPD
url: https://github.com/thomaslahely/ProjetBDCabinetConseil
---

Langage principal du dépôt ProjetBDCabinetConseil : TeX.

# Info505 – Analyse des Bases de Données

## Présentation

Ce projet présente une analyse complète des données à travers :

- Un **Modèle Conceptuel de Données (MCD)** qui décrit les entités principales du système et leurs relations.
- Un **Modèle Physique de Données (MPD)** qui traduit le MCD en tables, colonnes et contraintes pour une implémentation en base de données.
- Une étude des **dépendances fonctionnelles** afin d’optimiser la structure des données et assurer leur intégrité.

---

## Description du projet

### Modèle Conceptuel de Données (MCD)

Le MCD modélise les entités suivantes :

- **Candidat** : Personne postulant pour des missions.
- **Entreprise** : Organisation proposant des missions.
- **Mission** : Tâche ou projet nécessitant un candidat.
- **Fonction** : Type de poste disponible.
- **Diplôme** : Qualification détenue par un candidat.
- **Institut** : Établissement délivrant des diplômes.
- **Annonce** : Publication d’une mission.
- **Convention** : Accord entre un institut et un cabinet de conseil.

Les relations entre ces entités, telles que Candidat-Fonction, Entreprise-Mission ou Candidat-Diplôme, sont également définies pour représenter précisément les interactions du système.

### Modèle Physique de Données (MPD)

Le MPD est la mise en œuvre concrète du MCD sous forme de :

- Tables représentant les entités.
- Colonnes pour chaque attribut.
- Contraintes d’intégrité pour assurer la cohérence des données.

### Dépendances Fonctionnelles

Cette analyse permet de :

- Identifier les dépendances entre attributs.
- Normaliser les tables pour éviter les redondances.
- Assurer l’intégrité et la qualité des données.

---

## Usage

Ce projet sert de base à la conception d’une base de données relationnelle adaptée à la gestion des missions, candidats et entreprises. Il peut être utilisé comme support pédagogique ou pour démarrer un développement applicatif lié à ce domaine.



