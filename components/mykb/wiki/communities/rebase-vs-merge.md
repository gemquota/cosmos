---
type: "concept"
title: "Rebase vs Merge"
description: "Two ways to integrate branches: rewriting history or preserving it"
tags: ["git", "rebase", "merge", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Rebase vs Merge

## Summary
Rebase replays your commits on top of the target branch, producing a linear history; merge preserves the branch structure with a merge commit. Linear history eases bisecting and reviewing; merge history preserves context about how work combined.

## Details
- Rebase before merge keeps feature branches linear and integration clean.
- Never rebase shared branches — rewriting published history breaks other clones.
- Merges (including -no-ff) preserve grouping; squash merges collapse noise but lose granularity.
- mykb relevance: the wiki uses rebase-on-pull with squash merges for clean log history.

## Related
- [[wiki/communities/squash-merges|Squash Merges]]
- [[wiki/dev-tools/git-rebase|Git Rebase]]
- [[wiki/dev-tools/merge-conflicts|Merge Conflicts]]
- [[wiki/communities/cherry-picks|Cherry-Picks]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
