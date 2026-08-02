---
type: "concept"
title: "Crash Reports"
description: "Telemetry that captures what a client or service was doing when it crashed"
tags: ["crashes", "reporting", "telemetry", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Crash Reports

## Summary
Crash reporting collects stack traces, device or runtime context, and recent events from crashes so teams can triage and fix without a reproducer. Sentry, Crashlytics, and Windows Error Reporting are the archetypes.

## Details
- Group crashes by stack signature so the top crash becomes a queue, not a flood of tickets.
- Include breadcrumbs (recent user actions) — the best signal for what led to the crash.
- Rate-limit and sample uploads to protect user bandwidth and privacy.
- mykb relevance: crash reports from the agent loop would catch malformed tool results before they repeat.

## Related
- [[wiki/dev-tools/error-tracking-tools|Error Tracking Tools]]
- [[wiki/dev-tools/core-dumps|Core Dumps]]
- [[wiki/dev-tools/symbolication|Symbolication]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/incident-response|Incident Response]]
