---
type: "concept"
title: "QLoRA and Adapter Merging"
description: "Quantized LoRA training and the practice of merging adapters into base weights for deployment"
tags: ["qlora", "quantization", "lora", "fine-tuning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# QLoRA and Adapter Merging

## Summary
Quantized LoRA training and the practice of merging adapters into base weights for deployment

## Details
- QLoRA trains LoRA adapters on a 4-bit quantized base model.
- Reduces fine-tuning VRAM while retaining most quality.
- Merging adapters yields a standalone full-precision-ish model.
- Enables fine-tuning on consumer GPUs.

## Related
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — unquantized baseline
- [[wiki/ml-frameworks/lora-adapters|LoRA Adapters]] — adapter concept
- [[wiki/ai-ml/model-quantization|Model Quantization]] — 4-bit base
- [[wiki/ml-frameworks/model-merging|Model Merging]] — merge mechanics
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — practical path
