---
type: "concept"
title: "Four Golden Signals"
description: "Latency, traffic, errors, and saturation — the metrics that best describe user-facing health"
tags: ["monitoring", "golden-signals", "reliability", "metrics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Four Golden Signals

## Summary
The four golden signals from the Google SRE book are latency, traffic, errors, and saturation. Together they describe whether a system is fast, busy, correct, and near its limits — the small set of metrics that best describe user-facing health.

## Details
- Latency: how long requests take, including the error path — slow errors hurt users twice, so measure latency on failures as well as successes; percentiles (p50, p95, p99) matter more than averages.
- Traffic: demand in requests per second (or bytes, or users); errors: the rate of failed requests (as a ratio of traffic, not an absolute count); saturation: how close a critical resource — CPU, memory, connections, queue depth — sits to capacity, often the leading indicator of latency problems.
- Concrete example: a service dashboard showing request latency per endpoint, RPS, error ratio, and CPU/connection utilization; a saturation signal (connection pool at 90%) explains rising latency before errors appear; the four signals feed SLO burn-rate alerts.
- Failure modes: tracking only some signals — monitoring latency without saturation misses the cause; using averages, which hide tail problems; alerting on every counter instead of the few that describe health; saturation defined on the wrong resource, so the real bottleneck is invisible.
- Tradeoffs: the golden signals are a minimal, high-signal set that fits on one dashboard — richer systems add domain metrics, but the core four stay readable; the alternative, exhaustive metrics, is noise; the discipline is picking the top few per service and keeping them owned.
- Operational notes: define the four signals per service, put them on the top dashboard tier, and feed them into SLO alerts.
- RSIS3 relevance: the golden signals map to article latency, read traffic, curation errors, and storage saturation — the same four-question health view for the wiki.

## Related
- [[wiki/devops-infra/golden-signals|Golden Signals]]
- [[wiki/dev-tools/metric-backends|Metric Backends]]
- [[wiki/dev-tools/latency-percentiles|Latency Percentiles]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
