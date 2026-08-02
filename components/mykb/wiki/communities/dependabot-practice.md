---
type: "concept"
title: "Dependabot Practice"
description: "GitHub's dependency bot: security updates and version bumps in PRs"
tags: ["dependabot", "dependencies", "security", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dependabot Practice

## Summary
Dependabot opens PRs for dependency updates — both version bumps and security fixes — directly on GitHub, with configurable ecosystems and schedules. It is the lowest-friction starting point for dependency automation.

## Details
- Security updates target known-vulnerable ranges with minimal, reviewable diffs.
- Config (dependabot.yml) controls ecosystems, intervals, and open-PR limits.
- Review security PRs fast — a fix sitting unreviewed is a vulnerability still open.
- mykb relevance: the wiki enables Dependabot for npm, pip, and container base images.

## Related
- [[wiki/communities/dependency-updates|Dependency Updates]]
- [[wiki/communities/renovate-bot|Renovate Bot]]
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
