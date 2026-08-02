---
type: "concept"
title: "Scaffold Loops"
description: "Agent frameworks that wrap models with tools, memory, and control flow"
tags: ["scaffold", "agents", "tools", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.03629", "https://www.anthropic.com/research/building-effective-agents"]
---

# Scaffold Loops

## Summary
A scaffold is the software around a model — tools, memory, planning, and control flow — that turns a text generator into an agent. Scaffold loops are the iterative execution cycles within that scaffold (act, observe, decide), and Anthropic's 'Building Effective Agents' distinguishes workflow- and agent-style scaffolds.

## Details
- **Components** — tool calling, retrieval, short/long-term memory, and a control loop that decides the next action.
- **Workflow vs agent** — fixed pipelines (workflows) vs model-directed control (agents); most production systems mix them.
- **Capability leverage** — the same model with better scaffolding solves harder tasks; scaffold quality is a capability multiplier.
- **Safety surface** — scaffolds add attack surface: tool misuse, prompt injection via observations, and permission escalation.
- **RSIS3 relevance** — the nine-loop stack is a scaffold around Claude-like reasoning: fixed practices, gated actions, and telemetry.

## Related
- [[wiki/agent-systems/agent-bootstrapping|Agent Bootstrapping]] — scaffolds as seeds
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — tool side of scaffolding
- [[wiki/pulses/recursive-improvement-loops|Recursive Improvement Loops]] — scaffold that improves itself
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — containment
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — nested scaffolds
- [[wiki/agent-systems/planning-systems|Planning Systems]] — control flow
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
