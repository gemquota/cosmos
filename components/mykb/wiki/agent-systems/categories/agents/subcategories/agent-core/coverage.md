---
type: "entity"
title: "Coverage"
description: "RAG (Retrieval-Augmented Generation)"
tags: ["entity", "api", "ast", "bash", "deployment", "documentation"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---

## Coverage

RAG (Retrieval-Augmented Generation) — a pattern combining information retrieval with LLM generation for knowledge-grounded responses.

RAG compensates for a central limitation of pure generative models: their parametric knowledge is fixed at training time, so they can drift out of date or produce plausible but unsupported answers. By retrieving relevant passages from an external corpus and placing them into the prompt, a RAG system grounds each response in evidence that can be inspected, attributed, and refreshed without retraining. The pipeline divides into three stages: ingestion, retrieval, and generation. During ingestion, source documents are split into chunks, converted into embeddings by a text-embedding model, and indexed in a vector store. At query time, the user's question is embedded with the same model, and a similarity search returns the most relevant chunks, usually after applying metadata filters and a reranking pass. The final stage passes those chunks together with the question to an LLM, which is instructed to answer from the provided context and to say when the context is insufficient.

Chunk sizing and overlap materially affect quality: small chunks improve precision but lose surrounding context, while large chunks preserve coherence but dilute relevance. Hybrid retrieval, which combines dense vector search with sparse keyword matching, improves recall on names, acronyms, and identifiers. Rerankers and relevance thresholds reduce the chance that retrieved noise distracts the generator. Evaluation typically measures retrieval quality with recall@k and generation quality with faithfulness and answer-relevance scores over a golden question set.

Within this repository, RAG-style grounding appears wherever agents summarize or query wiki content: knowledge-grounded answers reduce drift and keep conclusions auditable. The main costs are added latency and token usage from the retrieval hop and longer prompts, so caching, selective retrieval, and smaller context windows are common mitigations.

**Related topics:** api, bash, deployment, documentation

**Domain:** Web Platforms › [[wiki/web-platforms/supercategories/api-services/index|Api Services]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Rest]] › Coverage

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/aborted|Aborted]]
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/aegis|Aegis]]
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/agent-active|Agent Active]]
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/ambiguity-projection-2|Ambiguity Projection 2]]
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/ambiguity-system|Ambiguity System]]
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/ambiguity|Ambiguity]]
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/ap|Ap]]
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-http/apex|Apex]]
