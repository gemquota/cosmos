---
type: "concept"
title: "Local Dev Logs"
description: "Logging practices for development machines before anything reaches central storage"
tags: ["logging", "development", "local", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Local Dev Logs

## Summary
Local dev logs are the fast, noisy, human-oriented output on a developer machine — colored console lines, file tails, and REPL prints. They trade structure for immediacy and should not be treated like production telemetry.

## Details
- Pretty-print locally (colors, spacing) while emitting the same events structured for central ingestion.
- Dev-only verbosity (debug level, request dumps) must not leak secrets or PII into committed examples.
- Keep dev configs separate so a local misconfig never ships logs to production sinks.
- mykb relevance: local wiki-build logging helps contributors see link and frontmatter issues instantly.

## Related
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/dev-tools/debug-logging|Debug Logging]]
- [[wiki/dev-tools/verbose-flag|Verbose Flag]]
- [[wiki/dev-tools/centralized-logging|Centralized Logging]]
- [[wiki/software-engineering/developer-experience|Developer Experience]]
