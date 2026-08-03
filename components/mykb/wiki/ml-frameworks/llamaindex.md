---
type: "concept"
title: "LlamaIndex"
description: "A data framework for connecting LLMs to enterprise and personal data via indexing and retrieval"
tags: ["llamaindex", "rag", "retrieval", "framework"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# LlamaIndex

## Summary

LlamaIndex (formerly GPT Index) is the data framework for RAG: connectors for sources, document processing, indexing structures, and query engines with retrieval strategies. It standardizes the data-to-context pipeline that retrieval-augmented applications are built on.

## Details
- Mechanism: readers/connectors ingest sources (files, wikis, APIs); documents are split into nodes with metadata; indexes (vector, summary, tree, knowledge-graph) structure them; query engines orchestrate retrieval + synthesis with strategies (hybrid, recursive, sub-question); data agents route queries across tools and indexes.
- Concrete example: a wiki assistant loads OKF markdown, chunks notes into nodes with frontmatter metadata, builds a vector index plus a keyword index, and queries with hybrid retrieval and reranking; a data agent answers "which syntheses cover constraint handling?" by routing to the right index and aggregating.
- Failure modes: over-indexing (indexes that duplicate and diverge); chunking defaults that split meaning; hidden complexity — the framework's defaults mask retrieval quality until production; and coupling to framework abstractions that complicate custom pipelines.
- Operational tradeoffs: LlamaIndex accelerates RAG construction at the cost of abstraction and version churn; the discipline is owning the retrieval pipeline's evaluation (recall, faithfulness), keeping index structure visible, and swapping framework pieces for custom code where measurement demands.
- RSIS3/mykb relevance: the wiki's retrieval experiments document index strategies, so the loop's search stack evolves with measured recall rather than framework defaults.
- Custom pipelines: when retrieval quality matters, own the split/embed/rank steps directly and use the framework only for connectors; measured recall beats framework convenience.
- Version pinning: LlamaIndex changes APIs and defaults quickly; pin versions in lockfiles and re-run retrieval evals on upgrades.
- Metadata filtering: use node metadata (source, date, tags) as retrieval filters before similarity search; metadata-aware retrieval cuts false positives that pure vector search produces.
- Index freshness: rebuild or incrementally update indexes when the corpus changes; a stale index quietly degrades answer quality while appearing healthy.

## Related
- [[wiki/ml-frameworks/langchain|LangChain]] — The orchestration sibling
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The RAG pattern it serves
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — The vector backbone
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Query result contracts
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb's retrieval architecture parallels it
