---
type: "concept"
title: "SFT"
description: "Supervised Fine-Tuning: training a model on labelled input-output pairs, the base stage of alignment recipes"
tags: ["sft", "fine-tuning", "alignment", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# SFT

## Summary
SFT continues pretraining on curated (prompt, response) pairs — instruction data or safe completions. It is the first stage of the standard alignment recipe and the cheapest reliable way to change behaviour.

## Details
- **Mechanism** — the base model is trained with standard next-token cross-entropy, but the loss is computed only on the response portion of each (prompt, response) pair; the prompt conditions the model while the response teaches the target behaviour, format, and style.
- **What it changes** — SFT teaches format, tone, and style — how to answer, when to refuse, how to structure output — but it does not reliably change factual knowledge or reasoning ability; the model reorganizes what pretraining already stored rather than acquiring new facts.
- **Data quality dominates** — small clean sets beat large noisy ones: a few thousand high-quality, diverse demonstrations with consistent formatting outperform millions of scraped chat logs, and duplicated prompts cause overfitting to narrow phrasings.
- **Failure modes** — overfitting to the fine-tuning distribution (losing generality), catastrophic forgetting of pretraining abilities when the dataset is narrow or the learning rate too high, and mode collapse to terse or repetitive styles when demonstrations lack diversity.
- **Placement in pipelines** — SFT precedes RLHF/DPO in the alignment recipe and stands alone for many domain adaptations; the SFT model also becomes the reference policy that KL constraints anchor to in later RL stages, so a weak SFT stage caps everything downstream.
- **RSIS3 relevance** — RRP-verified outputs are a natural SFT dataset for local RSIS3 model specialization: each accepted specification and its validated critique pair form labelled demonstrations, letting the system fine-tune a small model on its own verified output distribution rather than generic instruction data.

## Related
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — The instruction-following form of SFT
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — The general technique SFT instantiates
- [[wiki/ai-ml/rlhf|RLHF]] — The stage after SFT
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — What follows SFT in alignment
- [[wiki/ai-ml/catastrophic-forgetting|Catastrophic Forgetting]] — The risk SFT runs
