---
type: "concept"
title: "Glob Patterns"
description: "Shell wildcard patterns for matching filenames and paths"
tags: ["glob", "wildcards", "files", "shell"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Glob Patterns

## Summary
Globs match filenames with wildcards: `*` any run of characters, `?` one character, `[...]` character classes. `ls *.md` and `for f in wiki/**/*.md` are everyday glob uses.

## Details
- Globs expand before the command runs; quoting prevents expansion.
- `**` matches recursively in bash (with globstar) and zsh; dotfiles are not matched by `*`.
- RSIS3 relevance: batch operations over wiki files begin with glob patterns.

## Related
- [[wiki/os-shell/path-resolution|Path Resolution]] — globs expand into paths
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — globs drive scripted file loops
- [[wiki/os-shell/regex-engines|Regex Engines]] — globs are simpler, non-regex patterns
- [[wiki/os-shell/dotfiles|Dotfiles]] — why dotfiles need explicit globbing
- [[wiki/devops-infra/backups|Backups]] — backup filters use globs
