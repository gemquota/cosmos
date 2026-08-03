---
type: "concept"
title: "Building Effective Agents"
description: "Anthropic's December 2024 guidance: workflows vs agents, composable patterns, and three design principles"
tags: ["agents", "workflows", "anthropic", "augmented-llm", "aci"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://www.anthropic.com/engineering/building-effective-agents"]
---

# Building Effective Agents

## Summary
Anthropic's December 2024 post distills what they learned from dozens of teams building LLM agents: the most successful implementations use simple, composable patterns rather than complex frameworks. The central distinction is between workflows — LLMs and tools orchestrated through predefined code paths — and agents — LLMs that dynamically direct their own processes and tool usage. The recommendation is to find the simplest solution and only add complexity when it demonstrably improves outcomes.

## Details
- **Workflows vs agents** — workflows offer predictability for well-defined tasks; agents fit open-ended problems where the number of steps can't be predicted and flexibility is needed at scale.
- **Cost tradeoff** — agentic systems trade latency and cost for task performance; for many applications a single optimized LLM call with retrieval and in-context examples is enough.
- **Frameworks** — simplify low-level tasks but can obscure prompts and responses, making debugging harder; start with LLM APIs directly and understand any framework's internals before trusting it.
- **The augmented LLM** — the building block is an LLM enhanced with retrieval, tools, and memory; tailoring these capabilities and documenting their interface well is the core work.
- **Workflow patterns** — prompt chaining (fixed sequential steps with gates), routing (classify then dispatch), parallelization (independent subtasks), orchestrator-workers (dynamic decomposition), and evaluator-optimizer (generate, critique, refine).
- **Agents** — typically just LLMs using tools based on environmental feedback in a loop; ground truth from tool results at each step is crucial, with stopping conditions like max iterations for control.
- **Three principles** — maintain simplicity; prioritize transparency by showing the agent's planning steps; carefully craft the agent-computer interface (ACI) through thorough tool documentation and testing.

## Related
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — the workflow layer
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]] — Anthropic's applied system
- [[wiki/llm-agents/agentic-loops|Agentic Loops]] — the loop definition
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — curating what the model sees
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — orchestrator patterns
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- Anthropic, "Building Effective AI Agents", Dec 2024 — https://www.anthropic.com/engineering/building-effective-agents
