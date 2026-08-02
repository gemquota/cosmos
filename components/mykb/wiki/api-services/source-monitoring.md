---
type: "concept"
title: "Source Monitoring"
description: "Continuous checks that cited sources remain live and accurate"
tags: ["sources", "monitoring", "maintenance", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Source Monitoring

## Summary
Source monitoring runs scheduled checks over every reference URL: HTTP status, redirect targets, content fingerprints, and title changes.

## Details
- A change in response code or content signals either link rot or a rewrite, and each needs a different curation response.
- Monitoring output feeds link-rot reports and source-review schedules, converting static citations into a living dataset.
- For mykb, source monitoring is the automated half of content-freshness-review.

## Related
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/api-services/source-review-schedules|Source Review Schedules]]
- [[wiki/api-services/dead-link-detection|Dead Link Detection]]
- [[wiki/api-protocols/http-status-checks|HTTP Status Checks]]
- [[wiki/api-services/source-lifetimes|Source Lifetimes]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
