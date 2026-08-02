---
type: "concept"
title: "Visual Regression Testing"
description: "Pixel-based comparison of rendered UI against image baselines"
tags: ["visual-regression", "testing", "ui", "screenshots"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://playwright.dev/docs/test-snapshots", "https://docs.cypress.io/guides/tooling/visual-testing"]
---

# Visual Regression Testing

## Summary
Visual regression testing compares rendered UI screenshots against pixel baselines to catch unintended styling and layout changes. It detects what DOM assertions miss: fonts, spacing, colors, and responsive breakpoints.

## Details
- Tools: Playwright toHaveScreenshot, Cypress visual testing, Percy, Chromatic, and Applitools.
- Baselines are stored per platform and browser; diffs show highlight overlays.
- Stabilize flakiness: pin fonts, animations, and scroll position before capture.
- Test key breakpoints rather than every possible viewport size.
- Approval workflow: humans review diffs, accept intended changes, reject regressions.
- AI-assisted tools apply layout-aware comparison to cut false positives.
- Run a focused subset in PR CI and the full matrix on release.

## Related
- [[wiki/testing/snapshot-testing|Snapshot Testing]] — DOM-level baselines versus pixels
- [[wiki/testing/approval-testing|Approval Testing]] — human-reviewed visual diffs
- [[wiki/testing/ui-testing|UI Testing]] — behavioral UI checks alongside pixels
- [[wiki/testing/compatibility-testing|Compatibility Testing]] — browser matrices for visual checks
- [[wiki/web-platforms/css-layout|CSS Layout]] — layout changes visual tests catch
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — visual suites gating merges
