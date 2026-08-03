---
type: "concept"
title: "Hypothetical Document Embeddings (HyDE)"
description: "Technique that asks the LLM to draft a hypothetical answer and embeds that draft to search the index"
tags: ["embeddings", "rag", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Hypothetical Document Embeddings (HyDE)

## Summary
HyDE asks the LLM to draft a hypothetical answer to the query, embeds that draft, and uses it to search the index instead of embedding the raw query. The generated answer often sits closer in embedding space to real documents than the query does, which improves recall on short or ambiguous queries at the cost of one generation call.

## Details
The mechanism exploits a property of embedding models: documents that share vocabulary, structure, and topic cluster together, while a terse user query in a different register may land far from them. A hypothetical answer written in full-sentence, document-style language bridges that gap, so the vector search finds relevant passages the raw query would miss. The draft does not need to be factually correct — it only needs to be topically aligned — which is why the technique is robust even when the LLM invents details.

The main benefit is recall on short or ambiguous queries, where a few keywords rarely match the vocabulary of the target documents. It composes naturally with query transformations such as decomposition, and with reranking downstream, because the retrieval stage can cast a wider net and let a reranker sort out false positives.

The costs and failure modes are equally concrete. Each query now consumes a generation call, adding latency and token spend; at high query volume the price per search can dominate. The synthetic draft can drift from the actual answer, embedding a plausible-sounding but wrong topical framing that pulls in irrelevant documents. If the generation model shares biases with the index authors, HyDE can systematically favor certain phrasings. The standard mitigation is to treat HyDE as a recall stage only: always verify retrieved evidence against the source, and evaluate retrieval quality on held-out queries rather than assuming the draft is a good query.

For mykb, HyDE is a candidate technique for the wiki's TF-IDF-plus-embedding search layer, especially for natural-language questions written by agents rather than exact keyword matches. The mykb angle is that drafts should be grounded in the same vocabulary the wiki uses, and any HyDE deployment should log the draft alongside results so retrieval failures are explainable.

## Related
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — embedding space it exploits
- [[wiki/ai-ml/query-transformations|Query Transformations]] — family it belongs to
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — fixing false positives
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — using generation inside retrieval
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — why evidence still matters
