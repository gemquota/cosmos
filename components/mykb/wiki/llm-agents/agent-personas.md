---
type: "concept"
title: "Agent Personas"
description: "Stable role and style definitions that shape an agent's behavior"
tags: ["personas", "roles", "identity", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Agent Personas

## Summary
An agent persona is a defined role — researcher, reviewer, operator — with associated style, goals, and constraints that shape behavior. It matters because role framing improves consistency and separates concerns in multi-agent setups. Personas are the surface layer of agent identity.

## Details
- Components: role description, tone, knowledge scope, behavioral rules.
- Personas make multi-agent interactions legible and predictable.
- Must be versioned alongside the agent's identity.
- Open questions: persona stability under long sessions.

## Related
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — personas within identity
- [[wiki/agent-systems/autonomy-levels|Autonomy Levels]] — role determines allowed autonomy
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — personas in handoff context
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioning persona definitions
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — personas for delegated roles
