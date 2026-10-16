"""Moteur de recherche : trouve les chunks les plus proches d'une question.

Même principe que rag-cours/recherche.py. Le chargement (chunks, embeddings,
modèle) se fait une seule fois, à l'import du module.

Test rapide en ligne de commande :
    uv run python recherche.py "Quels projets utilisent Docker ?"
"""

import json
import os
import sys
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

INDEX = Path(os.environ.get("INDEX_DIR", Path(__file__).parent / "index"))
MODELE = "intfloat/multilingual-e5-small"
# 8 et pas 5 : « clustering » ne trouve le dépôt KmeansFMeans qu'au rang 8
# (le mot n'est pas dans son README). ~700 tokens de contexte, coût négligeable.
K_DEFAUT = 8
# Provisoire : à recalibrer sur une éval du portfolio (comme dans rag-cours).
# Les scores E5 sont tassés (souvent 0,75–0,90) : un petit écart compte.
SEUIL_REFUS = float(os.environ.get("SEUIL_REFUS", "0.80"))


def _charger_chunks(chemin):
    with open(chemin, encoding="utf-8") as f:
        return [json.loads(ligne) for ligne in f]


# --- chargement, une seule fois ----------------------------------------
chunks = _charger_chunks(INDEX / "chunks.jsonl")
embeddings = np.load(INDEX / "embeddings.npy")

assert len(chunks) == embeddings.shape[0], (
    f"{len(chunks)} chunks mais {embeddings.shape[0]} vecteurs — relance indexer.py"
)

modele = SentenceTransformer(MODELE)


def rechercher(question, k=K_DEFAUT):
    """Rend les k chunks les plus proches, du meilleur au moins bon.

    Chaque résultat est le dictionnaire du chunk, enrichi d'une clé "score".
    """
    vecteur = modele.encode(f"query: {question}", normalize_embeddings=True)
    # vecteurs normalisés des deux côtés → le produit scalaire EST le cosinus
    scores = embeddings @ vecteur
    meilleurs = np.argsort(-scores)[:k]

    resultats = []
    for indice in meilleurs:
        resultat = dict(chunks[indice])
        resultat["score"] = float(scores[indice])
        resultats.append(resultat)
    return resultats


def hors_domaine(resultats, seuil=SEUIL_REFUS):
    """True si le meilleur score est sous le seuil : aucune réponse fiable."""
    return not resultats or resultats[0]["score"] < seuil


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or input("Question : ")
    resultats = rechercher(question)
    print(f"hors domaine : {hors_domaine(resultats)} (seuil {SEUIL_REFUS})\n")
    for r in resultats:
        print(f"{r['score']:.3f}  {r['document']} › {r['section'] or '(intro)'}")
        print(f"       {r['chunk'][:150]!r}\n")
