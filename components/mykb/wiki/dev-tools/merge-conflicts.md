---
type: "concept"
title: "Merge Conflicts"
description: "The state where concurrent changes touch overlapping lines and git cannot auto-merge them"
tags: ["git", "merging", "conflicts", "collaboration"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Merge Conflicts

## Summary
A merge conflict occurs when two branches change the same lines and git cannot decide the result. Resolving it requires reading both sides and writing the intended combined output.

## Details
- Conflict markers show ours/theirs; edit to the correct result, then `git add` and continue.
- Prevention: small branches, frequent integration, and formatting consistency.
- RSIS3 relevance: concurrent wiki workers editing nearby notes will hit the same discipline.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]] — conflicts are a symptom of integration strategy
- [[wiki/dev-tools/git-rebase|Git Rebase]] — rebase surfaces conflicts earlier than merge
- [[wiki/software-engineering/code-review|Code Review]] — review before merge reduces conflict surface
- [[wiki/memory/git-for-notes|Git for Notes]] — text notes minimize conflict noise
- [[wiki/data-storage/data-versioning|Data Versioning]] — conflict resolution preserves version history
