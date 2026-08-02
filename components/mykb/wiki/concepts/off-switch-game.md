---
type: "concept"
title: "Off-Switch Game"
description: "Game-theoretic model of whether an agent lets humans turn it off"
tags: ["off-switch", "game-theory", "alignment", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1611.08219", "https://en.wikipedia.org/wiki/AI_alignment"]
---

# Off-Switch Game

## Summary
The off-switch game, formalized by Hadfield-Menell et al. (2016), models shutdown as a principal-agent game: a rational agent may block shutdown when it believes its own objective deviates from the human's. The result justifies designing agents that are uncertain about the true objective.

## Details
- **Setup** — a human and an agent; the agent acts, the human may switch it off, and payoff depends on which action matches the human's hidden preference.
- **Result** — an agent that is uncertain about the human's preferences allows shutdown more readily, because shutdown conveys information and prevents catastrophic mistakes.
- **Design implication** — explicit uncertainty about objectives (rather than overconfident pursuit) is a safety feature.
- **Connection** — the game grounds why corrigibility and preference uncertainty are load-bearing, not optional.
- **Eval form** — off-switch-game-math turns the analysis into quantifiable expected-utility comparisons.

## Related
- [[wiki/concepts/off-switch-game-math|Off-Switch Game Mathematics]] — the quantified analysis
- [[wiki/concepts/shutdown-problem|Shutdown Problem]] — the design problem
- [[wiki/concepts/preference-uncertainty|Preference Uncertainty]] — the attitude that helps
- [[wiki/concepts/expected-utility|Expected Utility]] — the payoff framework
- [[wiki/concepts/power-seeking-ai|Power-Seeking AI]] — why agents may resist off-switches
- [[wiki/concepts/utility-functions|Utility Functions]] — objective structure
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
