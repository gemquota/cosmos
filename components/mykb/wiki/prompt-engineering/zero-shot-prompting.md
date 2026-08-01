---
type: "concept"
title: "Zero-Shot Prompting"
description: "Prompting a model to perform a task with no examples, relying on instruction-following from pretraining and instruction tuning"
tags: ["prompt-engineering", "zero-shot", "instruction-following", "prompting"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2109.01652", "https://platform.openai.com/docs/guides/prompt-engineering"]
---

# Zero-Shot Prompting

## Summary
Zero-shot prompting asks the model to do a task from instructions alone, with no exemplars. Modern instruction-tuned models make it surprisingly strong, and it is the default mode for chat-style APIs where the user message is the whole task specification.

## Details
- Relies on instruction following learned during pretraining and reinforced by instruction tuning, rather than on in-context exemplars.
- 'Finetuned Language Models Are Zero-Shot Learners' and the FLAN line of work showed that instruction tuning dramatically improves zero-shot generalization across held-out tasks.
- Zero-shot prompts should be explicit about the task, the input schema, the output schema, and edge cases; ambiguity is the main failure source.
- Weak against unusual formats and domain jargon — those are exactly the cases where few-shot or retrieval prompting wins.
- Cost and latency advantage: one round trip, minimal tokens, easy to template and scale across many calls.
- RSIS3 relevance: L1 action loops default to zero-shot prompts and escalate to few-shot or tool-augmented prompts when evaluation scores drop.

## Related
- [[wiki/prompt-engineering/few-shot-prompting|Few-Shot Prompting]] — The escalation path when zero-shot output quality is insufficient
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — Zero-shot behaviour is largely set by the system prompt
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — The training method that powers zero-shot instruction following
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — The inference-time phenomenon zero-shot relies on
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Zero-shot baselines are the first row of every eval run
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb analysis tracks which zero-shot templates work per domain
- [[wiki/prompt-engineering/emergent-abilities|Emergent Abilities]] — Emergence makes zero-shot tasks viable at scale
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Research base for instruction-following methods
