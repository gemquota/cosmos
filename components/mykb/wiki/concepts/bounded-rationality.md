---
type: "concept"
title: "Bounded Rationality"
description: "Decision-making constrained by limited computation, time, and information"
tags: ["rationality", "decision-making", "cognition"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Bounded Rationality

## Summary
Bounded rationality describes decision-making under real constraints: limited computation, limited time, and incomplete information. Where classical rational-choice theory assumes an agent that can evaluate all options and pick the optimum, bounded rationality asks what a feasible agent — human or machine — actually does when the optimum is unreachable, and why that behavior can still be remarkably good.

## Details
- Herbert Simon's original formulation distinguished "substantive rationality" (choosing the best option, which requires omniscience) from "procedural rationality" (following a good process under constraints). The key concept is satisficing: instead of optimizing, the agent searches until it finds an option meeting an aspiration level, then stops. Satisficing is optimal when search itself costs resources, because the marginal value of continuing to search eventually falls below its cost.
- Gerd Gigerenzer's fast-and-frugal heuristics program sharpens the point: simple rules such as "take the first option that exceeds a threshold" or "ignore all cues but the most valid one" can match or beat complex statistical models, especially in small samples where elaborate estimators overfit. The tradeoff is bias versus variance — heuristics are systematically biased in specific ways but robust across environments, whereas complex optimizers are unbiased in theory but fragile in practice.
- Modern formulations include resource-rational analysis, which models cognition as optimal allocation of limited computation: the agent trades expected decision quality against the cost of thinking, and "irrational" behavior is often rational once thinking costs are priced in. This connects directly to machine-learning practice in compute budgeting, early stopping, and anytime algorithms that return the best answer found so far.
- Failure modes of bounded-rational agents are the mirror image: aspiration levels set too high cause endless search, heuristics applied outside their ecological niche produce systematic errors, and delegation of expensive reasoning to cheap shortcuts can harden bad habits.
- RSIS3 relevance: the loops are explicitly bounded-rational systems. L4 and L5 meta-optimizers cannot exhaustively search parameter space, so they satisface — run a budgeted set of experiments, keep what improves the metric, and stop when gains flatten. Treating that as principled bounded rationality, rather than a deficiency, informs how the system sets its aspiration levels.

## Related
- [[wiki/concepts/expected-value-reasoning|Expected Value Reasoning]] — the unbounded ideal
- [[wiki/concepts/multi-armed-bandit|Multi-Armed Bandit]] — the formal model of explore/exploit
- [[wiki/concepts/planning-as-search|Planning as Search]] — search under resource limits
- [[wiki/concepts/risk-literacy|Risk Literacy]] — heuristics in the risk domain
- [[wiki/agent-systems/planning-systems|Planning Systems]]
- [[wiki/concepts/satisficing|Satisficing]]
- [[wiki/concepts/utility-functions|Utility Functions]]
- [[wiki/concepts/dual-process-theory|Dual Process Theory]]
- [[wiki/concepts/exploration-exploitation|Exploration Exploitation]]
