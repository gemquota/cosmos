---
type: "concept"
title: "Byte-Pair Encoding"
description: "BPE: a bottom-up subword algorithm that iteratively merges the most frequent adjacent symbol pairs"
tags: ["byte-pair-encoding", "bpe", "tokenization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1508.07909", "https://en.wikipedia.org/wiki/Byte_pair_encoding"]
---

# Byte-Pair Encoding

## Summary
BPE builds a token vocabulary by repeatedly merging the most frequent pair of adjacent symbols in a corpus until the target vocabulary size is reached. GPT, Llama, and many other LLM tokenizers use BPE (often byte-level).

## Details
- Byte-level BPE avoids out-of-vocabulary characters entirely by starting from bytes.
- Vocabulary merges reflect corpus statistics, so domain text tokenizes more efficiently after custom training.
- Tokenizer choice changes token counts by tens of percent on the same text — relevant for cost.
- RSIS3 relevance: mykb's token accounting should use the exact tokenizer of the model in use, not estimates.
- Byte-pair encoding (BPE) builds a subword vocabulary greedily: it starts with characters and repeatedly merges the most frequent adjacent pair, adding each merged pair as a new token.
- BPE was adapted from data compression to machine translation for open-vocabulary modeling and remains the default tokenizer for most LLMs.
- The merge operations are deterministic given a corpus and target size, which makes BPE simple to implement and reproduce.
- BPE's biases — favoring frequent byte pairs and handling whitespace inconsistently — shape how models see text, including multilingual text.
- **Worked example / comparison** — Worked example — starting from bytes, 'th' and 'e' are common pairs, so merges like 'the' form early, while rare sequences stay split into byte-level tokens.
- For mykb, byte-pair-encoding is the concrete algorithm behind subword-tokenization and is paired with sentencepiece in the tokenizer cluster.

## Related
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]]
- [[wiki/ai-ml/sentencepiece|SentencePiece]]
- [[wiki/prompt-engineering/token-budgets|Token Budgets]]
- [[wiki/ai-ml/llama|Llama]]
- [[wiki/ml-frameworks/hugging-face|Hugging Face]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
