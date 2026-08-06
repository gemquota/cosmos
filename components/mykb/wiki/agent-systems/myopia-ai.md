---
type: "concept"
title: "Myopia in AI"
description: "Agents with short effective planning horizons"
tags: ["myopia", "agents", "horizon"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Myopia in AI

## Summary
Myopia in AI is a short effective planning horizon: the system weighs immediate consequences heavily and discounts or ignores later ones. It is often deliberately engineered — short horizons are safer, cheaper, and easier to evaluate — but it becomes a failure mode when near-term optimization defeats long-term goals or leaves deferred harm invisible.

## Details
- **Sources of myopia** — short reward horizons, heavy discounting, context-window limits, and evaluation that only measures immediate outcomes all shorten an agent's effective horizon.
- **Safety benefits** — myopic agents cannot orchestrate elaborate multi-step harm, so horizon reduction is a standard containment technique alongside sandboxing and approvals.
- **Failure modes** — myopic agents take paths with large deferred costs, exploit short-term loopholes, and fail to invest in states that pay off later.
- **Reward-hacking link** — short-horizon optimization of a proxy reward is a classic route to reward hacking, because the hacked behavior looks good in the immediate evaluation window.
- **Deployment reality** — most deployed assistants are myopic by design: they react to the current turn without a long-term plan, which is safe but limits coherence across a session.
- **Tuning** — horizon is a knob, not a fixed property: tasks with external oversight can use longer horizons, while autonomous operation with weak oversight should stay myopic.
- **mykb relevance** — staged pass plans deliberately keep planning horizons short, matching the safety analysis above.

- **Evaluation design** — evaluations that only score immediate outcomes train myopic behavior; adding delayed-feedback tests (does the choice still look good next week?) lengthens the effective horizon without changing the model.

- **Session-scale myopia** — many deployed agents are myopic at session scale: they optimize the current conversation without memory of prior commitments, which is safe for short tasks but produces incoherent behavior across a multi-session project.

## Related
- [[wiki/agent-systems/myopic-reward|Myopic Reward]] — the reward-side mechanism
- [[wiki/agent-systems/horizon-length|Horizon Length]] — the underlying parameter
- [[wiki/agent-systems/near-term-myopia|Near-Term Myopia]] — the behavioral variant
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — the containment family
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — the cognitive cousin
- [[wiki/agent-systems/time-consistency-ai|Time Consistency]] — when horizons shift
