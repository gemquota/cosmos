---
type: "concept"
title: "Continuous Integration"
description: "Merging small changes frequently and verifying every merge automatically"
tags: ["ci", "integration", "automation", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Continuous_integration", "https://martinfowler.com/articles/continuousIntegration.html"]
---

# Continuous Integration

## Summary
Continuous integration is the practice of merging every change into a shared mainline quickly — at least daily — and validating each merge with automated build and tests. CI keeps integration conflicts small and makes the mainline always releasable.

## Details
- The pipeline is the gate: every commit triggers build, tests, lint, and packaging; a red pipeline blocks merging.
- Small, frequent merges are the point — the longer a branch lives, the more expensive integration becomes.
- Fast feedback matters: a 10-minute pipeline shapes developer behavior; a 2-hour one gets ignored.
- CI is a prerequisite for CD: you cannot release continuously what you cannot integrate continuously.
- Include environment reproducibility (pinned dependencies, hermetic builds) so pipeline results are trustworthy.
- For the mykb bundle, CI validates frontmatter, link syntax, and article counts on every commit, catching graph breaks early.

Worked example — a wiki contributor adds a stub; CI runs the link checker and fails because a wikilink points to a missing file. The contributor fixes the link before merge, and the graph stays intact.

## Related
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/continuous-deployment|Continuous Deployment]]
- [[wiki/communities/trunk-strategy|Trunk Strategy]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/communities/build-caching|Build Caching]]
- [[wiki/communities/vulnerability-scanning-ci|Vulnerability Scanning in CI]]
- [[wiki/devops-infra/github-actions|GitHub Actions]]
- [[wiki/testing/ci-quality-gates|CI Quality Gates]]
