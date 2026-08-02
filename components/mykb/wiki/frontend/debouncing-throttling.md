---
type: "concept"
title: "Debouncing and Throttling"
description: "Rate-limiting event handler execution"
tags: [javascript", "performance", "events", "debounce", "throttle"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener", "https://lodash.com/docs/4.17.15#debounce"]
---

# Debouncing and Throttling

## Summary
Debouncing and throttling limit how often a function runs in response to high-frequency events. Debouncing waits for a pause before executing — ideal for search-as-you-type — while throttling caps executions to a fixed interval, ideal for scroll and resize. Both protect the main thread from doing expensive work on every event.

## Details
- Debounce: resets a timer on each call; the function runs only after events stop for the delay, optionally with a leading call.
- Throttle: runs at most once per interval, dropping intermediate calls; leading, trailing, and maxWait control the cadence.
- Use cases: input autocomplete (debounce), scroll position updates (throttle), resize recalculation (throttle).
- rAF alternative: for rendering-driven work, requestAnimationFrame ties updates to paint instead of wall-clock intervals.
- Async pitfalls: stale closures and out-of-order responses need AbortController or request sequencing.
- Modern touches: passive event listeners reduce scroll jank; scheduler APIs offer prioritized alternatives.

## Related
- [[wiki/frontend/long-tasks|Long Tasks]] — what rate limiting prevents
- [[wiki/frontend/dom-api|DOM API]] — the events being rate-limited
- [[wiki/frontend/animation-performance|Animation Performance]] — frame-timed updates
- [[wiki/frontend/fetch-api|Fetch API]] — aborting stale async work
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — responsive handlers
- [[wiki/frontend/intersection-observer|Intersection Observer]] — replacing scroll handlers entirely
