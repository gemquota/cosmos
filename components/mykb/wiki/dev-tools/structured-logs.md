---
type: "concept"
title: "Structured Logs"
description: "Log entries emitted as structured data (JSON) instead of free-form strings"
tags: ["logging", "structured", "json", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Structured Logs

## Summary
Structured logs emit each event as machine-readable key-value data — usually JSON — so aggregators can filter, group, and alert on fields instead of grepping text. They are the baseline for modern observability.

## Details
- Include timestamp, level, service, trace/correlation ID, and event name as first-class fields.
- Keep the message field human-readable but put the queryable facts in fields, not the message.
- Multiline stack traces and binary payloads need careful encoding; consider one event per line.
- mykb relevance: agent logs as structured events make audits and replays machine-queryable.

## Related
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
- [[wiki/dev-tools/centralized-logging|Centralized Logging]]
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs, Traces]]
