---
type: "concept"
title: "Parameter Expansion"
description: "${var:-default}, slicing, substitution, and indirection"
tags: ["parameter-expansion", "shell", "bash", "variables"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html"]
---
# Parameter Expansion
## Summary
Parameter expansion is the shell's variable machinery: ${var} interpolates a value, and a rich set of operators provides defaults, length, slicing, pattern substitution, case changes, and indirection.
## Details
- Defaults: ${var:-fallback} uses fallback only if unset or empty; ${var:=fallback} also assigns it; ${var:+alt} uses alt only when set; ${var:?msg} errors out if unset.
- Length and slicing: ${#var} gives length; ${var:offset:length} extracts a substring (also on arrays); negative offsets count from the end.
- Substitution: ${var/pat/repl} replaces the first match, ${var//pat/repl} all matches; ${var#pat} and ${var##pat} strip shortest/longest prefix, % and %% suffix.
- Case: ${var^} uppercases the first character, ${var^^} all, and lowercase with, and,.
- Indirection: ${!name} expands to the value of the variable named by name; declare -n namerefs give call-by-reference for functions.
- Arrays: ${arr[@]} all elements, ${#arr[@]} count, ${!arr[@]} indices; the same operators work on individual elements.
- Bash 4+ string transformations make awk/sed substitution in shell much less common; zsh adds ${(f)var} splitting and similar flags.
## Related
- [[wiki/os-shell/shell-expansion-order|Shell Expansion Order]] — where parameter expansion sits
- [[wiki/os-shell/quoting-rules|Quoting Rules]] — double quotes preserve expanded values
- [[wiki/os-shell/arrays-in-shell|Arrays in Bash/Zsh]] — expansion over whole arrays
- [[wiki/os-shell/environment-variables|Environment Variables]] — the exported form of parameters
- [[wiki/os-shell/errexit-and-shell-options|Errexit & Shell Options]] — ${var:?} as a guard
