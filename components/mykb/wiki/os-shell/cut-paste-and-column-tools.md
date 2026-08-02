---
type: "concept"
title: "Column Tools"
description: "cut, paste, column, join for tabular text"
tags: ["cut", "paste", "column", "join", "text"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html", "https://man7.org/linux/man-pages/man1/column.1.html"]
---
# Column Tools
## Summary
cut, paste, column, and join manipulate tabular text: cut selects fields or characters per line, paste merges lines side by side, column aligns output into tables, and join merges rows on a shared key.
## Details
- cut -d ',' -f 2,3 picks fields by delimiter; -c 1-5 and -b 1-5 select characters or bytes; --complement inverts the selection.
- paste -d ':' file1 file2 puts lines of several files on one line; paste -s - joins lines within a file into a single row.
- column -t aligns whitespace-delimited columns into neat tables; -s ':' -t works for custom delimiters, and -N names header fields.
- join requires both inputs sorted on the key: join -t, -1 2 -2 1 file1 file2 merges on field 2 of the first and field 1 of the second.
- comm -12 a b computes set intersection on sorted files; comm needs no delimiter and is the partner of join for line sets.
- Pipeline flow: cut extracts columns, sort orders them, join merges datasets, column renders the result for humans.
- Quoting inside fields (CSV with commas) breaks naive cut; awk with a real CSV parser or a tool like csvkit handles that case.
## Related
- [[wiki/os-shell/sort-and-uniq|sort & uniq]] — ordering before join and comm
- [[wiki/os-shell/awk-text-processing|Awk Text Processing]] — the general field processor
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — assembling these stages
- [[wiki/os-shell/jq-json-processing|jq]] — structured alternative for JSON
- [[wiki/os-shell/sed-editing|sed Editing]] — line-oriented text surgery
