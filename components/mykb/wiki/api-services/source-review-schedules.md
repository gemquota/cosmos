---
type: "concept"
title: "Source Review Schedules"
description: "The cadence at which sources are re-verified and re-read"
tags: ["sources", "schedules", "maintenance", "process"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Source Review Schedules

## Summary
Source review schedules assign each source a review interval based on its lifetime class: official docs reviewed quarterly, fast-moving pages monthly, stable specs yearly.

## Details
- A schedule turns link-rot monitoring into a workflow: each review re-checks the URL and re-reads whether the cited claim still holds.
- Schedules are recorded per source so a missed review is visible instead of implicit.
- For mykb, source review schedules are the bridge between automated checks and human freshness review.

## Related
- [[wiki/api-services/source-lifetimes|Source Lifetimes]]
- [[wiki/api-services/source-monitoring|Source Monitoring]]
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
- [[wiki/api-protocols/source-dates|Source Dates]]
- [[wiki/api-protocols/access-dates|Access Dates]]
