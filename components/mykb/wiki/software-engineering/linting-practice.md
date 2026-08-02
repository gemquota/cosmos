---
type: "concept"
title: "Linting Practice"
description: "Using linters to catch problems and enforce style automatically"
tags: ["linting", "static-analysis", "quality", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Lint_(software)", "https://en.wikipedia.org/wiki/Static_program_analysis"]
---

# Linting Practice

## Summary
Linting runs rules over code to catch bugs, smells, and style violations before they reach review. Practice means a small, opinionated rule set, fast execution, and enforcement in both editor and CI.

## Details
- Linters catch real bugs (unused variables, unsafe patterns) alongside style — configure both layers.
- Auto-fix what can be fixed; leave judgment calls to rules that are easy to override consciously.
- Run in the editor (instant feedback) and in CI (enforcement), with the same config.
- Rule fatigue is real: too many rules produce noise and disablements; curate ruthlessly.
- Custom rules encode team-specific standards; document why each non-standard rule exists.
- For the mykb bundle, linting covers articles: frontmatter fields, link syntax, and tag naming enforced by a custom linter.
- Worked example — the wiki linter flags an article with two tags and a broken wikilink before commit; the contributor fixes both locally, and CI confirms.

Worked example — the wiki linter flags an article with two tags and a broken wikilink before commit; the contributor fixes both locally, and CI confirms.

## Related
- [[wiki/software-engineering/static-analysis|Static Analysis]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
- [[wiki/communities/lint-staged|Lint-Staged]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/communities/pre-commit-hooks|Pre-Commit Hooks]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
- [[wiki/software-engineering/code-formatters|Code Formatters]]
