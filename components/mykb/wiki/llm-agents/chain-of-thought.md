---
type: "concept"
title: "Chain of Thought"
description: "Prompting models to reason step by step before answering"
tags: ["chain-of-thought", "reasoning", "prompting", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Chain of Thought

## Summary
Chain of thought elicits intermediate reasoning steps from a model before the final answer, improving performance on multi-step problems. It matters because it makes reasoning visible, auditable, and partially correctable. It is the baseline for most reasoning-adjacent agent techniques.

## Details
- Effect strongest on arithmetic, logic, and planning tasks.
- Exposes the reasoning trace for inspection and debugging.
- Cost: more tokens, and traces can be wrong-but-plausible.
- Open questions: when CoT helps versus adds noise.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — CoT as lightweight planning
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — aggregating multiple CoT traces
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — CoT with branching and search
- [[wiki/llm-agents/reflexion|Reflexion]] — critiquing the trace
- [[wiki/concepts/metacognition|Metacognition]] — reasoning about the reasoning
