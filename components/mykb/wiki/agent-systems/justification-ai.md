---
type: "concept"
title: "Justification in AI"
description: "Giving grounds for AI behavior"
tags: ["justification", "accountability", "ai"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Justification in AI

## Summary
Justification in AI is the practice of supplying grounds for a system's behavior — the evidence, rules, or values that support a decision — so the decision can be examined, challenged, and appealed. A justification is distinct from an explanation of mechanism: it gives reasons why the behavior is acceptable, not just how it was produced.

## Details
- **Grounds, not traces** — a decision trace says what happened; a justification says why it was the right call, referencing rules, evidence, and tradeoffs.
- **Contestability** — justifications exist so that affected parties can challenge a decision; without them, appeals reduce to asking for a different outcome with no basis.
- **Quality criteria** — justifications are only as good as their grounds: post-hoc rationalization, invented citations, and appeals to authority are worse than a clear admission of uncertainty.
- **Audience** — the same decision may need different justifications for a user, an auditor, or a regulator; each requires the grounds to be expressed in that audience's frame.
- **Relationship to explainability** — explainable AI provides the mechanism-level view; justification supplies the normative layer on top of it, and the two together make decisions auditable.
- **Failure modes** — models produce fluent post-hoc justifications for errors (confabulated rationales); systems must anchor justifications in logged evidence rather than generation.
- **mykb relevance** — source links and decision reports are the justification layer of the wiki: every claim and every retained decision carries its grounds.

- **Automated justification** — agents can generate justifications on demand if they log the evidence and rules consulted at decision time; retroactive generation produces rationalizations, which is why the logging must come first.

## Related
- [[wiki/agent-systems/explainability-ai|Explainable AI]] — the mechanism-level complement
- [[wiki/agent-systems/accountability-ai|AI Accountability]] — the system justifications feed
- [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance]] — the grounds in practice
- [[wiki/concepts/cross-examination|Cross-Examination]] — challenging the grounds
- [[wiki/agent-systems/self-critique|Self-Critique]] — auditing one's own grounds
- [[wiki/agent-systems/decision-reports|Decision Reports]] — recording justifications
