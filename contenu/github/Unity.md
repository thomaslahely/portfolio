---
titre: Dépôt GitHub Unity — TPs Unity: déplacement de personnage avec IA de poursuite, simulation de grues articulées
url: https://github.com/thomaslahely/Unity
---

Langage principal du dépôt Unity : C#.

# 🕹️ Projets Unity – Thomas Lahely

Bienvenue sur mon dépôt Unity regroupant plusieurs travaux pratiques réalisés dans le cadre de mes études. Ces projets utilisent le moteur **Unity** avec le langage **C#**, et abordent des concepts variés comme les déplacements, les articulations robotiques ou encore la gestion de la physique.

N’hésite pas à explorer mes repositories et à me contacter pour toute opportunité professionnelle ! 🚀

## 📁 Sommaire des TPs

| TP | Description |
|----|-------------|
| **TP1** | Contrôle d’un personnage avec déplacement, sprint, saut, et poursuite par un ennemi. 
| **TP2** | Simulation d’une grue avec gestion du pivot, du chariot, du moufle, de la caméra, et détection d'objets. 
| **TP3** | Commande avancée d’une grue articulée à l’aide d’axes personnalisés et états d’articulation. 

---

## 🧠 Détails techniques

### TP1 – Mouvement et poursuite
- Contrôle clavier : flèches pour avancer/reculer/rotation, `Shift` pour sprinter, `Space` pour sauter.
- Script `Mouvement.cs` pour le joueur.
- Script `Poursuite.cs` pour un ennemi qui suit le joueur.

### TP2 – Contrôle de grue
- Utilisation de composants `ArticulationBody` pour une simulation physique réaliste.
- Contrôles :
  - `← / →` : rotation de la flèche.
  - `↑ / ↓` : déplacement du chariot.
  - `Shift / Ctrl` : déplacement vertical du moufle.
- Changement de caméras (`C`).
- Scripts : `ControlGrue.cs`, `Declencheur.cs`, `Grappin.cs`, `ChariotControleur.cs`, etc.

### TP3 – Grue articulée par axes d’entrée
- Architecture modulaire avec des états (enum) pour chaque type de mouvement (`EtatChariot`, `EtatFleche`, `EtatRotation`, `EtatTranslation`).
- Contrôle d’axes via `Input.GetAxis` pour plus de finesse.
- Composants principaux : `ChariotCommande`, `FlecheCommande`, `RotationCommande`, `TranslationCommande`.



## 🚀 Pour lancer un TP

1. Ouvre Unity.
2. Clone ce dépôt :
   ```bash
   git clone https://github.com/thomaslahely/Unity.git
