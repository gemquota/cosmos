---
type: "concept"
title: "Async/Await Patterns"
description: "Writing asynchronous code that reads like synchronous code"
tags: ["async", "await", "concurrency", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Async/Await Patterns

## Summary
Async/await lets developers write non-blocking code with familiar sequential syntax: await suspends the function, the runtime resumes it when the promise resolves. It tames callback nesting at the cost of subtle suspension semantics.

## Details
- Await inside loops serializes; Promise.all / asyncio.gather parallelizes — choose deliberately.
- Error handling differs: try/catch works on await, but unhandled rejections still slip through.
- Beware holding locks or resources across await points — suspension is a scheduling point.
- mykb relevance: the acquisition pipeline uses async/await so fetching many sources runs concurrently.

## Related
- [[wiki/software-engineering/promises-vs-callbacks|Promises vs Callbacks]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/software-engineering/asynchronous-patterns|Asynchronous Patterns]]
- [[wiki/dev-tools/cancellation-tokens|Cancellation Tokens]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
