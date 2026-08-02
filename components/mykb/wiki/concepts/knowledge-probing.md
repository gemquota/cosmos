---
type: "concept"
title: "Knowledge Probing"
description: "Testing what knowledge a model stores and can recall"
tags: ["probing", "knowledge", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Knowledge Probing

## Summary
Knowledge probing tests whether a model holds specific facts and can retrieve them under controlled prompts.

## Details
- Knowledge probing tests whether a model holds specific facts and can retrieve them under controlled prompts.
- Probes distinguish stored knowledge from surface pattern-matching by varying phrasing and context.
- Negative probes (should-not-know facts) are safety-critical.
- RSIS3 relevance: the gap detector is a knowledge probe over the wiki's coverage.

## Related
- [[wiki/concepts/elicitation-techniques|Elicitation Techniques]] — the family
- [[wiki/concepts/probing-classifiers|Probing Classifiers]] — the classifier variant
- [[wiki/concepts/training-data-memorization|Training Data Memorization]] — what probes may find
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — stored-knowledge substrate
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
