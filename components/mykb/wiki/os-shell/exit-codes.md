---
type: "concept"
title: "Exit Codes"
description: "The integer status a process returns to its parent to report success or failure"
tags: ["exit-codes", "shell", "status", "contract"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Exit Codes

## Summary
Every process exits with an integer: 0 means success, non-zero means failure, and 126/127 have conventional meanings (not executable / command not found). Scripts and pipelines consume these codes as truth.

## Details
- `$?` holds the previous command's status; `if cmd; then` branches on it directly.
- `set -e` and `set -o pipefail` turn silent failures into loud ones.
- RSIS3 relevance: the harness treats non-zero exits from agent tools as actionable signals.

## Related
- [[wiki/os-shell/process-management|Process Management]] — exit status ends the process lifecycle
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — scripts are judged by their exit code
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — CLI contract includes exit status
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — pipelines gate on exit codes
- [[wiki/api-protocols/health-checks|Health Checks]] — exit codes are process health signals
