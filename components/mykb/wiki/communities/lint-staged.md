---
type: "concept"
title: "Lint-Staged"
description: "Running linters only on staged files for speed"
tags: ["lint-staged", "linting", "git", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Lint-Staged

## Summary
Lint-staged runs linters and formatters on only the files staged for commit, keeping pre-commit checks fast as repositories grow. It gives per-file enforcement without paying full-repo costs on every commit.

## Details
- Configure with husky/pre-commit: lint-staged picks staged paths and runs configured commands.
- Fast feedback is the point — full-repo checks stay in CI.
- Auto-fix modes (eslint --fix, prettier --write) let hooks fix what they flag.
- mykb relevance: the wiki stages markdown files and lints only those on commit.

## Related
- [[wiki/communities/pre-commit-hooks|Pre-Commit Hooks]]
- [[wiki/communities/git-hooks|Git Hooks]]
- [[wiki/software-engineering/linting-practice|Linting Practice]]
- [[wiki/software-engineering/code-formatters|Code Formatters]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
