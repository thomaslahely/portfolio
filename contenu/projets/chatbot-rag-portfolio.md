---
titre: Projet — chatbot RAG du portfolio
url: /projets/chatbot-rag-portfolio
---

# Projet — chatbot RAG du portfolio

## Résumé

Le chatbot de ce portfolio est un système de RAG (Retrieval-Augmented Generation)
codé à la main par Thomas, sans framework comme LangChain ou LlamaIndex. Il répond aux
questions des visiteurs sur le parcours et les projets de Thomas, en s'appuyant
uniquement sur le contenu du portfolio et en citant ses sources.

## Fonctionnement du RAG

Les pages du portfolio (écrites en Markdown) et les README des dépôts GitHub de Thomas
sont découpées en passages selon leurs titres et paragraphes. Chaque passage est
transformé en vecteur avec le modèle d'embeddings multilingue
`intfloat/multilingual-e5-small`. À chaque question, le chatbot calcule la similarité
cosinus entre la question et tous les passages, garde les 8 plus proches, et les
transmet au modèle de langage Claude (Anthropic), qui rédige la réponse en citant les
pages utilisées. Les réponses s'affichent au fil de l'eau (streaming).

## Fiabilité et sécurité

- Un seuil de similarité filtre les questions hors sujet avant tout appel au LLM.
- Les consignes du modèle lui interdisent d'inventer une information absente des
  documents, et le protègent contre l'injection de prompt.
- Limites de requêtes par adresse IP, taille de question bornée et plafond de dépense
  protègent contre les abus.
- La clé d'API n'est jamais dans le code ni dans le dépôt git.

## Évaluation et itérations

Thomas a appliqué la méthode de son précédent projet de RAG sur des cours (mesure du
recall@k et calibrage du seuil de refus). Un exemple d'itération : la question
« Thomas a-t-il fait du clustering ? » ne trouvait le bon dépôt qu'au 8e rang, car le
mot « clustering » n'apparaissait pas dans son README. La solution a été double :
envoyer 8 passages au lieu de 5, et rédiger des pages projet avec le vocabulaire
qu'utilise un recruteur.

## Architecture et déploiement

API en Python avec FastAPI, conteneurisée avec Docker et hébergée sur le serveur
personnel de Thomas, derrière le reverse proxy Caddy (HTTPS automatique).
Voir aussi le [serveur personnel lahely.fr](/projets/vps-lahely).

## Technologies

Python, FastAPI, sentence-transformers, NumPy, API Claude (Anthropic), Server-Sent
Events, Docker, Caddy.
