---
type: "concept"
title: "Branch Strategies"
description: "The workflow rules for how branches are created, merged, and protected"
tags: ["git", "branching", "workflow", "strategy"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Branch Strategies

## Summary
Branch strategies define the lifecycle of branches — main, feature, release, hotfix — and the merge rules between them. Git Flow, GitHub Flow, and trunk-based development are the canonical models; the choice shapes review, release, and risk.

## Details
- Every strategy balances integration frequency against stability: longer-lived branches diverge more.
- Protect main with review and CI gates; make the strategy explicit in CONTRIBUTING docs.
- The best strategy is the one the whole team actually follows — consistency beats cleverness.
- mykb relevance: the wiki repo uses trunk-based commits with short-lived feature branches.

## Related
- [[wiki/communities/git-flow|Git Flow]]
- [[wiki/communities/github-flow|GitHub Flow]]
- [[wiki/communities/trunk-strategy|Trunk Strategy]]
- [[wiki/communities/rebase-vs-merge|Rebase vs Merge]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
