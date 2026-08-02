---
type: "concept"
title: "Self-Ask Technique"
description: "Prompting method where the model asks and answers follow-up questions before the final answer"
tags: ["self-ask", "prompting", "reasoning", "questions"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Self-Ask Technique

## Summary
Prompting method where the model asks and answers follow-up questions before the final answer

## Details
- Explicit intermediate questions decompose multi-part problems.
- Improves recall of needed facts and reasoning steps.
- Closely related to query-decomposition in RAG.
- A predecessor of agentic planning patterns.

## Related
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — base technique
- [[wiki/prompt-engineering/least-to-most-prompting|Least-to-Most Prompting]] — ordering variant
- [[wiki/ai-ml/query-decomposition|Query Decomposition]] — retrieval analog
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — agentic evolution
- [[wiki/prompt-engineering/step-back-prompting|Step-Back Prompting]] — abstraction variant
