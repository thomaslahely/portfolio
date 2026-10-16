#!/usr/bin/env bash
# Déploiement du portfolio sur le VPS (dans ~/apps/portfolio, clone de ce dépôt).
#
# Lancé par GitHub Actions via une clé SSH bridée sur cette seule commande,
# ou à la main : ~/apps/portfolio/deploy.sh
#
# Tout le script est dans une fonction : bash la lit en entier avant de
# l'exécuter, donc le `git reset` qui réécrit ce fichier ne perturbe pas
# l'exécution en cours.
set -euo pipefail

main() {
  cd "$(dirname "$(readlink -f "$0")")"

  echo "== 1/4 code : alignement sur origin/main"
  git fetch --quiet origin main
  git reset --hard --quiet origin/main
  git log -1 --format='   %h %s'

  echo "== 2/4 site : build Astro dans un conteneur Node jetable"
  # tout le dépôt est monté : le site lit ses pages dans ../contenu/
  docker run --rm \
    -v "$PWD:/depot" -w /depot/site \
    -u "$(id -u):$(id -g)" -e npm_config_cache=/tmp/.npm \
    node:22-alpine \
    sh -c 'npm ci --no-audit --no-fund --loglevel=error && npm run build --silent'
  # copie EN PLACE (rsync --delete) : Caddy monte le dossier www/, le remplacer
  # par un autre dossier (mv) casserait le montage
  mkdir -p www
  rsync -a --delete site/dist/ www/

  echo "== 3/4 API : rebuild et redémarrage si l'image a changé"
  docker compose up -d --build --remove-orphans --quiet-pull
  docker image prune -f > /dev/null

  echo "== 4/4 vérification"
  for _ in $(seq 1 60); do
    etat=$(docker inspect -f '{{.State.Health.Status}}' portfolio-rag)
    if [ "$etat" = healthy ]; then
      echo "   API : healthy"
      echo "== déploiement terminé"
      return 0
    fi
    sleep 2
  done
  echo "   API : $etat après 120 s — logs :" >&2
  docker compose logs --tail 30 portfolio-rag >&2
  return 1
}

main "$@"
