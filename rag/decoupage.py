"""Découpage des contenus Markdown en chunks.

Un fichier .md = un document. On coupe d'abord aux titres (#, ##, ###),
puis on regroupe les paragraphes d'une section jusqu'à TAILLE_MAX caractères.

Chaque chunk garde le titre du document et celui de sa section : sans eux,
« j'ai utilisé Docker » ne dit pas de quel projet on parle, ni à l'embedding
ni au LLM.
"""

import re
from pathlib import Path

TAILLE_MAX = 1200  # caractères, ~300 tokens : une idée par chunk


def lire_front_matter(texte):
    """Sépare l'en-tête optionnel (--- cle: valeur ---) du corps Markdown."""
    meta = {}
    if texte.startswith("---\n"):
        fin = texte.find("\n---", 4)
        if fin != -1:
            for ligne in texte[4:fin].splitlines():
                if ":" in ligne:
                    cle, valeur = ligne.split(":", 1)
                    meta[cle.strip()] = valeur.strip().strip('"')
            texte = texte[fin + 4:]
    return meta, texte.lstrip("\n")


def sections(corps):
    """Coupe le corps aux titres de niveau 1 à 3 → liste de (titre, texte).

    Les lignes dans un bloc de code ``` ne sont jamais des titres :
    un « # installer les dépendances » dans un README bash n'en est pas un.
    """
    resultat = []
    titre, lignes = "", []
    dans_code = False
    for ligne in corps.splitlines():
        if ligne.lstrip().startswith("```"):
            dans_code = not dans_code
        titre_trouve = None if dans_code else re.match(r"^#{1,3}\s+(.*)", ligne)
        if titre_trouve:
            if "\n".join(lignes).strip():
                resultat.append((titre, "\n".join(lignes).strip()))
            titre, lignes = titre_trouve.group(1).strip(), []
        else:
            lignes.append(ligne)
    if "\n".join(lignes).strip():
        resultat.append((titre, "\n".join(lignes).strip()))
    return resultat


def regrouper(texte, taille_max=TAILLE_MAX):
    """Regroupe les paragraphes d'une section en morceaux d'au plus taille_max.

    On ne coupe jamais au milieu d'un paragraphe : un paragraphe trop long
    (gros bloc de code) devient un morceau à lui seul.
    """
    morceaux, courant = [], ""
    for paragraphe in re.split(r"\n\s*\n", texte):
        paragraphe = paragraphe.strip()
        if not paragraphe:
            continue
        if courant and len(courant) + 2 + len(paragraphe) > taille_max:
            morceaux.append(courant)
            courant = paragraphe
        else:
            courant = f"{courant}\n\n{paragraphe}" if courant else paragraphe
    if courant:
        morceaux.append(courant)
    return morceaux


def decouper_fichier(chemin, racine):
    """Rend les chunks d'un fichier .md, sans id (attribué par indexer.py)."""
    meta, corps = lire_front_matter(chemin.read_text(encoding="utf-8"))
    # les commentaires HTML sont des notes pour l'auteur, pas pour le bot
    corps = re.sub(r"<!--.*?-->", "", corps, flags=re.DOTALL)
    relatif = chemin.relative_to(racine).with_suffix("").as_posix()

    titre_doc = meta.get("titre", chemin.stem)
    # URL citée par le bot : celle du front matter, sinon la page du portfolio
    url = meta.get("url", f"/{relatif}")

    chunks = []
    for section, texte in sections(corps):
        for morceau in regrouper(texte):
            chunks.append({
                "document": relatif,
                "titre": titre_doc,
                "section": section,
                "url": url,
                "chunk": morceau,
            })
    return chunks


def texte_a_encoder(chunk):
    """Ce que voit le modèle d'embeddings : contexte + contenu."""
    entete = chunk["titre"]
    if chunk["section"] and chunk["section"] != chunk["titre"]:
        entete += f" — {chunk['section']}"
    return f"{entete}\n{chunk['chunk']}"


def decouper_dossier(racine):
    """Tous les .md du dossier, dans un ordre stable (ids reproductibles)."""
    racine = Path(racine)
    chunks = []
    for chemin in sorted(racine.rglob("*.md")):
        if chemin.name.startswith("_"):  # _LISEZMOI.md & co : pas indexés
            continue
        chunks.extend(decouper_fichier(chemin, racine))
    return chunks
