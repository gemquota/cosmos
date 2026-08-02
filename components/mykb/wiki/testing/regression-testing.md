---
type: "concept"
title: "Regression Testing"
description: "Re-running tests to detect behavior regressions after changes"
tags: ["regression-testing", "testing", "safety-net", "ci"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/regression-testing", "https://jestjs.io/docs/snapshot-testing"]
---

# Regression Testing

## Summary
Regression testing re-runs existing tests after code changes to detect unintended behavior changes. It is the safety net that lets teams refactor, upgrade dependencies, and add features without silently breaking behavior that users rely on.

## Details
- Any change can regress behavior: features, fixes, refactors, dependency bumps, and configuration edits.
- Strategy: run the full suite on release candidates and a targeted selection on pull requests.
- Regression test selection analyzes the changed-file graph to run only affected tests.
- Golden and snapshot tests form a specialized regression net for output stability.
- Keep the suite fast so regression runs fit in CI; slow suites get skipped and rot.
- Every fixed bug should add a regression test that fails on the old code and passes on the fix.
- Track flaky tests separately, since flakiness destroys regression signal.

## Related
- [[wiki/testing/regression-test-selection|Regression Test Selection]] — chooses which tests to rerun for a change
- [[wiki/testing/snapshot-testing|Snapshot Testing]] — output-stability regression checks
- [[wiki/testing/flaky-tests|Flaky Tests]] — flakiness undermines regression signal
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — regression suites gate merges
- [[wiki/dev-tools/git-bisect|Git Bisect]] — finds the change that caused a regression
- [[wiki/testing/test-prioritization|Test Prioritization]] — orders regression runs by risk
