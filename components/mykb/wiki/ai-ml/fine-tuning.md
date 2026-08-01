---
type: "concept"
title: "Fine-Tuning"
description: "Updating a pretrained model's weights on a small labelled dataset to specialize it for a task or domain"
tags: ["fine-tuning", "transfer-learning", "llm", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/fine-tuning", "https://arxiv.org/abs/2104.09864"]
---

# Fine-Tuning

## Summary
Fine-tuning continues training from a pretrained checkpoint on task-specific data, adapting the weights instead of the prompt. It beats prompting when the skill is hard to describe, the data distribution is stable, and latency or token cost per call must shrink.

## Details
- Parameter-efficient variants (LoRA and friends) train a small set of adapter weights, cutting memory and cost while approaching full fine-tuning quality.
- OpenAI's fine-tuning guide covers preparing datasets, creating jobs, and evaluating checkpoints on a held-out test set.
- Fine-tuning is a sampling-distribution shift, not a facts update: it teaches behaviour, and it can still hallucinate or drift from base knowledge.
- Data quality dominates: a few hundred excellent examples usually beat thousands of noisy ones; duplicates and label noise cause overfitting.
- Risk: catastrophic forgetting of general abilities — mitigated by mixing general data or using LoRA with low rank.
- RSIS3 relevance: L2 improvement loops can fine-tune small local models (via Llama.cpp/Ollama) on mykb-curated instruction pairs, closing the loop between memory and behaviour.

## Related
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — The specialized fine-tuning recipe for instruction-following
- [[wiki/ai-ml/rlhf|RLHF]] — The preference-based successor stage after fine-tuning
- [[wiki/ai-ml/sft|SFT]] — Supervised fine-tuning is the base stage of the recipe
- [[wiki/ai-ml/catastrophic-forgetting|Catastrophic Forgetting]] — The main fine-tuning failure mode
- [[wiki/ai-ml/dpo|DPO]] — A preference-tuning alternative to RLHF
- [[wiki/testing/eval-sets|Eval Sets]] — Held-out evals gate fine-tune checkpoints
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb-curated data feeds specialization loops
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Curated training data flows through the wiki
