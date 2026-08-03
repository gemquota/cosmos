---
type: "concept"
title: "Macrotasks"
description: "Task-queue units like timers and I/O callbacks"
tags: ["javascript", "macrotasks", "event-loop", "async"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Macrotasks

## Summary
Macrotasks are the task-queue units of the event loop — timers, I/O callbacks, and events. They run one at a time, after the microtask queue drains, and each task can render between executions, which is why long-running tasks block the page.

## Details
- Mechanism: the event loop picks a task from the task queue (timers, I/O, events, rendering as a distinct step), runs it to completion, then drains microtasks before the next task; tasks are scheduled by setTimeout/setInterval, fetch and I/O callbacks, and user events; each task is a unit of work with its own microtask phase.
- Concrete example: a setTimeout callback runs as a macrotask; a promise resolution inside it runs in the microtask phase before the next task; a click handler that does heavy work delays all subsequent tasks and rendering — the page janks; splitting work with setTimeout or scheduler.yield lets rendering happen between tasks.
- Failure modes: recursive setTimeout chains that starve other tasks; heavy work inside a single task blocking rendering and input; microtask floods (promise chains) that delay the next task; assuming task order across sources (event timing is not guaranteed); timer throttling in background tabs surprising background work.
- Tradeoffs: macrotasks let the browser interleave work and rendering — the yield point of the event loop; the alternative, doing everything synchronously, is simpler and blocks; the mature pattern is chunking heavy work into tasks and yielding to rendering.
- Operational notes: measure long tasks with performance APIs, chunk work, and keep timers independent of rendering assumptions.
- RSIS3 relevance: the dashboard's telemetry rendering should chunk work into tasks so a heavy update never blocks the UI loop.

## Related
- [[wiki/web-platforms/javascript-event-loop|JavaScript Event Loop]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/task-queues|Task Queues]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/microtasks|Microtasks]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/macrotasks|Macrotasks]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
- [[wiki/web-platforms/web-components|Web Components]] — related coverage in the same cluster
