---
type: "concept"
title: "Supervised Fine-Tuning"
description: "Training a model on input-output pairs for task mastery"
tags: ["sft", "fine-tuning", "training", "supervised"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/fine-tuning", "https://arxiv.org/abs/2009.01325"]
---

# Supervised Fine-Tuning

## Summary
Supervised fine-tuning (SFT) trains a pretrained model on (input, output) examples, teaching it task behavior directly. It is the first stage of most post-training pipelines, converting a base model into an instruction-following one. SFT sets the behavioral envelope that later RLHF or DPO refines.

## Details
- **Data** — instruction datasets with diverse tasks and high-quality completions; a few thousand to tens of thousands of examples typically suffice.
- **Training** — standard cross-entropy over outputs; LoRA or full fine-tuning both work, with compute and quality tradeoffs.
- **Risks** — overfitting narrows generality; contamination and duplicated data inflate eval scores.
- **Worked example** — a code model is SFT on 30k (issue → patch) pairs, then evaluated on held-out repo tasks before RLHF.
- **Position in pipeline** — pretraining → SFT → preference optimization → optional RL; each stage has a different objective and data need.
- **mykb relevance** — SFT, fine-tuning, and instruction tuning are existing mykb topics.

## Related
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — instruction tuning stage
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — fine-tuning umbrella
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — existing fine-tuning concept
- [[wiki/ai-ml/instruction-datasets|Instruction Datasets]] — SFT data
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — efficient SFT
- [[wiki/ai-ml/fine-tuning-data-curation|Fine-Tuning Data Curation]] — curating SFT data
- [[wiki/ai-ml/reinforcement-learning-from-human-feedback|Reinforcement Learning from Human Feedback]] — the next stage
- [[wiki/ai-ml/sft|SFT]] — existing SFT concept
