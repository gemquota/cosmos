---
type: "concept"
title: "Agent Personas"
description: "Stable role and style definitions that shape an agent's behavior"
tags: ["personas", "roles", "identity", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Agent Personas

## Summary

Agent personas assign an agent a role, style, and constraints — a senior reviewer, a skeptical auditor, a domain specialist — shaping how it frames problems, what it notices, and how it communicates. Personas are prompt-side configuration with real behavioral consequences.

## Details
- Mechanism: a persona is system-prompt scaffolding: role definition, goals, values, tone, constraints, and sometimes example behavior; it steers the model's priors toward a perspective (thoroughness, safety-consciousness, brevity) without changing capabilities; personas compose with tools and policies — they are context, not enforcement.
- Concrete example: a "red-team reviewer" persona checks every proposal for failure modes and attacks, producing adversarial reviews; a "domain expert" persona brings terminology and standards awareness to technical notes; a "concise operator" persona compresses verbose outputs. The failure pattern: personas that override safety instructions or claim authority they lack.
- Failure modes: personas as fake enforcement — a persona can encourage but not guarantee behavior, so critical constraints must live in policies and gates; persona conflicts (two agents with contradictory roles sharing a task); and personas that add noise — long, unhelpful role fluff that burns context.
- Operational tradeoffs: personas are cheap, high-leverage steering with the trade that they are soft controls; the discipline is writing personas as concrete behavioral contracts, testing their effect on outputs, and keeping hard requirements in the policy layer.
- RSIS3/mykb relevance: the wiki's loop uses personas for reviewers and specialists, and records which personas shaped each synthesis so output bias stays attributable.
- Persona vs capability: a persona cannot add knowledge the model lacks — pair personas with retrieval and tools so role framing steers real competence.
- Evaluation: sample outputs with and without the persona to confirm it changes behavior in the intended direction; a persona with no measurable effect is context waste.

## Related
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — personas within identity
- [[wiki/agent-systems/autonomy-levels|Autonomy Levels]] — role determines allowed autonomy
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — personas in handoff context
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioning persona definitions
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — personas for delegated roles
