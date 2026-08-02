---
type: "concept"
title: "Promises vs Callbacks"
description: "Two APIs for composing asynchronous results and their tradeoffs"
tags: ["async", "promises", "callbacks", "composition"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Promises vs Callbacks

## Summary
Callbacks pass a function to run when async work completes; promises return an object with then/catch composition and a single settled state. Promises fix callback hell — nesting, error inversion, and hard composition — with a monadic chain.

## Details
- Promises settle once: then/catch run at most one branch, making state reasoning simple.
- Callback errors are easy to swallow; promises propagate rejection unless handled.
- Promise.all and async/await are the payoff — parallel fan-out and sequential reads in the same syntax.
- mykb relevance: the source-fetching layer should return promises so retries compose cleanly.

## Related
- [[wiki/software-engineering/async-await-patterns|Async/Await Patterns]]
- [[wiki/software-engineering/asynchronous-patterns|Asynchronous Patterns]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/software-engineering/concurrency-models|Promises]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
