---
type: "concept"
title: "TF-IDF"
description: "Classic term-weighting scheme scoring how important a word is to a document in a corpus"
tags: ["retrieval", "information-retrieval", "tf-idf", "lexical", "ranking"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Tf%E2%80%93idf"]
---

# TF-IDF

## Summary
TF-IDF weighs a term by how often it appears in a document (term frequency) against how rare it is across the corpus (inverse document frequency). It turns each document into a sparse vector and is the classic lexical baseline for search. mykb's search engine is built around TF-IDF over its markdown wiki.

## Details
- **Formula** — `tf-idf(t,d) = tf(t,d) * log(N / df(t))` where N is corpus size and df is the number of documents containing t; rare terms get higher weight.
- **Bag of words** — order is ignored; preprocessing (tokenization, stopword removal, stemming) heavily affects quality.
- **Comparison table** — TF-IDF (weighted bag of words, fast, interpretable) vs BM25 (adds term-frequency saturation and document-length normalization, usually stronger) vs embeddings (semantic, heavier).
- **Worked example** — a wiki note mentioning 'spaced repetition' often but rarely elsewhere in mykb ranks high for that query despite other notes using synonyms.
- **Limitations** — no meaning: synonyms are missed, polysemy confuses scores; this is why mykb pairs it with embedding search.
- **Uses beyond search** — keyword extraction, document similarity (cosine over TF-IDF vectors), and topic modeling inputs.

## Related
- [[wiki/data-storage/bm25|BM25]] — the probabilistic successor that usually outperforms TF-IDF
- [[wiki/data-storage/tokenization|Tokenization]] — first step before TF-IDF weighting
- [[wiki/data-storage/stopwords|Stopwords]] — common terms often filtered before weighting
- [[wiki/data-storage/stemming|Stemming]] — normalizes word forms to boost term matching
- [[wiki/data-storage/semantic-search|Semantic Search]] — the meaning-based alternative to TF-IDF
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — an FTS engine that exposes TF-IDF-style ranking
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — documents mykb's TF-IDF search design
- [[wiki/memory/README|Memory Layer]] — the retrieval layer TF-IDF serves
