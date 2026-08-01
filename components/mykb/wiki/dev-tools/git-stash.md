---
type: "concept"
title: "Git Stash"
description: "Temporarily setting aside uncommitted changes so the working tree can be switched or cleaned"
tags: ["git", "workflow", "uncommitted", "state"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Git Stash

## Summary
`git stash` saves uncommitted changes away and restores a clean working tree, then reapplies them later with `git stash pop`. It is the emergency tool for switching branches or experiments without losing work.

## Details
- Stashes are stack-ordered; name them (`git stash push -m`) to keep track.
- Stash only untracked files explicitly with `-u`; conflicts can occur on pop after unrelated changes.
- RSIS3 relevance: agents switching tasks mid-edit can stash a half-written article.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]] — stash supports context switching between branches
- [[wiki/dev-tools/git-rebase|Git Rebase]] — stash clears the tree before rebasing
- [[wiki/llm-agents/context-management|Context Management]] — stashing is git's context switch
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — stash is a lightweight recovery net
