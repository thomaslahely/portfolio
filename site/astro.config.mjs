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
  // Chaque page est un dossier (/projets/ → projets/index.html) : l'adresse officielle finit par « / ».
  // Avec 'always', le serveur de dev refuse /projets sans « / » : un lien oublié se voit tout de suite
  // (en production, Caddy le rattraperait par une redirection 308, un aller-retour de plus).
  trailingSlash: 'always',
  // Le moteur Markdown par défaut d'Astro 7 (Sätteri) garde les commentaires HTML :
  // ce plugin remark (paquet @astrojs/markdown-remark) les retire.
  markdown: {
    remarkPlugins: [retirerCommentaires],
  },
  vite: {
    build: {
      // Aucun script collé dans le HTML : le script du chat sort dans un fichier de /_astro/.
      // La politique de sécurité du site (en-tête Content-Security-Policy, dans le Caddyfile du VPS)
      // n'autorise que les scripts servis en fichiers (script-src 'self'), pas les scripts en ligne.
      // undefined = règle habituelle pour le reste (petites feuilles de style intégrées à la page).
      assetsInlineLimit: (chemin) => (chemin.endsWith('.js') ? false : undefined),
    },
    server: {
      // en dev, /api/* part vers l'API FastAPI locale (en prod, c'est Caddy qui route)
      proxy: { '/api': 'http://127.0.0.1:8000' },
    },
  },
});
