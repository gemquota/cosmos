---
type: "concept"
title: "Log Rotation"
description: "Splitting and pruning log files so disk never fills from logging alone"
tags: ["logging", "rotation", "ops", "files"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Log Rotation

## Summary
Log rotation renames and compresses the current log file on a schedule or size threshold, keeping a bounded set of archives. It prevents a single noisy process from filling the disk and crashing the host.

## Details
- Size-based and time-based rotation trade predictability against disk usage; compress old archives to save space.
- Handlers must reopen the log after rotation or keep writing to a deleted inode — the classic silent-loss bug.
- Centralized logging makes local rotation less critical, but it still protects the host during shipping outages.
- mykb relevance: rotate agent session logs with retention that matches audit requirements.

## Related
- [[wiki/dev-tools/log-retention|Log Retention]]
- [[wiki/dev-tools/local-dev-logs|Local Dev Logs]]
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
- [[wiki/dev-tools/centralized-logging|Centralized Logging]]
- [[wiki/devops-infra/log-aggregation-pipelines|Log Aggregation Pipelines]]
