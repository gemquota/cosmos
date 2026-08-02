---
type: "concept"
title: "Coding Standards"
description: "The shared conventions that keep a codebase consistent and reviewable"
tags: ["coding-standards", "conventions", "quality", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Coding_conventions", "https://en.wikipedia.org/wiki/Software_quality"]
---

# Coding Standards

## Summary
Coding standards are the agreed conventions — naming, formatting, structure, and idioms — that make a codebase readable as if by one author. Their value is not the specific rule but the consistency: reviews focus on logic, and newcomers learn faster.

## Details
- Standards should be few, explicit, and enforced by tooling; a 50-page handbook no one reads is fiction.
- Style rules belong in formatters and linters, not in review comments.
- Standards adapt: revisit them when the team or the ecosystem changes, and record the rationale.
- Consistency beats perfection: a slightly imperfect standard followed everywhere beats a perfect one ignored.
- Content standards apply too: the wiki's frontmatter and linking rules are coding standards for articles.
- For the mykb bundle, standards cover slug format, frontmatter fields, tag naming, and link syntax.
- Worked example — the wiki's standards doc: kebab-case slugs, three-plus tags, ISO timestamps, and verified sources; CI enforces each one mechanically.

Worked example — the wiki's standards doc: kebab-case slugs, three-plus tags, ISO timestamps, and verified sources; CI enforces each one mechanically.

## Related
- [[wiki/software-engineering/linting-practice|Linting Practice]]
- [[wiki/software-engineering/code-formatters|Code Formatters]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]]
- [[wiki/communities/pre-commit-hooks|Pre-Commit Hooks]]
- [[wiki/software-engineering/code-smells|Code Smells]]
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
