---
type: "concept"
title: "Abductive Reasoning"
description: "Inference to the best explanation for observed evidence"
tags: ["abduction", "reasoning", "explanation", "inference"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Abductive Reasoning

## Summary
Abductive reasoning infers the most plausible explanation for observed evidence — reasoning from effect to likely cause. It matters because diagnosis, debugging, and hypothesis generation are abductive. It is the default reasoning mode of agents trying to understand failures.

## Details
- Output is a hypothesis, not certainty: the best available explanation.
- Ties to non-monotonic logic and Bayesian inference.
- Agent use: diagnosing test failures, tracing incidents.
- Open questions: ranking explanations with LLM plausibility.

## Related
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — diagnosis as planning backward
- [[wiki/concepts/backward-chaining|Backward Chaining]] — the inference mechanics
- [[wiki/concepts/defeasible-reasoning|Defeasible Reasoning]] — hypotheses can be defeated
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — probabilistic abduction
- [[wiki/llm-agents/traceability|Traceability]] — evidence for explanations
