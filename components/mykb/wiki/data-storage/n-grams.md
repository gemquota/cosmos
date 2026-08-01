---
type: "concept"
title: "N-grams"
description: "Contiguous sequences of n tokens or characters used as matching features"
tags: ["n-grams", "tokenization", "features", "nlp"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# N-grams

## Summary
N-grams are contiguous slices of n tokens (word n-grams) or n characters (character n-grams) extracted from text. They capture local word order and spelling, serving both IR features and fuzzy matching.

## Details
- **Word n-grams** — 'memory consolidation' as a bigram is more precise than either unigram alone.
- **Character n-grams** — robust to spelling variation and morphology; the basis for many edit-distance approximations.
- **Use** — language models, TF-IDF features, and record linkage blocking keys.

## Related
- [[wiki/data-storage/tokenization|Tokenization]] — the step that produces n-gram units
- [[wiki/data-storage/tf-idf|TF-IDF]] — weighted n-gram features
- [[wiki/data-storage/bm25|BM25]] — phrase and n-gram queries in FTS
- [[wiki/data-storage/edit-distance|Edit Distance]] — character n-grams approximate it
- [[wiki/data-storage/index|Data Storage]] — text feature family
