---
type: "concept"
title: "In-Context Learning"
description: "Task adaptation that happens at inference time from examples and instructions in the prompt, without weight updates"
tags: ["in-context-learning", "llm", "prompting"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# In-Context Learning

## Summary
In-context learning is the ability of a model to adapt its behaviour from the examples and instructions present in its context window. Few-shot and zero-shot prompting are its two practical expressions, and it is the phenomenon that makes prompt engineering possible.

## Details
- Emerges strongly at scale; GPT-3's paper framed it as a third paradigm alongside fine-tuning.
- Contrasts with training-time adaptation: no gradient steps, no persistent memory of the task.
- Quality is bounded by the model's pretraining; hard skills still require fine-tuning.
- RSIS3 relevance: L1 loops rely on in-context learning for every pulse; mykb supplies the examples.

## Related
- [[wiki/prompt-engineering/few-shot-prompting|Few-Shot Prompting]] — The exemplar-driven form of in-context learning
- [[wiki/prompt-engineering/zero-shot-prompting|Zero-Shot Prompting]] — The instruction-only form
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — System prompts exploit in-context learning persistently
- [[wiki/prompt-engineering/emergent-abilities|Emergent Abilities]] — The scaling phenomenon behind in-context learning
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — Training that strengthens in-context instruction following
