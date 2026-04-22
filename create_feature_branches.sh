#!/usr/bin/env bash
# create_feature_branches.sh
# Crée les branches Git par fonctionnalité à partir de main.
# Idempotent : repart de la branche courante après chaque création.
#
# Branches créées :
#   feature/initialisation  – Phase 🚀 Initialisation
#   feature/gestion         – Phase 📋 Gestion
#   feature/conception      – Phase 🏗️ Conception
#   feature/client-marty    – Phase 🔌 Client – Marty
#   feature/client-ui       – Phase 🖥️ Client – UI
#   feature/arbitre         – Phase ⚖️ Arbitre
#   feature/integration     – Phase 🔗 Intégration

set -euo pipefail

REMOTE="${REMOTE:-origin}"
BASE_BRANCH="${BASE_BRANCH:-main}"

BRANCHES=(
    "feature/initialisation"
    "feature/gestion"
    "feature/conception"
    "feature/client-marty"
    "feature/client-ui"
    "feature/arbitre"
    "feature/integration"
)

echo "Base : ${REMOTE}/${BASE_BRANCH}"
echo ""

git fetch "${REMOTE}" "${BASE_BRANCH}" 2>/dev/null || true

created=0
already=0

for branch in "${BRANCHES[@]}"; do
    if git ls-remote --exit-code --heads "${REMOTE}" "${branch}" > /dev/null 2>&1; then
        echo "  [déjà présente] ${branch}"
        already=$((already + 1))
    else
        git push "${REMOTE}" "${REMOTE}/${BASE_BRANCH}:refs/heads/${branch}"
        echo "  [créée]         ${branch}"
        created=$((created + 1))
    fi
done

echo ""
echo "Résumé :"
echo "  Branches créées       : ${created}"
echo "  Branches déjà présentes : ${already}"
