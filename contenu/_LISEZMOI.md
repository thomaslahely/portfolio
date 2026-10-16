# Contenu du portfolio (et base de connaissances du chatbot)

Chaque fichier `.md` de ce dossier est indexé par `rag/indexer.py`
(sauf ceux dont le nom commence par `_`, comme celui-ci).

## Organisation

- `cv.md` : parcours, formation, compétences
- `projets/<slug>.md` : une page par projet
- `notes/<slug>.md` : articles / notes techniques
- `github/<depot>.md` : README récupérés par `rag/recup_github.py` (ne pas éditer à la main)

## En-tête (front matter)

```
---
titre: Nom lisible du document
url: /projets/mon-projet        (optionnel, sinon déduit du chemin)
---
```

## Conseils d'écriture pour un bon RAG

- Des titres `##` explicites : chaque section devient un ou plusieurs chunks,
  et son titre est ajouté au texte encodé.
- Une idée par section. Nommer les choses (« ce projet utilise Docker »)
  plutôt que « il utilise ça » : chaque chunk doit se comprendre seul.
- Ne rien écrire de privé : tout ce qui est ici peut être cité publiquement par le bot.
- Après modification : `cd rag && uv run python indexer.py`
