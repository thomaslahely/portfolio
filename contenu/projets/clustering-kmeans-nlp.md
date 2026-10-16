---
titre: Projet — clustering (K-Means, Fuzzy C-Means) et analyse de sentiments
url: /projets/clustering-kmeans-nlp
---

# Projet — clustering (K-Means, Fuzzy C-Means) et analyse de sentiments

<!-- À COMPLÉTER : dans quel cours / quelle année ? seul ou en binôme ?
     Ce que tu as appris, une difficulté rencontrée, un résultat chiffré du rapport. -->

## Résumé

Projet de data science et de machine learning en Python, en trois parties :
une implémentation de l'algorithme K-Means écrite à la main, une comparaison
d'algorithmes de clustering (K-Means et Fuzzy C-Means) évaluée avec l'indice de Dunn,
et une analyse de sentiments sur des tweets (NLP).
Code source : [dépôt KmeansFMeans](https://github.com/thomaslahely/KmeansFMeans).

## Clustering et apprentissage non supervisé : K-Means implémenté à la main

Thomas a implémenté l'algorithme K-Means sans bibliothèque : calcul des distances
euclidiennes, affectation de chaque point au centroïde le plus proche, mise à jour des
centroïdes et critère de convergence. Chaque itération est visualisée avec matplotlib,
et le résultat est comparé à l'implémentation de scikit-learn.

## Comparaison K-Means / Fuzzy C-Means et indice de Dunn

Sur des jeux de données synthétiques générés avec `make_blobs`, Thomas compare K-Means
(avec trois stratégies d'initialisation des centroïdes) et Fuzzy C-Means, un clustering
flou où chaque point a un degré d'appartenance à chaque cluster. La qualité des
partitions est mesurée avec l'indice de Dunn. Les conclusions sont détaillées dans un
rapport d'analyse comparative.

## Analyse de sentiments sur des tweets (NLP)

Classification de sentiments sur des tweets, dont un jeu de données sur les compagnies
aériennes américaines : nettoyage du texte (ponctuation, emojis, mots vides),
tokenisation et racinisation (stemming) avec NLTK, vectorisation TF-IDF, puis
classification supervisée par Random Forest.

## Technologies

Python, NumPy, pandas, scikit-learn, scikit-fuzzy, SciPy, NLTK, matplotlib, seaborn.
