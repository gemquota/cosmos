---
type: "concept"
title: "Supervisor Pattern and Swarm"
description: "Two coordination styles: a central supervisor directing workers, or a flat swarm of peers"
tags: ["agents", "orchestration", "supervisor", "swarm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2304.03442", "https://arxiv.org/abs/2307.09288"]
---

# Supervisor Pattern and Swarm

## Summary
The supervisor pattern concentrates planning in one agent that delegates to specialized workers; a swarm distributes decision-making across many peers that collaborate or compete. Supervisors give control and auditability; swarms give resilience and parallelism. Many production systems blend the two.

## Details
- **Supervisor** — one planner issues tasks, collects results, and resolves conflicts; simpler to reason about, but the supervisor becomes a bottleneck and single point of failure.
- **Swarm** — peers negotiate via shared context, voting, or market mechanisms; scales and tolerates failure, but behavior is emergent and harder to audit.
- **Blended designs** — hierarchical supervisors with swarm-like worker pools, or swarms with a lightweight coordinator for final decisions.
- **Worked example** — a supervisor routes sub-tasks to a pool of writer agents, then a critic agent reviews; disagreement escalates to the supervisor.
- **Selection** — choose supervisor when correctness is critical and audit needed; choose swarm when throughput and diversity of views matter.
- **mykb relevance** — RSIS3's executive planner is a supervisor over its pulse phases and sub-agents.

## Related
- [[wiki/agent-systems/agent-consensus|Agent Consensus]] — swarm decision-making
- [[wiki/agent-systems/voting-agents|Voting Agents]] — swarm-style aggregation
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — nested supervision
- [[wiki/agent-systems/delegation-and-handoffs|Delegation and Handoffs]] — supervisor-to-worker handoffs
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — monitoring supervised work
- [[wiki/agent-systems/market-based-agent-coordination|Market-Based Agent Coordination]] — market-driven swarms
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
