---
type: "concept"
title: "MASS"
description: "Multi-agent system: multiple agents cooperating or competing toward goals"
tags: ["entity", "acronym", "agents", "multi-agent", "systems"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# MASS

## Summary

MASS is an acronym recorded in session telemetry and most commonly expands to multi-agent system, a setup in which multiple agents interact, share information, and coordinate on tasks. Multi-agent systems matter because complex work decomposes across specialized agents that delegate, critique, and combine results. The design challenge is alignment: agents must cooperate without conflicting objectives or duplicated effort.

## Details

- **Definition** — A multi-agent system is a collection of autonomous agents whose individual actions combine into collective behavior, coordinated or emergent.
- **Coordination patterns** — Orchestrator-worker, peer debate, pipeline, and market-style competition are common topologies with different fault and trust profiles.
- **Communication** — Agents exchange messages, shared memory, or artifacts; the medium defines what information is visible and when.
- **Worked example** — A research system splits a question across a planner, three researcher agents, and a verifier; the verifier rejects claims that lack evidence and triggers rework.
- **Failure modes** — Agents repeating each other's errors, goal conflicts, runaway token costs, and unproductive loops are the classic failure modes.
- **Practical relevance** — In Cosmos, multi-agent arrangements appear in delegation, handoffs, and parallel research workflows inside RSIS3 loops.
- **Variants** — Homogeneous swarms retry the same role many times; heterogeneous teams assign distinct capabilities and oversight.
- **Evaluation** — Multi-agent systems need per-agent and system-level evaluation, since local competence does not guarantee collective success.
- **Telemetry note** — The stub carries no other definition; the multi-agent reading follows from the agent-centric session context that recorded it.
- **Shared context** — A shared memory or message bus gives agents a common ground, but conflicting writes and stale reads corrupt it; ownership rules help.
- **Cost control** — Each agent multiplies token usage; budgets, caps on debate rounds, and early termination keep collective runs affordable.
- **Failure containment** — A misbehaving agent should be isolatable — sandboxed tools, read-only permissions, and veto rights prevent one failure from poisoning the team.
- **Worked example** — Three agents draft, review, and merge a design doc; the reviewer agent rejects twice before the drafter converges on an accepted version.

## Related

- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — coordinating many agents
- [[wiki/agent-systems/delegation-and-handoffs|Delegation and Handoffs]] — passing work between agents
- [[wiki/agent-systems/agent-pipelines|Agent Pipelines]] — sequential agent structure
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining task completion
- [[wiki/agent-systems/hidden-goals|Hidden Goals]] — alignment risk in cooperation
- [[wiki/concepts/emergent-improver|Emergent Improver]] — collective capability growth
