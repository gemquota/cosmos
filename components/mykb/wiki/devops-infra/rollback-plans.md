---
type: "concept"
title: "Rollback Plans"
description: "Predefined, rehearsed procedures for reverting bad releases quickly and safely"
tags: ["rollback", "releases", "reliability", "deployments"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Rollback Plans

## Summary
A rollback plan defines how to revert a release before it hurts users: what to switch back, what data constraints exist, and who decides.

## Details
- Design for rollback: blue-green traffic switches, image version pins, and feature flags beat code-level revert.
- Schema changes break naive rollbacks — plan data rollback or forward-fix separately.
- Rehearse rollbacks; a rollback you have never run will fail when you need it.
- Open question: when roll-forward is safer than rollback.

## Related
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — switch-back as rollback
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — weight-based rollback
- [[wiki/devops-infra/feature-flags|Feature Flags]] — runtime rollback without redeploy
- [[wiki/devops-infra/backups|Backups]] — data-level rollback
