---
type: "concept"
title: "CSV and TSV Output Parsing"
description: "Parsing tabular model outputs in CSV or TSV for downstream processing"
tags: ["csv-parsing", "csv", "structured", "parsing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# CSV and TSV Output Parsing

## Summary
Parsing tabular model outputs in CSV or TSV for downstream processing

## Details
- Tables benefit from simple delimiters but suffer quoting issues.
- Validation should check column counts and escaping.
- Better for bulk tabular extraction than JSON.
- Feeds data pipelines and analytics.

## Related
- [[wiki/prompt-engineering/table-output-generation|Table Output Generation]] — generation side
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — family
- [[wiki/prompt-engineering/xml-output-parsing|XML Output Parsing]] — sibling format
- [[wiki/prompt-engineering/output-format-negotiation|Output Format Negotiation]] — format choice
- [[wiki/agent-systems/data-science-agents|Data Science Agents]] — consumer
