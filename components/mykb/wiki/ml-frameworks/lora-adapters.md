---
type: "concept"
title: "LoRA Adapters"
description: "The small trainable matrices that LoRA adds to each layer for parameter-efficient tuning"
tags: ["lora-adapters", "lora", "adapters", "fine-tuning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# LoRA Adapters

## Summary
The small trainable matrices that LoRA adds to each layer for parameter-efficient tuning

## Details
- Each adapter stores low-rank A and B matrices per layer.
- Adapters are portable artifacts, swappable at runtime.
- Multiple adapters enable multi-tenant serving.
- Merging folds adapters back into base weights.

## Related
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — training method
- [[wiki/ml-frameworks/qlora-adapter-merging|QLoRA and Adapter Merging]] — quantized adapters
- [[wiki/ml-frameworks/model-merging|Model Merging]] — combining adapters
- [[wiki/ml-frameworks/peft-methods|PEFT Methods]] — tooling
- [[wiki/ml-frameworks/model-composition|Model Composition]] — multi-adapter serving
