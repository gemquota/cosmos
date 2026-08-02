---
type: "concept"
title: "Error Tracking Tools"
description: "Services that aggregate exceptions and errors with context across releases"
tags: ["error-tracking", "exceptions", "monitoring", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Error Tracking Tools

## Summary
Error tracking tools (Sentry, Bugsnag, Rollbar) aggregate exceptions from many instances into grouped issues with stack traces, breadcrumbs, and release attribution. They turn scattered errors into a prioritized backlog.

## Details
- Deduplicate by stack trace and version so the same bug is one issue, not ten thousand events.
- Tie errors to releases to see regressions the moment a deploy lands.
- Include user and request context, but redact PII before it reaches the store.
- mykb relevance: wiki pipeline errors aggregated by stage reveal which acquisition step fails most.

## Related
- [[wiki/dev-tools/crash-reports|Crash Reports]]
- [[wiki/dev-tools/apm-tools|APM Tools]]
- [[wiki/dev-tools/exception-handling-practice|Exception Handling Practice]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
