---
type: "concept"
title: "AI Responsibility"
description: "Attributing responsibility for AI outcomes"
tags: ["responsibility", "ethics", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# AI Responsibility

## Summary

AI responsibility asks who is responsible for AI behavior and harm — developers, deployers, users, or the system. Moral responsibility requires agency and knowledge that current systems lack, so the burden falls on the humans in the chain.

## Details
- Mechanism: responsibility analysis maps the causal chain (model training, deployment decisions, use context) to actors with capacity (knowledge, control, foresight); moral responsibility traditionally requires agency and knowledge — properties systems lack — so responsibility is distributed among the people who chose, built, and deployed the system; legal responsibility assigns liability via contracts, product law, and regulation.
- Concrete example: a biased hiring model traces to training-data choices, deployment thresholds, and monitoring decisions — each with a responsible party; an autonomous agent that posts harmful content is the deployer's responsibility (they set permissions and oversight), not the model's; a misuse case shifts some responsibility to the user, bounded by what was foreseeable.
- Failure modes: responsibility diffusion — everyone in the chain claims a small part, so nobody is answerable; attributing responsibility to the system (which lacks agency and cannot be sanctioned); and responsibility without capability (holding someone accountable who lacked control or information).
- Operational tradeoffs: responsibility assignment shapes liability, incentives, and design — clear assignment pushes diligence upstream (developers/deployers); the discipline is mapping responsibility at design time (who decides, who can intervene, who answers), documenting it, and matching accountability mechanisms (the institutional layer) to it.
- RSIS3/mykb relevance: worker reports assign responsibility for pass outcomes — each synthesis records who/what ran it and who reviewed it, keeping the loop's outputs attributable.
- Responsibility registers: record per system who decides, who can intervene, and who answers — a one-page register beats a paragraph in the handbook nobody reads.
- Incident loop: when harm occurs, the postmortem should name the responsibility gaps, not just the technical cause; fixes then target the accountability structure.

## Related
- [[wiki/agent-systems/accountability-ai|AI Accountability]] — the institutional layer
- [[wiki/concepts/moral-agency|Moral Agency]] — the philosophical layer
- [[wiki/agent-systems/legal-accountability|Legal Accountability for AI]] — the legal layer
- [[wiki/concepts/human-supervision-limits|Human Supervision Limits]] — the complicating factor
- [[wiki/concepts/oversight|Oversight]]
- [[wiki/testing/responsible-ai-principles|Responsible Ai Principles]]
