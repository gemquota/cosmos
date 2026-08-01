---
type: "concept"
title: "Lemmatization"
description: "Reducing words to dictionary lemma forms using vocabulary and morphology"
tags: ["lemmatization", "nlp", "normalization", "lexical"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Lemmatization

## Summary
Lemmatization maps inflected words to their dictionary lemma ('better' → 'good', 'ran' → 'run') using vocabulary and part-of-speech context. It is more accurate than stemming but slower and language-dependent.

## Details
- **Contrast** — stemming chops affixes blindly; lemmatization returns real dictionary words.
- **Cost** — needs POS tagging and lexical resources (WordNet, spaCy models); heavier per token.
- **Use** — IR normalization, topic modeling, and linguistic applications where readable forms matter.

## Related
- [[wiki/data-storage/stemming|Stemming]] — the fast, crude alternative
- [[wiki/data-storage/tokenization|Tokenization]] — the preceding pipeline step
- [[wiki/data-storage/stopwords|Stopwords]] — often removed before lemmatization
- [[wiki/data-storage/tf-idf|TF-IDF]] — lemmatized terms feed weighting
- [[wiki/data-storage/index|Data Storage]] — text normalization
