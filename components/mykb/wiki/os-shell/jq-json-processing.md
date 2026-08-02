---
type: "concept"
title: "jq"
description: "Filtering and transforming JSON in pipelines"
tags: ["jq", "json", "processing", "cli"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://jqlang.github.io/jq/manual/"]
---

# jq

## Summary
jq is a command-line processor for JSON: it filters, extracts, and transforms structured data with a small functional language. It is the standard tool for pulling fields out of API responses and reshaping JSON in pipelines.

## Details
- Basic filters: .key selects a field, .[] iterates arrays, .[0] indexes, .a.b chains; length, keys, and type inspect values.
- map, select, and pipes compose: .items | map(select(.active)) | map(.name) applies transformations in one pass.
- -r emits raw strings instead of JSON quotes, making jq output safe for cut, grep, and shell variables; -c gives compact lines.
- Constructing output: {name: .user.name, id: .id} builds objects, and @csv/@tsv/@"\(.x)" formats arrays for tables.
- Variables and functions: . as $root | ... captures context, def f(x): ...; defines reusable filters.
- Slurp mode (-s) reads the whole document as an array; from_entries/to_entries convert between objects and key/value lists.
- jq reads stdin or files, and exit status is 0 on success, 1 on invalid input, 2 on usage error; jq errors out on malformed JSON.

## Related
- [[wiki/dev-tools/jq-querying|Jq Querying]] — query patterns for structured data
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — jq as the JSON stage
- [[wiki/os-shell/curl-and-http-clients|curl & HTTP Clients]] — fetching the JSON jq consumes
- [[wiki/data-storage/json-ld|JSON-LD]] — structured data beyond plain JSON
- [[wiki/api-protocols/openapi|OpenAPI]] — the schemas jq output often feeds
