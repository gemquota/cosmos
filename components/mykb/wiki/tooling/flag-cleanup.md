---
type: "concept"
title: "Flag Cleanup"
description: "Removing feature flags and their dead branches after rollout completes"
tags: ["feature-flags", "cleanup", "refactoring", "delivery"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Flag Cleanup

## Summary
Flag cleanup removes the now-default code path and the flag machinery once a rollout is done, leaving one clear implementation. It is the maintenance half of feature flags: the flag is a temporary scaffolding for controlled rollout, and cleanup is the demolition that prevents the scaffolding from becoming permanent architecture.

## Details
- Cleanup is a code change: delete the old branch, the flag check, and the config entry. The complete change touches the code (remove the conditional), the configuration (remove the flag definition and any environment overrides), the docs (remove the flag from runbooks), and the tests (replace flag-matrix tests with tests of the one remaining path).
- Do it promptly — the longer a flag lives, the more code accretes around it. Every release that runs with the flag adds code that assumes the flag's existence; every team member who learns the flag treats it as permanent; and every code path that branches on it doubles the surface area for bugs. A flag that survives a quarter is a flag that will survive a year.
- Concrete example: a new curation pipeline ships behind `USE_NEW_PIPELINE`. Rollout completes, the flag is on everywhere, and the old pipeline is dead code — but it stays because "we might need to roll back." Six months later, the old path has drifted from the new one, rollback would be dangerous anyway, and every bug report now has to be triaged against two implementations. Cleanup deletes the old path and makes the new one the only one.
- Include a flag inventory in the rollout plan so nothing is forgotten. The rollout plan should name the flag, the owner, the removal criteria (metrics met, soak period passed), and the removal date; the inventory turns cleanup from a vague intention into a scheduled, owned task.
- Failure modes: cleanup that removes the flag but not the dead branch, leaving the code path with no reachable entry; cleanup that forgets the config entry, so the flag name lingers in every environment's config; and premature cleanup that deletes the rollback path while the new behavior is still unstable.
- Tradeoffs: the discipline of scheduling cleanup trades a small planning cost for permanently lower complexity; skipping cleanup trades the plan for flag debt that compounds — every future change has to reason about both branches, and the eventual cleanup gets harder and riskier the longer it waits.
- mykb relevance: after a curation feature stabilizes, the worker removes its flag in the same pass — the wiki's own automation should model the cleanup discipline it documents.

## Related
- [[wiki/tooling/flag-debt|Flag Debt]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/tooling/rollout-plans|Rollout Plans]]
- [[wiki/software-engineering/code-smells|Code Smells]]
