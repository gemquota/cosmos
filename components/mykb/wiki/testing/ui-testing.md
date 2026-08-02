---
type: "concept"
title: "UI Testing"
description: "Testing rendered interfaces at widget and screen level"
tags: ["ui-testing", "testing", "frontend", "browser"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://playwright.dev/docs/test-intro", "https://testing-library.com/docs/"]
---

# UI Testing

## Summary
UI testing verifies rendered interfaces at widget and screen level, covering interactions, state, and accessibility in a real or simulated browser. It covers the layer where users actually feel bugs.

## Details
- Levels: component tests in a simulated DOM, page tests, and full E2E journeys.
- Tools: Playwright, Cypress, Testing Library, WebdriverIO, and Selenium.
- Assert on user-visible behavior: text, roles, focus, navigation, and error messages.
- Control time and network: fake clocks, intercept requests, and seed state.
- Responsive and accessibility checks belong in UI tests.
- Balance speed and fidelity: run the fast layer per commit and the browser layer in CI.
- Visual regression adds pixel-level coverage beyond DOM assertions.

## Related
- [[wiki/testing/component-testing|Component Testing]] — widget-level UI verification
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — journeys beyond screen level
- [[wiki/testing/visual-regression-testing|Visual Regression Testing]] — pixel-level UI checks
- [[wiki/testing/accessibility-testing|Accessibility Testing]] — inclusive UI verification
- [[wiki/testing/page-object-model|Page Object Model]] — structuring UI test code
- [[wiki/web-platforms/web-apis|Web APIs]] — browser APIs UI tests drive
