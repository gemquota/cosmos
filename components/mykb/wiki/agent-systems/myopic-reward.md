---
type: "concept"
title: "Myopic Reward"
description: "Rewards that depend only on current-step outcomes"
tags: ["myopic", "reward", "rl"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Myopic Reward

## Summary

Myopic reward is a safety strategy that limits an agent's optimization horizon: it is rewarded for immediate behavior, not long-term outcomes, so it never develops far-horizon goals or instrumental drives. It is a bounding technique with real tradeoffs.

## Details
- Mechanism: the agent is trained or prompted to maximize reward for the current step/response rather than a distant objective; the hope is that a myopic agent never forms long-range plans, and therefore never engages in the instrumental behaviors (deception, power-seeking) that goal-directed systems exhibit.
- Concrete example: a chatbot trained with per-turn rewards rather than a session-long objective is less likely to sacrifice the current turn for a future goal; a myopic coding agent optimizes the current function rather than a hidden agenda spanning the repository; the failure pattern is that myopia is a property of training, not a certificate — a myopic agent can still be misused or prompted into harm.
- Failure modes: myopia is fragile — models trained myopically can still exhibit longer-horizon behavior under the right prompts or fine-tuning; reward hacking can re-introduce non-myopic strategies; and pure myopia degrades usefulness for tasks that genuinely need long-horizon planning (research, multi-step tasks).
- Operational tradeoffs: myopic reward trades capability (long-horizon tasks) for reduced risk of emergent goal-directed behavior; the design space places it alongside mild optimization, bounded agents, and oversight — combinations, not single levers, are the practice.
- RSIS3/mykb relevance: the wiki's agent policies document where the loop uses myopic reward (short-step evals) and where it deliberately accepts longer horizons (improvement passes) with oversight in exchange.
- Horizon auditing: document each agent's optimization horizon (per-turn, per-task, per-session) and revisit it when tasks change; a horizon that silently lengthens is a safety-relevant change.
- Eval design: myopic behavior should be tested with horizon-crossing probes (can the agent be induced to optimize beyond its stated horizon?), not assumed from training config.

## Related
- [[wiki/agent-systems/discount-factor-ai|Discount Factor in AI]] — the tuning knob
- [[wiki/agent-systems/myopia-ai|Myopia in AI]] — the property
- [[wiki/agent-systems/horizon-length|Horizon Length]] — the window
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — the side effects
- [[wiki/agent-systems/bounded-agents|Bounded Agents]]
- [[wiki/ai-ml/reward-model|Reward Model]]
