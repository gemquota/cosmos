---
type: "concept"
title: "Zero-Downtime Deploys"
description: "Deployment techniques that keep services available while new versions take over"
tags: ["deployments", "zero-downtime", "reliability", "devops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Zero-Downtime Deploys

## Summary
Zero-downtime deployment updates software without interrupting service: rolling, blue-green, and canary are the main strategies. The hard parts are draining old instances, readiness, and state compatibility.

## Details
- Rolling updates replace instances incrementally; blue-green switches wholesale; canaries ramp by traffic.
- Readiness gates, grace periods, and connection draining make each strategy safe.
- Schema changes are the usual culprit: backward-compatible migrations first.
- Open question: how to measure that a deploy truly had zero user impact.

## Related
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — wholesale switch strategy
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — gradual ramp strategy
- [[wiki/infrastructure/rolling-restarts|Rolling Restarts]] — incremental replacement
- [[wiki/infrastructure/graceful-termination|Graceful Termination]] — the drain half of the swap
