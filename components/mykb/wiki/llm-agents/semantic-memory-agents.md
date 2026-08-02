---
type: "concept"
title: "Semantic Memory for Agents"
description: "Storing distilled, queryable knowledge an agent can reuse across tasks"
tags: ["agents", "memory", "semantic", "knowledge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.09288", "https://arxiv.org/abs/2005.11401"]
---

# Semantic Memory for Agents

## Summary
Semantic memory holds the agent's distilled knowledge — facts, concepts, and learned patterns — independent of any single episode. It is what makes an agent cumulatively smarter. Unlike episodic memory it is queried by meaning, usually through embeddings, vector search, or a knowledge graph.

## Details
- **Content** — project conventions, domain facts, resolved-how-tos, and stable identities; written during consolidation, read on demand.
- **Storage** — vector stores with embeddings, graph stores with typed relations, or hybrid; retrieval quality depends on chunking and indexing.
- **Writes** — consolidation pipelines summarize episodes into semantic entries; provenance links entries back to evidence.
- **Worked example** — after fixing a bug, an agent writes a semantic entry "service X returns 503 when Y is stale"; a later task retrieves it before debugging.
- **Staleness** — semantic memory drifts as the world changes; versioning, timestamps, and refresh rules matter.
- **mykb relevance** — mykb is literally a semantic memory: OKF wiki files, vector search, and graph engine serve RSIS3's recall.

## Related
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — graph-based semantics
- [[wiki/llm-agents/episodic-memory-agents|Episodic Memory for Agents]] — the experience source
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — using semantic memory at generation time
- [[wiki/ai-ml/citations-and-provenance|Citations and Provenance]] — evidence for semantic claims
- [[wiki/prompt-engineering/context-injection|Context Injection]] — injecting semantic memory into context
- [[wiki/llm-agents/conversation-history-management|Conversation History Management]] — related concept in this cluster
- [[wiki/concepts/semantic-memory|Semantic Memory]] — memory type it builds on
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — memory consolidation research
