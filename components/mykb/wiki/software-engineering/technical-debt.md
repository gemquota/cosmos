---
type: "concept"
title: "Technical Debt"
description: "The accumulated cost of expedient software decisions that must be paid back later"
tags: ["technical-debt", "quality", "maintenance", "economics"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/TechnicalDebt.html"]
---

# Technical Debt

## Summary
Technical debt is the metaphor, popularized by Ward Cunningham and refined by Martin Fowler, for the cost of taking shortcuts in software that will need to be repaid with interest. It is not inherently bad — debt can be a rational trade — but unmanaged debt slows every future change.

## Details
- The metaphor: borrowing time now to ship faster, paying interest later through bugs, slow development, and onboarding friction.
- Fowler's quadrant classifies debt by intent (deliberate vs inadvertent) and by nature (prudent vs reckless), producing four types from 'prudent and deliberate' to 'reckless and inadvertent'.
- Visible symptoms: high change failure rate, growing bug counts, estimation creep, and the fear of touching old code.
- Management is about tracking, not eliminating: record debt in a visible register, tie repayment to feature work, and cap interest with hygiene standards.
- Refactoring and tests are the repayment instruments; code review prevents new reckless debt from accruing.
- RSIS3 relevance: stubs in mykb are deliberately small debts — noted, linked, and scheduled for expansion during curation rounds.
- Worked example: a quick script hardcodes credentials (debt); the repayment is moving them to a secrets manager and adding a test.

## Related
- [[wiki/software-engineering/refactoring|Refactoring]] — the primary way debt is repaid
- [[wiki/software-engineering/code-review|Code Review]] — the gate that limits reckless debt
- [[wiki/software-engineering/bus-factor|Bus Factor]] — undocumented shortcuts concentrate risk in one person
- [[wiki/software-engineering/estimation-techniques|Estimation Techniques]] — debt makes estimates unreliable until repaid
- [[wiki/security/secrets-management|Secrets Management]] — hardcoded secrets are classic technical debt
- [[wiki/memory/provenance|Provenance]] — knowing why a shortcut happened helps pay it back
- [[wiki/concepts/cognitive-load|Cognitive Load]] — debt raises the cognitive load of future changes
