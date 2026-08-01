---
type: "concept"
title: "Preference Tuning"
description: "Aligning model behaviour to human preferences via comparison data, covering RLHF, DPO, and related methods"
tags: ["preference-tuning", "alignment", "rlhf", "dpo"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Preference Tuning

## Summary
Preference tuning is the alignment family that uses human (or AI) comparisons between outputs to steer behaviour. It sits after SFT in the standard recipe and is the main way assistants learn to be helpful and safe.

## Details
- Data form: pairs or ranks of completions for the same prompt, labelled by preference.
- Methods differ in optimization: RLHF (reward model + RL), DPO (direct loss), RLAIF (AI labels).
- Preference data quality — diversity, label agreement — is the dominant factor in outcome quality.
- RSIS3 relevance: RRP critiques produce natural preference pairs for mykb's alignment dataset.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The canonical preference-tuning method
- [[wiki/ai-ml/dpo|DPO]] — The direct, RL-free alternative
- [[wiki/ai-ml/reward-model|Reward Model]] — The component RLHF needs and DPO skips
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — Preference tuning applied to safety
- [[wiki/ai-ml/sft|SFT]] — The stage preference tuning follows
