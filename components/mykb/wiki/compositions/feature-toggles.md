---
type: "concept"
title: "Feature Toggles"
description: "Runtime switches that turn features on and off without deploys"
tags: ["feature-toggles", "flags", "delivery", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Feature Toggles

## Summary
Feature toggles gate code paths at runtime — off by default, flipped via config — letting teams merge early, release slowly, and roll back instantly. They are the mechanism behind trunk-based development and progressive delivery.

## Details
- Types: release toggles, experiment toggles, ops toggles, permission toggles — each with a lifecycle.
- Toggle configuration is code-adjacent: version it, review it, and make it auditable.
- Every toggle is debt until removed — schedule cleanup in the rollout plan.
- mykb relevance: wiki curation features ship behind toggles per worker group.

## Related
- [[wiki/tooling/feature-flag-sdks|Feature Flag SDKs]]
- [[wiki/tooling/flag-debt|Flag Debt]]
- [[wiki/dev-tools/trunk-based-development|Trunk-Based Development]]
- [[wiki/tooling/progressive-delivery|Progressive Delivery]]
- [[wiki/devops-infra/feature-flags|Feature Flags]]
