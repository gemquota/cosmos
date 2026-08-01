---
type: "concept"
title: "Shell Aliases"
description: "User-defined shorthand that expands to longer commands"
tags: ["aliases", "shell", "shortcuts", "productivity"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Shell Aliases

## Summary
Aliases map a short name to a command: `alias ll='ls -la'`. They shrink repetitive typing but do not take arguments — for that, use a function.

## Details
- Defined in the shell rc file; `alias` lists current aliases, `unalias` removes them.
- Functions (`ll() { ls -la "$@"; }`) handle arguments and are preferred for logic.
- RSIS3 relevance: agents keep a curated alias set per session for repeated tool calls.

## Related
- [[wiki/os-shell/dotfiles|Dotfiles]] — aliases live in dotfiles
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — zsh adds global and suffix aliases
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — aliases reshape CLI usage
- [[wiki/software-engineering/developer-experience|Developer Experience]] — aliases cut friction
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — aliases shorten repeated tool calls
