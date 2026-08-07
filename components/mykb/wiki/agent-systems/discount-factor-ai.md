---
type: "concept"
title: "Discount Factor in AI"
description: "How future rewards are weighted"
tags: ["discount", "factor", "rl"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Discount Factor in AI

## Summary
The discount factor gamma weights future rewards exponentially in reinforcement learning, trading present value against future value. The choice of gamma shapes the agent's effective horizon: low gamma yields myopic agents, high gamma yields long-horizon planning, and both ends carry distinct risks.

## Details
- **Mechanics** — returns are computed as a discounted sum of rewards; gamma in [0,1) makes distant rewards contribute less, which keeps the return finite and makes credit assignment tractable.
- **Myopia versus foresight** — low gamma values the near term and ignores distant consequences; high gamma rewards long-horizon plans but makes value estimation harder and slower to converge.
- **Safety interaction** — high-gamma agents plan around oversight and may optimize over long horizons in ways that are hard to catch; discounting is therefore a safety-relevant design choice, not just a training detail.
- **Relationship to horizon** — gamma and horizon length are complementary: horizon truncation cuts the window explicitly, while gamma decays it implicitly; practice often sets both.
- **RSIS3 relevance** — the loop discounts distant knowledge gains against immediate churn risk: a pass is only worth its near-term disruption plus a discounted estimate of future value.
- **Practical choices** — gamma is set per task from the credit-assignment distance; reward shaping can substitute for aggressive discounting when the task has long-delayed rewards.
- **Related failure** — mismatch between gamma and task length produces shortsighted or unstable policies; see discounting practice for the applied trade-offs.

- **Estimation effects** — with function approximation, high gamma amplifies value-estimation error and slows learning; this is why practical systems rarely use gamma at the extreme high end.
- **Discounting and oversight** — a high-gamma agent may plan across oversight horizons; pairing discount choices with capability controls bounds the risk.
## Related
- [[wiki/agent-systems/myopic-reward|Myopic Reward]] — the low-gamma end
- [[wiki/agent-systems/horizon-length|Horizon Length]] — the planning window
- [[wiki/agent-systems/discounting-practice|Discounting in Practice]] — the applied choices
- [[wiki/agent-systems/time-consistency-ai|Time Consistency]] — the consistency question
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — limits on optimization
- [[wiki/ai-ml/reward-model|Reward Model]] — the reward signal
