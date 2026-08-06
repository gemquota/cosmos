---
type: "concept"
title: "Agent Ensembling"
description: "Running multiple agents or models on the same task and combining results for robustness"
tags: ["agents", "ensembling", "robustness", "voting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2205.11916", "https://arxiv.org/abs/2303.17548"]
---

# Agent Ensembling

## Summary
Agent ensembling runs several agents or model variants on the same task and combines their outputs — by voting, averaging scores, or selecting the best. Ensembles improve reliability on high-stakes outputs where a single model may be wrong. The cost is multiplied inference; the payoff is reduced variance and better calibration.

## Details
- **Patterns** — self-consistency (sample multiple reasoning paths from one model), diverse-model ensembles, and generator-critic pairs.
- **Aggregation** — majority voting, weighted scoring by model confidence, or a verifier that selects the best candidate.
- **When it pays** — ambiguous classification, code generation, factual claims, and tasks with a checkable ground truth.
- **Worked example** — three models propose an answer; a verifier agent checks each against evidence and returns the supported one.
- **Diminishing returns** — gains shrink after a few members; correlated models (same family) add less diversity.
- **mykb relevance** — voting agents and self-consistency are existing mykb topics; ensembles are the general pattern behind them.

- **Diversity is the lever** — ensembles improve most when members err independently; same-family models correlate, so diversity comes from different families, temperatures, prompts, or decomposition strategies.
- **Cost-aware sizing** — N members multiply inference cost, so size the ensemble from an error-reduction curve rather than a fixed count, and use a smaller ensemble for easy queries.
- **Failure handling** — a tied vote or conflicting verifier verdict should route to escalation or abstention rather than a random pick.
- **Calibration benefit** — disagreements between ensemble members can estimate uncertainty: high agreement signals confidence, wide disagreement signals ambiguity that should be flagged.
## Related
- [[wiki/agent-systems/voting-agents|Voting Agents]] — agents voting on answers
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — verification as selection
- [[wiki/agent-systems/agent-consensus|Agent Consensus]] — consensus among agents
- [[wiki/ai-ml/best-of-n-sampling|Best-of-N Sampling]] — sampling and selecting best
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — judging ensemble outputs
- [[wiki/agent-systems/generator-verifier-loop|Generator-Verifier Loop]] — generate then verify across members
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the RSIS3/mykb architecture it serves
