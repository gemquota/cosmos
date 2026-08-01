---
type: "concept"
title: "Safety Tuning"
description: "Training techniques — SFT on safe responses, RLHF, and preference data — that teach models to refuse harmful requests"
tags: ["safety-tuning", "alignment", "training", "safety"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Safety Tuning

## Summary
Safety tuning is the training-side counterpart to runtime guardrails: aligning models against harmful behaviour using curated data and preference optimization. It is why modern models refuse most dangerous requests out of the box.

## Details
- Stages: supervised fine-tuning on safe exemplars, RLHF/DPO on safety preferences, and iterative red-team feedback.
- Safety tuning can degrade general capability and over-generalize (refusing benign variants of harmful topics).
- Robustness gap: safety tuning is bypassable via jailbreaks, which is why runtime guardrails remain necessary.
- RSIS3 relevance: any locally fine-tuned RSIS3 model needs a safety-tuning pass on the same preference data used for behaviour.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The main preference-optimization stage
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — The observable outcome of safety tuning
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — Finding the gaps safety tuning misses
- [[wiki/ai-ml/dpo|DPO]] — A cheaper preference-tuning alternative
- [[wiki/ai-ml/constitutional-ai|Constitutional AI]] — A principle-driven safety-tuning method
