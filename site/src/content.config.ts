// Les pages du site viennent de ../contenu/ : les mêmes fichiers Markdown
// alimentent le site ET le chatbot (rag/indexer.py).
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const schema = z.object({
  titre: z.string(),
  url: z.string().optional(),
});

const projets = defineCollection({
  loader: glob({ pattern: '*.md', base: '../contenu/projets' }),
  schema,
});

const notes = defineCollection({
  loader: glob({ pattern: '*.md', base: '../contenu/notes' }),
  schema,
});

const pages = defineCollection({
  loader: glob({ pattern: 'cv.md', base: '../contenu' }),
  schema,
});

export const collections = { projets, notes, pages };
