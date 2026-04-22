# AKIMBOT

Projet de coordination et de suivi pour l'organisation du travail autour du Gantt, du GitHub Project et des issues.

## Attendus du projet

Selon la presentation du projet, les points attendus sont:

- application client robot (Marty + interface PyQt)
- application serveur arbitre (API REST + score)
- gestion des fichiers `.dance` et `.battle`
- suivi de projet avec GitHub (issues, project, branches, PR)
- tests, revue de code et demo finale

## Intervenants

- RAJHONSON
- IHEB
- ILLAS

## Pourquoi il y a un script de sync

Le planning change souvent, et refaire les issues a la main prend du temps.
Le script `sync_gantt_project.py` sert surtout a garder GitHub coherent avec le fichier Gantt:

- lire les micro-taches depuis `gantt.xlsx`
- creer les issues manquantes
- ajouter les elements dans le GitHub Project
- ajouter les titres de phase pour que le board reste lisible

Si le planning ne bouge presque plus, on peut tres bien fonctionner sans relancer la sync.

## Installation

1. Rendre le script executable:

```bash
chmod +x install.sh
```

2. Lancer l'installation:

```bash
./install.sh
```

Le script cree un environnement virtuel `.venv` puis installe les paquets de `requirements.txt`.

## Utilisation

Execution de la synchronisation:

```bash
.venv/bin/python sync_gantt_project.py
```

Le script est idempotent: si tu le relances, il ne recree pas tout depuis zero.

## Statut de synchro actuel

Etat verifie le 20/04/2026:

- 64 taches Gantt detectees
- 64 issues presentes
- 64 elements presents dans le GitHub Project
- 0 tache manquante

Conclusion: il n'est pas necessaire de relancer la sync si le Gantt ne change pas.

## Branches Git par fonctionnalité

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
