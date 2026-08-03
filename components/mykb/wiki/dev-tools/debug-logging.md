---
type: "concept"
title: "Debug Logging"
description: "High-detail logging written to explain internals during troubleshooting"
tags: ["logging", "debugging", "verbosity", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Debug Logging

## Summary
Debug logging emits the fine-grained detail — decisions, intermediate values, request payloads — that only matters while chasing a bug. Kept behind a level or flag, it turns an opaque system into a story you can read, without paying the cost in normal operation.

## Details
- Mechanism: debug lines are written with intent — what was decided and why, not just that a function ran; they sit behind a log level (DEBUG) or a runtime flag; expensive debug work (serialization, formatting, full payloads) is guarded so it costs nothing when disabled; in production, debug output is sampled and redacted because it captures the most sensitive data.
- Concrete example: an ingestion pipeline logs at debug the article ID, the stage decision (accepted or rejected and why), and the intermediate parse result; troubleshooting a failed run sets the level to debug for that request ID only; the replay reads as a step-by-step story ending in the failure.
- Failure modes: debug logs that are actually noise — every function entry logged, drowning the signal; sensitive data (tokens, PII, full payloads) written at debug and accidentally enabled in production; expensive formatting executed even when the level is off (guard the call, not just the level); debug logs that describe what happened but not why a decision was made.
- Tradeoffs: debug logging gives replayable detail on demand at the cost of code noise and privacy risk; the alternative — no debug output — makes production bugs unfindable without redeploys; the mature pattern is intent-bearing debug lines, guarded evaluation, and redaction policies.
- Operational notes: keep debug output behind levels, sample it in production, and make the toggle per-request.
- RSIS3 relevance: debug-log the agent decision trace so a failed article can be replayed step by step — the story format RSIS3 needs for loop debugging.

## Related
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/dev-tools/verbose-flag|Verbose Flag]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/printf-debugging|Printf Debugging]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
