---
type: "concept"
title: "Automated Canary"
description: "Canary rollouts that promote or roll back without human judgement calls"
tags: ["canary", "automation", "deployment", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Automated Canary

## Summary
Automated canary rollouts run the analysis loop themselves: deploy to a small slice, watch metrics, promote on health, roll back on regression — no human in the loop. Argo Rollouts, Flagger, and Spinnaker operationalize this.

## Details
- Automation needs trustworthy metrics and pre-agreed thresholds to be safe.
- Keep a human escape hatch: auto-rollback plus a pause-and-review mode.
- Automate the promotion path and the rollback path with equal care.
- mykb relevance: the wiki deploy auto-promotes a canary once link-health metrics pass.

## Related
- [[wiki/tooling/canary-analysis|Canary Analysis]]
- [[wiki/tooling/progressive-delivery|Progressive Delivery]]
- [[wiki/devops-infra/canary-and-blue-green-revisited|Canary and Blue-Green Revisited]]
- [[wiki/dev-tools/continuous-deployment|Continuous Deployment]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
