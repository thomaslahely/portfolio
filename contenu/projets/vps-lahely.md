---
titre: Projet — serveur personnel lahely.fr
url: /projets/vps-lahely
---

# Projet — serveur personnel lahely.fr

## Objectif du projet

Thomas a installé et administre son propre serveur (VPS OVHcloud sous Ubuntu)
pour apprendre l'administration système en conditions réelles. Ce serveur héberge
le portfolio lahely.fr, ce chatbot, et plusieurs services auto-hébergés.

## Sécurisation du serveur

L'accès SSH se fait uniquement par clé : l'authentification par mot de passe et la
connexion root sont désactivées. Le pare-feu ufw bloque tout le trafic entrant sauf
SSH, HTTP et HTTPS. fail2ban bannit automatiquement les adresses qui multiplient les
tentatives de connexion SSH. Les mises à jour de sécurité s'installent seules
(unattended-upgrades), et une sauvegarde complète du serveur est faite chaque jour.

## Architecture Docker et reverse proxy Caddy

Chaque service tourne dans son propre conteneur Docker, décrit par un fichier
Docker Compose. Tous les conteneurs partagent un réseau Docker commun. Caddy sert de
reverse proxy : c'est le seul conteneur exposé sur Internet (ports 80 et 443), et il
obtient et renouvelle automatiquement les certificats HTTPS Let's Encrypt.
Grâce à un enregistrement DNS wildcard, publier un nouveau service sur un
sous-domaine demande seulement trois lignes de configuration Caddy.

## Services hébergés

- Uptime Kuma : supervision de la disponibilité des sites.
- Vaultwarden : gestionnaire de mots de passe compatible Bitwarden, avec inscriptions
  fermées et 2FA.
- Le chatbot RAG du portfolio (voir le projet « chatbot du portfolio »).

## Ce que Thomas a appris

Le piège principal rencontré : les ports publiés par Docker contournent le pare-feu ufw.
La règle adoptée est donc qu'aucun conteneur, à part Caddy, ne publie de port public.
Thomas a aussi appris à toujours valider une configuration avant de la recharger
(`caddy validate`, `sshd -t`) et à vérifier chaque changement (curl, logs, dig).

## Technologies

Ubuntu, Docker, Docker Compose, Caddy, Let's Encrypt, ufw, fail2ban, DNS (OVH, DNSSEC).
