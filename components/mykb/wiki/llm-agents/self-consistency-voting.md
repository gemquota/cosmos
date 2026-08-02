---
type: "concept"
title: "Self-Consistency Voting"
description: "Sampling multiple reasoning paths and taking a majority vote on the answer"
tags: ["reasoning", "voting", "decoding", "robustness"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2205.11916", "https://arxiv.org/abs/2203.02155"]
---

# Self-Consistency Voting

## Summary
Self-consistency samples several independent reasoning chains for the same question, then votes on the final answer. It exploits the intuition that correct reasoning paths agree with each other more than incorrect ones. It is a pure inference-time technique that improves accuracy without retraining.

## Details
- **Mechanism** — run the model N times with sampling temperature above zero, extract each final answer, and pick the most frequent (or highest-scored) one.
- **Cost** — N× inference cost for gains that shrink as N grows; typical N is 5–40.
- **Aggregation variants** — majority vote, weighted vote by model confidence, or verification by a second pass.
- **Worked example** — a math agent samples 16 solutions; 11 agree on an answer, and that answer is returned with the agreement rate as confidence.
- **Limitations** — systematic biases survive voting; if the model consistently makes the same mistake, voting amplifies it.
- **mykb relevance** — self-consistency is an existing mykb topic and a building block for voting agents and ensembles.

## Related
- [[wiki/agent-systems/voting-agents|Voting Agents]] — agents voting on answers
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — existing self-consistency concept
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — the sampling knob
- [[wiki/ai-ml/best-of-n-sampling|Best-of-N Sampling]] — selecting best instead of voting
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — sampling regimes
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — reasoning chains to sample
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
