---
type: "concept"
title: "Awk Text Processing"
description: "The awk language for pattern-scanning and field-oriented processing of text files"
tags: ["awk", "text", "scripts", "fields"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Awk Text Processing

## Summary
awk is a small programming language built for scanning text line by line and acting on field patterns: `awk '{print $1}'` prints the first field of every line. It is the tool of choice when columns matter more than lines.

## Details
- Pattern-action pairs: `awk '/error/ {print NR, $0}'` prints matching line numbers and content.
- Built-in variables NR, NF, FS, and OFS control records and field splitting.
- RSIS3 relevance: log parsing and CSV field extraction in the wiki toolchain use awk idioms.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — awk is the transformation stage of pipelines
- [[wiki/os-shell/sed-editing|Sed Editing]] — sed edits; awk computes
- [[wiki/os-shell/grep-patterns|Grep Patterns]] — awk supersets grep's filtering for structured data
- [[wiki/software-engineering/functional-programming|Functional Programming]] — awk maps functions over records
- [[wiki/devops-infra/observability|Observability]] — awk mines logs
