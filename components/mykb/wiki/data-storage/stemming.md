---
type: "concept"
title: "Stemming"
description: "Reducing words to their base or root form by chopping affixes"
tags: ["stemming", "nlp", "normalization", "lexical"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Stemming

## Summary
Stemming crudely removes suffixes so running, runs, and ran all match run. It is a fast, language-specific normalization that improves lexical recall — every inflected form retrieves the same pages — at the cost of precision and occasionally ugly stems.

## Details
- Algorithms: Porter and Snowball stemmers apply rule-based suffix stripping for English and other languages; aggressive rules produce non-words (ponies to poni); language choice matters because rules do not transfer.
- Trade-off: higher recall for inflected forms — searching embedding matches embeddings and embedded — against conflated distinct words (policy and police can collide) and stems that are not words.
- Concrete example: an FTS engine over mykb text with the Porter stemmer makes a query for embedding retrieve pages containing embeddings and embedded; a stemmed TF-IDF index groups inflections under one term, changing weights; BM25 in Lucene and FTS5 typically indexes stemmed terms.
- Failure modes: stemming across languages incorrectly (English rules on German text); over-aggressive stems collapsing unrelated words, hurting precision; stemmers applied to numbers or code tokens, corrupting identifiers; inconsistent stemming between index and query, silently missing matches.
- Tradeoffs: stemming is fast and improves recall for inflected languages; the alternative, lemmatization, uses dictionaries for accurate base forms at higher cost; the mature pattern is stemming for lexical search and lemmatization where accuracy matters.
- Operational notes: enable the stemmer per language, verify index/query consistency, and evaluate recall on real queries.
- RSIS3 relevance: FTS engines over mykb text can enable stemmers so embedding and embeddings retrieve the same pages — the normalization that keeps lexical search usable.

## Practice
- Keep the stemmer consistent between indexing and querying; a mismatch is a silent recall bug.
## Related
- [[wiki/data-storage/lemmatization|Lemmatization]] — the dictionary-based, more accurate alternative
- [[wiki/data-storage/tokenization|Tokenization]] — the step before stemming
- [[wiki/data-storage/stopwords|Stopwords]] — filtering that typically precedes stemming
- [[wiki/data-storage/tf-idf|TF-IDF]] — stemmed terms change TF-IDF weights
- [[wiki/data-storage/bm25|BM25]] — BM25 indexes stemmed terms in most engines
- [[wiki/data-storage/00-index|Data Storage]] — text normalization
