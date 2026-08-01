---
type: "concept"
title: "Git Rebase"
description: "Rewriting commit history by replaying commits onto a new base"
tags: ["git", "history", "workflow", "rewriting"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Git Rebase

## Summary
`git rebase` replays a branch's commits onto another base, producing a linear history and clean integration points. It is the tool for tidying history before merge — and the source of the golden rule: never rebase published history.

## Details
- Interactive rebase (`-i`) lets you reorder, squash, edit, and drop commits.
- Use over merge when a linear, readable history matters; force-push only on unpublished branches.
- RSIS3 relevance: wiki edit history can be squashed into meaningful 'knowledge units' before publishing.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]] — rebase is a workflow choice, not a mandate
- [[wiki/dev-tools/git-stash|Git Stash]] — stash protects uncommitted work before rebasing
- [[wiki/dev-tools/merge-conflicts|Merge Conflicts]] — rebases trigger conflicts to resolve on the branch
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — rewritten history changes what rollback can do
- [[wiki/memory/git-for-notes|Git for Notes]] — note history is rebased too
