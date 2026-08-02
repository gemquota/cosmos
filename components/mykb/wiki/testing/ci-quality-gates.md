---
type: "concept"
title: "CI Quality Gates"
description: "Enforcing coverage, lint, and test thresholds before merge"
tags: ["ci", "testing", "quality-gates", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.github.com/en/actions", "https://docs.gitlab.com/ee/ci/"]
---

# CI Quality Gates

## Summary
CI quality gates are automated checks, lint, typecheck, coverage, tests, and security scans, that must pass before a merge or release proceeds. They encode team standards as executable policy instead of relying on memory.

## Details
- Implement in GitHub Actions, GitLab CI, Jenkins, or CircleCI pipelines.
- Common gates: build, unit and integration tests, diff coverage, lint, SAST, dependency scans, and preview deploys.
- Graduated enforcement: comments for warnings, hard blocks for failures.
- Keep the pipeline fast: parallelize, cache, and select affected tests.
- Gate failures must be actionable and attributable to avoid gate fatigue.
- Merge queues and branch protection enforce gates atomically.
- Treat gates as living policy reviewed and tuned with the team.

## Related
- [[wiki/devops-infra/github-actions|GitHub Actions]] — a common quality-gate host
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — pipeline shapes gates live in
- [[wiki/testing/diff-coverage|Diff Coverage]] — a precision coverage gate
- [[wiki/testing/flaky-tests|Flaky Tests]] — flakiness breaks gate trust
- [[wiki/testing/vulnerability-scanning|Vulnerability Scanning]] — security gates in CI
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — human review beyond automated gates
