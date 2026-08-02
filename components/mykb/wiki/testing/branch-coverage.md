---
type: "concept"
title: "Branch Coverage"
description: "Measuring coverage of decision outcomes and condition combinations"
tags: ["branch-coverage", "coverage", "testing", "metrics"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://coverage.readthedocs.io/en/latest/branch.html", "https://www.ibm.com/topics/branch-coverage"]
---

# Branch Coverage

## Summary
Branch coverage tracks whether each decision outcome, both the true and false side of every if, switch, and loop, actually executed. It is stricter than line coverage and catches untested edge paths that line counts hide.

## Details
- Measured by coverage.py in branch mode, Istanbul branches, JaCoCo, and gcov.
- A line can be covered while one of its branches is not, hiding a bug in plain sight.
- Full branch coverage on all code is expensive; target decision-heavy logic first.
- Report branch percentages per function to find coverage gaps precisely.
- Pair with boundary-value analysis: branch gaps point at missing edge tests.
- CI gates should set separate branch and line thresholds.
- Condition coverage, each operand of a compound condition, goes even deeper.

## Related
- [[wiki/testing/coverage-metrics|Coverage Metrics]] — the family branch coverage belongs to
- [[wiki/testing/diff-coverage|Diff Coverage]] — branch coverage gated on changed lines
- [[wiki/testing/boundary-value-analysis|Boundary Value Analysis]] — edge tests that exercise branches
- [[wiki/testing/mutation-testing|Mutation Testing]] — stronger than branch coverage
- [[wiki/dev-tools/code-coverage|Code Coverage]] — tooling that reports branches
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — enforcing branch thresholds
