---
type: "concept"
title: "Multi-Step Reasoning"
description: "Prompts and methods that decompose problems into intermediate reasoning steps to improve complex answers"
tags: ["reasoning", "chain-of-thought", "prompting", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Multi-Step Reasoning

## Summary
Multi-step reasoning makes a model show or construct intermediate steps before the final answer, which sharply improves performance on math, logic, and planning tasks. It is implemented by prompting (chain-of-thought) and by tool use (calculation, search) that externalizes the steps.

## Details
- Mechanism: chain-of-thought prompting (Wei et al., 2022) asks the model to reason step by step, converting hidden computation into visible intermediate tokens that improve accuracy; reasoning can also be externalized — writing notes, running code, or querying tools turns internal steps into verifiable artifacts.
- Concrete example: a math word problem solved via explicit steps (translate, set up equation, solve, verify); an agent planning a task writes a plan, executes tool calls, and revises based on results; a prompt mandates showing work so a reviewer can check each step.
- Failure modes: costs mount — more tokens, more latency, longer error chains where one wrong step propagates; models that fabricate confident-but-wrong intermediate steps; prompts that force steps where none are needed, degrading simple tasks; step output leaking into final answers when not separated.
- Tradeoffs: stepwise reasoning trades tokens and latency for accuracy on complex tasks; the alternative, direct answers, is fast and often wrong on hard problems; the mature pattern is chain-of-thought or tool-assisted reasoning where complexity justifies it, with evals measuring the trade.
- Operational notes: eval reasoning outputs separately, cap step counts, and verify externalized steps against their tools.
- RSIS3 relevance: RRP's critique-refine cycles are multi-step reasoning applied to prompts themselves — the same decompose-then-verify structure.

- Separate reasoning output from the final answer in the prompt so steps inform, not pollute, the conclusion.
## Related
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — The engineered form of stepwise reasoning
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Externalizing steps as tool calls
- [[wiki/prompt-engineering/agent-state|Agent State]] — Tracking intermediate reasoning state
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — System prompts can mandate stepwise output
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Reasoning quality needs its own evals
