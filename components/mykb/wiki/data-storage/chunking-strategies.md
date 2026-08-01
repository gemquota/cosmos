---
type: "concept"
title: "Chunking Strategies"
description: "Approaches for splitting documents into retrievable units that balance context completeness and precision"
tags: ["chunking", "rag", "retrieval", "preprocessing", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://python.langchain.com/docs/how_to/recursive_text_splitter/"]
---

# Chunking Strategies

## Summary
Chunking splits long documents into pieces that get embedded and retrieved, so every retrieved unit is small enough to be useful context yet large enough to be self-contained. Chunk boundaries and sizes are among the biggest quality levers in RAG. mykb's wiki notes are naturally atomic, but longer syntheses still need chunking decisions.

## Details
- **Fixed-size** — split every N tokens with overlap; simple, but can cut sentences and meaning mid-way.
- **Recursive/structural** — split on paragraph, sentence, then token boundaries (LangChain's recursive splitter); respects document structure.
- **Semantic chunking** — group sentences by embedding similarity so chunks align with topics instead of byte offsets.
- **Trade-off** — small chunks (100-200 tokens) mean precise retrieval but missing context; large chunks (500-1000) mean more context but diluter matches; overlap (10-20%) prevents boundary loss.
- **Worked example** — a 2,000-token synthesis page chunked at 400 tokens with 80 overlap yields about six retrievable pieces; a query about its conclusion retrieves only the final chunk, and the LLM sees no unrelated preamble.

## Related
- [[wiki/data-storage/embeddings|Embeddings]] — chunks are the units that get embedded
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — chunking quality drives RAG answer quality
- [[wiki/data-storage/tokenization|Tokenization]] — defines the tokens chunk sizes count
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — pairs with chunking to scope retrieval
- [[wiki/data-storage/vector-databases|Vector Databases]] — stores and searches the resulting chunks
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — documents chunking trade-offs for mykb
- [[wiki/data-storage/n-grams|N-grams]] — the text units chunk sizes are measured in
- [[wiki/syntheses/knowledge-system|Knowledge System]] — chunked notes feed the knowledge loop
