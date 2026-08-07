---
type: "concept"
title: "Sub-Agent Delegation"
description: "Spawning dedicated agents for isolated subtasks and collecting their results"
tags: ["delegation", "sub-agents", "orchestration", "agents", "parallelism"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://openai.github.io/openai-agents-python/"]
---

# Sub-Agent Delegation

## Summary
Sub-agent delegation is the pattern where a main agent hands a well-scoped subtask to a fresh agent with its own context, tools, and budget, then collects the result. It matters because it isolates context, avoids distracting the main thread, and parallelizes independent work. RSIS3 exposes this through spawn_agent and invoke_agent tools.

## Details
- **When to delegate**: long-running, self-contained, or context-heavy subtasks that would pollute the main context.
- **Contract**: the delegation includes a clear objective, input data, allowed tools, and a success/failure result format.
- **Context isolation** is the main win: the sub-agent's context dies with it.
- **Handoffs**: delegation either returns a result or transfers control permanently, depending on the protocol.
- RSIS3 uses sub-agents for isolated tasks like research sweeps and file-scoped refactors, with results logged for traceability.
- Worked example: a planner agent delegates dependency upgrades to three sub-agents, one per package, and merges their patches.

- **Result contract** — delegations define a structured result format (status, artifacts, errors), so the main agent can consume outcomes without parsing prose.
- **Failure isolation** — a sub-agent crash terminates only that sub-agent; the main agent observes the failure, logs it, and can re-spawn with fresh context.
- **Oversight** — destructive sub-agent actions still pass through the same permission and approval gates; delegation is not an escape hatch from safety controls.
- **Cost accounting** — each delegation spends its own budget and context; the main agent should track aggregate sub-agent spend to avoid surprise token bills.

- **Measurement** — delegation quality is measured by outcome (did the subtask succeed), isolation (did a failure stay contained), and overhead (tokens and latency spent on the handoff); all three are tracked per delegation.

## Related

- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — the tree structure delegation creates
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — the transfer contract between agents
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — delegation as a question to a specialist
- [[wiki/llm-agents/agent-personas|Agent Personas]] — role framing for delegated work
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — shared knowledge passed during delegation