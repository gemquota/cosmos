#!/usr/bin/env bash
# COSMOS — auto-sync main → gh-pages (GitHub Pages deploy, pass 11 ops).
#
# Mirrors the manual procedure from docs/audit-suite/34_OPERATIONAL_MANUAL.md
# §6 — but inside an isolated git worktree, so the main checkout's
# untracked/ignored artifacts (node_modules, dist/, local screenshots) are
# never touched. Emits a "Deploy: sync main <sha> — <subject>" commit only
# when the tree actually changed (idempotent).
#
# Usage:
#   infra/deploy/sync-gh-pages.sh          # from a full checkout of main
#   REMOTE=origin infra/deploy/sync-gh-pages.sh
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REMOTE="${REMOTE:-origin}"
cd "$DIR"

MAIN_SHA="$(git rev-parse --short main)"
MAIN_SUBJECT="$(git log -1 --format=%s main)"
if ! git show-ref --verify --quiet refs/heads/gh-pages; then
  echo "Creating gh-pages branch at main $MAIN_SHA..."
  git branch gh-pages main
fi

WT="$DIR/.git/gh-pages-wt"
if [ -e "$WT" ]; then
  git worktree remove --force "$WT" >/dev/null 2>&1 || true
fi
git worktree add --detach "$WT" gh-pages >/dev/null

cd "$WT"
git rm -rf --ignore-unmatch . >/dev/null 2>&1 || true
git checkout main -- .
git add -A
if git diff --cached --quiet; then
  echo "gh-pages unchanged vs main — nothing to deploy"
  cd "$DIR"
  git worktree remove --force "$WT"
  exit 0
fi
git commit -m "Deploy: sync main $MAIN_SHA — $MAIN_SUBJECT"
git push "$REMOTE" gh-pages
cd "$DIR"
git worktree remove --force "$WT"
echo "✅ Deployed main $MAIN_SHA → gh-pages"
