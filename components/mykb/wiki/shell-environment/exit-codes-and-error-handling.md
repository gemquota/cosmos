---
type: "concept"
title: "Exit Codes & Error Handling"
description: "The 0-255 exit status contract and set -e style error propagation"
tags: ["shell", "exit-codes", "bash", "errors"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Exit Codes & Error Handling

## Summary
The 0-255 exit status contract and set -e style error propagation. Exit codes are the only reliable channel a command has to report success or failure to its caller, and scripts that ignore or mask them produce silent corruption instead of loud failures.

## Details
- **The contract** — every command exits with a status in 0-255: 0 means success, non-zero means failure; the value is a uint8, so negative or large numbers wrap (exit -1 becomes 255); by convention 1-127 are application errors, 126 means 'found but not executable', 127 means 'command not found', and 128+n means killed by signal n (e.g., 130 = SIGINT); scripts that exit with arbitrary large values get them truncated, which breaks documented exit-code contracts.
- **Reading status** — `$?` holds the previous command's status, but it is consumed by the very next command, so capture it immediately; `&&` and `||` branch on status without blocking the script, and `if cmd; then` runs the command directly in the condition, which is the robust way to test failure rather than wrapping it in a subshell.
- **set -e mechanics** — `set -e` (errexit) exits the script on any command that returns non-zero, but with well-known exceptions: commands in `if`/`while`/`until` conditions, commands in `&&`/`||` lists except the last, commands whose failure is explicitly tested, and most commands in a pipeline except the last; these exceptions exist so tests and conditional checks do not kill the script, and they are the usual source of 'why did set -e not catch that?' confusion.
- **Pipelines** — by default a pipeline's status is the last command's status, so a failing `grep` or `head` in the middle is invisible; `set -o pipefail` makes the pipeline return the rightmost non-zero status, and combining `set -euo pipefail` with checking `${PIPESTATUS[@]}` is the standard hardening recipe for every script that processes text.
- **Failure modes** — the dangerous patterns are: ignoring status (a failed `rm`, `mv`, or `sed` that leaves the file system half-updated while the script continues), masking errors with unconditional `|| true`, using `$?` after it was already consumed, `set -e` in functions invoked in conditions where the shell disables errexit, and exit-code collisions (two unrelated errors both returning 1, so callers cannot distinguish them).
- **Design guidance** — return distinct codes per error class (usage error, missing input, partial failure), print the failing command and context to stderr before exiting, and let the script's exit code propagate through CI: a job that exits 0 despite a failed step invalidates every downstream gate; trap EXIT/ERR can log the failing line number for debugging.
- **RSIS3 relevance** — RSIS3's automation runs shell pipelines for builds, snapshot regeneration, and practice checks; each run's exit status is the first signal the loop logs, so the telemetry layer should record status, stderr tail, and the failing pipeline stage — an exit-0 run with corrupted output is worse than a loud failure.

## Related
- [[wiki/devops-infra/slo-and-error-budgets|SLOs & Error Budgets]] — related coverage in the same cluster
- [[wiki/os-shell/syscalls-and-trap-handling|Syscalls & Trap Handling]] — related coverage in the same cluster
- [[wiki/os-shell/exit-codes|Exit Codes]] — related coverage in the same cluster
- [[wiki/devops-infra/error-budgets|Error Budgets]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
