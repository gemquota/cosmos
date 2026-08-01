---
type: "concept"
title: "SFT"
description: "Supervised Fine-Tuning: training a model on labelled input-output pairs, the base stage of alignment recipes"
tags: ["sft", "fine-tuning", "alignment", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SFT

## Summary
SFT continues pretraining on curated (prompt, response) pairs — instruction data or safe completions. It is the first stage of the standard alignment recipe and the cheapest reliable way to change behaviour.

## Details
- Loss is standard next-token cross-entropy on the response portion.
- SFT teaches format, tone, and style; it does not reliably change factual knowledge.
- Quality of data dominates: small clean sets beat large noisy ones.
- Precedes RLHF/DPO in alignment pipelines and stands alone for many domain adaptations.
- RSIS3 relevance: RRP-verified outputs are a natural SFT dataset for local RSIS3 model specialization.

## Related
- [[wiki/ai-ml/instruction-tuning|Instruction Tuning]] — The instruction-following form of SFT
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — The general technique SFT instantiates
- [[wiki/ai-ml/rlhf|RLHF]] — The stage after SFT
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — What follows SFT in alignment
- [[wiki/ai-ml/catastrophic-forgetting|Catastrophic Forgetting]] — The risk SFT runs
