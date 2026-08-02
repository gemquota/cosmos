---
type: "concept"
title: "Git Hooks"
description: "Scripts that git runs automatically at workflow events"
tags: ["git-hooks", "git", "automation", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Git Hooks

## Summary
Git hooks are scripts triggered by git events — pre-commit, pre-push, post-merge, commit-msg — letting teams enforce or automate workflow steps locally. They are powerful but per-clone: they are not enforced on other machines unless CI checks too.

## Details
- Hooks live in .git/hooks; teams share them via templates, core.hooksPath, or tools like husky/lefthook.
- Client-side hooks gate the developer; server-side hooks (pre-receive) gate the repo.
- Hooks must be fast and non-fragile or developers disable them.
- mykb relevance: the wiki repo's pre-commit hook validates frontmatter and link syntax.

## Related
- [[wiki/communities/pre-commit-hooks|Pre-Commit Hooks]]
- [[wiki/communities/lint-staged|Lint-Staged]]
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
