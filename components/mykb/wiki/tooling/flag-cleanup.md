---
type: "concept"
title: "Flag Cleanup"
description: "Removing feature flags and their dead branches after rollout completes"
tags: ["feature-flags", "cleanup", "refactoring", "delivery"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Flag Cleanup

## Summary
Flag cleanup removes the now-default code path and the flag machinery once a rollout is done, leaving one clear implementation. Skipping cleanup is how flag debt accumulates; scheduling it is part of the rollout plan.

## Details
- Cleanup is a code change: delete the old branch, the flag check, and the config entry.
- Do it promptly — the longer a flag lives, the more code accretes around it.
- Include a flag inventory in the rollout plan so nothing is forgotten.
- mykb relevance: after a curation feature stabilizes, the worker removes its flag in the same pass.

## Related
- [[wiki/tooling/flag-debt|Flag Debt]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/tooling/rollout-plans|Rollout Plans]]
- [[wiki/software-engineering/code-smells|Code Smells]]
