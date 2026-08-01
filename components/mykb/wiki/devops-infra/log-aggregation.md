---
type: "concept"
title: "Log Aggregation"
description: "Centralized collection, storage, and search of logs from many services for debugging and analysis"
tags: ["logging", "observability", "elasticsearch", "loki", "opentelemetry"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://opentelemetry.io/docs/concepts/signals/logs/"]
---

# Log Aggregation

## Summary
Log aggregation collects log lines from every service into a central store where they can be searched, filtered, and correlated with traces and metrics. Without it, debugging a distributed system means SSHing into random hosts with grep. Modern pipelines treat logs as structured events with shared attributes, enabling fast, precise queries.

## Details
- Pipeline: agents on each host (Fluent Bit, OpenTelemetry Collector, vector) ship logs to a central backend (Loki, Elasticsearch, ClickHouse) for indexing and query.
- Structured logging: JSON logs with fields (level, service, trace_id, duration) make queries powerful; unstructured free-text logs degrade into regex archaeology.
- Correlation: attaching trace IDs and resource attributes lets operators jump from a trace span to the log lines of the same request.
- Retention and cost: hot storage for recent data, cheaper tiers for archives; retention policies are a cost decision, not just a storage one.
- Query patterns: error-rate searches, per-service log streams, and field-based filtering replace host-by-host debugging.
- Worked example: a mykb incident lookup starts with a trace ID from the dashboard, then pulls every log line tagged with that trace_id across daemon, hub, and gateway in one query.
- Alerting from logs is possible but should be secondary to metrics: metrics detect, logs explain.

## Related
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — log queries feed dashboard panels
- [[wiki/devops-infra/severity-levels|Severity Levels]] — log levels and incident severity align
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — trace IDs unify logs across services
- [[wiki/devops-infra/observability|Observability]] — logs as the third pillar
- [[wiki/devops-infra/clickhouse|ClickHouse]] — columnar backend for high-volume log storage
- [[wiki/devops-infra/incident-response|Incident Response]] — log search during investigations
