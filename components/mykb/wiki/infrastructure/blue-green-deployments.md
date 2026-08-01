---
type: "concept"
title: "Blue-Green Deployments"
description: "Deployment strategy that runs two identical environments and switches traffic for instant rollback"
tags: ["deployment", "blue-green", "rollback", "devops", "zero-downtime"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html"]
---

# Blue-Green Deployments

## Summary
Blue-green deployment keeps two fully provisioned environments — the live "blue" and the staged "green" — and releases by deploying to the idle one, validating, then switching traffic. The switch is the entire release: a load-balancer or DNS update rather than a rolling mutation. Rollback is equally fast, just switch back.

## Details
- Setup: both environments are identical; new versions deploy to the inactive side and are smoke-tested before any user traffic arrives.
- Traffic switch: a load balancer, router, or DNS record flips from blue to green; DNS propagation delays make LB switches preferable for quick rollback.
- Instant rollback: if the new version misbehaves, flip traffic back — no redeploy, no rebuild; the old side is still running and warm.
- Cost: two environments must run simultaneously, roughly doubling capacity cost; cloud autoscaling can reduce idle spend by shrinking the inactive side.
- Database pain point: schema changes are shared between environments, so migrations must be backward-compatible or the switch must be phased — schema-migration planning is mandatory.
- Comparison: blue-green favors full traffic switches and instant rollback; canary deployments favor gradual, metrics-gated ramp-up and lower blast radius.
- Worked example: mykb stages a release on green, runs synthetic checks against it, flips the ingress weight to 100% green, and keeps blue warm for an hour before reusing it.

## Related
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — the property blue-green preserves
- [[wiki/devops-infra/rollback-plans|Rollback Plans]] — switch-back as the rollback mechanism
- [[wiki/infrastructure/schema-migrations|Schema Migrations]] — shared-state constraint on switching
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — gradual alternative with smaller blast radius
- [[wiki/devops-infra/feature-flags|Feature Flags]] — runtime toggles complementing full switches
- [[wiki/devops-infra/kubernetes|Kubernetes]] — blue-green via multi-service traffic weights
