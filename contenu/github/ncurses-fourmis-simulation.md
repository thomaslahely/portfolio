---
titre: Dépôt GitHub ncurses-fourmis-simulation —  Simulation de colonie de fourmis en temps réel dans un terminal — interface ncurses, multi-threading   
url: https://github.com/thomaslahely/ncurses-fourmis-simulation
---

Langage principal du dépôt ncurses-fourmis-simulation : C.

# 🐜 Simulation de fourmis en C avec ncurses

Ce projet est une simulation interactive d'une colonie de fourmis dans un environnement 2D, développée en langage C avec `ncurses` pour l'interface utilisateur et `pthread` pour la gestion multithread.

## ✨ Fonctionnalités

- Interface graphique en mode texte avec `ncurses`
- Ajout/suppression d'obstacles
- Ajout/suppression de fourmis (chaque fourmi est un thread)
- Déplacement aléatoire des fourmis
- Interface par clic souris (gauche uniquement)
- Affichage des messages en temps réel

## 🎮 Contrôles

- `@` : Ajouter une fourmi
- `#` : Ajouter un obstacle
- `X` : Supprimer une entité
- `F2` : Quitter l'application
- Clic gauche : interaction selon l'outil sélectionné

## 🧪 Dépendances

- `ncurses`
- `pthread`

