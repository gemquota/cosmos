---
type: "concept"
title: "Log Aggregators"
description: "Systems that collect, index, and search logs from many services in one place"
tags: ["logging", "aggregation", "tooling", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Log Aggregators

## Summary
Log aggregators (ELK, Loki, Graylog, ClickHouse-based pipelines) pull logs from every host into a central store with search and alerting. Centralization turns per-host grep into one query box.

## Details
- Agents ship logs with structured metadata (service, level, trace_id) so queries can filter reliably.
- Storage tiering keeps hot search fast while cold logs archive cheaply; retention is a cost decision.
- Searchable logs without trace correlation solve only half the debugging story — pair with tracing.
- RSIS3 relevance: agent session logs routed through an aggregator make audit trails searchable.

## Related
- [[wiki/devops-infra/log-aggregation|Log Aggregation]]
- [[wiki/devops-infra/log-aggregation-pipelines|Log Aggregation Pipelines]]
- [[wiki/dev-tools/centralized-logging|Centralized Logging]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/devops-infra/clickhouse|ClickHouse]]
