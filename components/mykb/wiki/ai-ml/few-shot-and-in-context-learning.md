---
type: "concept"
title: "Few-Shot and In-Context Learning"
description: "Teaching models new tasks through examples placed directly in the prompt without weight updates"
tags: ["few-shot", "in-context-learning", "prompting", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2005.14165", "https://arxiv.org/abs/2301.00234"]
---

# Few-Shot and In-Context Learning

## Summary
Few-shot learning gives a model several input-output examples in the prompt so it can perform a new task immediately. It matters because it turns the prompt into the primary adaptation surface, no training required. In-context learning is how most production systems adapt generic models to specific jobs.

## Details
- **Shot counts** — zero-shot (instructions only), few-shot (2-8 examples), and many-shot (dozens, approaching fine-tune-like quality).
- **Example quality** — diverse, correct examples matter more than quantity; wrong examples poison the pattern.
- **Worked example** — classification: three labeled examples then the query; the model mirrors the label format.
- **Limits** — context-window cost, format sensitivity, and weaker long-horizon retention than fine-tuning.
- **mykb relevance** — mykb prompts embed examples from the knowledge graph to steer output formats.
- **Robustness** — test example ordering and phrasing, since in-context learning is sensitive to both.
- **Selection** — retrieve examples dynamically per query to maximize relevance rather than using a fixed set.

## Related
- [[wiki/prompt-engineering/prompt-engineering-fundamentals|Prompt Engineering Fundamentals]] — technique base
- [[wiki/ai-ml/meta-prompting|Meta-Prompting]] — meta technique
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — budget constraint
- [[wiki/ai-ml/instruction-datasets|Instruction Datasets]] — training analog
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]] — when few-shot suffices
- [[wiki/ai-ml/sentencepiece|SentencePiece]] — subword tokenization
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — context budgeting
