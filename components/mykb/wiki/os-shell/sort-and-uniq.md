---
type: "concept"
title: "sort & uniq"
description: "Field/version sorting and deduplication"
tags: ["sort", "uniq", "text", "command-line"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html", "https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html"]
---

# sort & uniq

## Summary
sort orders lines and uniq collapses adjacent duplicates; together they deduplicate, count, and group text data. Sorting by fields, numbers, and version numbers covers most log and data-analysis needs.

## Details
- Default sort is byte-wise lexicographic in the locale; -n compares numbers, -h human sizes (2K, 10M), and -V version numbers (v1.2 < v1.10).
- Field sorting: -k 2,2 sorts by the second field, -t : sets the delimiter; -s keeps stable order for equal keys.
- -r reverses, -u outputs only unique lines, -f folds case, -c checks whether input is sorted, and -z uses NUL separators for arbitrary filenames.
- Sorting huge files: use --buffer-size and -T for temp space; for streaming uniqueness keep runs sorted first.
- uniq assumes sorted input: -c counts occurrences, -d prints only duplicates, -u only singletons, and -f/-s skip fields or characters.
- The classic log-analysis chain: grep | awk '{print $1}' | sort | uniq -c | sort -rn for a top-N histogram.
- For set operations across files, comm needs sorted inputs and gives intersection, union, and difference.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — where sort/uniq stage
- [[wiki/os-shell/cut-paste-and-column-tools|Column Tools]] — field extraction before sorting
- [[wiki/os-shell/grep-patterns|Grep Patterns]] — selecting lines to sort
- [[wiki/os-shell/awk-text-processing|Awk Text Processing]] — the compute stage in the chain
- [[wiki/dev-tools/semver-tooling|Semver Tooling]] — version-aware sorting
