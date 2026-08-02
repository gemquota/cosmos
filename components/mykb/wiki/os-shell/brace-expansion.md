---
type: "concept"
title: "Brace Expansion"
description: "{a,b} generation, sequences, and interaction with other expansions"
tags: ["brace-expansion", "shell", "bash", "sequences"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html"]
---

# Brace Expansion

## Summary
Brace expansion generates multiple words from a pattern: {a,b,c} yields a b c, and {1..10} or {1..10..2} yields numeric sequences. It is purely textual and happens first in the expansion pipeline, before variables and globs.

## Details
- Comma lists {red,green,blue} expand to one word per element; nested braces and combinations multiply: {a,b}{1,2} gives a1 a2 b1 b2.
- Sequence ranges {1..5}, {01..10} (zero-padded), {a..e}, and steps {1..10..2} produce ordered words; descending {10..1} works too.
- Because it runs before parameter expansion, a variable inside braces is not expanded into elements — construct lists explicitly when data is dynamic.
- Brace expansion also drives mkdir -p dir/{a,b,c} and cp file{,.bak} idioms, which rely on expansion before pathname matching.
- zsh implements the same feature; zsh's globbing can also do numeric ranges directly in patterns.
- Disable with set +B or shopt -u braceexpand? No — set -B enables it; set +B disables; it is on by default in interactive bash.
- Beware unintended expansion in unknown text: braces in filenames or JSON templates need quoting.

## Related
- [[wiki/os-shell/shell-expansion-order|Shell Expansion Order]] — braces run first
- [[wiki/os-shell/quoting-rules|Quoting Rules]] — how to suppress accidental expansion
- [[wiki/os-shell/glob-patterns|Glob Patterns]] — the filename stage that follows
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — expansion idioms in scripts
- [[wiki/os-shell/path-resolution|Path Resolution]] — where generated paths get resolved
