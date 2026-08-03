---
type: "concept"
title: "Canary & Blue-Green Deploys"
description: "Incremental and instantaneous release strategies with rollback"
tags: ["canary", "blue-green", "deployment", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Canary & Blue-Green Deploys

## Summary
Canary and blue-green are progressive delivery strategies that release with a limited blast radius. Blue-green keeps two full environments and flips traffic atomically; canary shifts small fractions of traffic to a new version while comparing health metrics. The "revisited" framing reflects the modern norm: metric-gated analysis, automated rollback, and controller-driven orchestration instead of manual DNS flips.

## Details
- Blue-green: two identical environments, one live, one staging; a router switch moves all traffic, and rollback is just switching back. It costs double capacity and complicates schema changes — the old environment must keep serving while the new one migrates data, so a backward-compatible migration window is required.
- Canary: the new version receives 5-10% of traffic; compare error rate, latency, and business metrics, then promote in steps or abort. Canaries handle data migration better because both versions share the data path, but need careful routing (sticky sessions, header-based selection) and enough traffic for statistically meaningful comparison.
- Concrete example: Argo Rollouts with a blue-green strategy and automated promotion; Flagger with a canary analysis querying Prometheus for 5xx rate and p99 latency over a five-minute window.
- Failure modes: canary traffic too small to detect problems — a 1% failure rate on 10% of traffic hides issues until promotion; blue-green flips with stale config or failed readiness in the new environment; session affinity breaking mid-analysis; metric divergence from caching skew causing false alarms.
- Tradeoffs: blue-green gives near-instant rollback and clean semantics but doubles cost and complicates stateful releases; canary is cheaper and tests real traffic gradually but needs solid metrics and a longer promotion window. A common hybrid is canary for API services and blue-green for static frontends and workers.
- RSIS3 relevance: RSIS3's L2 strategy experiments can reuse canary-style evaluation — run a new parameter set on a small slice of tasks, compare pulse telemetry, and promote or revert.

## Related
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — related coverage in the same cluster
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
