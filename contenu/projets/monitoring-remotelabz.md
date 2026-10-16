---
titre: Projet TER — monitoring de la plateforme RemoteLabz (Prometheus, Grafana, Playwright)
url: /projets/monitoring-remotelabz
---

# Projet TER — monitoring de la plateforme RemoteLabz

<!-- À COMPLÉTER : année du TER, encadrant / équipe, ton rôle exact,
     ce que tu as appris, résultat (dashboards obtenus, problèmes détectés). -->

## Résumé

Dans le cadre d'un TER (travail d'étude et de recherche), Thomas a contribué à
RemoteLabz, une plateforme open source d'apprentissage pratique à distance qui permet
aux enseignants de créer des environnements réseau simulés (QEMU, RabbitMQ, Docker)
pour leurs étudiants. Son travail : mettre en place une stack d'observabilité qui
surveille la machine hébergeant la plateforme et les résultats de ses tests automatisés.
Code source : [dépôt ProjetTER](https://github.com/thomaslahely/ProjetTER).

## Supervision système : Prometheus, Grafana, Node Exporter

Node Exporter, lancé dans un conteneur Docker, expose les métriques de la machine
virtuelle (CPU, mémoire, disque, réseau). Prometheus, installé comme service systemd,
collecte ces métriques toutes les 15 secondes, et Grafana les affiche dans des tableaux
de bord.

## Tests de bout en bout avec Playwright et exportateur de métriques

Thomas a préparé des tests de bout en bout Playwright sur l'application, et écrit un
exportateur de métriques personnalisé en Node.js (`metrics.js`, avec Express et
prom-client) qui publie les résultats des tests au format Prometheus. Ce service est
maintenu en fonctionnement par le gestionnaire de processus pm2. Les résultats des
tests deviennent ainsi visibles dans Grafana, à côté des métriques système.

## Technologies

Linux, Docker, Prometheus, Grafana, Node Exporter, systemd, Node.js, Express,
prom-client, Playwright, pm2.
