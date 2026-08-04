---
type: "concept"
title: "PEFT Methods"
description: "Parameter-efficient fine-tuning techniques including LoRA, prefix tuning, and adapters"
tags: ["peft", "fine-tuning", "efficiency", "adapters"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# PEFT Methods

## Summary

Parameter-efficient fine-tuning (PEFT) methods adapt large models to new tasks while updating only a small fraction of the parameters. LoRA, prefix tuning, and adapters are the best-known families, often reducing trainable parameters by orders of magnitude. PEFT matters because it makes fine-tuning affordable on modest hardware and enables many task-specific variants of a single base model. PEFT effectiveness depends on the task: narrow, well-defined adaptation works very well, while broad capability shifts may need more trainable parameters.

## Details

- **Definition** — PEFT freezes the base model and trains a small set of additional or selected parameters, keeping most of the original weights intact.
- **LoRA** — low-rank adaptation injects small trainable matrices into attention and feed-forward layers, producing adapters that can be swapped or merged.
- **Prefix and prompt tuning** — these methods learn soft tokens prepended to inputs, steering behavior without changing weights.
- **Adapters** — small bottleneck modules inserted between layers provide another modular fine-tuning route.
- **Cost benefits** — dramatically reduced memory and compute allow fine-tuning on consumer hardware and many variants per base model.
- **Quality tradeoffs** — PEFT often approaches full fine-tuning quality on narrow tasks but can lag on broad, deep adaptation.
- **Modularity** — multiple adapters can be composed, routed, or merged, enabling multi-task systems from one base.
- **Worked example** — a team trains a LoRA adapter per customer domain on a shared 70B model, then routes requests to the right adapter without retraining.
- **Failure modes** — adapter interference when combined, forgetting of base capabilities, and sensitivity to rank choice are common pitfalls.
- **Practical relevance** — PEFT underpins cost-effective customization and the adapter ecosystems used by serving platforms.
- **Task matching** — for style or format adaptation, small adapters often match full fine-tuning; for deep knowledge changes, larger capacity is safer.


## Related

- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation]] — the LoRA family
- [[wiki/ml-frameworks/qlora-adapter-merging|QLoRA and Adapter Merging]] — quantized PEFT workflow
- [[wiki/ml-frameworks/lora-adapters|LoRA Adapters]] — the concrete artifacts
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — the full-cost baseline
- [[wiki/ai-ml/catastrophic-forgetting-mitigation|Catastrophic Forgetting Mitigation]] — the risk addressed
- [[wiki/ml-frameworks/model-composition|Model Composition]] — combining adapters

