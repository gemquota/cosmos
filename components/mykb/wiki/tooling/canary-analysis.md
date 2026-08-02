---
type: "concept"
title: "Canary Analysis"
description: "Comparing canary metrics against the stable baseline to judge a rollout"
tags: ["canary", "analysis", "metrics", "deployment"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Canary Analysis

## Summary
Canary analysis statistically compares the canary's metrics — errors, latency, saturation — against the baseline during rollout. Tools like Kayenta/Argo Rollouts automate the judgement: pass promotes, fail rolls back.

## Details
- Compare like-for-like: same metric, same time window, traffic-adjusted.
- Use tests (Mann-Whitney, delta thresholds) instead of eyeballing dashboards.
- Decide thresholds before the rollout, not during the panic.
- mykb relevance: canary analysis gates the new link-checker before full rollout.

## Related
- [[wiki/tooling/automated-canary|Automated Canary]]
- [[wiki/tooling/progressive-delivery|Progressive Delivery]]
- [[wiki/tooling/rollout-plans|Rollout Plans]]
- [[wiki/devops-infra/canary-and-blue-green-revisited|Canary and Blue-Green Revisited]]
- [[wiki/dev-tools/four-golden-signals|Four Golden Signals]]
