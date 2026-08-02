---
type: "entity"
title: "Bash Scripting Patterns"
tags: ["shell", "bash", "scripting", "terminal", "automation"]
source: ["sessions/"]
status: "growing"
---

# Bash Scripting Patterns

Shell scripting patterns observed across the ecosystem — from Termux automation to build pipelines.

## Common Patterns

### Colorized Output
echo "═══ TITLE ═══"
echo "✓ Success"
echo "✗ Failure"

### Port Detection (Android-safe)
port=8091
while nc -z 127.0.0.1 $port 2>/dev/null; do port=$((port + 1)); done

### Process Management
PID=$!
sleep 2
kill $PID 2>/dev/null
wait $PID 2>/dev/null

## Error Handling

Robust scripts treat every command as fallible. The `set -e` option aborts on the first failing command, but it is blunt: a command that fails inside a condition or pipeline may exit the whole script unexpectedly. The finer-grained approach combines `set -euo pipefail` — errexit, nounset, and pipefail — with explicit checks of exit statuses. [[wiki/os-shell/errexit-and-shell-options|errexit and shell options]] documents the trade-offs, and [[wiki/os-shell/exit-codes|exit codes]] explains how to interpret command results. A script should also set its own exit code deliberately so callers can distinguish success, warning, and failure paths.

## Portability

Scripts that run on both Termux and desktop Linux must avoid GNU-isms and locale-dependent output. Use portable alternatives — `printf` instead of `echo` for predictable formatting, `nc -z` for connectivity probes, and explicit paths for tools that differ between environments. [[wiki/os-shell/brace-expansion|brace expansion]] and [[wiki/os-shell/command-substitution|command substitution]] are core features to understand before relying on them, because quoting inside substitutions is a common source of subtle bugs. Prefer `$(...)` over backticks, and always quote expansions: unquoted variables split on whitespace and glob characters, which corrupts filenames and arguments.

## Automation Patterns

Automation scripts share a shape: detect prerequisites, run the work, verify the result, and report. Port detection loops probe until a free port is found, as in the example above; process management captures `$!` right after launching, then polls or kills by PID. [[wiki/os-shell/environment-variables|environment variables]] carry configuration between invocations, and exit codes plus a final summary line make the script friendly to CI logs. The [[wiki/shell-environment/index|Shell Environment]] and [[wiki/os-shell/index|OS & Shell]] clusters collect the surrounding reference material for these patterns.

See also: [[wiki/shell-environment/index|Shell Environment]], [[wiki/os-shell/index|OS & Shell]]
