---
type: "concept"
title: "Debug Logging"
description: "High-detail logging written to explain internals during troubleshooting"
tags: ["logging", "debugging", "verbosity", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Debug Logging

## Summary
Debug logging emits the fine-grained detail — decisions, intermediate values, request payloads — that only matter while chasing a bug. Kept behind a level or flag, it turns an opaque system into a story you can read.

## Details
- Write debug lines with intent: what was decided and why, not just that a function ran.
- Guard expensive debug work (formatting, serialization) so it costs nothing when disabled.
- Debug logs in production need sampling and redaction — they capture the most sensitive data.
- mykb relevance: debug-log the agent decision trace so a failed article can be replayed step by step.

## Related
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/dev-tools/verbose-flag|Verbose Flag]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/printf-debugging|Printf Debugging]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
