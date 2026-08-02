---
type: "concept"
title: "Citations and Provenance"
description: "Attaching verifiable sources and lineage to model outputs"
tags: ["citations", "provenance", "grounding", "trust"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2302.09114", "https://arxiv.org/abs/2005.11401"]
---

# Citations and Provenance

## Summary
Citations and provenance connect every claim in an answer to the evidence that supports it. They matter because grounded answers are auditable: users can verify facts, and pipelines can detect unsupported statements. Provenance also records where the evidence came from, including retrieved documents and tool outputs.

## Details
- **Citation styles** — inline brackets mapping claims to numbered sources, with source text retrievable for inspection.
- **Provenance chain** — capture retrieval query, source chunk, reranker scores, and generation prompt for every answer.
- **Worked example** — a research agent returns a summary where each paragraph cites document IDs; a checker verifies each citation actually contains the claim.
- **Failure mode** — models cite plausible-looking sources; verification must compare the claim against the cited text, not just the presence of a citation.
- **mykb relevance** — RSIS3 synthesis claims should cite mykb sources so the knowledge graph stays falsifiable.
- **Tooling** — pipelines store evidence objects per answer, so citation checks are automated in CI rather than manual.
- **Failure handling** — when a claim cannot be cited, the system should soften the claim or refuse rather than fabricate a source.

## Related
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — generation anchored in evidence
- [[wiki/ai-ml/grounding-and-factuality|Grounding and Factuality]] — quality axis
- [[wiki/agent-systems/research-agents|Research Agents]] — heavy citation users
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — why citations reduce hallucination
- [[wiki/ai-ml/provenance-and-disclosure|Provenance and Disclosure]] — disclosure layer
- [[wiki/agent-systems/agent-logs-and-audits|Agent Logs and Audits]] — provenance records
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — the synthesis pipeline
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph substrate
