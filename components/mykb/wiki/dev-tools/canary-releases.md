---
type: "concept"
title: "Canary Releases"
description: "Rolling a change out to a small slice of traffic before wider exposure"
tags: ["canary", "deployment", "risk", "release"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/CanaryRelease.html", "https://en.wikipedia.org/wiki/Continuous_delivery"]
---

# Canary Releases

## Summary
A canary release ships a new version to a small fraction of users or traffic — the canary — while the rest stay on the stable version. Metrics decide whether the canary is promoted or rolled back, making release risk measurable instead of binary.

## Details
- Canaries scale exposure in stages: 1%, 5%, 25%, 100%, with a health gate between each.
- Comparison is the point: canary metrics vs baseline on errors, latency, and business signals.
- Automated canary analysis (Argo Rollouts, Flagger) removes human judgment from the gate.
- The canary must be able to absorb a disaster: a bad 1% slice is recoverable, a bad 100% is an outage.
- Feature flags complement canaries: canaries test the build, flags test the feature.
- For the mykb bundle, a canary release publishes the new link-checker to a subset of articles before the full corpus.

Worked example — the wiki deploy sends 5% of read traffic to the new index build; link-error metrics compare against the baseline for an hour, then promotion to 100% or automatic rollback.

## Related
- [[wiki/tooling/automated-canary|Automated Canary]]
- [[wiki/tooling/canary-analysis|Canary Analysis]]
- [[wiki/tooling/rollout-plans|Rollout Plans]]
- [[wiki/dev-tools/continuous-deployment|Continuous Deployment]]
- [[wiki/tooling/progressive-delivery|Progressive Delivery]]
- [[wiki/tooling/smoke-tests|Smoke Tests]]
- [[wiki/tooling/traffic-shadowing|Traffic Shadowing]]
- [[wiki/devops-infra/canary-and-blue-green-revisited|Canary & Blue-Green Deploys]]
- [[wiki/devops-infra/mirroring-and-shadow-traffic|Mirroring & Shadow Traffic]]
