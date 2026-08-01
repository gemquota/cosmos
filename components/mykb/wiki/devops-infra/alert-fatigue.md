---
type: "concept"
title: "Alert Fatigue"
description: "Desensitization to alerts when too many are noisy, leading to missed real incidents"
tags: ["alerting", "fatigue", "monitoring", "sre"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Alert Fatigue

## Summary
Alert fatigue sets in when most pages are false alarms or non-urgent, training responders to ignore or dismiss them.

## Details
- Causes: alerting on every metric, static thresholds, and no alert ownership.
- Cures: alert on SLO burn and user impact, tune thresholds with data, and silence noise.
- Every page should require an action; informational items belong in dashboards.
- Open question: how to measure and budget page volume like error budgets.

## Related
- [[wiki/devops-infra/golden-signals|Golden Signals]] — high-signal alerts reduce noise
- [[wiki/devops-infra/severity-levels|Severity Levels]] — routing urgency correctly
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — absorbing the informational load
- [[wiki/devops-infra/observability|Observability]] — better data, fewer alarms
