---
type: "entity"
title: "CI/CD Patterns"
status: "growing"
tags: ["devops", "ci", "cd", "github-actions", "automation"]
source: ["sessions/"]
---

# CI/CD Patterns

CI/CD patterns across the ecosystem.

## GitHub Actions
```yaml
name: Deploy
on: push
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: peaceiris/actions-gh-pages@v3
```

## Patterns
- Matrix testing across Python/node versions
- pip/npm caching for faster runs
- Conditional deploys (main branch only)
- Status badges in README

## Pipeline Structure

- Split pipelines into stages (lint, test, build, deploy) so failures stop early and logs stay scannable.
- Cache dependencies — pip, npm, Go module caches — keyed by lockfile hash to speed up identical runs.
- Store build artifacts and test reports as pipeline artifacts so failures can be inspected after the run.
- Keep deploy jobs conditional on branch, tag, or environment so production changes are deliberate.

## Branch and Release Strategy

- Trunk-based development keeps the main branch always releasable; feature branches are short-lived and merged after review.
- Pull-request checks run the same test suite as the main pipeline, catching regressions before merge.
- Tagged releases trigger production deploys, while main builds deploy to staging.
- Conventional commit messages let automation derive changelogs and version bumps.

## Reliability and Observability

- Add status badges to the README so build health is visible at the repository entry point.
- Retry flaky steps with bounded retries, but track flakiness so it is fixed rather than papered over.
- Alert on pipeline failure and on deploy completion so engineers notice broken builds promptly.


## Example Walkthrough

A typical push to main runs: checkout and setup, dependency install from cache, lint and type checks, unit tests on a matrix of versions, build and publish artifacts, then a conditional deploy to staging (and to production only on tags). Each stage writes machine-readable output so the summary page renders pass/fail at a glance, and any failed stage stops the pipeline before artifacts are published.


See also: [[wiki/devops-infra/00-index|DevOps & Infrastructure]], [[wiki/development/00-index|Development]]

## Related Concepts

- [[wiki/devops-infra/github-actions|GitHub Actions]] — the CI runner seen in the example pipeline
- [[wiki/dev-tools/conventional-commits|Conventional Commits]] — commit conventions that drive automation
- [[wiki/devops-infra/feature-flags|Feature Flags]] — decoupling deploy from release
- [[wiki/devops-infra/incident-response|Incident Response]] — the process a failed deploy should trigger

