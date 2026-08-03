---
type: "synthesis"
title: "Responsible Disclosure for AI"
description: "Norms for disclosing AI vulnerabilities safely"
tags: ["disclosure", "security", "norms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Responsible Disclosure for AI

## Summary
Responsible disclosure coordinates vulnerability reporting: researchers report privately, vendors fix, then public disclosure after a window.

## Details
- Responsible disclosure coordinates vulnerability reporting: researchers report privately, vendors fix, then public disclosure after a window.
- It balances transparency with user safety.
- AI disclosure adds nuance: disclosed jailbreaks spread fast.
- RSIS3 relevance: the bundle's incident fixes would follow report-fix-publish order.

- The coordination principle: researchers report privately, vendors get a fixed window to fix, and public disclosure follows — the window balances transparency against the risk of publicizing a live vulnerability.
- AI-specific complications: jailbreaks and prompt-injection chains spread faster than traditional exploits once disclosed, and a fix may require retraining or prompting changes rather than a patch, which lengthens the window.
- Who discloses: the researcher, the vendor, or a coordinating body — the standing rule is that the party with the most information and the least conflict publishes, and the other parties coordinate on timing.
- Disclosure quality: a good disclosure includes the trigger, the impact, the fix, and the workaround; publishing partial information helps attackers more than it helps defenders.
- Tension with AI safety: for model vulnerabilities, full public disclosure can accelerate misuse; the window and the audience should be tuned per severity, with coordinated disclosure as the default.
- Incident handling for the bundle: the documented intent is report-fix-publish order — a report is acknowledged, a fix is prepared and verified, and only then is the issue published.
- Post-disclosure follow-up: after publication, the incident should feed the same review cycle as other incidents, so the disclosure becomes a lesson rather than an endpoint.
- Legal and contractual context: coordinated disclosure also respects NDAs and bug-bounty terms, so the window and audience should be checked against any existing agreement before publication.
## Related
- [[wiki/syntheses/coordinated-disclosure|Coordinated Disclosure]] — the formal process
- [[wiki/syntheses/vulnerability-reports-ai|Vulnerability Reports]] — the channel
- [[wiki/syntheses/security-advisories-ai|Security Advisories]] — the response
- [[wiki/syntheses/bug-bounty-ai|Bug Bounties for AI]] — the incentive
- [[wiki/concepts/incident-driven-improvement|Incident-Driven Improvement]] — the full treatment of this theme
- [[wiki/security-auth/responsible-disclosure|Responsible Disclosure]] — existing graph context
