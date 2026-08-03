---
type: "concept"
title: "Grep Patterns"
description: "Searching text with the grep family: matching lines against patterns"
tags: ["grep", "search", "regex", "text"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Grep Patterns

## Summary
grep searches input for lines matching a pattern and prints the matches. With `-E` (extended regex), `-v` (invert), `-r` (recursive), `-c` (count), and `-l` (file names), it is the universal text search tool; ripgrep (`rg`) is the faster, modern implementation that most developers reach for first, and its exit-status contract is identical to grep's.

## Details
- Mechanism: grep reads lines from files or stdin and applies the pattern (basic regex by default; `-E` for extended, `-P` for PCRE on GNU grep) with leftmost-longest or leftmost-first semantics depending on flavor; `-i` ignores case, `-w` matches whole words, `-x` whole lines, `-v` inverts, and `-o` prints only the matched part. Recursive search (`-r`) descends directories, `-l`/`-L` list matching/non-matching files, `-C 3`/`-B`/`-A` add context, and `--exclude`/`--include` filter file names. ripgrep adds sane defaults (respects `.gitignore`, skips binaries, searches hidden files only with `--hidden`) and is typically an order of magnitude faster on large trees.
- Concrete examples: `rg -n "status: \"growing\"" components/mykb/wiki` finds all promoted articles; `rg -l "TODO" src/` lists files with TODOs; `grep -c '^ERROR' app.log` counts error lines; `ps aux | grep -v grep | grep java` filters its own noise; `rg "pattern" --type py` restricts to Python files; `echo $PATH | tr ':' '\n' | grep -qx "$HOME/bin"` checks membership exactly.
- Failure modes: the classic mistakes are forgetting that grep's exit status distinguishes "no match" (1) from "error" (2) — a script treating 1 as failure for a search-and-maybe action is usually wrong — and regex surprises: a pattern with special characters matched literally (`grep .` matches everything), `^`/`$` anchoring subtleties, and catastrophic backtracking in `-P` patterns on hostile input. Case sensitivity and locale-dependent character classes (`[a-z]` vs `[[:alpha:]]`) cause mismatches, and `grep -v` pipelines silently change exit status when nothing is left.
- Operational tradeoffs: grep/ripgrep are the filter stage of every text pipeline — cheap, composable, streaming — and the tradeoff is simplicity versus expressiveness: for structured queries (JSON, CSV, logs with fields), jq or awk are better tools, and for huge corpora a real index beats linear scanning. The practice rules: use `rg` for code search (`.gitignore`-aware, fast, colorized), reserve plain grep for pipelines and one-off checks, always think about the exit code in scripts, and quote patterns so the shell does not expand them.
- RSIS3/mykb relevance: finding concepts and links across the wiki corpus is grep work; the agent toolchain's search over MyKB uses the same pattern-over-lines model, and the exit-status discipline (0/1/2) is exactly how RSIS3 tools should report found/not-found/error outcomes.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — grep is the filter stage
- [[wiki/os-shell/regex-engines|Regex Engines]] — grep patterns are regular expressions
- [[wiki/os-shell/glob-patterns|Glob Patterns]] — globs select files; grep selects lines
- [[wiki/dev-tools/jq-querying|Jq Querying]] — jq extends search to JSON structure
- [[wiki/devops-infra/observability|Observability]] — grep is the first log query
