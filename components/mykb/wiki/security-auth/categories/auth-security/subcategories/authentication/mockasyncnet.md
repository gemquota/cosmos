---
type: "entity"
title: "MockAsyncNet"
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---
description: "Test doubles that replace asynchronous network I/O with deterministic, controllable behavior"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "testing", "async"]

# MockAsyncNet

## Summary
MockAsyncNet is the practice of replacing real asynchronous network I/O in tests with controllable doubles that return canned responses, delays, or errors. It matters because real sockets make tests slow, flaky, and environment-dependent. Deterministic async mocks let teams verify timeouts, retries, and error paths reliably in every run.

## Details
- **Definition** — an async network mock intercepts connection, request, and response flows at the client boundary, fulfilling awaitable contracts without touching the network.
- **Determinism** — canned responses and injected delays make timing-based behavior such as timeouts and retries reproducible in every run.
- **Error injection** — simulating connection resets, DNS failures, and malformed payloads exercises branches that rarely occur against real services.
- **Recording** — the mock records request bodies, headers, and ordering so tests can assert what the client actually sent.
- **Latency control** — configurable response delays test race conditions and backoff logic without waiting real seconds.
- **Boundary discipline** — mocking at the client boundary keeps the transport code itself covered by integration or contract tests elsewhere.
- **Ordering and concurrency** — mocks can script sequences of responses and resolve pending calls in a controlled order to exercise concurrent client behavior.
- **Common failure modes** — mocks that return data shaped differently from the real API, and async fixtures that forget to await, producing silent false passes.
- **Worked example** — a retry test configures the mock to fail twice then succeed; the client's backoff and eventual success are asserted in milliseconds.
- **Practical relevance** — deterministic async network mocks make network-dependent code testable in CI without external services.

## Related
- [[wiki/testing/mocking|Mocking]] — the general technique
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — tool support
- [[wiki/testing/integration-testing|Integration Testing]] — where real I/O belongs
- [[wiki/api-protocols/timeouts|Timeouts]] — the behavior being tested
- [[wiki/api-protocols/websockets|WebSockets]] — a common async surface
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — injecting network faults
