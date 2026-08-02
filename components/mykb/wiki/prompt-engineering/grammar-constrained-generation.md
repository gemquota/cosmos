---
type: "concept"
title: "Grammar-Constrained Generation"
description: "Decoding restricted to tokens valid under a formal grammar"
tags: ["grammar-constrained", "grammar", "decoding", "structured"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Grammar-Constrained Generation

## Summary
Decoding restricted to tokens valid under a formal grammar

## Details
- A parser guides token choice so output always parses.
- Supports JSON, code, and domain-specific languages.
- Eliminates syntax errors by construction.
- Implemented by constrained-decoding engines.

## Related
- [[wiki/prompt-engineering/constrained-decoding|Constrained Decoding]] — umbrella
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — common instance
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — application
- [[wiki/prompt-engineering/latex-generation|LaTeX Generation]] — formal target
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — API payloads
