---
type: "concept"
title: "Tokenization"
description: "Splitting text into tokens — words, subwords, or characters — for processing"
tags: ["tokenization", "nlp", "preprocessing", "tokens"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Tokenization

## Summary
Tokenization breaks raw text into the units a downstream system consumes: whitespace words, punctuation-aware tokens, or subword pieces like BPE. Every retriever and language model depends on this first step — tokenizer choice changes term statistics and can break or fix matching.

## Details
- Granularity: word tokens are human-readable and map to terms for TF-IDF and BM25; subword tokens (BPE, WordPiece, SentencePiece) handle rare words and unknown vocabulary for models; character tokens serve fuzzy matching.
- Effects: don't tokenizes as dont or do + n't depending on the tokenizer — the choice decides whether a query matches; stemming and stopword filtering run on tokens; chunk sizes for embedding models are measured in tokens, so tokenizer and chunker must agree.
- Concrete example: a TF-IDF pipeline tokenizes on whitespace and punctuation, producing lowercase word tokens; a BERT-style embedder applies WordPiece, splitting consolidation into subwords; a search query tokenized differently from the index yields zero matches — a classic tokenizer-mismatch bug.
- Failure modes: inconsistent tokenization between index and query; language-specific tokenization applied to the wrong language; subword tokenizers producing tokens that are meaningless to lexical indexes; tokenizer changes invalidating stored term statistics without reindexing; punctuation and URL handling breaking token boundaries.
- Tradeoffs: word tokens are interpretable and cheap; subword tokens are robust and model-native but opaque; the mature pattern is one tokenizer per consumer, kept consistent within each pipeline and aligned across hybrid search.
- Operational notes: document the tokenizer per pipeline, reindex after changes, and test cross-tokenizer queries.
- RSIS3 relevance: mykb's TF-IDF pipeline and any embedding model each apply their own tokenizer — consistency matters for hybrid fusion.

## Related
- [[wiki/data-storage/n-grams|N-grams]] — contiguous token sequences built after tokenization
- [[wiki/data-storage/stemming|Stemming]] — normalizes tokens to root forms
- [[wiki/data-storage/stopwords|Stopwords]] — tokens often filtered after tokenization
- [[wiki/data-storage/tf-idf|TF-IDF]] — the weighting scheme that consumes tokens
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — chunk sizes are measured in tokens
- [[wiki/data-storage/index|Data Storage]] — text preprocessing
