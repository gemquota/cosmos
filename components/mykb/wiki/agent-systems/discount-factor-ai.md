---
type: "concept"
title: "Discount Factor in AI"
description: "How future rewards are weighted"
tags: ["discount", "factor", "rl"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Discount Factor in AI

## Summary
The discount factor gamma weights future rewards exponentially, trading present for future value.

## Details
- The discount factor gamma weights future rewards exponentially, trading present for future value.
- Low gamma yields myopic agents; high gamma yields long-horizon planning.
- Discounting interacts with safety: high gamma agents may plan around oversight.
- RSIS3 relevance: the loop discounts distant knowledge gains against immediate churn risk.

## Related
- [[wiki/agent-systems/myopic-reward|Myopic Reward]] — the low-gamma end
- [[wiki/agent-systems/horizon-length|Horizon Length]] — the window
- [[wiki/agent-systems/discounting-practice|Discounting in Practice]] — the applied choices
- [[wiki/agent-systems/time-consistency-ai|Time Consistency]] — the consistency question
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — the full treatment of this theme
- [[wiki/ai-ml/reward-model|Reward Model]] — existing graph context
