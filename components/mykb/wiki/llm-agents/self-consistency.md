---
type: "concept"
title: "Self-Consistency"
description: "Sampling multiple reasoning paths and taking the majority answer"
tags: ["self-consistency", "reasoning", "sampling", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Self-Consistency

## Summary
Self-consistency improves answer reliability by sampling several independent reasoning paths and aggregating the most common answer. It matters because diverse traces surface the answer that many paths agree on. It is a cheap ensemble without extra models.

## Details
- Assumes errors are diverse but the correct answer is consistent.
- Cost: multiple generations per question; used selectively.
- Pairs well with chain of thought.
- Open questions: aggregation schemes beyond majority vote.

## Related
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — measuring the reliability gain
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the sampling distribution
- [[wiki/concepts/calibration|Calibration]] — agreement as a confidence signal
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — search as a stronger alternative
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — consistency as a filter
