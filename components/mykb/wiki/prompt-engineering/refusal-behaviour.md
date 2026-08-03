---
type: "concept"
title: "Refusal Behaviour"
description: "The trained tendency of a model to decline requests that violate safety, legal, or policy boundaries"
tags: ["refusal", "safety", "alignment", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Refusal Behaviour

## Summary
Refusal behaviour is the model's learned ability to say I can't help with that instead of complying with disallowed requests. It is a product of safety tuning and RLHF, and it can both over- and under-trigger — the two extremes are measured in safety evals.

## Details
- Mechanism: safety tuning shapes the model's refusal threshold; the model declines when a request crosses learned policy boundaries; the threshold is influenced by system-prompt policy, temperature, and fine-tuning data.
- Concrete example: a model refuses a harmful request cleanly; the same model over-refuses a benign safety-adjacent question (copyrighted-style writing, medical advice) because the boundary generalizes too broadly; a jailbreak exploits under-refusal by reframing the request so it no longer looks disallowed.
- Failure modes: over-refusal degrading user experience — benign requests declined, driving users away; under-refusal letting harmful requests through, the failure jailbreaks exploit; refusal thresholds that shift between model versions without notice; refusals that are inconsistent (refusing and complying with similar requests).
- Tradeoffs: refusal behaviour trades helpfulness for safety — the calibration point is a product decision; the alternative extremes (always refuse, never refuse) are simpler and worse; the mature pattern is calibrated refusal measured by evals, with system-policy adjustments and runtime guardrails as the enforcement layer.
- Operational notes: track over- and under-refusal rates in evals, and test the boundary cases after every model change.
- RSIS3 relevance: RSIS3's own boundaries (no self-destruction, crisis handling) are refusal-like constraints in its prompt system — the same calibration question applies to its guardrails.

- Measure refusal consistency across phrasings of the same request, since inconsistent refusals signal calibration drift.
## Related
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — The training that produces refusal behaviour
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — Attacks designed to defeat refusals
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — System policy shapes refusal boundaries
- [[wiki/ai-ml/guardrails|Guardrails]] — Runtime enforcement when refusals fail
- [[wiki/ai-ml/sycophancy|Sycophancy]] — The opposing failure of saying what the user wants
