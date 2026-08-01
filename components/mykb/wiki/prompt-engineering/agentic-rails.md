---
type: "concept"
title: "Agentic Rails"
description: "Execution-level guardrails that constrain what an agent may do: allowed tools, permissions, budgets, and action policies"
tags: ["agentic-rails", "guardrails", "agents", "safety"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Agentic Rails

## Summary
Agentic rails are policies enforced around an agent's actions rather than its text — which tools it may call, what arguments are allowed, how many steps it gets, and what requires human approval. They are the practical safety layer for autonomous systems.

## Details
- Implementations: allow/deny tool lists, argument validators, step caps, rate limits, and approval gates for risky actions.
- Rails protect against both attacks and accidents: runaway loops, destructive commands, and cost blowups.
- Design principle: least privilege — an agent should only see and use the tools the task requires.
- RSIS3 relevance: the L1 loop should treat every tool invocation as passing through a rail policy that mykb logs.

## Related
- [[wiki/ai-ml/guardrails|Guardrails]] — The umbrella runtime-safety concept
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — The actions rails govern
- [[wiki/prompt-engineering/tool-selection|Tool Selection]] — Selection happens inside rail constraints
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — Rails contain injection-driven tool misuse
- [[raw/archive/session-artifacts-2026-07/topics/security|security — Action policy as security control
