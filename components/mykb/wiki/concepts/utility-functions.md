---
type: "concept"
title: "Utility Functions"
description: "Numerical objectives agents maximize when choosing actions"
tags: ["utility", "decision-making", "rationality", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Utility Functions

## Summary
A utility function assigns a number to outcomes so the agent can compare options and choose the best. It matters because it turns preferences into a decision rule — and because a poorly specified utility invites reward hacking. Most real agents optimize proxies of utility.

## Details
- Foundations: expected utility theory and rational choice. Von Neumann-Morgenstern utility theory shows that a preference ordering satisfying a few axioms (completeness, transitivity, continuity, independence) can be represented by a utility function, and that rational choice under uncertainty is expected-utility maximization. The theory's power is representational: any consistent preference structure becomes a single numeric function, and the decision problem becomes "maximize". The axioms are also the theory's vulnerability — real preferences (and real systems) routinely violate them, and the utility representation then quietly encodes the violations as if they were consistent.
- The function's shape encodes the agent's risk attitude: concave utility means risk aversion (a guaranteed $50 beats a 50% shot at $100), convex means risk seeking, linear means risk neutrality. Utility is not value or reward — it is the transformation of outcomes into the quantity actually maximized, which is why the same outcome can produce different behavior under different utility functions.
- Inverse problems: inferring utility from behavior. Given an agent's choices, can we recover its utility function? Inverse reinforcement learning does exactly this — observe behavior, infer the reward — and the problem is ill-posed: infinitely many utility functions explain the same behavior, so inference needs strong priors. This is the technical heart of value learning: if the goal is to align an AI with human values, the values must be inferred from imperfect behavioral evidence, with all the ambiguity that entails.
- Specification risk: proxy mismatch, misspecified weights. A utility function is a specification, and specifications fail in known ways: the proxy (what is easy to measure) diverges from the true objective (what is wanted), the weights between multiple objectives are wrong or entangled, and the function's edge-case behavior is unexamined until an optimizer finds it. The utility is not a neutral description — it is an invitation: every optimizer will search its maximum, including the regions the specifier never considered.
- Open questions: multi-objective utilities and lexicographic preferences. How to combine incommensurable objectives (safety and capability) into one function, and how to represent preferences that refuse tradeoffs (a constraint that cannot be priced) — the open questions where utility theory meets side constraints.
- RSIS3 relevance: the bundle's metrics are utility proxies — improvement metrics, practice compliance, and telemetry coverage are the numeric objectives the loops maximize, and the discipline of asking "is the proxy the intent?" is the same discipline the field applies to any utility.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — what goes wrong with utilities
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — limits on utility maximization
- [[wiki/concepts/satisficing|Satisficing]] — the alternative to maximizing
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — utility in sequential decisions
- [[wiki/concepts/policy-gradient|Policy Gradient]] — learning policies that maximize utility
