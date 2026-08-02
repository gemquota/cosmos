---
type: "concept"
title: "Trap Handlers"
description: "trap for signals and EXIT, and cleanup patterns"
tags: ["trap", "signals", "cleanup", "bash", "exithandlers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Signals.html"]
---

# Trap Handlers

## Summary
The trap builtin registers shell code to run when a signal arrives or a special event occurs. The EXIT trap is the standard way to guarantee cleanup — temp files removed, locks released — whether a script finishes normally or dies mid-way.

## Details
- trap 'cmd' SIGNAL attaches a handler; trap - SIGNAL resets it to default, and trap -l lists signal names and numbers.
- EXIT runs on normal exit, exit builtin, and errexit-triggered termination; it also runs after a script's last command completes.
- ERR runs after any command that returns non-zero (when not in a condition); DEBUG runs before every command, useful for tracing wrappers.
- RETURN fires when a function or sourced script finishes, making it possible to restore shell state automatically.
- Signal handlers run after the current command completes, not between every byte; backgrounding long work or using wait is how scripts respond promptly.
- A handler's exit status replaces the script's unless the script exits explicitly inside the handler; preserve $? first for reliable codes.
- Traps are inherited across subshells but not exported to child scripts; common patterns use a trap cleanup EXIT with mktemp.

## Related
- [[wiki/os-shell/process-signals|Process Signals]] — the events traps handle
- [[wiki/os-shell/errexit-and-shell-options|Errexit & Shell Options]] — ERR and EXIT traps interact with set -e
- [[wiki/os-shell/exit-codes|Exit Codes]] — what cleanup handlers must preserve
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — where cleanup discipline lives
- [[wiki/os-shell/file-locking|File Locking]] — locks that traps must release
