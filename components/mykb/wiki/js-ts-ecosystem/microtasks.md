---
type: "concept"
title: "Microtasks"
description: "Queue drained after each task, before rendering"
tags: ["javascript", "microtasks", "event-loop", "async"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Microtasks

## Summary
Microtasks are the queue drained after each task, before rendering: promise resolutions and queueMicrotask callbacks run here. They give async continuations a guaranteed, prompt turn — at the cost of delaying paint if the queue never empties.

## Details
- Mechanism: after a macrotask completes, the engine drains the microtask queue to exhaustion before rendering or the next task; promise then/catch/finally callbacks and queueMicrotask schedule microtasks; await continuations run as microtasks; a microtask scheduled by a microtask runs in the same drain.
- Concrete example: a promise chain of .then calls runs entirely in one microtask drain, before the browser paints; awaiting a resolved value continues as a microtask; a mutation observer callback fires in the microtask phase; a microtask storm (a loop of promises that keeps scheduling) delays rendering indefinitely — the page freezes without a long task appearing.
- Failure modes: unbounded microtask chains delaying paint; awaiting in tight loops scheduling microtasks instead of yielding to tasks; assuming microtasks run before DOM updates paint; queueMicrotask used for heavy work, blocking the drain; interop surprises where promise implementations differ across runtimes.
- Tradeoffs: microtasks give fast, ordered async continuations at the cost of starving rendering when overused; macrotasks (setTimeout, scheduler) yield to the browser; the mature pattern is microtasks for coordination and macrotasks for yielding heavy work.
- Operational notes: watch for frozen paint with promise-heavy code, and use task scheduling APIs to yield.
- RSIS3 relevance: the dashboard's reactive updates should avoid microtask storms so telemetry refreshes never delay paint.
- Debouncing anti-pattern: using promise chains or queueMicrotask as a throttle still starves rendering because the drain never yields between scheduled items; a microtask-based debounce can postpone paint for an entire burst. Throttle with setTimeout, rAF, or scheduler.yield so the browser gets a rendering checkpoint, and keep promise chains in production code bounded in length.

## Related
- [[wiki/web-platforms/javascript-event-loop|JavaScript Event Loop]]
- [[wiki/js-ts-ecosystem/macrotasks|Macrotasks]]
- [[wiki/js-ts-ecosystem/task-queues|Task Queues]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/web-components|Web Components]]
