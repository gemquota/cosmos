---
type: "concept"
title: "Model Merging"
description: "Combining weights from multiple fine-tuned models into one capable model"
tags: ["model-merging", "models", "merging", "weights"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model Merging

## Summary

Model merging combines the weights of multiple fine-tuned models into a single model that exhibits several capabilities at once, without additional training. Techniques range from simple weight averaging to sophisticated methods that resolve conflicting parameters. Merging matters because it is a cheap alternative to multi-task training, letting practitioners combine specialized skills into one deployable model. Merging is most attractive when models share a base and have been fine-tuned for complementary skills, since compatibility determines success.

## Details

- **Definition** — model merging produces one weight set from two or more models with the same architecture, typically fine-tunes of a common base.
- **Weight averaging** — averaging parameters across models is the simplest form and works well when fine-tunes are close to the base.
- **Task arithmetic** — treating fine-tuned weights as task vectors and adding or subtracting them enables capability composition and unlearning.
- **Advanced methods** — techniques such as TIES and DARE resolve sign conflicts and prune redundant changes before merging.
- **Benefits** — merging avoids retraining costs, preserves multiple skills, and can even improve robustness by ensembling implicitly.
- **Limitations** — models with conflicting weights can interfere, and merged models may lose some specialized accuracy.
- **Relation to composition** — merging is one form of model composition, alongside routing and adapters; each trades simplicity against flexibility.
- **Worked example** — a base model fine-tuned for coding and another for instruction following are merged so one checkpoint can serve both use cases.
- **Failure modes** — naive averaging of very different fine-tunes can degrade both skills; evaluation must verify each retained capability.
- **Practical relevance** — for teams managing many adapters or fine-tunes, merging reduces deployment footprint and cost.
- **Compatibility check** — fine-tunes that drift far from the shared base are harder to merge, so distance between models predicts merge quality.


## Related

- [[wiki/ml-frameworks/model-composition|Model Composition]] — the broader design space
- [[wiki/ml-frameworks/lora-adapters|LoRA Adapters]] — merge-friendly fine-tuning
- [[wiki/ml-frameworks/peft-methods|PEFT Methods]] — parameter-efficient context
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — the source of specialized models
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — managing checkpoints
- [[wiki/ml-frameworks/qlora-adapter-merging|QLoRA and Adapter Merging]] — adapter-specific merging

