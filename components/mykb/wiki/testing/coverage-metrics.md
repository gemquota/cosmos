---
type: "concept"
title: "Coverage Metrics"
description: "Line, branch, and statement coverage measures and their interpretation"
tags: ["coverage", "testing", "metrics", "quality-gates"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://coverage.readthedocs.io/", "https://about.codecov.io/"]
---

# Coverage Metrics

## Summary
Coverage metrics measure which code was executed by tests, covering lines, statements, branches, and functions, as a rough proxy for how much behavior is verified. They find untested code but say nothing about the quality of assertions.

## Details
- Tools: coverage.py, Istanbul, JaCoCo, gcov, and the Go cover tool.
- Line coverage counts executed lines; branch coverage counts decision outcomes.
- Misuse: 100 percent coverage with weak assertions still allows broken behavior.
- Use coverage to find dead zones, guide new tests, and enforce diff coverage on PRs.
- Mutation testing measures effectiveness where coverage only measures reach.
- Coverage of integration and E2E paths is meaningful for glue code.
- Watch per-module trends instead of one global number.

## Related
- [[wiki/testing/branch-coverage|Branch Coverage]] — decision outcomes beyond lines
- [[wiki/testing/diff-coverage|Diff Coverage]] — coverage gated on changed lines
- [[wiki/dev-tools/code-coverage|Code Coverage]] — tooling perspective on the metric
- [[wiki/testing/mutation-testing|Mutation Testing]] — effectiveness beyond reach
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — coverage thresholds before merge
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — reviewing what coverage hides
