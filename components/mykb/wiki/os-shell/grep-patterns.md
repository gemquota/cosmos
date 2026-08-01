---
type: "concept"
title: "Grep Patterns"
description: "Searching text with the grep family: matching lines against patterns"
tags: ["grep", "search", "regex", "text"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Grep Patterns

## Summary
grep searches input for lines matching a pattern and prints them. With -E (extended regex), -v (invert), -r (recursive), and -c (count), it is the universal text search tool; ripgrep (rg) is the faster modern implementation.

## Details
- Exit status is part of the contract: 0 found, 1 not found, 2 error — useful in scripts.
- Recursive search with context (`-C 3`) and file listing (`-l`) dominate code search.
- RSIS3 relevance: finding concepts and links across the wiki corpus is grep work.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — grep is the filter stage
- [[wiki/os-shell/regex-engines|Regex Engines]] — grep patterns are regular expressions
- [[wiki/os-shell/glob-patterns|Glob Patterns]] — globs select files; grep selects lines
- [[wiki/dev-tools/jq-querying|Jq Querying]] — jq extends search to JSON structure
- [[wiki/devops-infra/observability|Observability]] — grep is the first log query
