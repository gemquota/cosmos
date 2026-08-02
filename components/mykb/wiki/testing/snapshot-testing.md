---
type: "concept"
title: "Snapshot Testing"
description: "Comparing serialized output against stored baseline references"
tags: ["snapshot-testing", "testing", "baselines", "jest"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://jestjs.io/docs/snapshot-testing", "https://vitest.dev/guide/snapshot"]
---

# Snapshot Testing

## Summary
Snapshot testing serializes a component or function's output and compares it against a stored baseline on later runs. Any unexpected change fails the test, surfacing drift in rendering, JSON, configuration, or error messages.

## Details
- Jest toMatchSnapshot, Vitest snapshots, and Swift SnapshotTesting are common implementations.
- The first run writes the baseline; subsequent runs diff output against it.
- Excellent for UI trees, error messages, config files, and API response shapes.
- Pitfalls: huge snapshots nobody reviews and trivial changes churning baselines.
- Update workflow: inspect the diff, accept intended changes, reject accidental ones.
- Pair with visual regression for pixels and semantic diffing for text.
- Snapshots complement assertions; verify important properties explicitly as well.

## Related
- [[wiki/testing/golden-file-management|Golden File Management]] — canonical output files as baselines
- [[wiki/testing/visual-regression-testing|Visual Regression Testing]] — pixel-level rendering baselines
- [[wiki/testing/approval-testing|Approval Testing]] — human-reviewed diffs against baselines
- [[wiki/testing/regression-testing|Regression Testing]] — snapshots are a regression net
- [[wiki/testing/ui-testing|UI Testing]] — rendered output snapshot subjects
- [[wiki/testing/golden-tests|Golden Tests]] — LLM-era golden baselines
