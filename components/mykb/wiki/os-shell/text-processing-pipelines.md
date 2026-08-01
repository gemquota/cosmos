---
type: "concept"
title: "Text Processing Pipelines"
description: "Chaining text-transforming commands so each stage filters or reshapes the stream"
tags: ["pipelines", "text", "unix", "grep-awk-sed"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/coreutils/manual/coreutils.html"]
---

# Text Processing Pipelines

## Summary
Text processing pipelines chain commands so each reads the previous stage's output, transforms it, and passes it on. Coreutils (cat, sort, uniq, head, tail, wc, cut, tr) plus grep, sed, and awk form the canonical toolkit for turning raw text into answers.

## Details
- The pipe operator connects stdout of one command to stdin of the next; each stage runs concurrently, bounded by the slowest stage.
- Canonical idiom: filter with grep, transform with sed or awk, aggregate with sort | uniq -c | sort -rn.
- Streaming matters: `tail -f access.log | grep ERROR` processes data as it arrives, enabling live monitoring.
- Powerful one-liners are built from small stages: `cut -d, -f2 file | sort -u | wc -l` counts unique fields.
- Text means everything can meet everything: logs, CSVs, JSON (via jq), and wiki markdown are all pipeline fodder.
- Efficiency tips: order filters to drop data early, prefer locale-safe tools, and know when a small script beats a long pipeline.
- RSIS3 relevance: mykb's markdown corpus is grep/awk-friendly, so agents and scripts can mine the wiki without a database.

## Related
- [[wiki/os-shell/grep-patterns|Grep Patterns]] — the filtering stage of most pipelines
- [[wiki/os-shell/awk-text-processing|Awk Text Processing]] — column and record processing
- [[wiki/os-shell/sed-editing|Sed Editing]] — stream edits for substitution and deletion
- [[wiki/dev-tools/jq-querying|Jq Querying]] — pipeline processing for JSON documents
- [[wiki/os-shell/stdin-stdout-stderr|Stdin Stdout Stderr]] — the streams pipelines move data through
- [[wiki/os-shell/unix-philosophy|Unix Philosophy]] — composition is the philosophy's core
- [[wiki/software-engineering/functional-programming|Functional Programming]] — pipelines are dataflow composition
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — structured text that pipelines can process
- [[wiki/devops-infra/observability|Observability]] — log pipelines are observability plumbing
