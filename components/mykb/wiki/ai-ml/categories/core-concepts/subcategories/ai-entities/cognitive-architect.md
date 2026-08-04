---
type: "entity"
title: "Cognitive Architect"
description: "Referenced in session 019f182d"
tags: ["entity", "android", "api", "ast", "auth", "aws"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# Cognitive Architect

## Summary
A cognitive architect designs the structures that give an AI system its reasoning abilities: perception, memory, planning, and control loops composed into a coherent architecture. The concept matters because capability is not just model choice — it is how components are arranged. Cognitive architecture thinking turns a single model call into an organized, inspectable mind. Architecture is the discipline that turns model capability into dependable behavior.

## Details
- **Definition** — the cognitive architect is the designer role that specifies components such as memory systems, planning modules, tool interfaces, and feedback loops for an agent.
- **Components** — typical building blocks include perception, short-term and long-term memory, goal representation, planning, action selection, and self-monitoring.
- **Design trade-offs** — architectures balance autonomy against controllability, reactivity against deliberation, and generality against specialization.
- **Patterns** — common arrangements include the perception-action loop, hierarchical planners, subsumption-style layers, and hybrid reactive-deliberative designs.
- **Relation to LLM agents** — modern agents instantiate classic cognitive architecture ideas with models as the reasoning core and tools as the effectors.
- **Worked example** — an architect designs a research agent as: a planner that decomposes questions, a retrieval memory, a synthesis module, and a verification loop.
- **Failure modes** — over-engineered architectures add latency and fragility, while under-specified ones lack the structure needed for reliability.
- **Evaluation** — architectures are judged on task performance, robustness, resource use, and how inspectable and controllable behavior remains.
- **Practical relevance** — the cognitive architect's choices determine whether a system can learn, remember, and correct itself, which is the core of recursive self-improvement.
- **Abstraction** — clean component boundaries let each piece be tested and replaced independently.
- **Tension** — simpler architectures are easier to debug but less capable; the architect manages this trade.
- **Failure example** — bolting memory onto an agent without integration testing produces confident, inconsistent behavior.

## Related
- [[wiki/agent-systems/agent-memory-systems|Agent Memory Systems]] — the memory component of an architecture
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning and goal decomposition
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — the reactive core
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — self-monitoring components
- [[wiki/agent-systems/agent-loop|The Agent Loop]] — the runtime cycle architectures organize
