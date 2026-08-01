---
type: "concept"
title: "Golden Signals"
description: "The four metrics — latency, traffic, errors, saturation — that best characterize service health"
tags: ["monitoring", "sre", "metrics", "latency", "alerting"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://sre.google/sre-book/monitoring-distributed-systems/"]
---

# Golden Signals

## Summary
The golden signals are the four metrics that most reliably indicate whether a user-facing service is healthy: latency, traffic, errors, and saturation. They come from Google's SRE book and give operators a small, high-signal set to monitor instead of an unreadable wall of dashboards. Alerts and SLOs are typically built on top of them.

## Details
- Latency: the time to serve a request — measured in distributions (p50, p95, p99), not averages, because tails drive user experience.
- Traffic: demand on the service — requests per second, bandwidth, or sessions; trends here explain scaling and capacity needs.
- Errors: the rate of failed requests, distinguishing HTTP 5xx from application-level failures (a 200 that returns wrong data still fails the user).
- Saturation: how full the service is — utilization of the bottleneck resource (CPU, queue depth, connection pool, disk); saturation predicts latency growth before it happens.
- RED and USE methods complement them: RED (rate, errors, duration) for request-driven services; USE (utilization, saturation, errors) for resources.
- Alerting: SLO burn-rate alerts on golden signals beat alerting on every metric — few, meaningful pages instead of alert fatigue.
- Worked example: a mykb API dashboard shows p95 latency, RPS, 5xx rate, and DB queue depth; the pager fires only when error budget burns too fast.

## Related
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — where the signals get visualized
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]] — what disciplined signal selection prevents
- [[wiki/devops-infra/error-budgets|Error Budgets]] — signals feed the SLO budget
- [[wiki/devops-infra/observability|Observability]] — the broader practice these metrics belong to
- [[wiki/api-protocols/health-checks|Health Checks]] — binary health alongside the signals
- [[wiki/api-protocols/timeouts|Timeouts]] — bounding latency tails
