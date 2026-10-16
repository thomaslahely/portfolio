"""Récupère les README des dépôts GitHub publics → contenu/github/<depot>.md

    uv run python recup_github.py              (utilisateur par défaut)
    uv run python recup_github.py autre_nom

Les forks sont ignorés (ce n'est pas mon travail). Le dossier contenu/github/
est entièrement régénéré : ne pas y éditer de fichiers à la main.
API publique sans authentification : 60 requêtes/heure, largement assez.
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

UTILISATEUR = "thomaslahely"
# dépôts dont le README n'apprend rien sur le projet (le bot citerait du bruit) :
# ils sont décrits à la main dans contenu/projets/
EXCLUS = {
    "Olympique",  # README par défaut de Laravel (sponsors, contact Laravel…)
}
DOSSIER = Path(__file__).parent.parent / "contenu" / "github"
API = "https://api.github.com"


def appel(url, accept="application/vnd.github+json"):
    requete = urllib.request.Request(url, headers={
        "Accept": accept,
        "User-Agent": "portfolio-rag",
    })
    with urllib.request.urlopen(requete, timeout=20) as reponse:
        return reponse.read().decode("utf-8")


def main():
    utilisateur = sys.argv[1] if len(sys.argv) > 1 else UTILISATEUR
    depots = json.loads(appel(f"{API}/users/{utilisateur}/repos?per_page=100&sort=updated"))
    depots = [d for d in depots if not d["fork"] and d["name"] not in EXCLUS]
    print(f"{len(depots)} dépôts (hors forks) pour {utilisateur}")

    DOSSIER.mkdir(parents=True, exist_ok=True)
    for ancien in DOSSIER.glob("*.md"):
        ancien.unlink()

    for depot in depots:
        nom = depot["name"]
        try:
            # media type "raw" : le Markdown brut, pas du JSON en base64
            readme = appel(f"{API}/repos/{utilisateur}/{nom}/readme",
                           accept="application/vnd.github.raw")
        except urllib.error.HTTPError as erreur:
            if erreur.code == 404:
                print(f"  - {nom} : pas de README, ignoré")
                continue
            raise

        # le dépôt <utilisateur>/<utilisateur> est le README de profil GitHub
        if nom.lower() == utilisateur.lower():
            titre = f"Profil GitHub de {utilisateur}"
        else:
            titre = f"Dépôt GitHub {nom}"
            if depot["description"]:
                titre += f" — {depot['description']}"
        langage = depot["language"] or "non précisé"

        entete = (
            "---\n"
            f"titre: {titre.replace(chr(10), ' ')}\n"
            f"url: {depot['html_url']}\n"
            "---\n\n"
            f"Langage principal du dépôt {nom} : {langage}.\n\n"
        )
        (DOSSIER / f"{nom}.md").write_text(entete + readme, encoding="utf-8")
        print(f"  + {nom} ({len(readme)} car., {langage})")


if __name__ == "__main__":
    main()
