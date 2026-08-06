---
type: "concept"
title: "Horizon Length"
description: "How far ahead an agent plans or is rewarded"
tags: ["horizon", "planning", "rl"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Horizon Length

## Summary
Horizon length is how far ahead an agent plans or is rewarded: a short-horizon agent weighs only near-term consequences, while a long-horizon agent plans and optimizes across many steps. The choice is a central design lever in reinforcement learning and agent safety because it trades short-term safety and simplicity against long-term competence and risk.

## Details
- **Two meanings** — the planning horizon bounds how many steps a planner considers; the reward horizon bounds how far into the future a reward signal reaches.
- **Safety of short horizons** — short-horizon agents are easier to bound and audit because they cannot chain many consequences; they are also easier to fool by deferred effects.
- **Competence of long horizons** — long horizons enable goal-directed behavior, investment, and coherent multi-step plans, but multiply the space of ways to go wrong.
- **Discount factor link** — exponential discounting compresses a long reward horizon into a tractable sum; the effective horizon is roughly the time after which future rewards are negligible.
- **Myopia spectrum** — near-term myopia and pathological short-sightedness sit at one end; far-sighted strategic behavior sits at the other, and most systems are somewhere between.
- **Time inconsistency** — a system's effective horizon can change with context or over time, producing preferences that differ from what an earlier self would have chosen.
- **Design guidance** — horizon should be matched to the task: short and staged for risky operations, longer for research and planning, and always shorter than the oversight window.

- **Oversight coupling** — the safe horizon length depends on the oversight window: an agent should not plan further ahead than its supervisor can verify, or deferred effects will escape review.

## Related
- [[wiki/agent-systems/myopia-ai|Myopia in AI]] — the short end of the spectrum
- [[wiki/agent-systems/discount-factor-ai|Discount Factor in AI]] — the discount expression of horizon
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — where planning horizons are set
- [[wiki/agent-systems/time-consistency-ai|Time Consistency]] — when horizons drift
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — bounding horizon as a safety measure
- [[wiki/agent-systems/near-term-myopia|Near-Term Myopia]] — the failure mode
