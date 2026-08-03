---
type: "concept"
title: "Multi-Agent Orchestration"
description: "Coordinating several agents with distinct roles into one coherent system"
tags: ["multi-agent", "orchestration", "coordination", "agents", "architecture"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2308.08155"]
---

# Multi-Agent Orchestration

## Summary
Multi-agent orchestration is the coordination of multiple agents — specialists, workers, critics — that together solve problems no single agent handles well. It matters because role separation (planner vs. coder vs. reviewer) improves modularity and accountability, and because naive handoffs introduce coordination overhead. Frameworks like AutoGen show the pattern: agents converse through structured protocols.

## Details
- **Topologies**: orchestrator-worker, peer debate, pipeline, and blackboard (shared state) are the common shapes.
- **Handoffs** transfer control between agents with explicit context so nothing is lost.
- **Debate and critique** improve quality when agents disagree or review each other's output.
- Costs: token amplification, duplicated context, and failure cascades require careful scoping.
- RSIS3 uses sub-agent delegation (spawn_agent/invoke_agent) for isolated subtasks rather than always-on multi-agent chatter.
- Worked example: a planner agent decomposes a task, a coder agent implements it, and a reviewer agent gates the result.

## Related

- [[wiki/llm-agents/debate-agents|Debate Agents]] — agents that critique each other's answers
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — querying specialist agents on demand
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — tree-structured role delegation
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — shared-state coordination
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — the transfer mechanism between agents
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — research on multi-agent memory systems
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the shared knowledge substrate agents coordinate over