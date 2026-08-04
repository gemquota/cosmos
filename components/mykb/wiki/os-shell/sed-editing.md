---
type: "entity"
title: "Sed Editing"
description: "The stream editor for scripted, non-interactive text transformations"
tags: ["sed", "text", "stream", "editing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Sed Editing

## Summary
sed (stream editor) applies scripted edits — substitute, delete, print, insert — to a text stream without opening an interactive editor. Its canonical form, `sed -i 's/old/new/g' file`, is the workhorse of scripted in-place replacement, and its line-addressed, regex-driven model makes it the transformation stage of countless pipelines.

## Details
- Mechanism: sed reads input line by line, applies the script's commands in order, and writes the result; by default it prints every line, so `p` (print) and `-n` (suppress auto-print) work together. Commands take addresses: `sed -n '10,20p'` prints lines 10-20, `sed '/^#/d'` deletes comment lines, `sed '2,4s/foo/bar/'` substitutes only in that range, and `$` addresses the last line. Substitutions support capture groups with `\1` (BRE) or `\1` with `-E` (ERE), flags like `g` (global), `i` (case-insensitive on GNU), and `p` (print only changed lines). The `s///` delimiter can be any character (`s|/usr|/opt|`), which avoids leaning-toothpick escapes when paths contain slashes.
- Concrete examples: `sed -i 's/status: "stub"/status: "growing"/' article.md` flips a frontmatter field; `sed -n '1,20p' log.txt` extracts a head range; `sed -i '/^DEBUG/d' app.log` strips debug lines; `sed 's/^/  /' file` indents every line; `sed -E 's/([0-9]{4})-([0-9]{2})/\2-\1/'` reorders date components; `sed 'N;N;s/\n/ /g'` joins triples of lines.
- Failure modes: the classic failures are `-i` on a symlink or across platforms (GNU `sed -i` follows symlinks and creates a new file, breaking hard links and permissions unless `--follow-symlinks` or a temp-file strategy is used; BSD/macOS `sed -i` requires a suffix argument), substitution delimiter or escape mistakes that silently match nothing, and greedy `.*` replacements that eat more than intended. Editing in place without a backup (`-i.bak`) is one power cut away from data loss, and using sed where structure matters (YAML, JSON) corrupts files that a real parser would preserve.
- Operational tradeoffs: sed is the fastest way to do mechanical, line-oriented edits across many files — zero dependencies, streaming, scriptable — and the tradeoff is its limits: no multi-line awareness by default, no field logic (awk's job), and no structural parsing. The practice rules: use `-i.bak` or edit in a git working tree, prefer `-E` for readable regex, test the command on a sample (`sed -n 's/old/new/p'`) before applying `-i`, and escalate to awk or a real parser the moment edits need context beyond a line. RSIS3 relevance: batch renaming and frontmatter edits across wiki files are sed tasks, and the same care — preview, backup, idempotency — applies to the harness's bulk rewrite passes.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — sed is a pipeline transformation stage
- [[wiki/os-shell/awk-text-processing|Awk Text Processing]] — awk for fields, sed for line edits
- [[wiki/os-shell/regex-engines|Regex Engines]] — sed depends on regular expression engines
- [[wiki/software-engineering/refactoring|Refactoring]] — mechanical text changes at scale
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — batch edits curate notes
