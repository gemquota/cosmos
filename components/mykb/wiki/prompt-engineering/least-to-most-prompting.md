---
type: "concept"
title: "Least-to-Most Prompting"
description: "Teaching a model to solve problems by first solving simpler subproblems in increasing difficulty"
tags: ["least-to-most", "prompting", "decomposition", "reasoning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Least-to-Most Prompting

## Summary
Teaching a model to solve problems by first solving simpler subproblems in increasing difficulty

## Details
- Problems are decomposed and solved in order of increasing difficulty.
- Earlier solutions inform later steps.
- Strong on compositional and multi-step reasoning.
- Related to curriculum-learning-llm in training.

## Related
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — base
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — question variant
- [[wiki/ai-ml/curriculum-learning-llm|Curriculum Learning for LLMs]] — training analog
- [[wiki/prompt-engineering/program-of-thoughts|Program of Thoughts]] — structured variant
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — agentic version
