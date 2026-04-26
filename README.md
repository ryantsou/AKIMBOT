# 🤖 AKIMBOT

Bienvenue sur le dépôt du projet **AKIMBOT** ! 
Il s'agit de notre projet visant à développer un système complet pour contrôler le robot Marty (via une interface graphique) et gérer des affrontements/danses via un serveur arbitre central.

## 🎯 Les grands objectifs du projet

Pour mener à bien ce projet, voici ce que nous allons développer :

- **L'application client robot** : pour piloter Marty et lire les capteurs (interface PyQt + librairie martypy).
- **L'application serveur arbitre** : une API REST (FastAPI) pour centraliser et calculer les scores.
- **La gestion des fichiers** : parsing et exécution des chorégraphies (`.dance`) et des règles (`.battle`).
- **La gestion de projet** : suivi rigoureux sur GitHub (issues, kanban, branches, pull requests).
- **La qualité** : tests unitaires, revue de code, et bien sûr une démo finale fonctionnelle !

## 👥 L'équipe

- **RAJHONSON**
- **IHEB**
- **ILLAS**

## ✍️ Convention de nommage des commits

Pour éviter que notre historique Git ne se transforme en un champ de bataille illisible, on s'est mis d'accord sur la convention suivante : `type(scope): description`

- `feat` : Nouvelle fonctionnalité (ex: `feat(client): ajout du pad directionnel`)
- `fix` : Correction d'un bug (ex: `fix(arbitre): correction du calcul des scores`)
- `docs` : Modification de la documentation (ex: `docs: mise à jour du README`)
- `style` : Formatage, indentation, etc. sans impact sur le code (ex: `style: nettoyage client_robot.py`)
- `chore` : Maintenance, tâches techniques ou configuration (ex: `chore: ajout de FastAPI dans requirements.txt`)

## 🔄 Le script de synchronisation (Optionnel)

Au début, notre planning sur Excel changeait souvent et recréer les issues GitHub à la main devenait vite laborieux. 
On a donc mis en place le script `sync_gantt_project.py` pour générer automatiquement nos tickets depuis l'Excel. 

En résumé, il fait ça :
- Il lit l'onglet Gantt de `gantt.xlsx`.
- Il crée les tickets manquants sur GitHub et les place dans notre Kanban.

> **Note :** Maintenant que notre backlog est fixe et propre, on n'a normalement plus besoin de relancer ce script ! Tout se passe directement sur GitHub.

## 🛠️ Installation

Pour configurer l'environnement (`.venv`) et installer les dépendances :
```bash
chmod +x install.sh
./install.sh
```

## 🚀 Lancement

**Lancer l'interface Client Robot :**
```bash
.venv/bin/python client_robot.py
```

## 🌿 Branches Git par fonctionnalité

Chaque phase du Gantt correspond à une branche dédiée :

| Branche | Phase |
|---|---|
| `feature/initialisation` | 🚀 Initialisation |
| `feature/gestion` | 📋 Gestion |
| `feature/conception` | 🏗️ Conception |
| `feature/client-marty` | 🔌 Client – Marty |
| `feature/client-ui` | 🖥️ Client – UI |
| `feature/arbitre` | ⚖️ Arbitre |
| `feature/integration` | 🔗 Intégration |

### Création des branches

Le script `create_feature_branches.sh` crée toutes les branches depuis `main` en une seule commande :

```bash
chmod +x create_feature_branches.sh
./create_feature_branches.sh
```

Le script est idempotent : il ne recrée pas une branche qui existe déjà.

### Convention de nommage

- Branches de fonctionnalité : `feature/<nom-court>` (minuscules, tirets)
- Branches de correction : `fix/<description>`
- Branches de release : `release/<version>`

Toute modification transite par une **Pull Request** vers `main` (branche protégée).

## Fichiers importants

- `gantt.xlsx`: planning source
- `sync_gantt_project.py`: synchronisation Gantt -> GitHub
- `install.sh`: creation de l'environnement local
- `create_feature_branches.sh`: création des branches Git par fonctionnalité
