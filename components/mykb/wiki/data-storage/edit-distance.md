---
type: "concept"
title: "Edit Distance"
description: "Minimum number of edits (insert, delete, substitute) to turn one string into another"
tags: ["edit-distance", "levenshtein", "strings", "fuzzy"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Edit Distance

## Summary
Edit distance, most commonly Levenshtein distance, counts the minimal insertions, deletions, and substitutions between two strings. It powers fuzzy matching, autocorrect, and record linkage on names.

## Details
- **Algorithm** — dynamic programming over prefixes; O(n*m) time for Levenshtein.
- **Variants** — Damerau adds transpositions; Hamming requires equal length; longest common subsequence is deletion-only.
- **Use** — typo-tolerant search, entity matching, and OCR cleanup; too slow for corpus-wide comparison without blocking.

## Related
- [[wiki/data-storage/jaccard-similarity|Jaccard Similarity]] — set-level closeness for shingles
- [[wiki/data-storage/n-grams|N-grams]] — character n-grams approximate edit distance cheaply
- [[wiki/data-storage/deduplication|Deduplication]] — fuzzy duplicate detection
- [[wiki/data-storage/semantic-search|Semantic Search]] — lexical fuzzy matching as a search layer
- [[wiki/data-storage/index|Data Storage]] — string similarity family
