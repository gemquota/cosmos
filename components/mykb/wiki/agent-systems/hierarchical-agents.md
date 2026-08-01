---
type: "concept"
title: "Hierarchical Agents"
description: "Agents organized in a tree where higher levels delegate to lower ones"
tags: ["hierarchical", "delegation", "multi-agent", "architecture"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Hierarchical Agents

## Summary
Hierarchical agents arrange roles in a tree: a top-level planner delegates subtasks to mid-level coordinators, which delegate further to workers. It matters because it scales coordination and matches organizational structure. RSIS3's executive planner plus sub-agents is a shallow hierarchy.

## Details
- Each level abstracts the level below: workers report outcomes, not process.
- Benefits: modular roles, bounded context, clear accountability.
- Risks: information loss and latency across layers.
- Open questions: optimal depth and span of control.

## Related
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — the delegation mechanism
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — the broader pattern
- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]] — planning analog
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — moving work between levels
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — the flat alternative
