---
type: "concept"
title: "Revert Strategies"
description: "Backing out bad changes by reverting commits or restoring old state"
tags: ["revert", "git", "rollback", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Revert Strategies

## Summary
Revert strategies decide how to undo a bad change: git revert makes a new commit that undoes it (history-preserving), git reset rewinds history (destructive), or restore brings back files. Choice depends on whether history was shared.

## Details
- Prefer revert for published history; reset only for unpushed local history.
- Revert the commit, not the feature: partial reverts of multi-commit work break semantics.
- A revert is itself a change — review and test it like any commit.
- mykb relevance: a broken wiki article edit is reverted with a new commit and re-reviewed.

## Related
- [[wiki/communities/rebase-vs-merge|Rebase vs Merge]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/communities/cherry-picks|Cherry-Picks]]
- [[wiki/dev-tools/git-rebase|Git Rebase]]
- [[wiki/dev-tools/release-management|Release Management]]
