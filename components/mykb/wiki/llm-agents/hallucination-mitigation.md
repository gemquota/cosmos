---
type: "concept"
title: "Hallucination Mitigation"
description: "Techniques for reducing fabricated or ungrounded model output"
tags: ["hallucination", "grounding", "llm", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Hallucination Mitigation

## Summary
Hallucination mitigation is the set of techniques — grounding, verification, constrained decoding, self-checks — that reduce fabricated content. It matters because ungrounded claims break trust in agent work. Mitigation is a pipeline, not a single fix.

## Details
- Grounding: require retrieval or tool evidence before asserting facts.
- Verification: cross-check claims against sources; flag unverifiable ones.
- Self-checks: reflection and calibration reduce but do not eliminate hallucinations.
- RSIS3 relevance: mykb sources give the agent evidence to cite.
- Open questions: reliable detection of subtle, plausible hallucinations.

## Related
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — self-checking as a mitigation
- [[wiki/concepts/confabulation|Confabulation]] — the phenomenon being mitigated
- [[wiki/concepts/calibration|Calibration]] — confidence as a detection signal
- [[wiki/llm-agents/rag-agent|RAG Agent]] — grounding via retrieval
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — sampling multiple answers to detect drift
