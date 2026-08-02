---
type: "concept"
title: "Squash Merges"
description: "Collapsing a branch's commits into one before merging to main"
tags: ["squash-merges", "git", "history", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Squash Merges

## Summary
Squash merging folds a feature branch's whole commit set into a single commit on main, trading granular history for a clean, readable log. It is the standard for PR-based workflows where branch commits are messy.

## Details
- Squashing loses per-commit granularity and bisect fidelity within the branch.
- Pair squash with a good PR title and description — that becomes the commit message.
- Use conventional commits on the squashed message for changelog automation.
- mykb relevance: the wiki's PRs squash to one conventional commit each.

## Related
- [[wiki/communities/rebase-vs-merge|Rebase vs Merge]]
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/communities/semantic-release|Semantic Release]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
