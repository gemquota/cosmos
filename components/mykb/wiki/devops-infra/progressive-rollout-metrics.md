---
type: "concept"
title: "Progressive Rollout Metrics"
description: "Tracking error rate and latency while shifting traffic"
tags: ["rollout", "metrics", "canary", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Progressive Rollout Metrics

## Summary
Progressive rollout metrics are the health signals that gate each step of a gradual release — error rate, latency, saturation, business outcomes. The rollout proceeds only while the metrics stay within tolerance; the metrics, not the calendar, decide when the new version is safe to trust.

## Details
- Mechanism: during each rollout step, the controller compares the new version's metrics against the baseline (previous version or a control group) over a window; checks are defined with thresholds and consecutive-failure counts; failures pause, abort, or roll back; metric sources include logs, traces, service meshes, and business analytics.
- Concrete example: a canary analysis queries Prometheus for the 5xx ratio and p99 latency; the new version must stay under 1% errors and within 10% of baseline latency for five consecutive minutes; a business metric (checkout completion rate) is compared between canary and control cohorts.
- Failure modes: metric blindness — checking errors but not latency or business outcomes, so a slow or revenue-harming release passes; insufficient sample size in the canary, so thresholds never trip; baseline noise — a canary compared to a degraded baseline looks fine; metric sources that lag, delaying detection; thresholds tuned to normal variance, causing false aborts that block legitimate releases.
- Tradeoffs: rich rollout metrics buy the confidence to automate promotion but cost instrumentation, alert design, and tuning time; the alternative — time-based or manual promotion — is simpler and blind; the mature pattern is a small set of high-signal checks (error rate, latency, one business metric) that are tuned on real incident data.
- Operational notes: log every promotion decision with the metric evidence, tune thresholds after each rollout, and test the abort path.
- RSIS3 relevance: RSIS3's pulse telemetry is exactly this concept — the metrics that gate whether a new loop strategy is promoted, held, or reverted.

## Related
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs & Traces]]
- [[wiki/devops-infra/prometheus-and-metrics|Prometheus & Metrics]]
- [[wiki/devops-infra/progressive-delivery-models|Progressive Delivery Models]]
- [[wiki/devops-infra/progressive-sync-strategies|Progressive Sync Strategies]]
