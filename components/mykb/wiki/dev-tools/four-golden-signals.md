---
type: "concept"
title: "Four Golden Signals"
description: "Latency, traffic, errors, and saturation — the metrics that best describe user-facing health"
tags: ["monitoring", "golden-signals", "reliability", "metrics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Four Golden Signals

## Summary
The four golden signals from the Google SRE book are latency, traffic, errors, and saturation. Together they describe whether a system is fast, busy, correct, and near its limits.

## Details
- Latency measures how long requests take, including the error path — slow errors hurt users twice.
- Traffic is demand (requests per second); errors are failed requests; saturation is how close to capacity the resource sits.
- Pick the top few per service: most systems only need a handful of saturation metrics, not every counter.
- mykb relevance: the golden signals map to article latency, read traffic, curation errors, and storage saturation.

## Related
- [[wiki/devops-infra/golden-signals|Golden Signals]]
- [[wiki/dev-tools/metric-backends|Metric Backends]]
- [[wiki/dev-tools/latency-percentiles|Latency Percentiles]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
