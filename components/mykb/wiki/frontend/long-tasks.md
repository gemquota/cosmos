---
type: "concept"
title: "Long Tasks"
description: "Main-thread task length and its effect on responsiveness"
tags: [performance", "main-thread", "long-tasks", "responsiveness", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/long-tasks-devtools", "https://developer.mozilla.org/en-US/docs/Web/API/PerformanceLongTaskTiming"]
---

# Long Tasks

## Summary
A long task is any main-thread task that runs longer than 50 milliseconds, blocking input, rendering, and painting for that whole window. They are the direct cause of sluggish interfaces and poor Interaction to Next Paint. The Long Tasks API exposes them, and DevTools shows them as red segments in the performance panel.

## Details
- Threshold: 50ms comes from human perception research — beyond it, users notice unresponsiveness and dropped frames.
- Sources: big component renders, synchronous parsing of large bundles, layout storms, and third-party scripts.
- INP link: a user interaction that lands inside a long task waits until the task finishes, inflating responsiveness scores.
- Splitting: break monolithic work into chunks with async yielding, requestIdleCallback, or scheduler.yield.
- Offloading: move CPU-heavy work to Web Workers; keep the main thread for DOM and interaction.
- Observability: PerformanceObserver with entryType longtask surfaces offenders; lab tools simulate slow devices to expose them.

## Related
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — INP is driven by task length
- [[wiki/frontend/web-workers|Web Workers]] — moving work off the main thread
- [[wiki/frontend/debouncing-throttling|Debouncing and Throttling]] — limiting task-triggering events
- [[wiki/frontend/reflow-repaint|Reflow and Repaint]] — layout storms inside long tasks
- [[wiki/web-platforms/browser-engines|Browser Engines]] — how the main thread is scheduled
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — the discipline
