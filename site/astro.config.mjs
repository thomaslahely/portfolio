// @ts-check
import { defineConfig } from 'astro/config';

/**
 * Retire les commentaires HTML (<!-- À COMPLÉTER … -->) du Markdown publié :
 * ce sont des notes pour l'auteur, elles ne doivent pas finir dans le HTML du site.
 * (Le chatbot les ignore déjà : voir rag/decoupage.py.)
 */
function retirerCommentaires() {
  /** @param {any} noeud */
  const nettoyer = (noeud) => {
    if (!noeud.children) return;
    noeud.children = noeud.children.filter(
      (/** @type {any} */ enfant) =>
        !(enfant.type === 'html' && enfant.value.trim().startsWith('<!--')),
    );
    noeud.children.forEach(nettoyer);
  };
  return nettoyer;
}

export default defineConfig({
  site: 'https://lahely.fr',
  // Le moteur Markdown par défaut d'Astro 7 (Sätteri) garde les commentaires HTML :
  // ce plugin remark (paquet @astrojs/markdown-remark) les retire.
  markdown: {
    remarkPlugins: [retirerCommentaires],
  },
  vite: {
    server: {
      // en dev, /api/* part vers l'API FastAPI locale (en prod, c'est Caddy qui route)
      proxy: { '/api': 'http://127.0.0.1:8000' },
    },
  },
});
