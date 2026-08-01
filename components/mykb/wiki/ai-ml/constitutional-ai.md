---
type: "concept"
title: "Constitutional AI"
description: "Aligning models with a written constitution of principles, using AI feedback instead of human labels for most training"
tags: ["constitutional-ai", "alignment", "safety", "rlhf"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Constitutional AI

## Summary
Constitutional AI (Anthropic, 2022) replaces most human preference labels with AI critique-and-revision against a written principle set. The model critiques its own outputs, revises them, and the pairs train a preference model — scaled alignment with less human labour.

## Details
- Two stages: supervised revision from AI critiques, then preference learning from AI-ranked revisions.
- The constitution encodes values (helpfulness, honesty, safety) as explicit principles.
- Trade-off: inherits the judging model's biases; human oversight moves to principle design.
- RSIS3 relevance: RSIS3's self-improvement is analogous — a written RRP constitution governs how it critiques and revises its own behaviour.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The framework constitutional AI modifies
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The family it belongs to
- [[wiki/ai-ml/reward-model|Reward Model]] — The component trained from AI feedback
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — Its main application area
- [[wiki/ai-ml/guardrails|Guardrails]] — Runtime complement to constitutional alignment
