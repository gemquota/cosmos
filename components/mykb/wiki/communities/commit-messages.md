---
type: "concept"
title: "Commit Messages"
description: "The conventions that make git history readable and machine-usable"
tags: ["commit-messages", "git", "conventions", "documentation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Commit Messages

## Summary
Commit messages are the smallest unit of project documentation: a subject that states what and why, a body with context, and optional trailers. Conventional Commits makes subjects machine-parseable for changelogs and releases.

## Details
- Write imperative subjects (Fix login bug, not Fixed) and keep them under 72 characters.
- Body explains the why and the tradeoffs; trailers add references (Fixes #123, Reviewed-by).
- Conventional Commits (feat:, fix:) drive semantic-release and changelog generation.
- mykb relevance: every wiki PR squashes to a conventional commit that feeds the changelog.

## Related
- [[wiki/dev-tools/conventional-commits|Conventional Commits]]
- [[wiki/communities/semantic-release|Semantic Release]]
- [[wiki/communities/changelog-generation|Changelog Generation]]
- [[wiki/communities/squash-merges|Squash Merges]]
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]]
