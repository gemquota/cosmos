---
type: "concept"
title: "Belief States"
description: "The agent's internal model of the world, updated by observations"
tags: ["beliefs", "reasoning", "uncertainty", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process", "https://en.wikipedia.org/wiki/Belief"]
---

# Belief States

## Summary
Belief states are the agent's internal estimate of the world given everything it has seen: what is true, what is uncertain, and what changed. They matter because decisions are only as good as the beliefs they are based on. POMDP theory formalizes beliefs as probability distributions over hidden states.

## Details
- Beliefs update as observations arrive; contradictory evidence should revise them.
- Well-calibrated beliefs carry uncertainty, not just point estimates.
- Stale beliefs cause confidently wrong actions; agents must re-verify.
- Open questions: belief persistence across sessions and belief revision policy.
- A belief state is a probability distribution over the possible hidden states of the world, maintained by an agent from its observations and actions.
- It is the central concept in partially observable environments: since the agent cannot see the true state, it tracks a weighted set of hypotheses.
- Bayesian updates refine the belief as evidence arrives; actions are chosen to both exploit current beliefs and gather information.
- Belief-state tracking is the foundation of POMDP planning and of modern agent memory systems that summarize what an agent thinks it knows.
- **Worked example / comparison** — Worked example — a wiki agent unsure whether a source is live holds a belief (0.8 live) updated by each status check; a failed check drops it toward zero and triggers an archive fallback.
- For mykb, belief states are documented as the uncertainty layer beneath agent planning, complementing world-models.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]]
- [[wiki/concepts/perception-loop|Perception Loop]]
- [[wiki/concepts/world-models|World Models]]
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]]
- [[wiki/concepts/bayesian-networks|Bayesian Networks]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
