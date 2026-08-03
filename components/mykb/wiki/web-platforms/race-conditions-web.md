---
type: "concept"
title: "Race Conditions on the Web"
description: "Concurrent requests and clients producing inconsistent state"
tags: ["concurrency", "security", "web", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Race Conditions on the Web

## Summary

Race conditions in web apps arise when async operations interleave: out-of-order responses, double submissions, stale reads after writes. They are the source of many subtle, intermittent bugs that pass testing and fail production.

## Details
- Mechanism: two async flows touch shared state without ordering guarantees — a slow earlier request resolves after a fast later one and overwrites newer data; a double-click fires two identical mutations; a timer and a fetch compete to update the same UI. The browser's single thread does not remove races; it only makes them deterministic in timing.
- Concrete example: a search box with debounce still shows results from query A after the user typed B when A's response arrives late; the fix is an incrementing request id (ignore stale responses) plus cancellation. A checkout button that enables on state change can double-submit unless the handler is idempotent and guarded.
- Failure modes: optimistic UI that is not reconciled with the server's actual result; autosave racing with manual save (older snapshot wins); storage events and tabs clobbering each other; and test flakiness — a race that never reproduces locally but hits 1% of users with slower networks.
- Operational tradeoffs: staleness guards, idempotency keys, and request sequencing add complexity but convert heisenbugs into predictable behavior; a version counter (or ETag) on mutable resources is the cheapest general guard.
- RSIS3/mykb relevance: the wiki sync daemon sequences writes with an epoch counter and fencing tokens so concurrent note edits cannot interleave; this node documents the pattern for loop tooling.
- Testing races: reproduce with controlled delays (paused fetches, injected latency) rather than hoping; a race that cannot be deterministically tested will resurface in production at the worst moment.
- State discipline: keep a single version counter per mutable resource and ignore stale updates at the UI boundary; the guard is three lines and eliminates the whole class of out-of-order overwrites.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/toctou|TOCTOU Vulnerabilities]]
- [[wiki/web-platforms/atomic-writes|Atomic Writes]]
- [[wiki/web-platforms/file-locks|File Locking]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/web-platforms/web-apis|Web APIs]]
