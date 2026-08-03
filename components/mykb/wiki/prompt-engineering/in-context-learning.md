---
type: "concept"
title: "In-Context Learning"
description: "Task adaptation that happens at inference time from examples and instructions in the prompt, without weight updates"
tags: ["in-context-learning", "llm", "prompting"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# In-Context Learning

## Summary
In-context learning is the ability of a model to adapt its behaviour from the examples and instructions present in its context window — no weight updates. Few-shot and zero-shot prompting are its two practical expressions, and it is the phenomenon that makes prompt engineering possible.

## Details
- Mechanism: examples and instructions in the prompt shape the model's output distribution at inference time; the model generalizes the pattern from the provided exemplars; this contrasts with training-time adaptation — no gradient steps, no persistent memory of the task beyond the session.
- Concrete example: a few-shot prompt shows three article-summary pairs and the model follows the format for the fourth; a zero-shot instruction describes the task and the model complies; a system prompt exploits in-context learning persistently by establishing role and rules for the whole session.
- Failure modes: exemplars that are inconsistent or mislabeled, teaching the wrong pattern; context overflow diluting the signal; few-shot examples that work on one model and fail on another; the model following example format over explicit instructions; relying on in-context learning for skills the model lacks at any scale.
- Tradeoffs: in-context learning gives task adaptation without retraining — cheap and flexible — at the cost of context budget and quality bounds set by pretraining; the alternative, fine-tuning, is expensive and persistent; the mature pattern is in-context learning for routine adaptation plus fine-tuning where hard skills are required.
- Operational notes: curate exemplars carefully, eval few-shot vs zero-shot, and treat context as a budget to manage.
- RSIS3 relevance: L1 loops rely on in-context learning for every pulse; mykb supplies the examples — the quality of those exemplars bounds loop performance.

## Related
- [[wiki/prompt-engineering/few-shot-prompting|Few-Shot Prompting]] — The exemplar-driven form of in-context learning
- [[wiki/prompt-engineering/zero-shot-prompting|Zero-Shot Prompting]] — The instruction-only form
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — System prompts exploit in-context learning persistently
- [[wiki/prompt-engineering/emergent-abilities|Emergent Abilities]] — The scaling phenomenon behind in-context learning
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — Training that strengthens in-context instruction following
