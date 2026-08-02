---
type: "concept"
title: "Log Levels"
description: "The debug/info/warn/error taxonomy that grades log importance"
tags: ["logging", "levels", "standards", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Log Levels

## Summary
Log levels (trace, debug, info, warn, error, fatal) grade each event's importance so operators can filter noise and escalation can react to errors. Consistent use makes the levels meaningful.

## Details
- info is for normal lifecycle events, warn for recoverable anomalies, error for failures needing attention.
- Levels should be per-event, not per-module: the same component logs info sometimes and error other times.
- Dynamic level switching (raising verbosity at runtime) is the escape hatch for production debugging.
- mykb relevance: define levels for curation events so a broken link logs at warn and a failed sync at error.

## Related
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/debug-logging|Debug Logging]]
- [[wiki/dev-tools/verbose-flag|Verbose Flag]]
- [[wiki/dev-tools/local-dev-logs|Local Dev Logs]]
- [[wiki/devops-infra/log-aggregation|Log Aggregation]]
