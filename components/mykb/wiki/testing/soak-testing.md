---
type: "concept"
title: "Soak Testing"
description: "Sustained long-running operation to expose leaks and drift"
tags: ["soak-testing", "testing", "stability", "leaks"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grafana.com/docs/k6/latest/testing-guides/soak-testing/", "https://www.ibm.com/topics/soak-testing"]
---

# Soak Testing

## Summary
Soak testing sustains realistic load over hours or days to expose leaks and drift: memory growth, connection exhaustion, disk filling, and gradual slowdown. Short tests miss these long-horizon defects entirely.

## Details
- Run at production-like or moderate load for eight hours to several days.
- Watch trends: memory, garbage collection, open connections, temp files, and queue depth.
- Classic findings: slow leaks, unbounded caches, index bloat, and clock or date drift.
- Pair with alerting: trend charts, not snapshots, reveal gradual degradation.
- Include cleanup paths: sessions, logs, and temporary artifacts must stay bounded.
- Run small-scale soak in CI and full-scale soaks before major releases.
- Automate soak results into dashboards for long-term comparison.

## Related
- [[wiki/testing/load-testing|Load Testing]] — the sustained-load baseline
- [[wiki/devops-infra/observability|Observability]] — trend metrics soak relies on
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — visualizing drift over time
- [[wiki/testing/performance-testing|Performance Testing]] — the family soak belongs to
- [[wiki/devops-infra/golden-signals|Golden Signals]] — the metrics soak watches
- [[wiki/testing/test-environments|Test Environments]] — dedicated infrastructure for long runs
