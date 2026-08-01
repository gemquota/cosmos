---
type: "concept"
title: "Refusal Behaviour"
description: "The trained tendency of a model to decline requests that violate safety, legal, or policy boundaries"
tags: ["refusal", "safety", "alignment", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Refusal Behaviour

## Summary
Refusal behaviour is the model's learned ability to say 'I can't help with that' instead of complying with disallowed requests. It is a product of safety tuning and RLHF, and it can both over- and under-trigger.

## Details
- Over-refusal is a common production problem: models decline benign requests (copyright, safety-adjacent topics) too eagerly.
- Under-refusal is the safety failure jailbreaks exploit; both extremes are measured in safety evals.
- Tuning levers: system-prompt policy, temperature, and fine-tune data can shift refusal thresholds.
- RSIS3 relevance: RSIS3's own boundaries (no self-destruction, crisis handling) are refusal-like constraints in its prompt system.

## Related
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — The training that produces refusal behaviour
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — Attacks designed to defeat refusals
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — System policy shapes refusal boundaries
- [[wiki/ai-ml/guardrails|Guardrails]] — Runtime enforcement when refusals fail
- [[wiki/ai-ml/sycophancy|Sycophancy]] — The opposing failure of saying what the user wants
