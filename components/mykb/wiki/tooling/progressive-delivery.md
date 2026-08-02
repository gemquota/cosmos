---
type: "concept"
title: "Progressive Delivery"
description: "Shipping changes gradually with automated gates instead of one big switch"
tags: ["progressive-delivery", "deployment", "flags", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Progressive Delivery

## Summary
Progressive delivery exposes a change to an increasing share of users — canary percentage, region, audience — while automated checks decide whether to continue. It is continuous delivery plus explicit risk management.

## Details
- Mechanisms: canaries, ring deployments, feature flags, traffic splitting, and analysis.
- Gates are automated where possible: metrics comparisons decide promote or rollback.
- The goal is small, reversible exposure with evidence at every step.
- mykb relevance: wiki pipeline changes progress per worker ring with metric gates.

## Related
- [[wiki/tooling/rollout-plans|Rollout Plans]]
- [[wiki/tooling/canary-analysis|Canary Analysis]]
- [[wiki/tooling/automated-canary|Automated Canary]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
