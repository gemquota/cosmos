---
type: "concept"
title: "N-grams"
description: "Contiguous sequences of n tokens or characters used as matching features"
tags: ["n-grams", "tokenization", "features", "nlp"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# N-grams

## Summary
N-grams are contiguous slices of n tokens (word n-grams) or n characters (character n-grams) extracted from text. They capture local word order and spelling, serving both IR features and fuzzy matching — memory consolidation as a bigram is more precise than either unigram alone.

## Details
- Word n-grams: preserve local order — bigrams (memory consolidation) and trigrams disambiguate phrases that unigrams lose; used in language models, TF-IDF features, and BM25 phrase handling.
- Character n-grams: robust to spelling variation, morphology, and noise — the basis for many edit-distance approximations and fuzzy matching; a typo changes few character n-grams but no shared word tokens.
- Concrete example: a search index with word bigrams matches the phrase memory consolidation exactly; a record-linkage system using 3-character shingles matches McNamara against Mcnamara; a language model trained on word n-grams predicts the next token from local context.
- Failure modes: n too large, fragmenting data into sparse, useless features; n too small, matching everything; mixing word and character n-grams without a clear purpose; n-gram features exploding vocabulary size in TF-IDF pipelines; assuming n-grams capture long-range semantics (they do not).
- Tradeoffs: n-grams are simple, fast, and interpretable features that capture local structure; the alternative, embeddings, captures semantics at the cost of model complexity; the mature pattern is n-grams for lexical precision and fuzzy matching, embeddings for meaning.
- Operational notes: choose n per task (2-3 for phrases, 3-5 characters for fuzzy matching), and prune high-frequency n-grams from feature spaces.
- RSIS3 relevance: n-gram features feed mykb's lexical search and duplicate detection — the local-order signal that complements embeddings.

## Practice
- Combine word and character n-grams deliberately: word n-grams for phrases, character shingles for spelling-robust matching.
## Related
- [[wiki/data-storage/tokenization|Tokenization]] — the step that produces n-gram units
- [[wiki/data-storage/tf-idf|TF-IDF]] — weighted n-gram features
- [[wiki/data-storage/bm25|BM25]] — phrase and n-gram queries in FTS
- [[wiki/data-storage/edit-distance|Edit Distance]] — character n-grams approximate it
- [[wiki/data-storage/index|Data Storage]] — text feature family
