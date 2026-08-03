---
type: "entity"
title: "MockWorker"
resource: ""
---
description: "Replacing Web Worker instances in tests with controllable doubles"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "testing", "web-workers"]
timestamp: "2026-07-19T22:41:42Z"

# MockWorker

## Summary
A MockWorker replaces a real Web Worker in tests with a double that captures posted messages and responds with scripted results. It matters because real workers introduce threads, timing, and environment quirks that make tests slow and flaky. Mocking the worker isolates the main-thread logic that the tests actually target, keeping them fast and deterministic.

## Details
- **Definition** — a mock worker implements the Worker interface: postMessage and a message event channel, without spawning a real background thread.
- **Message capture** — the mock records payloads sent by the main thread so tests can assert what was posted and in what order.
- **Scripted replies** — tests configure responses, delays, or error events, simulating the worker's output for each scenario.
- **Error simulation** — firing error events verifies how the main thread handles worker crashes and retries.
- **Lifecycle** — terminate() is tracked so tests can confirm cleanup and that no further messages are processed afterward.
- **Transfer semantics** — tests can verify whether payloads are passed by reference or transferred, which matters for typed arrays and ownership.
- **Scope** — mocking works well for logic that coordinates workers; the worker's own computation still needs direct tests.
- **Common failure modes** — mocks that emit messages synchronously when real workers are asynchronous, and tests that never await the handler under test.
- **Worked example** — a UI controller that posts a chunk of work to a worker is tested with a mock that replies with a known result; the controller's loading and success states are asserted.
- **Practical relevance** — worker mocks make parallel-processing UI code testable in plain unit tests without a browser runtime.

## Related
- [[wiki/frontend/web-workers|Web Workers]] — the real API being faked
- [[wiki/testing/mocking|Mocking]] — the general technique
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — tool support
- [[wiki/testing/unit-testing|Unit Testing]] — test scope
- [[wiki/web-platforms/browser-engines|Browser Engines]] — runtime behavior
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]] — module boundaries
