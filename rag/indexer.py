"""Indexation : contenu/*.md → index/chunks.jsonl + index/embeddings.npy.

À relancer à chaque modification du contenu :
    uv run python indexer.py
"""

import json
import os
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

from decoupage import decouper_dossier, texte_a_encoder

ICI = Path(__file__).parent
CONTENU = Path(os.environ.get("CONTENU_DIR", ICI.parent / "contenu"))
INDEX = Path(os.environ.get("INDEX_DIR", ICI / "index"))
MODELE = "intfloat/multilingual-e5-small"


def main():
    chunks = decouper_dossier(CONTENU)
    if not chunks:
        raise SystemExit(f"aucun .md trouvé dans {CONTENU}")
    for numero, chunk in enumerate(chunks, start=1):
        chunk["id"] = numero

    documents = sorted({c["document"] for c in chunks})
    tailles = [len(c["chunk"]) for c in chunks]
    print(f"{len(chunks)} chunks · {len(documents)} documents · "
          f"taille moyenne {sum(tailles) // len(tailles)} car. · max {max(tailles)}")

    # les modèles E5 exigent le préfixe "passage: " sur les documents
    modele = SentenceTransformer(MODELE)
    embeddings = modele.encode(
        [f"passage: {texte_a_encoder(c)}" for c in chunks],
        batch_size=32,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    INDEX.mkdir(parents=True, exist_ok=True)
    with open(INDEX / "chunks.jsonl", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    np.save(INDEX / "embeddings.npy", embeddings)
    print(f"index écrit dans {INDEX} : {embeddings.shape}")


if __name__ == "__main__":
    main()
