---
type: "concept"
title: "Hallucination Mitigation"
description: "Techniques for reducing fabricated or ungrounded model output"
tags: ["hallucination", "grounding", "llm", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2005.11401", "https://arxiv.org/abs/2205.11916"]
---

# Hallucination Mitigation

## Summary
Hallucination mitigation is the set of techniques — grounding, verification, constrained decoding, self-checks — that reduce fabricated content. It matters because ungrounded claims break trust in agent work. Mitigation is a pipeline, not a single fix.

## Details
- **Grounding** — retrieval-augmented generation and citations bind outputs to sources the model can be checked against.
- **Verification** — a verifier or critic agent checks claims, quotes, and numbers against retrieved evidence before release.
- **Constrained decoding** — grammar and schema constraints prevent structurally impossible outputs and force citation formats.
- **Self-consistency** — sampling multiple answers and keeping the majority reduces random fabrications.
- **Confidence and calibration** — models asked to self-report uncertainty are overconfident; calibration measurement keeps their signal honest.
- **Worked example** — a research agent drafts, then a citation checker confirms each claim maps to a source, and unverifiable claims are flagged or dropped.
- **mykb relevance** — hallucination mitigation is a documented mykb topic; RSIS3's verification phases apply it to self-generated code and claims.

## Related
- [[wiki/ai-ml/calibration-and-confidence|Calibration and Confidence]] — honest confidence
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — voting out hallucinations
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — verification agents
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — distinguishing attacks from errors
- [[wiki/ai-ml/grounding-and-factuality|Grounding and Factuality]] — factual grounding
- [[wiki/ai-ml/hallucination-benchmarks|Hallucination Benchmarks]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — red-teaming practice
