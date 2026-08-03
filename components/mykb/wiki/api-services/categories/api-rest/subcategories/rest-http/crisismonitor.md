---
type: "entity"
title: "CrisisMonitor"
description: "A monitoring component that watches for anomalies and escalates critical events"
tags: ["entity", "monitoring", "alerting", "anomaly-detection", "operations"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# CrisisMonitor

## Summary

CrisisMonitor is a monitoring component that watches system signals for anomalies and escalates events that cross critical thresholds. It matters because the difference between an incident and a crisis is response time: early, accurate detection limits blast radius. A good crisis monitor combines signal collection, threshold logic, and reliable escalation paths.

## Details

- **Definition** — A crisis monitor continuously evaluates metrics, logs, and events against rules, emitting alerts when conditions indicate a developing failure.
- **Signal selection** — Meaningful signals include error rates, latency percentiles, queue depths, and resource utilization; each needs a baseline to be interpretable.
- **Thresholds** — Static thresholds are simple but brittle; dynamic baselines and anomaly detection adapt to seasonality and gradual drift.
- **Escalation** — Alerts route through tiers — dashboard, ticket, page — with ownership and acknowledgement so nothing falls through the cracks.
- **Worked example** — Error rate on an API crosses its threshold for five minutes; CrisisMonitor opens an incident, pages the on-call, and posts context to the channel.
- **Common failure modes** — Alert fatigue from noisy rules, thresholds tuned after the fact, and monitors that check only the endpoint instead of the dependencies.
- **Practical relevance** — Monitoring is what makes reliability promises operational; without it, regressions surface as user complaints instead of alerts.
- **Runbooks** — Each alert should point to a runbook that describes triage steps, reducing time-to-recovery during real crises.
- **Telemetry note** — Recorded in API, authentication, and backend sessions, consistent with a component guarding service health across those layers.
- **Data quality** — Monitor output is only as good as its inputs: missing metrics, clock skew, and silent gaps in collection create false calm.
- **Postmortems** — Every crisis should be reviewed against the monitor's log — whether detection preceded user impact, and which signals were missed.
- **Worked example** — Latency p95 climbs for three minutes while error rate stays flat; the monitor's anomaly rule flags the drift, and the team catches a scaling issue early.

## Related

- [[wiki/dev-tools/structured-logs|Structured Logs]] — the signals monitored
- [[wiki/cloud-infra/snapshot-strategies|Snapshot Strategies]] — capturing state at alert time
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — the observed errors
- [[wiki/testing/stress-testing|Stress Testing]] — exercising crisis paths
- [[wiki/os-shell/daemon-processes|Daemon Processes]] — the monitored services
- [[wiki/concepts/prediction-markets|Prediction Markets]] — aggregating risk signals
