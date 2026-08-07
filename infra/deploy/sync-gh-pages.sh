#!/usr/bin/env bash
# COSMOS — auto-sync main → gh-pages (GitHub Pages deploy, pass 11 ops).
#
# Mirrors the manual procedure from docs/audit-suite/34_OPERATIONAL_MANUAL.md
# §6: replace the gh-pages tree with the main tree and commit a
# "Deploy: sync main <sha> — <subject>" message. Works locally (any remote
# auth) and in GitHub Actions with the default GITHUB_TOKEN.
#
# Usage:
#   infra/deploy/sync-gh-pages.sh          # from a full checkout of main
#   REMOTE=origin infra/deploy/sync-gh-pages.sh
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REMOTE="${REMOTE:-origin}"
cd "$DIR"

if [ "$(git branch --show-current)" != "main" ]; then
  if git rev-parse --verify --quiet main >/dev/null 2>&1; then
    echo "Switching to main..."
    git checkout main >/dev/null 2>&1
  else
    echo "⚠  No main branch here (current: $(git branch --show-current))" >&2
    exit 2
  fi
fi

MAIN_SHA="$(git rev-parse --short main)"
MAIN_SUBJECT="$(git log -1 --format=%s main)"
if ! git show-ref --verify --quiet refs/heads/gh-pages; then
  echo "Creating gh-pages branch..."
  git branch gh-pages
fi

git checkout gh-pages >/dev/null 2>&1
git rm -rf --ignore-unmatch . >/dev/null 2>&1 || true
git checkout main -- .
git add -A
if git diff --cached --quiet; then
  echo "gh-pages unchanged vs main — nothing to deploy"
  git checkout main >/dev/null 2>&1
  exit 0
fi
git commit -m "Deploy: sync main $MAIN_SHA — $MAIN_SUBJECT"
git checkout main >/dev/null 2>&1
git push "$REMOTE" gh-pages
echo "✅ Deployed main $MAIN_SHA → gh-pages"
