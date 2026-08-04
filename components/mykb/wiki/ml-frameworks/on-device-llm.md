---
type: "concept"
title: "On-Device LLMs"
description: "Language models that run locally on phones, laptops, or embedded hardware"
tags: ["on-device", "llm", "edge", "privacy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# On-Device LLMs

## Summary

On-device LLMs are language models that run entirely on local hardware such as phones, laptops, or embedded systems, with no network dependency for inference. Advances in quantization, small-model design, and efficient runtimes have made them practical. On-device LLMs matter because they offer privacy, offline availability, low latency, and predictable cost for personal and edge applications. Progress is driven by hardware and runtime advances as much as by model design, so the field evolves as devices get faster.

## Details

- **Definition** — an on-device LLM performs generation locally, loading weights from device storage and computing outputs on local processors.
- **Hardware realities** — phones and laptops offer limited RAM and compute, so models are typically small, quantized, and optimized for the specific chip.
- **Quantization** — 4-bit and 8-bit weight compression reduces memory footprint by severalfold while retaining most capability.
- **Runtimes** — projects like llama.cpp and ONNX Runtime provide the kernels and execution engines that make local inference fast.
- **Privacy** — local processing keeps prompts and outputs on the device, supporting data minimization and compliance.
- **Offline capability** — on-device models work without connectivity, enabling assistants, translation, and writing help anywhere.
- **Hybrid patterns** — devices commonly combine a local model for simple tasks with cloud escalation for complex ones.
- **Worked example** — a phone's keyboard completes sentences locally while reserving a larger cloud model for long-form drafting requests.
- **Failure modes** — limited context windows, slower generation, and weaker reasoning constrain on-device models relative to cloud models.
- **Practical relevance** — on-device LLMs are a growing deployment target for consumer and enterprise apps that prioritize privacy and availability.
- **Chip acceleration** — neural engines and NPUs on modern devices make local generation practical for models that would have been too slow a few years ago.


## Related

- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — the broader computing paradigm
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — the model class
- [[wiki/ai-ml/model-quantization|Model Quantization]] — the enabling compression
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — the reference runtime
- [[wiki/llm-agents/data-minimization-agents|Data Minimization for Agents]] — the privacy principle
- [[wiki/ml-frameworks/onnx-runtime|ONNX Runtime]] — a cross-platform runtime

