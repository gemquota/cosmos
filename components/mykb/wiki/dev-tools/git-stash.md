---
type: "concept"
title: "Git Stash"
description: "Temporarily setting aside uncommitted changes so the working tree can be switched or cleaned"
tags: ["git", "workflow", "uncommitted", "state"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://git-scm.com/docs/git-stash", "https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning"]
---

# Git Stash

## Summary
`git stash` saves uncommitted changes away and restores a clean working tree, then reapplies them later with `git stash pop`. It is the emergency tool for switching branches or experiments without losing work.

## Details
- Stashes are stack-ordered; name them (`git stash push -m`) to keep track.
- Stash only untracked files explicitly with `-u`; conflicts can occur on pop after unrelated changes.
- RSIS3 relevance: agents switching tasks mid-edit can stash a half-written article.
- git stash temporarily shelves uncommitted changes so the working tree can switch context, then restores them later.
- Stashes are identified, listed, and can be popped, applied, or dropped; they are not a substitute for commits.
- The danger is stash loss and stash drift: a stale stash can conflict with the branch it is eventually applied to.
- Stash works best for short interruptions; anything longer deserves a branch or a commit.
- **Worked example / comparison** — Worked example — mid-edit on an article, an urgent fix is needed; git stash shelves the edits, the fix lands on its own commit, and git stash pop restores the original work.
- For mykb, git-stash is documented as the quick context-switch tool in the git toolkit cluster.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]]
- [[wiki/dev-tools/git-rebase|Git Rebase]]
- [[wiki/llm-agents/context-management|Context Management]]
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
