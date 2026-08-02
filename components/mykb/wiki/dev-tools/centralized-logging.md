---
type: "concept"
title: "Centralized Logging"
description: "Shipping logs from many hosts to one searchable store"
tags: ["logging", "aggregation", "observability", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Centralized Logging

## Summary
Centralized logging collects stdout, files, and structured events from every service into one system where they can be searched, correlated, and alerted on. It is the difference between ssh-and-grep and a single query box.

## Details
- Shipping agents (Fluent Bit, Vector, Promtail) parse, tag, and batch logs before forwarding.
- Centralization enables cross-service correlation by trace ID and near-real-time alerting on log patterns.
- Lossy shipping under backpressure is normal: design alerts around metrics, not around log completeness.
- mykb relevance: centralize agent logs to make the whole acquisition pipeline searchable from one place.

## Related
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
- [[wiki/devops-infra/log-aggregation|Log Aggregation]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/log-retention|Log Retention]]
- [[wiki/devops-infra/observability|Observability]]
