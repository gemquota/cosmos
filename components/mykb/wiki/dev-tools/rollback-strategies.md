---
type: "concept"
title: "Rollback Strategies"
description: "The prepared ways to undo a bad release quickly"
tags: ["rollback", "deployment", "recovery", "release"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Rollback_(data_management)", "https://en.wikipedia.org/wiki/Deployment_environment"]
---

# Rollback Strategies

## Summary
Rollback strategies are the rehearsed paths for undoing a bad deployment: revert the version, restore the previous artifact, or flip a feature flag. The best rollback is the one that takes seconds and was practiced before the emergency.

## Details
- The fastest rollbacks are architectural: blue-green keeps the old version warm; feature flags disable the change; database migrations are additive and reversible.
- Version rollback (redeploy the previous artifact) is simple but needs backward-compatible data.
- Database rollbacks are the hard case: schema changes need downgrade scripts or forward-only discipline.
- Practice rollbacks in drills; a rollback path that has never run is a theory.
- Measure rollback speed: time-to-rollback is a release SLO like any other.
- For the mykb bundle, rollback means restoring the previous bundle and index, rehearsed monthly.

Worked example — a wiki release breaks article rendering; the team flips the feature flag off in 30 seconds, then repairs the renderer on the stable version and re-releases.

## Related
- [[wiki/communities/revert-strategies|Revert Strategies]]
- [[wiki/devops-infra/automated-rollbacks|Automated Rollbacks]]
- [[wiki/dev-tools/continuous-deployment|Continuous Deployment]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/tooling/restore-drills|Restore Drills]]
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]]
