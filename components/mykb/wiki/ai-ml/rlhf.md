---
type: "concept"
title: "RLHF"
description: "Reinforcement Learning from Human Feedback: aligning a model's outputs to human preferences using a learned reward signal"
tags: ["rlhf", "alignment", "reinforcement-learning", "preferences"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2203.02155"]
---

# RLHF

## Summary
RLHF aligns language models with human preferences in three stages: supervised fine-tuning, training a reward model on human comparisons, and optimizing the policy against that reward with reinforcement learning. InstructGPT showed the recipe turns generic GPT-3 into an instruction-following assistant.

## Details
- The reward model learns from pairwise human preferences (which of two outputs is better), producing a scalar quality signal.
- RL optimization uses PPO in the classic recipe; the policy is regularized toward the SFT model with a KL penalty to avoid reward hacking.
- Human feedback at scale is expensive, which motivated alternatives like RLAIF, DPO, and preference tuning from synthetic labels.
- Reward hacking is the known failure mode: the policy exploits reward-model blind spots, producing confident nonsense.
- RLHF changes behaviour and style more than facts; factual reliability comes mainly from data and retrieval.
- RSIS3 relevance: mykb can store preference pairs from pulse outcomes, and L3 evolution can periodically re-align local models on that data.

## Related
- [[wiki/ai-ml/reward-model|Reward Model]] — The learned preference scorer at the core of RLHF
- [[wiki/ai-ml/ppo|PPO]] — The RL algorithm in the classic RLHF stack
- [[wiki/ai-ml/dpo|DPO]] — Direct preference optimization, a simpler alternative
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The family RLHF belongs to
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — RLHF is a core safety-tuning lever
- [[wiki/ai-ml/sycophancy|Sycophancy]] — A known RLHF failure: learning to flatter rather than be correct
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Research context for alignment methods
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Preference data curated in the wiki
