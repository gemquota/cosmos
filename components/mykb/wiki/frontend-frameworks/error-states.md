---
type: "concept"
title: "Error States"
description: "Handling failures in the UI: recovery paths, retries, and humane error messages"
tags: ["errors", "ux", "state", "reliability", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary", "https://www.nngroup.com/articles/error-message-guidelines/"]
---
# Error States

## Summary
Error states turn failures into recoverable moments: explain what failed, why it matters, and what the user can do. Good error design distinguishes transient failures (retry) from permanent ones (fix input, contact support). Error boundaries contain crashes so the rest of the app survives.

## Details
- **Content** — plain-language message, affected context, and one clear recovery action; avoid raw error codes without explanation.
- **Retry policy** — transient errors offer retry with backoff; permanent errors stop the loop and surface the next step.
- **Error boundaries** — framework-level boundaries isolate crashes; a failed region degrades without taking down the page.
- **Telemetry** — every surfaced error reports to monitoring with context.
- **Worked example** — the mykb sync panel shows "Sync failed — retrying in 30s" with a manual retry button and a link to the log.
- **Relevance** — RSIS3's agents must translate internal failures into the same humane error vocabulary.

## Related
- [[wiki/frontend-frameworks/async-state|Async State]] — adjacent concept in this wiki
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — adjacent concept in this wiki
- [[wiki/api-protocols/503-handling|Handling 503]] — adjacent concept in this wiki
- [[wiki/api-protocols/429-handling|Handling 429]] — adjacent concept in this wiki
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — existing coverage
