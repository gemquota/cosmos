---
type: "concept"
title: "Low-Rank Adaptation (LoRA)"
description: "Parameter-efficient fine-tuning that trains small low-rank update matrices instead of full weights"
tags: ["lora", "fine-tuning", "efficiency", "adapters"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Low-Rank Adaptation (LoRA)

## Summary
Parameter-efficient fine-tuning that trains small low-rank update matrices instead of full weights

## Details
- Freezes base weights and learns low-rank delta matrices.
- Cuts trainable parameters by orders of magnitude.
- Adapters can be swapped and merged at serve time.
- The default modern fine-tuning method.

## Related
- [[wiki/ml-frameworks/lora-adapters|LoRA Adapters]] — adapter mechanics
- [[wiki/ml-frameworks/peft-methods|PEFT Methods]] — method family
- [[wiki/ml-frameworks/qlora-adapter-merging|QLoRA and Adapter Merging]] — quantized variant
- [[wiki/ml-frameworks/model-merging|Model Merging]] — adapter combination
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — application area
