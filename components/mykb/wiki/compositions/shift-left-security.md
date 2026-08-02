---
type: "concept"
title: "Shift-Left Security"
description: "Moving security checks earlier in the development process"
tags: ["shift-left", "security", "testing", "ci"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Shift_left_testing", "https://en.wikipedia.org/wiki/DevSecOps"]
---

# Shift-Left Security

## Summary
Shift-left security moves security activities earlier — into design, coding, and CI — where fixes are cheap. The practice pairs automation (SAST, dependency scanning, secret detection) with human review so most vulnerabilities never reach production.

## Details
- Checks move left: threat modeling at design, linting and SAST in the editor, scanning in CI, gates before merge.
- The economic argument is steep: fixing in production costs orders of magnitude more than fixing in design.
- Automation is necessary: humans cannot review every dependency and code path manually.
- Left-shifting without gates is decoration — violations must block or escalate.
- The right shift stays too: runtime monitoring and incident response still matter.
- For the mykb bundle, link verification and source checks run in CI before articles publish.
- Worked example — the wiki CI fails merges on secret leaks, critical dependency CVEs, and broken source links — all caught minutes after the commit, not after the release.

Worked example — the wiki CI fails merges on secret leaks, critical dependency CVEs, and broken source links — all caught minutes after the commit, not after the release.

## Related
- [[wiki/tooling/secure-sdlc|Secure SDLC]]
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/software-engineering/static-analysis|Static Analysis]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/communities/vulnerability-scanning-ci|Vulnerability Scanning in CI]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/communities/license-checking|License Checking]]
- [[wiki/testing/security-testing|Security Testing]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
