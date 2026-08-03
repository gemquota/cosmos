---
type: "concept"
title: "Log Levels"
description: "The debug/info/warn/error taxonomy that grades log importance"
tags: ["logging", "levels", "standards", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Log Levels

## Summary
Log levels (trace, debug, info, warn, error, fatal) grade each event's importance so operators can filter noise and escalation can react to errors. Consistent use makes the levels meaningful — the taxonomy is only as good as the discipline behind it.

## Details
- Mechanism: trace is for fine-grained internals, debug for troubleshooting detail, info for normal lifecycle events, warn for recoverable anomalies, error for failures needing attention, fatal for unrecoverable states; levels are configured per deployment (production usually info+); dynamic level switching raises verbosity at runtime for debugging without redeploys.
- Concrete example: a curation pipeline logs info when an article is indexed, warn when a link is broken but recoverable, error when a sync fails, and debug on request for a failing article's full trace; alerts fire on error+ while dashboards count warns.
- Failure modes: level inflation — everything logged at error, so errors lose meaning; levels per module rather than per event, so a component logs all-or-nothing; sensitive data at debug level enabled in production; dynamic level switches that are not thread-safe or not reverted, leaving verbose logs on; levels defined differently across services, breaking aggregation.
- Tradeoffs: a consistent level taxonomy costs discipline but makes log filtering and alerting meaningful; the alternative — ungraded logging — makes every line equal and everything noise; the mature pattern is a documented level contract per event type, with runtime verbosity control.
- Operational notes: document the level contract, sample debug output in production, and audit level usage in reviews.
- RSIS3 relevance: define levels for curation events so a broken link logs at warn and a failed sync at error — the graded signal RSIS3 needs from its pipelines.

- Treat the level contract as part of the code review: wrong levels are caught in review, not in production.
## Related
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/debug-logging|Debug Logging]]
- [[wiki/dev-tools/verbose-flag|Verbose Flag]]
- [[wiki/dev-tools/local-dev-logs|Local Dev Logs]]
- [[wiki/devops-infra/log-aggregation|Log Aggregation]]
