---
type: "concept"
title: "Source Lifetimes"
description: "How long a source URL is expected to remain live and relevant"
tags: ["sources", "lifetimes", "maintenance", "references"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Source Lifetimes

## Summary
Source lifetimes estimate how long a URL will stay live and how long its content stays relevant — both decay, at different rates.

## Details
- Official docs pages have long lifetimes but change; blog posts die fast; spec documents live long and change slowly.
- Lifetime estimates drive review scheduling: short-lived sources get frequent checks, long-lived ones get sparse checks.
- For mykb, source lifetimes are the input to source-review-schedules and link-rot risk scoring.

## Related
- [[wiki/api-services/source-review-schedules|Source Review Schedules]]
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/api-protocols/source-dates|Source Dates]]
- [[wiki/concepts/dated-sources|Dated Sources]]
- [[wiki/api-services/source-lifetimes|Source Lifetimes]]
- [[wiki/concepts/stale-articles|Stale Articles]]
