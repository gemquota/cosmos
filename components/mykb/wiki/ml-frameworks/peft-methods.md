---
type: "concept"
title: "PEFT Methods"
description: "Parameter-efficient fine-tuning techniques including LoRA, prefix tuning, and adapters"
tags: ["peft", "fine-tuning", "efficiency", "adapters"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# PEFT Methods

## Summary
Parameter-efficient fine-tuning techniques including LoRA, prefix tuning, and adapters

## Details
- PEFT updates tiny parameter subsets or inserted modules.
- Reduces memory, storage, and training cost.
- Preserves base model quality across many tasks.
- The Hugging Face PEFT library standardizes these.

## Related
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — flagship method
- [[wiki/ml-frameworks/qlora-adapter-merging|QLoRA and Adapter Merging]] — quantization combo
- [[wiki/ml-frameworks/lora-adapters|LoRA Adapters]] — artifact type
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — use case
- [[wiki/ai-ml/catastrophic-forgetting-mitigation|Catastrophic Forgetting Mitigation]] — stability benefit
