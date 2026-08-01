---
type: "concept"
title: "Multi-Step Reasoning"
description: "Prompts and methods that decompose problems into intermediate reasoning steps to improve complex answers"
tags: ["reasoning", "chain-of-thought", "prompting", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Multi-Step Reasoning

## Summary
Multi-step reasoning makes a model show or construct intermediate steps before the final answer, which sharply improves performance on math, logic, and planning tasks. It is implemented by prompting (chain-of-thought) and by tool use (calculation, search).

## Details
- Chain-of-thought prompting (Wei et al., 2022) asks the model to reason step by step; 'Let's think step by step' is the folk version.
- Reasoning can be externalized: writing notes, running code, or querying tools converts internal steps into verifiable artifacts.
- Costs: more tokens, more latency, and longer error chains — one wrong step propagates.
- RSIS3 relevance: RRP's critique-refine cycles are multi-step reasoning applied to prompts themselves.

## Related
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — The engineered form of stepwise reasoning
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Externalizing steps as tool calls
- [[wiki/prompt-engineering/agent-state|Agent State]] — Tracking intermediate reasoning state
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — System prompts can mandate stepwise output
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Reasoning quality needs its own evals
