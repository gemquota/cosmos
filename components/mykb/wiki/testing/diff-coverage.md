---
type: "concept"
title: "Diff Coverage"
description: "Requiring coverage on newly changed lines in pull requests"
tags: ["diff-coverage", "coverage", "testing", "code-review"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/codecov/diff-cover", "https://docs.codecov.com/docs/commit-status"]
---

# Diff Coverage

## Summary
Diff coverage requires that lines changed in a pull request are covered by tests. It focuses quality gates on new code, where risk concentrates, instead of letting legacy gaps hide behind historical averages.

## Details
- Tools: diff-cover, Codecov patch coverage, Coveralls, and GitLab coverage reports.
- Typical gate: 80 to 90 percent coverage on the diff, blocking merge when new lines are untested.
- Prevents coverage gaming: teams cannot hide new untested logic behind global averages.
- Pair with lint and code review; diff coverage is a signal, not a substitute.
- Refactors count only genuinely new lines as needing coverage.
- Set explicit thresholds per repository and revisit them with the team.
- A failing diff-coverage gate should link directly to the uncovered lines.

## Related
- [[wiki/testing/coverage-metrics|Coverage Metrics]] — the broader measure diff coverage uses
- [[wiki/testing/branch-coverage|Branch Coverage]] — a stricter lens on changed lines
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — where diff coverage is enforced
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — human review complements the gate
- [[wiki/software-engineering/git-workflows|Git Workflows]] — PRs are where diff coverage applies
- [[wiki/dev-tools/code-coverage|Code Coverage]] — tooling backing the metric
