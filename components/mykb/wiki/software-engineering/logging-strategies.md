---
type: "concept"
title: "Logging Strategies"
description: "Deciding what to log, at what level, and where it goes"
tags: ["logging", "strategy", "observability", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Logging_(computing)", "https://opentelemetry.io/docs/concepts/observability-primer/"]
---

# Logging Strategies

## Summary
Logging strategies decide the content, structure, and destination of log events: what deserves a log line, at which level, with which fields, and where it ships. Structured, leveled, and correlation-tagged logs turn storage into a debuggable history.

## Details
- Log events, not strings: structured fields (timestamp, level, service, trace ID, event name) make logs queryable.
- Levels are a contract: debug for internals, info for lifecycle, warn for anomalies, error for failures.
- Log the decisions and their context — what was attempted, what was chosen, and why — not just that a function ran.
- Shipping, retention, and cost shape strategy: hot search, warm archive, cold compliance tiers.
- PII and secrets need redaction policies before logs leave the host.
- For the mykb bundle, logging strategy covers the acquisition pipeline: every article event structured and traceable.

Worked example — a failed wiki sync logs structured events: {event: sync_started, batch: 40}, {event: source_fetch_failed, url: ..., status: 503, trace_id: ...}. The aggregator groups by url and the alert fires on repeated 503s.

## Related
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/software-engineering/observability-practice|Observability Practice]]
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
- [[wiki/dev-tools/log-retention|Log Retention]]
- [[wiki/devops-infra/log-aggregation|Log Aggregation]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
