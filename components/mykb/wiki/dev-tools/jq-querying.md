---
type: "concept"
title: "Jq Querying"
description: "Filtering and transforming JSON from the command line with jq"
tags: ["jq", "json", "cli", "data-processing"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Jq Querying

## Summary
jq is the sed/awk of JSON: it filters, slices, and reshapes JSON documents in pipelines. One-liners like `.items[].name` extract fields from API responses without writing a program.

## Details
- Expressions combine path filters, pipes, maps, and conditionals; `-r` emits raw strings for further piping.
- jq makes API debugging scriptable: `curl ... | jq '.data'`.
- RSIS3 relevance: the wiki's JSON indexes are jq-queryable knowledge artifacts.

## Related
- [[wiki/dev-tools/curl-patterns|Curl Patterns]] — curl fetches, jq processes
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — jq slots into shell pipelines
- [[wiki/api-protocols/rest-apis|REST APIs]] — inspecting JSON API responses
- [[wiki/data-storage/json-ld|JSON-LD]] — linked data as JSON for querying
