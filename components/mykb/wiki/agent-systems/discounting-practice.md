---
type: "concept"
title: "Discounting in Practice"
description: "How real systems set discounting"
tags: ["discounting", "practice", "rl"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Discounting in Practice

## Summary
Discounting in practice is choosing gamma, horizon truncation, and reward shaping for real tasks: balancing task difficulty, credit assignment, and safety. The theory says how discounting works; practice decides what value makes the system behave the way you want.

## Details
- **Choosing gamma** — match gamma to the typical credit-assignment distance: tasks with long-delayed rewards need high gamma, while fast tasks can use lower values that converge quickly.
- **Horizon truncation** — capping episode length bounds variance and cost; truncation is a blunt instrument compared with gamma but is simple and auditable.
- **Reward shaping** — dense intermediate rewards substitute for aggressive discounting when the true reward is distant; shaping must be tested against the terminal objective to avoid gaming.
- **Safety in practice** — real systems often choose shorter effective horizons on high-risk actions and longer ones on safe exploration, making discounting a policy decision rather than a single number.
- **Bad discounting symptoms** — shortsighted policies (too low), unstable or slow learning (too high), and policies that optimize the shaping reward instead of the goal.
- **RSIS3 relevance** — the bundle's staged passes are a practical discounting scheme: each pass balances immediate disruption against a discounted estimate of future knowledge value.
- **Measurement** — validate the chosen discount by checking that the agent's behavior on delayed-reward probes matches the intended trade-off, not by the tuning curve alone.

- **Documenting the choice** — the gamma and horizon decisions are recorded with the rationale, so a later policy failure can be traced to the discount choice rather than the model.
- **Sensitivity check** — test a small range of gamma values on a probe task; if behavior flips sharply, the task rewards are probably mis-specified rather than the discount wrong.
## Related
- [[wiki/agent-systems/discount-factor-ai|Discount Factor in AI]] — the theory
- [[wiki/agent-systems/horizon-length|Horizon Length]] — the window
- [[wiki/agent-systems/myopia-ai|Myopia in AI]] — the safety end
- [[wiki/agent-systems/time-consistency-ai|Time Consistency]] — consistency across time
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — limits on optimization
- [[wiki/ai-ml/reward-model|Reward Model]] — the reward signal
