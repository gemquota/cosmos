---
type: "concept"
title: "Link-Rot Monitoring"
description: "Watching for external URLs that go dead over time"
tags: ["link-rot", "monitoring", "maintenance", "references"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Link-Rot Monitoring

## Summary
Link-rot monitoring periodically re-checks every external URL in the wiki and flags those that no longer resolve to the expected content.

## Details
- Rot has two flavors: hard 404s and silent rewrites, and both need different handling — archive recovery versus content review.
- Monitoring cadence is set by source-lifetimes: short-lived URLs are checked more often.
- For mykb, link-rot monitoring is the main consumer of http-status-checks and the main producer of archive-url remediation.

## Related
- [[wiki/api-services/dead-link-detection|Dead Link Detection]]
- [[wiki/api-services/source-monitoring|Source Monitoring]]
- [[wiki/api-protocols/http-status-checks|HTTP Status Checks]]
- [[wiki/api-protocols/archive-urls|Archive URLs]]
- [[wiki/api-services/source-lifetimes|Source Lifetimes]]
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
