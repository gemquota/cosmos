---
type: "concept"
title: "Grounded Generation"
description: "Generating responses anchored to retrieved evidence or verifiable sources"
tags: ["grounding", "generation", "rag", "factuality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2005.11401", "https://arxiv.org/abs/2302.09114"]
---

# Grounded Generation

## Summary
Grounded generation produces answers from a provided evidence set rather than from the model memory alone. It matters because grounded answers are checkable and less prone to hallucination. The evidence constrains what the model can say, and provenance makes every claim auditable.

## Details
- **Pattern** — retrieve evidence, then instruct the model to answer only from that evidence, citing chunk IDs.
- **Strengths** — verifiable claims, fresh knowledge, and domain control without retraining.
- **Worked example** — a legal assistant answers only from retrieved case excerpts; each sentence carries a case citation, and a checker validates the quote exists.
- **Failure modes** — models can ignore grounding when evidence is weak, or parrot evidence that is itself wrong.
- **mykb relevance** — grounded synthesis is the core loop: mykb knowledge in, cited answers out.
- **Constraints** — instruct the model to answer only from evidence and to mark gaps explicitly, reducing confident fabrication.
- **Checker loop** — a verifier validates each claim against the cited chunk before delivery.

## Related
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — parent pattern
- [[wiki/ai-ml/citations-and-provenance|Citations and Provenance]] — citation layer
- [[wiki/ai-ml/grounding-and-factuality|Grounding and Factuality]] — quality axis
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — reducing fabrication
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — agentic variant
- [[wiki/agent-systems/research-agents|Research Agents]] — heavy user
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — the synthesis pipeline
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
