---
type: "concept"
title: "Continuous Deployment"
description: "Shipping every passing change to production automatically"
tags: ["continuous-deployment", "automation", "delivery", "release"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Continuous_deployment", "https://en.wikipedia.org/wiki/Continuous_delivery"]
---

# Continuous Deployment

## Summary
Continuous deployment extends continuous delivery by automatically releasing every change that passes the pipeline — no human release decision. It removes the release bottleneck entirely and is how leading web companies ship hundreds of times a day.

## Details
- The difference from CD: CD keeps changes releasable; CDE actually releases them, automatically.
- Safety comes from small changes, automated verification, feature flags, canaries, and automatic rollback.
- It demands excellent monitoring: if production breaks, the pipeline must notice and respond faster than users do.
- Not every product fits — regulated environments and physical systems may require explicit release gates.
- Cultural fit matters: teams that fear releases should fix the fear (pipelines, rollbacks), not abandon automation.
- For the mykb bundle, continuous deployment would publish verified article batches the moment they pass curation checks.

Comparison — a team practicing CD runs the same pipeline but presses a button to promote. With CDE, the button disappears; the pipeline promotes, canaries, and rolls back by itself.

## Related
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/tooling/automated-canary|Automated Canary]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/tooling/smoke-tests|Smoke Tests]]
- [[wiki/devops-infra/automated-rollbacks|Automated Rollbacks]]
- [[wiki/devops-infra/deploy-safety-checks|Deploy Safety Checks]]
