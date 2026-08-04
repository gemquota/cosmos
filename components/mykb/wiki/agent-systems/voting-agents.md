---
type: "concept"
title: "Voting Agents"
description: "Aggregating multiple agent answers through voting to reach a final decision"
tags: ["voting", "agents", "voting", "aggregation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Voting Agents

## Summary
Voting agents aggregate multiple agent answers through voting to reach a final decision, trading extra computation for reliability. The approach matters because individual model outputs are noisy, and independent samples can be combined into a much more stable answer. Diversity of voters, not their raw count, determines how much the vote helps. Voting converts extra inference spend into reliability when answers are hard.

## Details
- **Definition** — voting is an ensemble technique where several agents or samples produce answers and a rule selects the winner, typically majority or weighted plurality.
- **Mechanism** — each voter produces an answer independently, then an aggregation rule counts votes, optionally weighted by confidence, expertise, or prior accuracy.
- **Diversity** — voters must differ in meaningful ways, such as different prompts, contexts, or models; identical voters simply repeat the same error.
- **Variants** — self-consistency-voting samples multiple outputs from one model, while multi-agent voting uses genuinely separate agents.
- **Worked example** — five agents classify a support ticket's severity; four vote high severity, so the system routes it to the urgent queue.
- **Failure modes** — correlated errors, sycophantic agreement, and a confident minority can all produce wrong winners; calibration checks help.
- **Cost** — voting multiplies inference cost and latency, so it is reserved for high-stakes decisions where the error cost justifies the spend.
- **Practical relevance** — voting is a simple, effective reliability lever and a building block for agent-consensus systems.
- **Confidence weighting** — weighting votes by per-voter calibration improves accuracy over simple majority.
- **Cost control** — sample counts should be tuned per difficulty tier to avoid over-spending on easy tasks.
- **Disagreement signal** — high disagreement is itself useful: it marks questions that need escalation.
- **Failure example** — five voters prompted identically produce five copies of the same mistake.

## Related
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — the single-model sampling variant
- [[wiki/agent-systems/agent-consensus|Agent Consensus]] — broader agreement mechanisms
- [[wiki/agent-systems/agent-ensembling|Agent Ensembling]] — where voter diversity comes from
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — checking the voted result
- [[wiki/ai-ml/arena-ranking|Arena Ranking]] — preference voting at scale
