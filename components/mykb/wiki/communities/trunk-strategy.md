---
type: "concept"
title: "Trunk Strategy"
description: "The practice of committing small changes directly to the mainline"
tags: ["trunk-based", "git", "branching", "continuous-integration"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Trunk Strategy

## Summary
Trunk-based development keeps everyone on a short-lived branch or directly on main, merging small changes frequently behind feature toggles. It maximizes integration frequency and minimizes merge pain, and it is the foundation of continuous integration.

## Details
- Branches live hours, not weeks; feature flags hide incomplete work instead of branches.
- Requires discipline: small commits, fast CI, and toggles that actually isolate risk.
- Release from main with tags or toggles; rollback is a revert or flag flip.
- mykb relevance: the wiki workers commit to trunk in small verifiable batches.

## Related
- [[wiki/dev-tools/trunk-based-development|Trunk-Based Development]]
- [[wiki/communities/branch-strategies|Branch Strategies]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/communities/github-flow|GitHub Flow]]
