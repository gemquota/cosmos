---
type: "concept"
title: "End-to-End Testing"
description: "Driving complete user journeys through the full stack from UI to data store"
tags: ["e2e-testing", "testing", "playwright", "user-journeys"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://playwright.dev/docs/end-to-end-testing", "https://docs.cypress.io/guides/end-to-end-testing/writing-your-first-end-to-end-test"]
---

# End-to-End Testing

## Summary
End-to-end tests drive complete user journeys through the real stack, from browser or mobile client through API and database to third-party services. They provide the highest confidence and the lowest speed, so teams keep a small, high-value set focused on critical business paths.

## Details
- Tooling: Playwright and Cypress for web, Appium for mobile, all supporting parallel workers.
- Selectors: prefer roles, labels, and test IDs over CSS classes so style refactors do not break tests.
- Determinism: intercept and stub third-party calls and control time to keep journeys repeatable.
- Data setup: seed state through APIs instead of clicking through the UI, which is faster and more reliable.
- Flakiness control: explicit waits, retry policies, and timeouts tuned per action.
- Scope discipline: one E2E journey per critical flow, not exhaustive UI coverage.
- Run against a prod-like environment and on preview deployments for merge validation.

## Related
- [[wiki/testing/ui-testing|UI Testing]] — the widget and screen level below full journeys
- [[wiki/testing/test-environments|Test Environments]] — prod-like infrastructure for E2E runs
- [[wiki/testing/flaky-tests|Flaky Tests]] — the main operational cost of E2E suites
- [[wiki/testing/test-parallelism|Test Parallelism]] — sharding journeys across CI workers
- [[wiki/testing/component-testing|Component Testing]] — fast isolated alternative for UI logic
- [[wiki/testing/api-testing|API Testing]] — covers the same stack with less cost
