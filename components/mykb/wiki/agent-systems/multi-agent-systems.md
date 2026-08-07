---
type: "concept"
title: "Multi-Agent Systems"
description: "Multiple specialized agents collaborating, competing, or coordinating to complete tasks"
tags: ["agents", "multi-agent", "coordination", "orchestration"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2304.03442", "https://arxiv.org/abs/2308.08155"]
---

# Multi-Agent Systems

## Summary
Multi-agent systems decompose work across specialized agents that share context and coordinate outcomes. They matter because complex tasks — research, codebases, customer pipelines — exceed what one agent can reliably hold in context. Coordination style determines whether the system is a hierarchy, a peer network, or a market.

## Details
- **Patterns** — supervisor-and-workers, debate, pipelines, and swarms; each has different failure and cost profiles.
- **Shared state** — a shared scratchpad, blackboard, or memory system lets agents exchange intermediate results without leaking private context.
- **Coordination mechanisms** — handoffs, voting, consensus, and market bidding distribute decisions across the group.
- **Cost and latency** — N agents multiply token spend and add orchestration overhead; supervisor patterns concentrate cost in one planner.
- **Worked example** — a code team: planner decomposes the issue, coder implements, critic reviews, tester runs checks, and the verifier approves the merge.
- **mykb relevance** — the triad architecture (RSIS3 + mykb + myrsikb) is itself a multi-agent system with distinct responsibilities per component.

- **Emergence** — multi-agent systems produce behaviors no single agent designed: beneficial (division of labor) and harmful (unintended collusion, conflict spirals); both need monitoring.
- **Governance** — each agent needs an explicit role, permission set, and authority boundary; ambiguity here is how one agent's failure becomes everyone's.
- **Observability** — a cross-agent trace with a common request id is the minimum for debugging; without it, blame and diagnosis are guesswork.
- **Cost control** — agent count multiplies token spend and coordination overhead; the system should justify each additional agent against its marginal contribution.

## Related
- [[wiki/agent-systems/agent-consensus|Agent Consensus]] — reaching agreement across agents
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — decomposing work into sub-agents
- [[wiki/agent-systems/agent-ensembling|Agent Ensembling]] — running many agents for robustness
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — orchestration concepts in mykb
- [[wiki/agent-systems/market-based-agent-coordination|Market-Based Agent Coordination]] — market-driven coordination
- [[wiki/agent-systems/voting-agents|Voting Agents]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the RSIS3/mykb architecture it serves
