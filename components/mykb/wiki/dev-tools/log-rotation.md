---
type: "concept"
title: "Log Rotation"
description: "Splitting and pruning log files so disk never fills from logging alone"
tags: ["logging", "rotation", "ops", "files"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Log Rotation

## Summary
Log rotation renames and compresses the current log file on a schedule or size threshold, keeping a bounded set of archives. It prevents a single noisy process from filling the disk and crashing the host — a mundane mechanism with a famous failure mode.

## Details
- Mechanism: the logger (logrotate, systemd journal, app-level handlers) renames the active file, starts a new one, compresses old archives, and prunes beyond the retention count; size-based rotation bounds disk usage, time-based rotation bounds age; handlers must reopen the log after rotation.
- Concrete example: logrotate rotates an app log daily, keeps 7 compressed archives, and signals the app with copytruncate or a reopen signal; a 10GB/day noisy process is bounded to a few hundred MB on disk; journald bounds its own store by size and age.
- Failure modes: the classic silent-loss bug — the app keeps writing to the deleted inode after rotation, so logs vanish with no error; rotation never triggered because the cron is disabled; compression failing mid-rotation leaving the log missing; retention too short for audit requirements; multiple processes writing the same file, corrupting rotation.
- Tradeoffs: local rotation keeps the host safe and cheap but loses the history when the host dies — centralized logging is the complement; the tradeoff is disk cost versus retention; the mature pattern is local rotation as a safety net plus shipping to an aggregator for search and long-term retention.
- Operational notes: verify reopen behavior after rotation, monitor rotation age and failures, and align retention with audit needs.
- RSIS3 relevance: rotate agent session logs with retention that matches audit requirements — the same bounded-storage discipline RSIS3 applies to its own run artifacts.

## Practice
- Add a canary check that the log file is actually growing and being rotated, so silent-loss bugs cannot hide.
## Related
- [[wiki/dev-tools/log-retention|Log Retention]]
- [[wiki/dev-tools/local-dev-logs|Local Dev Logs]]
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
- [[wiki/dev-tools/centralized-logging|Centralized Logging]]
- [[wiki/devops-infra/log-aggregation-pipelines|Log Aggregation Pipelines]]
