---
type: "concept"
title: "Command Substitution"
description: "$(...) and backticks, output capture, and word splitting"
tags: ["command-substitution", "shell", "bash", "pipelines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html"]
---

# Command Substitution

## Summary
Command substitution captures a command's stdout and splices it into the current command line: $(date) or the legacy `date`. It runs the command in a subshell, strips trailing newlines from the output, and the result is then subject to word splitting and globbing unless quoted.

## Details
- Prefer $(...) over backticks: it nests cleanly ($(cmd1 $(cmd2))), and backslashes behave predictably inside $(...).
- The command runs in a subshell, so variable assignments inside it do not affect the parent; use process substitution or temp files to mutate state.
- Unquoted substitution results are word-split on IFS — the source of the classic "command not found: foo bar" bug; always quote: "$(cmd)".
- Trailing newlines are removed; embedded newlines are preserved and become part of the value.
- $(<file) is a bash optimization that reads a file without forking; printf -v var '%s' "$(cmd)" avoids a fork for simple cases.
- Exit status: the substitution's status is the command's; set -e and pipefail treat it like any other command.
- zsh matches bash here, but with SH_WORD_SPLIT off by default, unquoted substitutions do not split.

## Related
- [[wiki/os-shell/shell-expansion-order|Shell Expansion Order]] — substitution runs before splitting
- [[wiki/os-shell/quoting-rules|Quoting Rules]] — why quoted substitution is safer
- [[wiki/os-shell/process-substitution|Process Substitution]] — the <(...) alternative that avoids capture
- [[wiki/os-shell/parameter-expansion|Parameter Expansion]] — storing results in variables
- [[wiki/os-shell/errexit-and-shell-options|Errexit & Shell Options]] — failure propagation from substitutions
