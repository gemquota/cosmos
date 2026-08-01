---
type: "concept"
title: "Belief States"
description: "The agent's internal model of the world, updated by observations"
tags: ["beliefs", "reasoning", "uncertainty", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Belief States

## Summary
Belief states are the agent's internal estimate of the world given everything it has seen: what is true, what is uncertain, and what changed. They matter because decisions are only as good as the beliefs they are based on. POMDP theory formalizes beliefs as probability distributions over hidden states.

## Details
- Beliefs update as observations arrive; contradictory evidence should revise them.
- Well-calibrated beliefs carry uncertainty, not just point estimates.
- Stale beliefs cause confidently wrong actions; agents must re-verify.
- Open questions: belief persistence across sessions and belief revision policy.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — the loop that updates beliefs
- [[wiki/concepts/perception-loop|Perception Loop]] — the source of belief updates
- [[wiki/concepts/world-models|World Models]] — the larger structure beliefs live in
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]] — the formal framework
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — probabilistic belief representation
