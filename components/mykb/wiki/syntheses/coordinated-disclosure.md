---
type: "concept"
title: "Coordinated Disclosure"
description: "Structured multi-party vulnerability disclosure"
tags: ["disclosure", "coordination", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Coordinated Disclosure

## Summary
Coordinated disclosure is a formal process where researchers, vendors, and platforms agree on the timing and content of vulnerability publication. It replaces the two bad extremes — full disclosure that drops a live exploit on users, and indefinite secrecy that leaves users exposed without a fix — with a negotiated window in which the vendor can patch and users can update.

## Details
- Coordinated disclosure is a formal process where researchers, vendors, and platforms agree on timing and content of vulnerability publication. The typical shape: the researcher reports privately, the vendor acknowledges, a disclosure deadline (commonly 90 days) is agreed, the vendor ships a fix, and the researcher publishes after the fix or at the deadline.
- It reduces the harm window while preserving credit. The researcher gets attribution and a place in advisory acknowledgments; the vendor gets lead time to patch; users get a fix before the exploit is public. Each party trades a little control for a much better outcome than going it alone.
- Concrete example: a researcher finds an account-takeover bug in an AI service's OAuth handling, reports it privately with a PoC, the vendor confirms and ships a fix in six weeks, the advisory publishes with the researcher credited and a CVE assigned — users were never exposed to a public exploit, and the researcher's report became a bounded, solvable incident.
- Deadlines and goodwill make the process work. The deadline is the engine: without one, vendors stall and researchers leak; with one, both sides have an incentive to move. Goodwill matters when the deadline is missed — a vendor that communicates and ships a partial fix earns an extension, while one that goes silent gets the report published on schedule.
- Failure modes: vendor silence that forces unilateral publication; researchers who disclose early and hand attackers a live exploit; disclosure that publishes a PoC without a fix, creating a window of maximum risk; and legal threats against researchers, which end the program and the goodwill with it.
- Tradeoffs: the negotiated delay protects users of the affected product but keeps the vulnerability secret from everyone else, including defenders of similar systems; coordination is a trust exercise between parties with different incentives, so the process needs a neutral default (the deadline) that works when trust fails.
- RSIS3 relevance: multi-worker coordination on shared repos needs the same discipline — when one agent finds a flaw in shared state, the "disclosure" is a coordinated announcement with a fix plan and a deadline, not a unilateral change or an open broadcast.

## Related
- [[wiki/syntheses/responsible-disclosure-ai|Responsible Disclosure for AI]] — the norms
- [[wiki/syntheses/vulnerability-reports-ai|Vulnerability Reports]] — the channel
- [[wiki/syntheses/security-advisories-ai|Security Advisories]] — the publication
- [[wiki/syntheses/patch-management-ai|Patch Management for AI]] — the fix
- [[wiki/concepts/incident-driven-improvement|Incident-Driven Improvement]] — the full treatment of this theme
- [[wiki/security-auth/responsible-disclosure|Responsible Disclosure]] — existing graph context
