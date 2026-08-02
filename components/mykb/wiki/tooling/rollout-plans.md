---
type: "concept"
title: "Rollout Plans"
description: "Staged schedules for exposing a change to increasing fractions of users"
tags: ["rollout", "delivery", "planning", "feature-flags"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Rollout Plans

## Summary
A rollout plan sequences a change through increasing exposure — internal users, 1%, 10%, 100% — with gates and rollback criteria at each step. It turns deployment risk into a series of small, reversible decisions.

## Details
- Define per-stage gates: error rate, latency, support tickets, key metric health.
- Plan the rollback before the rollout: what flag or version reverts instantly?
- Involve on-call and comms: a staged rollout still needs an owner and a watch.
- mykb relevance: wiki pipeline changes roll out per worker group before global adoption.

## Related
- [[wiki/tooling/progressive-delivery|Progressive Delivery]]
- [[wiki/dev-tools/canary-releases|Canary Releases]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/dev-tools/release-management|Release Management]]
