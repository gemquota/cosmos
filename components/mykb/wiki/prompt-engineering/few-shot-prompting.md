---
type: "concept"
title: "Few-Shot Prompting"
description: "Providing a small number of input-output exemplars in the prompt to condition the model's behaviour at inference time"
tags: ["prompt-engineering", "few-shot", "in-context-learning", "prompting"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2005.14165", "https://www.promptingguide.ai/techniques/fewshot"]
---

# Few-Shot Prompting

## Summary
Few-shot prompting supplies several input-output examples inside the prompt so the model conditions on them at inference time without any weight update. It was one of the core results of the GPT-3 paper, which showed that a handful of exemplars could unlock tasks like translation, QA, and arithmetic.

## Details
- Exemplars demonstrate the input format, expected output shape, and reasoning style all at once, which is more sample-efficient than a prose description alone.
- GPT-3 ('Language Models are Few-Shot Learners') showed task performance climbing with the number of demonstrations, saturating well below fine-tuning quality but requiring zero gradient steps.
- Example selection matters: similar, correctly-labelled, and well-ordered exemplars outperform random ones; a bad label among the shots can poison the pattern.
- Label mapping is a known failure mode — a small number of semantically irrelevant examples can flip a model's predictions.
- Few-shot is the standard complement to system prompts: the system prompt sets rules, the shots demonstrate them.
- RSIS3 relevance: mykb's wiki stores exemplars per task family, so a session can retrieve the best few shots before invoking an LLM.

## Related
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — Few-shot exemplars are usually embedded under a system prompt
- [[wiki/prompt-engineering/zero-shot-prompting|Zero-Shot Prompting]] — The no-examples baseline that few-shot compares against
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — The underlying phenomenon that few-shot exploits
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — Decomposing tasks into stages, each with its own shots
- [[wiki/testing/eval-sets|Eval Sets]] — Few-shot exemplars are often curated from eval-set examples
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Research base for storing and retrieving exemplars in a wiki
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Exemplars become reusable wiki knowledge
- [[wiki/prompt-engineering/emergent-abilities|Emergent Abilities]] — Scale-linked capabilities few-shot relies on
