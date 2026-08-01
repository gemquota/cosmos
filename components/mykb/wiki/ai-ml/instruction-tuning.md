---
type: "concept"
title: "Instruction Tuning"
description: "Fine-tuning a pretrained model on instruction-response pairs so it follows natural-language instructions, including for unseen tasks"
tags: ["instruction-tuning", "fine-tuning", "zero-shot", "alignment"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2108.07258", "https://arxiv.org/abs/2202.12837"]
---

# Instruction Tuning

## Summary
Instruction tuning trains a base model on (instruction, response) pairs, teaching it to answer natural-language requests. FLAN showed that a modest number of templated tasks generalizes to held-out tasks, and the recipe is the foundation of every chat assistant released since.

## Details
- FLAN (2108.07258) tuned LaMDA-PT on 62 NLP tasks and observed strong zero-shot transfer to unseen task families.
- T0 (2202.12837) scaled the idea across many public datasets with prompted multi-task training, showing cross-task generalization curves.
- Instruction tuning is usually the SFT stage that precedes RLHF; it converts a next-token predictor into an instruction follower.
- Data design matters: diverse task templates, natural instructions, and explicit answer formats generalize better than uniform chat logs.
- The effect is behavioural: instruction-tuned models still lack knowledge they were not trained on, which is why retrieval complements them.
- RSIS3 relevance: instruction pairs produced during RRP sessions are natural SFT data; mykb can curate them for periodic local fine-tunes.

## Related
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — Instruction tuning is the canonical fine-tuning recipe
- [[wiki/prompt-engineering/zero-shot-prompting|Zero-Shot Prompting]] — Instruction tuning is what makes zero-shot work
- [[wiki/ai-ml/sft|SFT]] — Instruction tuning is supervised fine-tuning in practice
- [[wiki/ai-ml/rlhf|RLHF]] — The alignment stage that follows instruction tuning
- [[wiki/ai-ml/model-cards|Model Cards]] — Models document their instruction-tuning data
- [[wiki/concepts/mykb-implementation-report|mykb Implementation Report: 6-Phase Buildout — Actual State, Architecture, and Results]] — Implemented pipelines for curating instruction data
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Instruction pairs are wiki-curated knowledge
