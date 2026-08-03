---
type: "concept"
title: "Preference Tuning"
description: "Aligning model behaviour to human preferences via comparison data, covering RLHF, DPO, and related methods"
tags: ["preference-tuning", "alignment", "rlhf", "dpo"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Preference Tuning

## Summary
Preference tuning is the alignment family that uses human (or AI) comparisons between outputs to steer behaviour. It sits after SFT in the standard recipe and is the main way assistants learn to be helpful and safe.

## Details
- **Data form** — pairs or ranks of completions for the same prompt, labelled by preference; the labelling protocol (explicit comparisons, implicit signals like thumbs-up, or AI-generated critiques) shapes the distribution of what gets rewarded.
- **Methods differ in optimization** — RLHF trains a reward model on the comparisons and optimizes the policy with RL (typically PPO); DPO turns the same comparison data into a direct classification-style loss over the reference policy; RLAIF replaces human labels with AI-generated preferences to scale annotation; GRPO and RLOO reduce infrastructure while keeping an RL flavour.
- **Quality dominates** — preference data quality — diversity of prompts, label agreement between annotators, coverage of edge cases — is the dominant factor in outcome quality; a small high-agreement set curated for the target behaviour beats a large noisy one, and duplicate or near-duplicate prompts overfit the reward signal.
- **Failure modes** — sycophancy emerges when agreeable but wrong outputs are preferred; length bias rewards verbosity; reward hacking appears when the optimization target diverges from true preferences; and distribution shift makes the tuned model brittle on out-of-distribution prompts.
- **Evaluation** — because preferences are subjective, evals need both human review of sampled outputs and automated metrics (win rates against a baseline, refusal/helpfulness balance) with planted-error cases to catch sycophancy.
- **RSIS3 relevance** — RRP critiques produce natural preference pairs for mykb's alignment dataset: each refinement cycle generates rejected (earlier draft) and accepted (revised) versions of the same specification, which can be labelled and reused to tune a local preference model without extra annotation cost.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The canonical preference-tuning method
- [[wiki/ai-ml/dpo|DPO]] — The direct, RL-free alternative
- [[wiki/ai-ml/reward-model|Reward Model]] — The component RLHF needs and DPO skips
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — Preference tuning applied to safety
- [[wiki/ai-ml/sft|SFT]] — The stage preference tuning follows
