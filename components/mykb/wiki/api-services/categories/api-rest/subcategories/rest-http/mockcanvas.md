---
type: "entity"
title: "MockCanvas"
description: "A test double for a canvas drawing context that records operations"
tags: ["entity", "testing", "mock", "canvas", "frontend"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# MockCanvas

## Summary

MockCanvas is a test double that stands in for a canvas drawing context, recording draw calls instead of rendering pixels. It matters because canvas-heavy code is hard to test in headless environments where no real GPU or canvas exists. Recording the command stream lets tests assert what the code drew, when, and in what order.

## Details

- **Definition** — A mock canvas implements the same API as a drawing context, capturing calls, arguments, and state without performing real rasterization.
- **Why mock** — Headless tests, CI runners, and server-side rendering lack a real canvas; a mock keeps logic testable everywhere.
- **Assertions** — Tests can assert that specific commands ran, with which arguments, and in which sequence — catching drawing-logic regressions.
- **Worked example** — A chart component draws axes then bars; the mock records fillRect calls, and the test asserts the bar count and coordinates match the data.
- **Common failure modes** — Mocks that drift from the real API, asserting implementation details so tightly that any rendering change breaks tests, and untested fallbacks for missing canvas support.
- **Practical relevance** — Separating drawing logic from the context lets the same code run under mock, canvas, and WebGL backends.
- **Variants** — Spies wrap a real context to observe calls, while full mocks replace it entirely; both can record state snapshots.
- **Telemetry note** — Recorded in API and cloud sessions with a canvas tag, matching frontend testing infrastructure discussions.
- **Recording** — Storing the full command list enables snapshot tests that compare draw sequences across versions.
- **Fallbacks** — Real environments without canvas support should exercise the same code paths via feature detection and graceful degradation.
- **Worked example** — A component test runs under MockCanvas, asserts the axis and series draw calls, then the same assertions run against a real canvas in a browser test.

## Related

- [[wiki/web-platforms/canvas-2d|Canvas 2D]] — the API being mocked
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/bxgubd3|BxgUbd3]] — D3.js drawing over canvases
- [[wiki/testing/characterization-testing|Characterization Testing]] — locking in observed behavior
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/debugoverlay|DebugOverlay]] — debugging drawn output
- [[wiki/testing/api-testing|API Testing]] — the broader test strategy
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — the code under test
