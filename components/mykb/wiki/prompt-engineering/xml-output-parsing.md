---
type: "concept"
title: "XML Output Parsing"
description: "Using XML as a model output format and parsing it reliably"
tags: ["xml-parsing", "xml", "structured", "parsing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# XML Output Parsing

## Summary
Using XML as a model output format and parsing it reliably

## Details
- XML tags delimit fields, making extraction robust when generation is imperfect.
- Parsers must handle malformed or partial XML gracefully.
- A fallback when JSON guarantees are unavailable.
- Common in older agent and tool protocols.

## Related
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — output family
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — JSON alternative
- [[wiki/prompt-engineering/csv-tsv-output-parsing|CSV and TSV Output Parsing]] — tabular alternative
- [[wiki/prompt-engineering/markdown-output-rendering|Markdown Output Rendering]] — text alternative
- [[wiki/prompt-engineering/output-format-negotiation|Output Format Negotiation]] — format choice
