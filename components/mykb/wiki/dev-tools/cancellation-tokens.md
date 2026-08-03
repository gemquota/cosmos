---
type: "concept"
title: "Cancellation Tokens"
description: "Handles that propagate a cancel request through async work"
tags: ["cancellation", "async", "concurrency", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Cancellation Tokens

## Summary
A cancellation token is a handle that signals long-running or async work to stop — cooperatively, at checkpoints. It lets a timeout or a user action tear down a request cleanly, propagate cancellation through nested calls, and release resources, instead of leaking work or killing threads.

## Details
- Mechanism: a token is created by a CancellationTokenSource (or equivalent); work receives the token and checks it at safe points; when canceled, the token's state flips and registered callbacks run; the work unwinds — releasing sockets, locks, and DB handles — and throws or returns a cancellation result; tokens compose: a parent cancel cascades to children, and linked tokens merge a timeout with an explicit cancel.
- Concrete example: an HTTP request handler creates a token with a 5s timeout and passes it to a database call and a downstream API call; the user navigates away and the server cancels; both calls observe cancellation and release their connections; in-process work (a batch job, an agent run) cancels its in-flight tool calls with the same token.
- Failure modes: code that ignores the token, so cancellation never takes effect; cancellation checked only at function entry, so a long loop keeps running; resources not released on the cancel path, leaking handles; cancel being treated as an error, polluting logs and triggering wrong retry behavior; race conditions where work completes just as cancellation arrives.
- Tradeoffs: cooperative cancellation is safe and composable but requires every layer to participate — one non-cooperating call stalls the teardown; the alternative, killing threads or processes, is forceful and unsafe; the discipline is to thread tokens through every async boundary and treat cancellation as a normal, distinct outcome.
- Operational notes: log cancellation distinctly, add deadlines alongside tokens, and test the cancel path.
- RSIS3 relevance: cancel a stalled agent run and its in-flight tool calls with one token — the same cooperative teardown RSIS3 needs when a loop times out.

## Related
- [[wiki/dev-tools/timeout-policy|Timeout Policy]]
- [[wiki/software-engineering/async-await-patterns|Async/Await Patterns]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/dev-tools/graceful-degradation|Graceful Degradation]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
