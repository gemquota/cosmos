---
type: "concept"
title: "Verbose Flag"
description: "A CLI or config switch that raises logging verbosity on demand"
tags: ["cli", "logging", "debugging", "verbosity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Verbose Flag

## Summary
A verbose flag (-v, --verbose, -vvv) raises log verbosity at runtime so users can inspect internals without editing code. Repeated flags often map to escalating levels, from info to debug to trace, making verbosity a dial rather than a switch.

## Details
- Mechanism: the flag parses into a verbosity level that selects the log threshold; one -v enables debug, two -vv trace-level detail; verbose output goes to stderr or a log file, never into the stdout that scripts parse; paired with structured logging, verbose mode adds fields and events rather than wall-of-text lines.
- Concrete example: a wiki CLI runs quietly by default; `-v` logs each article processed; `-vv` logs each link resolution and decision; a user debugging a failed sync reruns with `-vv` and pipes stderr to a file; the flag is documented in help and consistent across subcommands.
- Failure modes: verbose output polluting stdout, breaking scripts that parse it; verbosity levels that are undocumented, so users guess; verbose mode leaking sensitive data (payloads, tokens); flags implemented inconsistently across subcommands; default verbosity too high, so the tool is noisy and the flag is meaningless.
- Tradeoffs: a verbose flag gives users on-demand visibility at the cost of a small parsing and documentation surface; the alternative — editing log levels in code or config — is slower and requires a rebuild; the mature pattern is repeatable flags, stderr output, structured events, and documented levels.
- Operational notes: keep default output quiet, test that stdout stays parseable at every verbosity, and document the levels in help text.
- RSIS3 relevance: the wiki CLI can expose a verbose flag to trace which articles and links it processes — the same on-demand introspection RSIS3 wants for its own runs.

- Make the flag repeatable and document each level so users can escalate verbosity without guessing.
## Related
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/dev-tools/debug-logging|Debug Logging]]
- [[wiki/dev-tools/local-dev-logs|Local Dev Logs]]
- [[wiki/shell-environment/shell-scripting-robustness|Shell Scripting Robustness]]
- [[wiki/software-engineering/developer-experience|Developer Experience]]
