import { getCollection, type CollectionEntry } from 'astro:content';

// Projets mis en avant, dans cet ordre ; les autres suivent par ordre alphabétique.
const ORDRE = [
  'chatbot-rag-portfolio',
  'clustering-kmeans-nlp',
  'vps-lahely',
  'monitoring-remotelabz',
];

export async function projetsTries() {
  const projets = await getCollection('projets');
  const rang = (id: string) => {
    const i = ORDRE.indexOf(id);
    return i === -1 ? ORDRE.length : i;
  };
  return projets.sort((a, b) => rang(a.id) - rang(b.id) || a.id.localeCompare(b.id));
}

/** « Projet — serveur personnel lahely.fr » → « Serveur personnel lahely.fr » */
export function titreCourt(projet: CollectionEntry<'projets'>) {
  const titre = projet.data.titre.replace(/^Projet( TER)?\s+—\s+/, '');
  return titre.charAt(0).toUpperCase() + titre.slice(1);
}

/** Premier paragraphe de la section « Résumé » (ou de la page), sans Markdown. */
export function resume(projet: CollectionEntry<'projets'>) {
  const corps = (projet.body ?? '').replace(/<!--[\s\S]*?-->/g, '');
  // sans section « Résumé » : le texte qui suit le premier titre ## (la ligne du titre est retirée avec lui)
  const section = corps.split(/^##\s+Résumé\s*$/m)[1] ?? corps.split(/^##\s+.*$/m)[1] ?? '';
  const paragraphe = section.trim().split(/\n\s*\n/)[0] ?? '';
  return paragraphe
    .split('\n')
    .filter((ligne) => !ligne.startsWith('Code source'))
    .join(' ')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/[`*]/g, '')
    .trim();
}
