---
type: "concept"
title: "Visual Regression Testing"
description: "Screenshot diffing for UI changes"
tags: [testing", "visual-regression", "screenshots", "ui", "qa"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://playwright.dev/docs/test-snapshots", "https://storybook.js.org/docs/writing-tests/visual-testing"]
---

# Visual Regression Testing

## Summary
Visual regression testing compares screenshots of UI before and after changes to catch unintended visual breaks — shifted layouts, color changes, and overflow that unit tests miss. Baselines are stored per commit, and diffs flag changes for human review. It complements functional tests by verifying appearance rather than behavior.

## Details
- Baselines: golden screenshots stored in the repo; changes produce pixel or perceptual diffs that need approval.
- Scope: component-level tests (Storybook) isolate pieces; page-level tests capture full flows and responsive breakpoints.
- Sensitivity: pixel-perfect diffing flags antialiasing and font-rendering noise; perceptual thresholds and masks reduce noise.
- Flake sources: animations, webfonts, and timestamps must be frozen or masked for stable comparisons.
- Workflow: approved diffs update baselines; rejected diffs block the change until fixed.
- CI: running visual tests per PR catches regressions early, with review screenshots posted to the PR.

## Related
- [[wiki/testing/golden-tests|Golden Tests]] — baseline comparison technique
- [[wiki/frontend/end-to-end-testing|End-to-End Testing]] — the functional counterpart
- [[wiki/frontend/frontend-testing|Frontend Testing]] — the test strategy umbrella
- [[wiki/frontend/design-systems|Design Systems]] — component baselines at scale
- [[wiki/web-platforms/browser-engines|Browser Engines]] — rendering differences between engines
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — baseline-based testing discipline
