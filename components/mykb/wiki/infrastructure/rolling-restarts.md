---
type: "concept"
title: "Rolling Restarts"
description: "Restarting a fleet gradually — one instance at a time — to apply changes without downtime"
tags: ["rolling", "restart", "deployment", "kubernetes"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Rolling Restarts

## Summary
A rolling restart replaces instances one at a time so the fleet always serves traffic during the change.

## Details
- Kubernetes Deployments do this natively: maxSurge and maxUnavailable control the pace.
- Rolling restarts are only safe if instances drain and become ready correctly — health checks gate each step.
- Rollback is a restart to the previous spec, cheap when images are immutable.
- Open question: when a full restart (not rolling) is the safer choice.

## Related
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — the property rolling keeps safe
- [[wiki/infrastructure/graceful-termination|Graceful Termination]] — each instance must drain
- [[wiki/infrastructure/containerization|Containerization]] — the deployment unit being rolled
- [[wiki/devops-infra/kubernetes|Kubernetes]] — native rolling update semantics
