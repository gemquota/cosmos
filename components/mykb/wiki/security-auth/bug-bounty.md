---
type: "concept"
title: "Bug Bounty"
description: "Programs that pay researchers to find and report security vulnerabilities"
tags: ["bug-bounty", "vulnerability", "researchers", "programs"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Bug_bounty_program"]
---

# Bug Bounty

## Summary
Bug bounty programs invite external researchers to find vulnerabilities in exchange for rewards, scaling testing beyond internal teams. Rules of engagement define scope, eligibility, and disclosure terms; a good program pairs rewards with fast triage, and bounties surface real-world findings but do not replace internal testing and secure development.

## Details
- Mechanism: a public or invite-only program publishes scope (what systems are in), rules (what is allowed, what is out), and rewards; researchers submit findings; the team triages, reproduces, fixes, and pays; disclosure is coordinated — the researcher stays quiet until the fix ships; Hall of Fame credit and transparent timelines keep researchers engaged.
- Concrete example: a company opens a program for its API and dashboard; a researcher finds an SSRF in a URL-fetching feature; the report includes a minimal reproducer; triage confirms severity, the fix ships in a week, and the researcher is paid and credited; the finding also feeds the internal test suite.
- Failure modes: scope ambiguity causing disputes and wasted researcher effort; slow triage that drives researchers away; rewards too low to attract quality research; disclosure disagreements that end in premature publication; programs that exist but are unstaffed, producing a queue of unhandled reports.
- Tradeoffs: bounties scale testing cheaply per finding and surface attacker-perspective bugs, at the cost of coordination, reward budgets, and disclosure risk; the alternative, internal testing alone, is safer and narrower; the mature pattern is a clearly scoped program with fast triage, plus internal testing and secure development as the foundation.
- Operational notes: keep scope current, staff triage, and publish metrics so the program stays credible.
- RSIS3 relevance: for mykb, a bounty-style disclosure policy with clear scope would fit a system holding sensitive memory data — the same coordination discipline for external reports.


## Related
- [[wiki/security-auth/responsible-disclosure|Responsible Disclosure]] — the disclosure policy bounties rest on
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — published findings become CVEs
- [[wiki/security-auth/security-training|Security Training]] — internal testing complements bounties
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — bounty findings feed detection
- [[wiki/api-services/dast|Dynamic Application Security Testing]] — automated external testing
