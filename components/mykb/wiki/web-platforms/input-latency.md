---
type: "concept"
title: "Input Latency"
description: "Delay from user input to visible response"
tags: ["performance", "interaction", "ux", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Input Latency

## Summary

Input latency is the delay between a user gesture and the visible response. It is determined by event handling, layout, and rendering on the main thread; long tasks and jank are the usual culprits, not network.

## Details
- Mechanism: a tap travels: hardware → browser → event listeners → style/layout/paint → compositor. Any main-thread work between the event and the paint adds latency; long tasks (>50ms) make the tap feel unresponsive. Interaction to Next Paint (INP) is the modern metric capturing this.
- Concrete example: a search box that filters 10,000 rows synchronously on each keystroke blocks input for hundreds of milliseconds; debouncing plus a worker or a virtualized list drops perceived latency to a frame or two. A button whose click handler triggers a layout-heavy re-render feels laggy even when the network is instant.
- Failure modes: measuring only page-load metrics while interaction suffers; event handlers doing heavy synchronous work (parsing, crypto, big DOM builds); layout thrash inside handlers; and third-party scripts inserting long tasks between gesture and response.
- Operational tradeoffs: reducing input latency means keeping handlers cheap, deferring work (rAF, workers, idle callbacks), and avoiding forced reflow; the cost is architectural complexity. Instrument with INP field data and long-task observers, and treat the 75th percentile as the operating target.
- RSIS3/mykb relevance: dashboard interactions (tab switches, chart filters) are measured for INP in rack telemetry, with slow handlers logged for the improvement loop.
- Instrumentation: measure INP with field data (CrUX or RUM) and correlate slow interactions with long-task attributions; a lab-only approach misses the third-party scripts and layout shifts that dominate real-user latency.
- Interaction budget: set an internal target (p75 INP under 200ms) and treat long-task attributions as bugs; without a target, latency regressions are only noticed as complaints.

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]]
- [[wiki/web-platforms/interaction-to-next-paint|Interaction to Next Paint]]
- [[wiki/web-platforms/largest-contentful-paint|Largest Contentful Paint]]
- [[wiki/web-platforms/cumulative-layout-shift|Cumulative Layout Shift]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
