---
type: "concept"
title: "Exit Codes"
description: "The integer status a process returns to its parent to report success or failure"
tags: ["exit-codes", "shell", "status", "contract"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Exit Codes

## Summary
Every process ends by returning a small integer to its parent: 0 means success, any non-zero value means failure, and a handful of codes have conventional meanings — 126 for "found but not executable", 127 for "command not found", and 128+N for death by signal N. Shells and pipelines treat this integer as the truth about whether a command worked.

## Details
- Mechanism: a process's `main` returns a value (or calls `exit(n)`), the kernel delivers it to the waiting parent via `waitpid`, and the shell stores it in `$?` immediately after each command. The shell's grammar consumes it directly: `if cmd; then` branches on `cmd`'s exit status without any explicit comparison, `&&` runs the right side only on 0, and `||` only on non-zero. By convention 1 is generic failure, 2 is usage error (grep uses it for errors, distinguishing it from "no match" which is 1), and commands like `curl`, `ssh`, and `rsync` define their own ranges to encode distinct failure causes.
- Concrete examples: `grep pattern file` returns 0 on a match, 1 on no match, and 2 on an error — a script must distinguish them; `set -e` makes a script exit on the first command returning non-zero, `set -o pipefail` makes a pipeline's status the last non-zero status among its stages, and `set -u` catches unset variables; `command -v foo || exit 127` checks for a missing tool; a daemon returns 0 on clean shutdown and 1 on a fatal config error so systemd can report it.
- Failure modes: the classic failures are pipelines whose final stage masks an earlier failure (`cmd1 | cmd2` reports only `cmd2`'s status unless `pipefail` is set), commands that return 0 despite failing (a `curl` without `-f` returns 0 on HTTP 404), scripts that use `$?` after another command has already overwritten it, and exit codes above 255 (the value is truncated mod 256, so 300 becomes 44). Neglecting `set -euo pipefail` lets scripts continue after failures and "succeed" while doing nothing.
- Operational tradeoffs: a disciplined exit-code contract is the cheapest reliability mechanism in Unix: every tool declares success/failure, and every script can chain on it. The tradeoffs are that 0-255 is a small namespace (encode distinct errors via stderr and logs, not just the code), and that some programs need `|| true` or explicit handling to be intentionally non-fatal. The practice rules: `set -euo pipefail` in every script, use `trap` for cleanup on failure, check `$?` immediately, and document non-standard codes.
- RSIS3/mykb relevance: the harness treats non-zero exits from agent tools as actionable signals; capturing exit codes plus stderr as structured outcomes (not just pass/fail) is exactly how RSIS3 records tool results in the registry for L2 improvement loops.

## Related
- [[wiki/os-shell/process-management|Process Management]] — exit status ends the process lifecycle
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — scripts are judged by their exit code
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — CLI contract includes exit status
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — pipelines gate on exit codes
- [[wiki/api-protocols/health-checks|Health Checks]] — exit codes are process health signals
