---
type: "concept"
title: "Hierarchical Agents"
description: "Agents organized in a tree where higher levels delegate to lower ones"
tags: ["hierarchical", "delegation", "multi-agent", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Hierarchical_control_system", "https://arxiv.org/abs/2210.03629", "https://en.wikipedia.org/wiki/Hierarchical_task_network"]
---

# Hierarchical Agents

## Summary
Hierarchical agents arrange roles in a tree: a top-level planner delegates subtasks to mid-level coordinators, which delegate further to workers. It scales coordination and matches organizational structure, with each level abstracting the one below it: the planner issues goals, coordinators decompose them, and workers return outcomes rather than process details.

## Details
- **Levels and abstraction** — each level reports outcomes, not transcripts; the abstraction is what keeps context bounded and accountability clear at every tier.
- **Benefits** — modular roles, bounded context windows, clear ownership, and delegation that scales beyond one context.
- **Risks** — information loss across layers (workers' context never reaches the planner) and latency from top-down serialization; hybrid designs let workers escalate exceptions directly.
- **Depth and span of control** — depth should be driven by span of control: add a level only when one node genuinely cannot supervise the next tier's work; too many levels add latency without adding capability.
- **Worked example** — a three-level wiki agent: a top-level editor delegates to section coordinators, which delegate to per-topic writers; each level reports summaries, not transcripts.
- **For mykb** — hierarchical delegation is how the curation workforce divides large passes into per-cluster batches, with promotion-readiness as the outcome contract between levels.
- **Relationship to other architectures** — a hierarchy is the top-down counterpart to the blackboard's flat shared-state coordination, and its delegation mechanics are the sub-agent delegation pattern at scale.

- **Exception escalation** — workers escalate anomalies directly to the level that can resolve them, bypassing the chain when the chain would add latency without adding judgment.
- **Accountability contract** — each level is accountable for its subtree's outcome, and the contract is written: the parent defines success criteria, the child reports against them.
- **Failure isolation** — hierarchy contains failures: a failing worker is retried or replaced by its parent without disturbing sibling subtrees, which is the resilience payoff of the tree.
## Related
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — the delegation mechanism
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — coordination patterns
- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]] — planning formalization
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — context transfer between levels
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — the flat alternative
- [[wiki/agent-systems/delegation-and-handoffs|Delegation and Handoffs]] — moving tasks between agents
