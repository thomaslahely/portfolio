// Plan du site pour les moteurs de recherche : https://lahely.fr/sitemap.xml
// (annoncé dans public/robots.txt). Écrit à la main plutôt qu'avec @astrojs/sitemap :
// une dépendance de moins pour vingt lignes. Une nouvelle page fixe s'ajoute dans PAGES_FIXES ;
// les projets et les notes sont trouvés tout seuls.
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

const PAGES_FIXES = ['/', '/projets/', '/notes/', '/a-propos/'];

export const GET: APIRoute = async ({ site }) => {
  const chemins = [
    ...PAGES_FIXES,
    ...(await getCollection('projets')).map((projet) => `/projets/${projet.id}/`).sort(),
    ...(await getCollection('notes')).map((note) => `/notes/${note.id}/`).sort(),
  ];
  const urls = chemins.map((chemin) => `  <url><loc>${new URL(chemin, site).href}</loc></url>`);
  const xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ...urls,
    '</urlset>',
    '',
  ].join('\n');
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
