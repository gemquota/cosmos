---
type: "concept"
title: "Sed Editing"
description: "The stream editor for scripted, non-interactive text transformations"
tags: ["sed", "text", "stream", "editing"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Sed Editing

## Summary
sed (stream editor) applies scripted edits — substitute, delete, print, insert — to a text stream without opening an editor. `sed -i 's/old/new/g' file` is the canonical in-place replace.

## Details
- Addresses select lines: `sed -n '10,20p'` prints a range; substitutions support capture groups.
- `-i` edits in place (use with care); `-E` enables extended regex.
- RSIS3 relevance: batch renaming and frontmatter edits across wiki files are sed tasks.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — sed is a pipeline transformation stage
- [[wiki/os-shell/awk-text-processing|Awk Text Processing]] — awk for fields, sed for line edits
- [[wiki/os-shell/regex-engines|Regex Engines]] — sed depends on regular expression engines
- [[wiki/software-engineering/refactoring|Refactoring]] — mechanical text changes at scale
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — batch edits curate notes
