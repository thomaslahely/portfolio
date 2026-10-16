---
titre: Projet — simulation multithreadée de fourmis en C (ncurses, pthread)
url: /projets/simulation-fourmis-c
---

# Projet — simulation multithreadée de fourmis en C

<!-- À COMPLÉTER : cours (système / programmation concurrente ?), année,
     difficultés rencontrées (synchronisation, interblocages…). -->

## Résumé

Simulation interactive d'une colonie de fourmis dans une grille 2D, affichée dans le
terminal. Chaque fourmi est un thread indépendant qui se déplace aléatoirement.
Code source : [dépôt ncurses-fourmis-simulation](https://github.com/thomaslahely/ncurses-fourmis-simulation).

## Programmation concurrente : un thread par fourmi

Thomas a utilisé la bibliothèque POSIX `pthread` : chaque fourmi ajoutée crée un
thread, supprimé quand la fourmi disparaît. L'accès concurrent à la grille partagée
est protégé par des mutex pour éviter les conflits entre threads.

## Interface en mode texte avec ncurses

L'interface est réalisée avec `ncurses` : affichage de la grille en temps réel, outils
pour ajouter des fourmis ou des obstacles et supprimer des entités, interaction par
clic de souris et messages d'état.

## Technologies

C, pthread (multithreading, mutex), ncurses, Linux.
