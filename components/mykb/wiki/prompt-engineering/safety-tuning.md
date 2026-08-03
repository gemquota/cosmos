---
type: "concept"
title: "Safety Tuning"
description: "Training techniques — SFT on safe responses, RLHF, and preference data — that teach models to refuse harmful requests"
tags: ["safety-tuning", "alignment", "training", "safety"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Safety Tuning

## Summary
Safety tuning is the training-side counterpart to runtime guardrails: aligning models against harmful behaviour using curated data and preference optimization. It is why modern models refuse most dangerous requests out of the box — and why runtime guardrails remain necessary, since it is bypassable via jailbreaks.

## Details
- Stages: supervised fine-tuning on safe exemplars teaches baseline refusal; RLHF or DPO optimizes preferences toward safe responses; iterative red-team feedback closes discovered gaps; the result is a refusal threshold the model applies at inference.
- Concrete example: a model trained with RLHF refuses a request for harmful instructions; a jailbreak reframes the request and the refusal fails — the safety-tuning gap that runtime guardrails cover; a domain-tuned model (legal, medical) is safety-tuned again so its specialized outputs respect policy.
- Failure modes: safety tuning degrading general capability (the alignment tax); over-generalization refusing benign variants of harmful topics; tuning data that misses categories, leaving blind spots; robustness gaps that jailbreaks exploit despite tuning.
- Tradeoffs: safety tuning trades some capability and helpfulness for aligned behaviour; the alternative, runtime-only guardrails, is cheaper and incomplete; the mature pattern is tuning plus guardrails plus red teaming — each layer covers the others' gaps.
- Operational notes: eval refusal calibration and capability retention after tuning, and refresh tuning as attack patterns evolve.
- RSIS3 relevance: any locally fine-tuned RSIS3 model needs a safety-tuning pass on the same preference data used for behaviour — the training-side half of its guardrails.

## Practice
- Treat safety tuning as a continuous loop with red teaming, not a one-time training pass.
- Document the preference data and tuning recipe so a later fine-tune can reproduce the same safety behaviour.
## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The main preference-optimization stage
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — The observable outcome of safety tuning
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — Finding the gaps safety tuning misses
- [[wiki/ai-ml/dpo|DPO]] — A cheaper preference-tuning alternative
- [[wiki/ai-ml/constitutional-ai|Constitutional AI]] — A principle-driven safety-tuning method
