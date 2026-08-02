---
type: "concept"
title: "Cancellation Tokens"
description: "Handles that propagate a cancel request through async work"
tags: ["cancellation", "async", "concurrency", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cancellation Tokens

## Summary
A cancellation token is a handle that signals long-running or async work to stop — cooperatively, at checkpoints. It lets a timeout or user action tear down a request cleanly instead of leaking work.

## Details
- Cancellation is cooperative: code checks the token at safe points and unwinds rather than killing threads.
- Tokens compose: a parent cancel cancels children; linked tokens merge timeouts with explicit cancels.
- Resources (sockets, locks, DB handles) must be released on cancel paths or leaks accumulate.
- mykb relevance: cancel a stalled agent run and its in-flight tool calls with one token.

## Related
- [[wiki/dev-tools/timeout-policy|Timeout Policy]]
- [[wiki/software-engineering/async-await-patterns|Async/Await Patterns]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/dev-tools/graceful-degradation|Graceful Degradation]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
