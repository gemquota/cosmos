---
type: "concept"
title: "Flag Debt"
description: "The accumulated cost of flags that are never cleaned up"
tags: ["feature-flags", "debt", "technical-debt", "cleanup"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Flag Debt

## Summary
Flag debt is the maintenance cost of stale flags: dead code paths, both-branch testing, confusion about which flags are live. Every flag is a liability once its rollout is done — the debt is unpaid cleanup work.

## Details
- Flags rot fast: half the flags in a mature system are permanently on or dead.
- Track flag lifecycle with owners, rollout dates, and cleanup deadlines.
- A flag that cannot be evaluated for cleanup should be treated as debt, not feature.
- mykb relevance: the wiki's curation flags need an owner and a review cadence.

## Related
- [[wiki/tooling/flag-cleanup|Flag Cleanup]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/software-engineering/technical-debt-management|Technical Debt Management]]
- [[wiki/tooling/rollout-plans|Rollout Plans]]
- [[wiki/software-engineering/code-smells|Code Smells]]
