---
type: "concept"
title: "Asynchronous Testing"
description: "Testing async code with waits, polling, and determinism controls"
tags: ["async-testing", "testing", "concurrency", "determinism"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://jestjs.io/docs/asynchronous", "https://github.com/pytest-dev/pytest-asyncio"]
---

# Asynchronous Testing

## Summary
Asynchronous testing verifies code that runs concurrently, promises, callbacks, threads, timers, and event loops, with waits, polling, and determinism controls. Flaky async tests almost always come from nondeterministic waits.

## Details
- JavaScript: async and await tests, fake timers, and promise resolution controls.
- Python: pytest-asyncio, anyio, and trio; awaitables need explicit event-loop handling.
- Patterns: explicit await or poll with timeout instead of arbitrary sleeps.
- Race detection: run many iterations and use tools like Go race and ThreadSanitizer.
- Mock the clock and scheduler to make timing deterministic.
- Assert on eventual state with bounded waits; avoid long blanket timeouts.
- Test cancellation, timeout, and error paths of async operations.

## Related
- [[wiki/testing/test-timeouts|Test Timeouts]] — bounding async waits
- [[wiki/testing/flaky-tests|Flaky Tests]] — nondeterministic waits cause flakes
- [[wiki/testing/test-parallelism|Test Parallelism]] — concurrency under parallel runs
- [[wiki/api-protocols/websockets|WebSockets]] — async protocols under test
- [[wiki/api-protocols/timeouts|Timeouts]] — deadlines in async contracts
- [[wiki/testing/test-frameworks|Test Frameworks]] — async support in runners
