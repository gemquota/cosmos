---
type: "concept"
title: "JavaScript Event Loop"
description: "How the runtime schedules tasks, microtasks, and rendering on the single main thread"
tags: ["javascript", "event-loop", "async", "concurrency", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop", "https://html.spec.whatwg.org/multipage/webappapis.html#event-loops"]
---
# JavaScript Event Loop

## Summary
JavaScript runs on one thread, and the event loop decides what runs when: a task queue of macrotasks, a microtask queue drained after each task, and a rendering step between tasks. Understanding this ordering explains promise timing, timer drift, and why long tasks freeze the page.

## Details
- **Task queue** — script blocks, timers, I/O callbacks, and events enqueue tasks; the loop runs one task then checks microtasks and rendering.
- **Microtasks** — promises and `queueMicrotask` run after the current task completes, before the next task and before rendering.
- **Rendering step** — browsers may render after tasks; long tasks postpone it, causing jank.
- **Ordering example** — `setTimeout(fn, 0)` runs after pending promise callbacks, not before; this surprises many developers.
- **Worked example** — the mykb UI defers non-urgent work with `requestIdleCallback` and splits heavy loops across tasks so input stays responsive.
- **Relevance** — RSIS3's agent loops must know whether their tool calls resolve in microtasks or tasks to schedule accurately.

## Related
- [[wiki/js-ts-ecosystem/microtasks|Microtasks]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/macrotasks|Macrotasks]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/task-queues|Task Queues]] — adjacent concept in this wiki
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — existing coverage
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
