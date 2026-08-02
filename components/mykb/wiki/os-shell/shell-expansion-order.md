---
type: "concept"
title: "Shell Expansion Order"
description: "The sequence bash/zsh apply brace, tilde, parameter, and other expansions"
tags: ["shell", "expansion", "bash", "zsh", "parsing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html", "https://zsh.sourceforge.io/Doc/Release/Expansion.html"]
---

# Shell Expansion Order

## Summary
Bash and zsh transform command text through a fixed pipeline of expansions. Getting the order right explains otherwise mysterious behavior: brace expansion happens first, then tilde, parameter, command, and arithmetic expansion, then word splitting, pathname expansion, and finally quote removal.

## Details
- Brace expansion {a,b} and {1..3} runs first, purely textually, before any variable or glob expansion — so {a,$b} expands braces even when $b is unset.
- Tilde expansion (~, ~user) follows; it occurs only at the start of a word or after : and = in assignments.
- Parameter expansion ($var), command substitution ($(...)), and arithmetic expansion ($((...))) happen next, left to right in a single pass.
- Word splitting then splits the results on IFS (space, tab, newline); quoting suppresses it, which is why "$var" is the safe form.
- Pathname expansion (globbing) runs after splitting, matching * ? [ ] against filenames, and unmatched globs stay literal by default.
- Quote removal strips syntactic quotes last; redirections are processed as commands are executed, not expanded.
- Zsh differences: no word splitting by default, glob qualifiers and extended globbing, and SH_WORD_SPLIT needed to mimic bash.

## Related
- [[wiki/os-shell/quoting-rules|Quoting Rules]] — the control that tames splitting and globbing
- [[wiki/os-shell/brace-expansion|Brace Expansion]] — the first stage in the pipeline
- [[wiki/os-shell/parameter-expansion|Parameter Expansion]] — the variable machinery
- [[wiki/os-shell/command-substitution|Command Substitution]] — embedding command output
- [[wiki/os-shell/glob-patterns|Glob Patterns]] — the final filename matching stage
