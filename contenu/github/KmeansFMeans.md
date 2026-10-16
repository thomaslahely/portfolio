---
titre: Dépôt GitHub KmeansFMeans — Implémentation et comparaison de K-Means et Fuzzy C-Means + analyse de sentiment sur tweets
url: https://github.com/thomaslahely/KmeansFMeans
---

Langage principal du dépôt KmeansFMeans : Python.

# DataSciences - Projet d'Analyse de Données et Machine Learning

## Structure du Projet

### 📁 TDNLP (Text Data & Natural Language Processing)
Analyse de sentiments sur des données Twitter avec machine learning.

#### Fichiers principaux :
- **Exo1.py** : Préprocessing de texte avec nettoyage, tokenisation et stemming
- **Exo2.py** : Classification de sentiments avec Random Forest et TF-IDF
- **tweets.txt** : Dataset de tweets avec métadonnées (ID, utilisateur, texte, sentiment, etc.)
- **US_Airlines_Twitter_Sentiment.csv** : Dataset de sentiments sur les compagnies aériennes

#### Fonctionnalités :
- Nettoyage de texte (suppression ponctuation, emojis, stop words)
- Tokenisation et stemming avec NLTK
- Vectorisation TF-IDF
- Classification Random Forest
- Visualisation des distributions de sentiments

### 📁 TP1 (K-Means Clustering)
Implémentation et analyse de l'algorithme K-Means.

#### Fichiers principaux :
- **Kmeans.py** : Implémentation complète de K-Means
- **biblioSklearn.py** : Comparaison avec scikit-learn
- **CRTP1** : Documentation détaillée de l'algorithme
- **Images** : Visualisations des itérations (`Iteration1.png`, `Iteration2.png`, etc.)

#### Fonctionnalités :
- Distance euclidienne
- Assignment des points aux clusters
- Mise à jour des centroïdes
- Critère de convergence
- Visualisation des itérations

### 📁 TP2 (Clustering Avancé)
Comparaison d'algorithmes de clustering avec évaluation de performance.

#### Fichiers principaux :
- **JeuDeDonnees.py** : Génération de datasets synthétiques avec `make_blobs`
- **Kmeans.py** : K-Means avec différents scénarios d'initialisation
- **FCmeans.py** : Fuzzy C-Means clustering
- **Dunn.py** : Calcul de l'indice de Dunn pour évaluation
- **Rapport.pdf** : Analyse comparative complète

#### Fonctionnalités :
- 3 scénarios d'initialisation des centroïdes
- Clustering flou avec degré d'appartenance
- Métriques d'évaluation (indice de Dunn)
- Comparaison des performances

## 🛠️ Technologies Utilisées

### Librairies Python :
- **Analyse de données** : `pandas`, `numpy`
- **Visualisation** : `matplotlib`, `seaborn`
- **Machine Learning** : `scikit-learn`
- **NLP** : `nltk`, `re`
- **Clustering flou** : `scikit-fuzzy`
- **Distance** : `scipy.spatial.distance`

### Algorithmes Implémentés :
- K-Means (implémentation native)
- Fuzzy C-Means
- Random Forest pour classification
- TF-IDF pour vectorisation de texte

## 📊 Datasets

1. **Tweets** : Données Twitter avec sentiments, métadonnées utilisateur
2. **Airlines Sentiment** : Sentiments sur compagnies aériennes US
3. **Données synthétiques** : Clusters générés avec `make_blobs`

## 🚀 Utilisation

### Prérequis :
```bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk scikit-fuzzy scipy
```

### Exécution :
```bash
# NLP et analyse de sentiments
cd TDNLP
python Exo1.py  # Préprocessing
python Exo2.py  # Classification

# Clustering K-Means
cd TP1
python Kmeans.py

# Clustering comparatif
cd TP2
python JeuDeDonnees.py  # Génération données
python Kmeans.py        # K-Means
python FCmeans.py       # Fuzzy C-Means
```
