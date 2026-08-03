---
type: "concept"
title: "Progressive Delivery Models"
description: "Phased rollout combining flags, canaries, and metrics gates"
tags: ["progressive-delivery", "releases", "canary", "metrics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Progressive Delivery Models

## Summary
Progressive delivery models — canary, blue-green, ring-based, dark launch — release software to a growing share of users instead of all-at-once, gating each step on health signals. The models differ in mechanics but share the principle: reduce blast radius and make rollback a decision, not a disaster.

## Details
- Canary: shift a small percentage of traffic to the new version, compare metrics, promote in steps or abort; gradual and cheap, requires metric quality and enough traffic for signal.
- Blue-green: run two full environments and flip traffic atomically; instant rollback, costs double capacity and complicates stateful changes.
- Ring-based: deploy outward through rings (internal, canary region, 10%, 50%, all) with a pause and judgment at each ring — a model used by large consumer platforms where traffic and environment fidelity vary by ring.
- Dark launch: run the new path in production without user-visible effect, comparing outputs — validated behavior before any traffic shifts.
- Concrete example: Flagger or Argo Rollouts stepping a canary 10/25/50/100% with Prometheus checks; a ring rollout that stops at 50% during a regression, holding the ring until fixed; a dark-launched rewrite whose results are scored offline for a week before the flag flips.
- Failure modes: promoting on weak metrics (not enough traffic or signal); automatic promotion overriding human judgment in subtle regressions; ring boundaries that leak (users bouncing between rings) breaking the experiment; stateful schema changes that make reverting a ring impossible.
- Tradeoffs: every model trades speed, cost, and complexity against safety; canaries suit APIs, blue-green suits static and stateless tiers, rings suit large fleets, dark launch suits rewrites; the common requirement is good observability and an explicit promotion decision path.
- RSIS3 relevance: RSIS3's strategy changes are progressive deliveries of behavior — a canary-style evaluation of new parameters, with pulse telemetry as the gate, mirrors these models directly.

## Related
- [[wiki/devops-infra/kubernetes-networking-models|Kubernetes Networking Models]]
- [[wiki/devops-infra/continuous-delivery-pipelines|Continuous Delivery Pipelines]]
- [[wiki/devops-infra/progressive-rollout-metrics|Progressive Rollout Metrics]]
- [[wiki/devops-infra/progressive-sync-strategies|Progressive Sync Strategies]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
