---
type: "concept"
title: "Self-Consistency"
description: "Sampling multiple reasoning paths and taking the majority answer"
tags: ["self-consistency", "reasoning", "sampling", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Self-Consistency

## Summary

Self-consistency improves answer reliability by sampling multiple reasoning paths and selecting the most consistent answer — majority vote over diverse chains of thought. It is a decoding-time ensemble that needs no training and lifts accuracy on reasoning tasks.

## Details
- Mechanism: generate N independent reasoning chains for the same question (temperature > 0 for diversity), extract the final answer from each, and pick the majority (or most confident) answer; the intuition is that correct reasoning paths converge while incorrect ones diverge. Contrast with single greedy decoding, which is one path, often confidently wrong.
- Concrete example: a math word problem sampled 8 times yields the same answer in 6 traces — the majority answer is chosen; an open-ended classification gets a vote across samples with the runner-up flagged as uncertainty; a code question's tests are run against the top-voted solution. The failure pattern: using it for divergent questions where answers legitimately differ.
- Failure modes: cost — N samples multiply tokens and latency; diversity failure (low temperature makes samples identical); majority voting on structured outputs needing aggregation logic; and answer extraction errors (the model's prose vs the actual answer).
- Operational tradeoffs: self-consistency buys accuracy and an uncertainty signal at N× inference cost; the discipline is picking N by task difficulty, pairing with answer extraction, and using vote margins as confidence for downstream gating.
- RSIS3/mykb relevance: the wiki's loop would use self-consistency on high-stakes extractions and ratings, with vote margins feeding the confidence field in telemetry.
- Answer extraction: for structured tasks, parse each sample's answer with the same parser and treat parse failures as votes for uncertainty rather than silently dropping them.
- Adaptive sampling: increase N when early samples disagree and stop early when a supermajority emerges — the fixed-N version wastes budget on easy questions.

## Related
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — measuring the reliability gain
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the sampling distribution
- [[wiki/concepts/calibration|Calibration]] — agreement as a confidence signal
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — search as a stronger alternative
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — consistency as a filter
