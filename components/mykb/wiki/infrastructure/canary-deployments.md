---
type: "concept"
title: "Canary Deployments"
description: "Progressive release strategy that routes a small percentage of traffic to a new version and ramps on success"
tags: ["canary", "deployment", "progressive", "metrics", "devops"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/CanaryRelease.html"]
---

# Canary Deployments

## Summary
Canary deployment exposes a new version to a small slice of real traffic, watches health and business metrics, and only then ramps the rollout wider. It limits the blast radius of bad releases while validating against production conditions that staging cannot replicate. The name comes from the canary in the coal mine: the small cohort detects danger early.

## Details
- Mechanics: a load balancer or service mesh splits traffic by weight or by a stable attribute (header, user-id hash) between old and new versions.
- Metric gates: the release pauses or rolls back if error rate, latency, or business metrics on the canary cohort breach SLO thresholds.
- Analysis can be automated (metric-based promotion) or manual (SRE review); automation is safer for high-change systems.
- Smoke tests first: run synthetic checks against the canary before letting real traffic in, then step 1% → 5% → 25% → 100% with evaluation between steps.
- Comparison: canaries ramp gradually with live validation; blue-green flips wholesale with instant rollback; canary rollback is a weight change, slightly slower but with a much smaller exposed cohort.
- Tooling: service meshes (Istio traffic splitting) and Kubernetes multi-service weights implement it natively; feature flags decouple code activation from deployment.
- Worked example: mykb ships a query-engine change to 5% of traffic, compares p95 latency and error rate for ten minutes, then promotes or reverts.

## Related
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — the goal canary releases serve
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — the metrics gates need visibility
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — the all-at-once alternative
- [[wiki/devops-infra/feature-flags|Feature Flags]] — runtime activation complementing canaries
- [[wiki/devops-infra/observability|Observability]] — measures the canary cohort's health
- [[wiki/infrastructure/service-mesh|Service Mesh]] — weighted traffic splitting for canaries
