---
type: "concept"
title: "Command-Line Interfaces"
description: "Text-based interfaces for controlling programs: arguments, flags, stdin/stdout, and exit status"
tags: ["cli", "design", "interface", "terminal"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://clig.dev/"]
---

# Command-Line Interfaces

## Summary
A command-line interface (CLI) is a text interface where a program receives arguments, reads stdin, writes stdout and stderr, and returns an exit code. The Command Line Interface Guidelines (clig.dev) distill the design rules that make CLIs learnable and scriptable.

## Details
- Core contract: parse options (`-v`, `--verbose`), positional arguments, and subcommands; read data from stdin; write results to stdout and diagnostics to stderr.
- Exit codes carry machine-readable outcomes: 0 success, non-zero failure; distinct codes can encode specific errors.
- Design rules: consistent flags across subcommands, short aliases for common options, `--help` and `--version`, and human-readable error messages with hints.
- Composability is the goal: a CLI that follows conventions slots into pipelines and scripts without modification.
- Progressive disclosure: common tasks stay simple; `--help` and man pages reveal depth.
- RSIS3 relevance: the agent's tool use is CLI-shaped — clear contracts make tools callable by both humans and models.
- Worked example: `rg -n 'TODO' wiki/` — options, pattern, path, with exit 0 when matches exist and 1 when none.

## Related
- [[wiki/os-shell/unix-philosophy|Unix Philosophy]] — CLIs are the philosophy's interface
- [[wiki/os-shell/stdin-stdout-stderr|Stdin Stdout Stderr]] — the three streams every CLI speaks
- [[wiki/os-shell/exit-codes|Exit Codes]] — the machine-readable result channel
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — scripts compose CLIs
- [[wiki/dev-tools/curl-patterns|Curl Patterns]] — a canonical CLI for HTTP
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — agents depend on well-designed CLIs
- [[wiki/memory/obsidian|Obsidian]] — a GUI tool with a CLI-accessible vault
