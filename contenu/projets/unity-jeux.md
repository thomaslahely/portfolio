---
titre: Projet — travaux pratiques Unity (personnage, IA de poursuite, grues articulées)
url: /projets/unity-jeux
---

# Projet — travaux pratiques Unity

<!-- À COMPLÉTER : cours et année, captures d'écran ou vidéo à ajouter sur le site. -->

## Résumé

Trois travaux pratiques réalisés pendant ses études avec le moteur de jeu Unity et le
langage C# : contrôle d'un personnage poursuivi par un ennemi, puis deux simulations
physiques de grues articulées.
Code source : [dépôt Unity](https://github.com/thomaslahely/Unity).

## Personnage et IA de poursuite

Contrôle clavier d'un personnage (déplacement, rotation, sprint, saut) et un ennemi
qui poursuit automatiquement le joueur.

## Simulation physique de grues

Les grues sont simulées avec les composants physiques `ArticulationBody` de Unity :
rotation de la flèche, déplacement du chariot, montée et descente du moufle, grappin,
détection d'objets et changement de caméra. Le troisième TP organise les commandes en
architecture modulaire, avec une machine à états (enum) par type de mouvement et des
axes d'entrée pour un contrôle progressif.

## Technologies

Unity, C#, moteur physique (ArticulationBody), machines à états.
