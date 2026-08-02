---
type: "concept"
title: "Error Monitoring for the Web"
description: "Capturing, aggregating, and triaging client-side errors, crashes, and performance regressions"
tags: ["errors", "monitoring", "observability", "javascript", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event", "https://docs.sentry.io/platforms/javascript/"]
---
# Error Monitoring for the Web

## Summary
Client-side errors happen outside server logs: uncaught exceptions, rejected promises, failed resources, and slow interactions. Error monitoring captures them with context — stack, URL, user, and breadcrumbs — then aggregates them for triage. It closes the gap between deployed code and what users actually experience.

## Details
- **Capture hooks** — `window.onerror`, `unhandledrejection`, and error boundaries collect exceptions; performance entries feed vitals telemetry.
- **Context** — versions, user IDs, and breadcrumbs turn a stack into an investigation; grouping by fingerprint dedupes noise.
- **Release tracking** — source maps map minified stacks back to source; releases tie errors to deploys.
- **Alerting** — rate-based alerts (new issues, spikes) beat per-instance noise.
- **Worked example** — the mykb dashboard reports exceptions with release tags and visualizes INP/LCP regressions per release.
- **Relevance** — RSIS3's agents produce lots of output; the same discipline applies to capturing tool errors.

## Related
- [[wiki/web-platforms/repaint-vs-reflow|Repaint vs Reflow]] — adjacent concept in this wiki
- [[wiki/web-platforms/frame-budget|Frame Budget]] — adjacent concept in this wiki
- [[wiki/web-platforms/input-latency|Input Latency]] — adjacent concept in this wiki
- [[wiki/web-platforms/interaction-to-next-paint|Interaction to Next Paint]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
