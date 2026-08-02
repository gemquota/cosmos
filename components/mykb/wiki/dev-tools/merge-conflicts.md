---
type: "concept"
title: "Merge Conflicts"
description: "The state where concurrent changes touch overlapping lines and git cannot auto-merge them"
tags: ["git", "merging", "conflicts", "collaboration"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging", "https://git-scm.com/docs/git-merge"]
---

# Merge Conflicts

## Summary
A merge conflict occurs when two branches change the same lines and git cannot decide the result. Resolving it requires reading both sides and writing the intended combined output.

## Details
- Conflict markers show ours/theirs; edit to the correct result, then `git add` and continue.
- Prevention: small branches, frequent integration, and formatting consistency.
- RSIS3 relevance: concurrent wiki workers editing nearby notes will hit the same discipline.
- A merge conflict occurs when two branches change the same lines in incompatible ways and git cannot combine them automatically.
- Conflict markers show both versions; resolving means deciding the correct merged result, not just picking a side blindly.
- Conflicts are cheaper to prevent than resolve: small, frequent merges and rebasing onto recent mainline shrink the conflict window.
- The resolution should be tested — the merge may be textually clean and semantically broken.
- **Worked example / comparison** — Worked example — two editors rewrite the same paragraph of a wiki article on different branches; the merge pauses with both versions marked, and a human reconciles them into one.
- For mykb, merge-conflicts is documented as the resolution skill behind the wiki's sync and collaboration practices.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]]
- [[wiki/dev-tools/git-rebase|Git Rebase]]
- [[wiki/software-engineering/code-review|Code Review]]
- [[wiki/memory/git-for-notes|Git for Notes]]
- [[wiki/data-storage/data-versioning|Data Versioning]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
