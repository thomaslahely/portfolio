---
titre: Projet — jeu des allumettes sur Arduino avec IA Minimax
url: /projets/jeu-allumettes-arduino
---

# Projet — jeu des allumettes sur Arduino avec IA Minimax

<!-- À COMPLÉTER : contexte (cours ? projet perso ?), durée, ce que tu as appris. -->

## Résumé

Thomas a programmé en C++ le jeu des 21 allumettes sur une carte Arduino (Elegoo Mega
2560), avec un écran LCD 16x2 et un clavier matriciel 4x4. Le joueur affronte
l'ordinateur, qui joue grâce à l'algorithme Minimax.
Code source : [dépôt jeu-allumettes-arduino](https://github.com/thomaslahely/jeu-allumettes-arduino).

## Intelligence artificielle de jeu : algorithme Minimax

L'ordinateur explore récursivement toutes les suites de coups possibles (prendre 1, 2
ou 3 allumettes) en alternant un joueur qui maximise le score et un joueur qui le
minimise. Il joue ainsi de façon optimale : il gagne toujours s'il commence, en laissant
à l'adversaire un nombre d'allumettes égal à un multiple de 4 plus 1.

## Électronique et systèmes embarqués

Thomas a réalisé le câblage sur breadboard (écran LCD, potentiomètre de contraste,
clavier matriciel) et utilisé les bibliothèques Arduino `LiquidCrystal` et `Keypad`
pour l'affichage et la saisie.

## Technologies

C++, Arduino, électronique (LCD, clavier matriciel), algorithme Minimax.
