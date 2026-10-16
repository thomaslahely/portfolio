---
titre: Note — Docker contourne le pare-feu ufw
url: /notes/docker-contourne-ufw
---

# Note — Docker contourne le pare-feu ufw

## Le problème

Sur un serveur Ubuntu protégé par ufw, on pourrait croire qu'un port non autorisé
dans ufw est inaccessible depuis Internet. C'est faux pour les conteneurs Docker :
une ligne `ports: "8080:8080"` dans un fichier Compose rend le port 8080 accessible
au monde entier, même si ufw ne l'autorise pas.

## Pourquoi

Docker écrit ses propres règles iptables (chaîne DOCKER) pour rediriger le trafic
vers les conteneurs. Ces règles sont évaluées avant celles d'ufw, qui ne les voit donc pas.

## La solution retenue

- Un seul conteneur publie des ports publics : le reverse proxy Caddy (80 et 443).
- Les autres services ne publient aucun port : Caddy les joint par le réseau Docker
  interne, en utilisant le nom du conteneur (par exemple `reverse_proxy vaultwarden:80`).
- Si un accès local est nécessaire, on publie seulement sur la boucle locale :
  `127.0.0.1:3001:3001`.

## Comment vérifier

La commande `ss -tlnp` liste les ports en écoute : une adresse `0.0.0.0` ou `[::]`
signifie « accessible depuis l'extérieur », `127.0.0.1` signifie « local uniquement ».
