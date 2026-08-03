---
type: "concept"
title: "Hierarchical Task Network"
description: "Planning by decomposing abstract tasks into concrete subtask networks"
tags: ["htn", "planning", "hierarchical", "tasks"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Hierarchical Task Network

## Summary
Hierarchical task network (HTN) planning starts from an abstract task and decomposes it via methods into smaller tasks until only primitive actions remain. It matters because it captures domain knowledge about how work is normally structured, making plans practical. It is the classical formalization of goal decomposition.

## Details
- Methods map task → subtask network with constraints. A method is an authored recipe: "to build a house, first lay the foundation, then frame, then roof — with the constraint that framing starts after foundation completes". Each method decomposes one abstract task into a partially ordered network of subtasks, and those subtasks may themselves be abstract, so the method library defines a hierarchy of expertise down to primitive actions that the planner can execute directly.
- The planner searches the space of decompositions. Starting from the top-level task, it repeatedly chooses a method for the current abstract task, expanding it into subtasks, until every branch ends in primitives. The search is over which methods to apply and in what order, guided by the constraints — and because the method library encodes how work is normally structured, the search space is dramatically smaller than the raw state space that a general planner would explore.
- Advantages: scalable, domain-informed; limitation: methods must be authored. HTN planning inherits its power from its knowledge: a good method library lets a planner handle problems that would swamp STRIPS-style search, and plans come out naturally hierarchical and explainable. The cost is that the library is hand-authored — building it requires exactly the knowledge-engineering effort that made expert systems expensive — and the planner is helpless on any task outside the library's coverage, with no graceful fallback when methods are missing.
- Open questions: authoring methods from LLM demonstrations. If methods can be induced from observed behavior or LLM-generated plans, the knowledge-engineering bottleneck disappears — but then the hierarchy inherits the LLM's errors, and the planner's auditability, the main reason to use HTN in the first place, depends on how the induced methods are validated.
- RSIS3 relevance: the loop structure is a task hierarchy — an improvement pass decomposes into retrieval, experiment, verification, and consolidation, each with its own methods and constraints — and the practices document is the method library that constrains how each subtask may be carried out.

## Related
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — the informal version of HTN
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the planning family
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — the subgoal mechanism
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — the multi-agent analog
- [[wiki/concepts/planning-as-search|Planning as Search]] — the search framing
