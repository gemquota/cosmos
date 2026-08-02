---
type: "concept"
title: "Verbose Flag"
description: "A CLI or config switch that raises logging verbosity on demand"
tags: ["cli", "logging", "debugging", "verbosity"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Verbose Flag

## Summary
A verbose flag ( -v, --verbose, -vvv ) raises log verbosity at runtime so users can inspect internals without editing code. Repeated flags often map to escalating levels from info to trace.

## Details
- Repeatable flags (-v -v) are the common convention: one v for debug, two for trace-level detail.
- Verbose output belongs on stderr or a log file, not mixed into stdout that scripts parse.
- Pair with structured logging so verbose mode adds fields and events instead of wall-of-text lines.
- mykb relevance: the wiki CLI can expose a verbose flag to trace which articles and links it processes.

## Related
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/dev-tools/debug-logging|Debug Logging]]
- [[wiki/dev-tools/local-dev-logs|Local Dev Logs]]
- [[wiki/shell-environment/shell-scripting-robustness|Shell Scripting Robustness]]
- [[wiki/software-engineering/developer-experience|Developer Experience]]
