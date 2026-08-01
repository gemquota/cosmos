---
type: "concept"
title: "Hierarchical Task Network"
description: "Planning by decomposing abstract tasks into concrete subtask networks"
tags: ["htn", "planning", "hierarchical", "tasks"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Hierarchical Task Network

## Summary
Hierarchical task network (HTN) planning starts from an abstract task and decomposes it via methods into smaller tasks until only primitive actions remain. It matters because it captures domain knowledge about how work is normally structured, making plans practical. It is the classical formalization of goal decomposition.

## Details
- Methods map task → subtask network with constraints.
- The planner searches the space of decompositions.
- Advantages: scalable, domain-informed; limitation: methods must be authored.
- Open questions: authoring methods from LLM demonstrations.

## Related
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — the informal version of HTN
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the planning family
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — the subgoal mechanism
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — the multi-agent analog
- [[wiki/concepts/planning-as-search|Planning as Search]] — the search framing
