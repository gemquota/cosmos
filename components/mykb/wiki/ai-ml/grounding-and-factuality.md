---
type: "concept"
title: "Grounding and Factuality"
description: "Ensuring model outputs stay consistent with evidence and the real world"
tags: ["factuality", "grounding", "hallucination", "trust"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2302.09114", "https://arxiv.org/abs/2202.03286"]
---

# Grounding and Factuality

## Summary
Grounding and factuality describe how well outputs match evidence and reality. They matter because unfaithful output undermines trust in any AI product. Systems achieve factuality through evidence grounding, verification, and calibration of confidence.

## Details
- **Grounding** — outputs trace to retrievable evidence; **factuality** — claims are true relative to the world.
- **Measurement** — faithfulness checks (claim contained in cited source), factual consistency metrics, and human audits.
- **Worked example** — a checker decomposes an answer into claims and verifies each against the cited chunk, flagging unsupported ones.
- **Levers** — stronger retrieval, constrained prompting, verification passes, and refusal on low-confidence answers.
- **mykb relevance** — RSIS3 must separate grounded knowledge statements from speculation to stay useful.
- **Calibration link** — models should express lower confidence on unsupported claims, tying factuality to calibration-and-confidence.
- **Worked example** — a checker decomposes an answer into claims and verifies each against the cited chunk, flagging unsupported ones.
- **Levers** — stronger retrieval, constrained prompting, verification passes, and refusal on low-confidence answers all raise factuality.

## Related
- [[wiki/ai-ml/citations-and-provenance|Citations and Provenance]] — evidence links
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — reduction methods
- [[wiki/ai-ml/calibration-and-confidence|Calibration and Confidence]] — confidence signals
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — automated checks
- [[wiki/agent-systems/research-agents|Research Agents]] — use case
- [[wiki/ai-ml/hallucination-benchmarks|Hallucination Benchmarks]] — related concept in this cluster
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — the synthesis pipeline
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph substrate
