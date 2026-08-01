---
type: "concept"
title: "Scheduled Jobs"
description: "Running work on a schedule — cron, batch, and maintenance tasks — reliably and observably"
tags: ["scheduled-jobs", "cron", "batch", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Scheduled Jobs

## Summary
Scheduled jobs execute recurring work — reports, cleanups, syncs, batch processing — on a timetable. They look simple until one misses, overlaps, or fires during a deploy.

## Details
- Schedule semantics: cron expressions, timezone awareness, and daylight-saving pitfalls.
- Overlap control and idempotency prevent double-runs of state-changing work.
- Observability: every run needs logs, outcome, and an alert when it silently fails.
- Open question: when scheduled jobs should be event-driven instead.

## Related
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — cron as a serverless trigger
- [[wiki/devops-infra/worker-pools|Worker Pools]] — executing the scheduled work
- [[wiki/devops-infra/github-actions|GitHub Actions]] — scheduled CI workflows
- [[wiki/api-protocols/webhooks|Webhooks]] — event-driven alternative
