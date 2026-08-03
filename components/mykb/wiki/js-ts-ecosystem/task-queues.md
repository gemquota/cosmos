---
type: "concept"
title: "Task Queues"
description: "How the event loop prioritizes queued work"
tags: ["javascript", "event-loop", "queues", "async"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Task Queues

## Summary
Task queues describe how the event loop prioritizes queued work: tasks (macrotasks) run one at a time, the microtask queue drains between them, and rendering checkpoints interleave — the order and fairness of these queues decide whether a page stays responsive.

## Details
- Mechanism: the event loop selects the next task from the task queue, runs it to completion, drains the microtask queue, then performs rendering and repeats; timers, I/O, and events enqueue tasks; promise callbacks enqueue microtasks; task sources can have distinct queues with browser-defined prioritization.
- Concrete example: a click handler schedules a setTimeout and resolves a promise — the promise continuation runs first (microtask drain), then the timer task; heavy work in a task delays rendering until the task ends; scheduler.yield and setTimeout(0) re-queue work as tasks, giving rendering a chance.
- Failure modes: task starvation — a flood of high-priority tasks delaying timers and rendering; microtask floods delaying the next task; assuming strict FIFO ordering across sources (the spec allows prioritization); timer throttling in background tabs; long tasks blocking input.
- Tradeoffs: the task/microtask split gives the browser its responsiveness model — microtasks for prompt continuations, tasks for yielding; the alternative, a single queue, is simpler and blocks; the mature pattern is chunking work into tasks and keeping microtask drains short.
- Operational notes: measure long tasks, chunk heavy loops, and keep promise chains bounded.
- RSIS3 relevance: the dashboard's event-driven updates depend on queue fairness — knowing the order explains jank and delayed renders.
- Scheduling hierarchy: requestAnimationFrame callbacks run in their own phase before paint, and idle callbacks run only when the queue is empty; the ordering of tasks from different sources is implementation-defined, so design around phases (task, microtask, render) rather than cross-source FIFO assumptions. For layout-affecting work, rAF is the reliable place to make changes; for deferred non-urgent work, idle callbacks fit.

## Related
- [[wiki/web-platforms/javascript-event-loop|JavaScript Event Loop]]
- [[wiki/js-ts-ecosystem/microtasks|Microtasks]]
- [[wiki/js-ts-ecosystem/macrotasks|Macrotasks]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/web-components|Web Components]]
