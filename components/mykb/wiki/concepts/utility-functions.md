---
type: "concept"
title: "Utility Functions"
description: "Numerical objectives agents maximize when choosing actions"
tags: ["utility", "decision-making", "rationality", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Utility Functions

## Summary
A utility function assigns a number to outcomes so the agent can compare options and choose the best. It matters because it turns preferences into a decision rule — and because a poorly specified utility invites reward hacking. Most real agents optimize proxies of utility.

## Details
- Foundations: expected utility theory and rational choice.
- Inverse problems: inferring utility from behavior.
- Specification risk: proxy mismatch, misspecified weights.
- Open questions: multi-objective utilities and lexicographic preferences.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — what goes wrong with utilities
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — limits on utility maximization
- [[wiki/concepts/satisficing|Satisficing]] — the alternative to maximizing
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — utility in sequential decisions
- [[wiki/concepts/policy-gradient|Policy Gradient]] — learning policies that maximize utility
