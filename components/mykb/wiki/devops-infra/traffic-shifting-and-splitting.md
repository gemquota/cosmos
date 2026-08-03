---
type: "concept"
title: "Traffic Shifting & Splitting"
description: "Moving percentages of traffic between versions gradually"
tags: ["traffic-shifting", "canary", "routing", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Traffic Shifting & Splitting

## Summary
Traffic shifting and splitting control what fraction of requests reach which version: shifting moves traffic gradually (10%, 50%, 100%) during canaries and blue-green flips, while splitting sends a stable ratio to two or more versions over time (A/B testing, multi-version operation). The mechanics are the same — routing weight — applied to different purposes.

## Details
- Mechanism: the router (service mesh, gateway, or LB) assigns weights per destination; shifting changes weights over time, usually gated on health metrics; splitting holds weights steady for experiments; selection can be random or deterministic by header, cookie, or user id (sticky and hash-based routing).
- Concrete example: Argo Rollouts or Flagger steps a canary through 10/25/50/100% while checking metrics; an Istio VirtualService splits 90/10 between versions for an A/B test keyed by cookie; a blue-green flip shifts 0-100% atomically or in steps; traffic splitting also supports dark launch by sending a copy to a shadow destination.
- Failure modes: sticky routing breaking the split (all traffic goes to one version); hash keys that cluster users onto one version, biasing the experiment; shifting too fast for metrics to react, letting a bad version get full traffic; weight config applied to the wrong router or environment; session state not shared between versions, so users see inconsistencies mid-flip.
- Tradeoffs: traffic control gives precise, reversible release decisions but adds routing complexity and needs real metric quality to gate shifts; the alternative — deploy-and-hope — is simpler and riskier; the payoff is that promotion and rollback become weight changes, not redeploys.
- Operational notes: validate weight changes in staging, monitor per-version metrics, and make rollback a documented weight flip.
- RSIS3 relevance: RSIS3's strategy changes can reuse traffic-style evaluation — split tasks between the current and candidate behavior by weight, compare outcomes, and shift as confidence grows.

## Related
- [[wiki/infrastructure/traffic-shaping-and-qos|Traffic Shaping & QoS]]
- [[wiki/devops-infra/mirroring-and-shadow-traffic|Mirroring & Shadow Traffic]]
- [[wiki/infrastructure/east-west-vs-north-south-traffic|East-West vs North-South Traffic]]
- [[wiki/infrastructure/traffic-engineering|Traffic Engineering]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
