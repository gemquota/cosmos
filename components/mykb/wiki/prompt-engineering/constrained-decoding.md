---
type: "concept"
title: "Constrained Decoding"
description: "Forcing generation to respect hard constraints such as schemas or grammars"
tags: ["constrained-decoding", "decoding", "constraints", "structured"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Constrained Decoding

## Summary
Forcing generation to respect hard constraints such as schemas or grammars

## Details
- Constraints apply at token selection time, guaranteeing compliance.
- Examples: JSON schema, regex, and formal grammar enforcement.
- More reliable than prompting alone.
- Tooling exists in outlines and guidance libraries.

## Related
- [[wiki/prompt-engineering/grammar-constrained-generation|Grammar-Constrained Generation]] — grammar variant
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — schema variant
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — goal
- [[wiki/prompt-engineering/xml-output-parsing|XML Output Parsing]] — format family
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — constraint source
