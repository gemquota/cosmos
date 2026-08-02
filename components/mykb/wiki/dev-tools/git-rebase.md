---
type: "concept"
title: "Git Rebase"
description: "Rewriting commit history by replaying commits onto a new base"
tags: ["git", "history", "workflow", "rewriting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://git-scm.com/docs/git-rebase", "https://git-scm.com/book/en/v2/Git-Branching-Rebasing"]
---

# Git Rebase

## Summary
`git rebase` replays a branch's commits onto another base, producing a linear history and clean integration points. It is the tool for tidying history before merge — and the source of the golden rule: never rebase published history.

## Details
- Interactive rebase (`-i`) lets you reorder, squash, edit, and drop commits.
- Use over merge when a linear, readable history matters; force-push only on unpublished branches.
- RSIS3 relevance: wiki edit history can be squashed into meaningful 'knowledge units' before publishing.
- git rebase rewrites a branch's commits onto another base, producing a linear history where feature commits sit on top of the latest mainline.
- Interactive rebase (rebase -i) allows reordering, squashing, and editing commits, which is how messy work becomes a clean story.
- Rebasing rewrites history, so it must never touch commits others have already based work on — the golden rule of rebasing.
- The alternative, merging, preserves reality but creates merge commits and a less readable linear narrative.
- **Worked example / comparison** — Comparison — merge keeps the true history with a merge commit; rebase rewrites it into a clean linear sequence; the choice trades honesty against readability.
- For mykb, git-rebase is documented as the history-shaping tool, with the golden rule guarding shared branches.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]]
- [[wiki/dev-tools/git-stash|Git Stash]]
- [[wiki/dev-tools/merge-conflicts|Merge Conflicts]]
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]]
- [[wiki/memory/git-for-notes|Git for Notes]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
