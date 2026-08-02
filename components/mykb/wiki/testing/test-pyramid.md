---
type: "concept"
title: "Test Pyramid"
description: "Balancing unit, integration, and end-to-end test proportions by cost and speed"
tags: ["test-pyramid", "testing", "strategy", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/TestPyramid.html", "https://www.ibm.com/topics/test-pyramid"]
---

# Test Pyramid

## Summary
The test pyramid describes the ideal distribution of tests: many fast unit tests, fewer integration tests, and a small number of slow end-to-end tests. Cost and speed drive the shape, and inverted pyramids signal operational pain.

## Details
- Origin: Mike Cohn's Succeeding with Agile popularized the pyramid model.
- Rationale: E2E tests are slow, flaky, and expensive; unit tests are cheap and localize failures.
- The shape shifts with architecture; microservices often hold more contract and integration tests.
- The trophy variant puts static analysis and unit tests at the base with few E2E tests.
- Anti-patterns: the ice-cream cone of mostly UI tests, and the hourglass with few unit tests.
- Rebalance by extracting logic into unit-testable layers.
- Treat the pyramid as a suite health metric, not a dogma.

## Related
- [[wiki/testing/test-trophy|Test Trophy]] — the modern web-app reweighting
- [[wiki/testing/unit-testing|Unit Testing]] — the wide fast base
- [[wiki/testing/integration-testing|Integration Testing]] — the middle layer
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — the thin slow top
- [[wiki/testing/measuring-test-roi|Measuring Test ROI]] — justifying layer proportions
- [[wiki/testing/test-prioritization|Test Prioritization]] — ordering within the pyramid
