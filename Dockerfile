# Image de l'API du chatbot (rag/api.py).
# Contexte de build = racine du dépôt : l'image embarque rag/ ET contenu/.
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    HF_HOME=/opt/huggingface \
    PYTHONUNBUFFERED=1

WORKDIR /app/rag

# 1. Dépendances seules d'abord : cette couche (torch…, la plus lourde) reste
#    en cache tant que pyproject.toml / uv.lock ne changent pas.
COPY rag/pyproject.toml rag/uv.lock ./
# cache uv monté HORS de l'image (sinon ~1,2 Go de paquets en double dedans),
# et réutilisé d'un build à l'autre
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# 2. Code et contenu, puis indexation au build : le modèle d'embeddings est
#    téléchargé ici, une fois, et l'index est figé dans l'image.
COPY rag/*.py ./
COPY contenu /app/contenu
RUN .venv/bin/python indexer.py

# 3. Exécution : utilisateur sans privilèges, aucun accès réseau à Hugging Face.
RUN useradd --system --no-create-home app
USER app
ENV HF_HUB_OFFLINE=1 \
    PATH="/app/rag/.venv/bin:$PATH"

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/api/sante', timeout=4)"

# un seul worker : les limites de requêtes sont gardées en mémoire (voir api.py)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
