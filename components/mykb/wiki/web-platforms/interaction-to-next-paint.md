---
type: "concept"
title: "Interaction to Next Paint"
description: "INP: the Core Web Vitals metric for input responsiveness"
tags: ["performance", "metrics", "core-web-vitals", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Interaction to Next Paint

## Summary

Interaction to Next Paint (INP) measures the latency of every significant interaction, reporting the worst (p75) as a Core Web Vital. It replaced FID because responsiveness is about the full response, not just first input.

## Details
- Mechanism: for each qualifying interaction (click, tap, key), INP measures input delay + event handler time + presentation delay up to the next paint; the metric is the p75 of the longest interactions, which excludes single outliers while catching systemic slowness. Chrome exposes it via the PerformanceObserver long-animation-frame and event timing APIs.
- Concrete example: a filter dropdown whose onChange triggers a 200ms synchronous re-render pushes INP far past the 200ms good threshold; deferring the render to a rAF or worker and updating only the changed subtree brings it under 100ms. A tap target that appears to respond instantly but commits layout 300ms later is equally penalized.
- Failure modes: optimizing only clicks while keyboard and touch interactions lag; heavy main-thread work from third-party scripts inflating every interaction; event handlers that return quickly but schedule long microtask/rAF chains; and measuring INP in the lab without real-user interaction patterns.
- Operational tradeoffs: hitting good INP (<200ms) means keeping the main thread free: chunk work, virtualize lists, and move parsing/encryption/formatting off-thread. It is the most actionable Core Web Vital because it targets code you control rather than assets.
- RSIS3/mykb relevance: the dashboard streams INP from real sessions into rack telemetry, and slow handlers trigger a loop pass with the offending interaction trace attached.
- Interaction tracing: capture the longest interactions with their attribution trees; a p75 INP regression without attribution is unfixable guesswork.
- Budget gate: block releases that regress p75 INP beyond target, and attach the slowest interaction trace to the ticket.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/largest-contentful-paint|Largest Contentful Paint]]
- [[wiki/web-platforms/cumulative-layout-shift|Cumulative Layout Shift]]
- [[wiki/web-platforms/cls-avoidance|CLS Avoidance]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
