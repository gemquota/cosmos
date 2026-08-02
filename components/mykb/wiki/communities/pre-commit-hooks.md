---
type: "concept"
title: "Pre-Commit Hooks"
description: "Checks that run before a commit is created"
tags: ["pre-commit", "git-hooks", "quality", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pre-Commit Hooks

## Summary
Pre-commit hooks run linters, formatters, and checks before each commit, catching issues at the earliest and cheapest point. Tools like pre-commit (framework) and husky manage and share them across the team.

## Details
- Fail the commit on violations so bad code never enters history.
- Keep them fast (seconds) or developers will bypass them with --no-verify.
- CI should run the same checks — local hooks are convenience, CI is enforcement.
- mykb relevance: the wiki pre-commit validates frontmatter fields and kebab-case slugs.

## Related
- [[wiki/communities/git-hooks|Git Hooks]]
- [[wiki/communities/lint-staged|Lint-Staged]]
- [[wiki/software-engineering/linting-practice|Linting Practice]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
