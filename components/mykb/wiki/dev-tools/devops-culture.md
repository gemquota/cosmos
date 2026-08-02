---
type: "concept"
title: "DevOps Culture"
description: "The culture of shared ownership across development and operations"
tags: ["devops", "culture", "collaboration", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/DevOps", "https://dora.dev/"]
---

# DevOps Culture

## Summary
DevOps is a cultural and technical movement that breaks the wall between developers and operators: one team owns a service from code to production, with automation, observability, and shared metrics. DORA research connects its practices — small batches, CI/CD, trunk-based development, blameless culture — to delivery performance.

## Details
- Shared ownership: developers handle deployment and on-call for what they build, closing the feedback loop.
- Automation is the enabler: CI/CD pipelines, infrastructure as code, and monitoring make fast, safe changes possible.
- The DORA four keys — deployment frequency, lead time, change failure rate, time to restore — measure the culture's results.
- Blameless postmortems and psychological safety turn incidents into learning instead of punishment.
- DevOps is not a team or a title: it is an operating model; platform teams serve it by providing golden paths.
- Anti-patterns: dev throwing builds over a wall, ops owning production invisibly, and tooling without cultural change.
- For the mykb bundle, devops culture means the wiki pipeline is owned end to end, with metrics for curation lag and link health.

Comparison — traditional ops: developers write code, hand it over, and ops deploys nervously. DevOps: the same small team ships daily via pipeline, watches dashboards, and runs game days to practice failure.

## Related
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/trunk-based-development|Trunk-Based Development]]
- [[wiki/communities/blameless-postmortems|Blameless Postmortems]]
- [[wiki/tooling/platform-engineering|Platform Engineering]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/dev-tools/runbook-automation|Runbook Automation]]
- [[wiki/dev-tools/status-pages|Status Pages]]
- [[wiki/devops-infra/on-call-practices|On-Call Practices]]
- [[wiki/devops-infra/ci-cd-best-practices|CI/CD Best Practices]]
