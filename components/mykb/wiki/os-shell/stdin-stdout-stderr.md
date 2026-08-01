---
type: "concept"
title: "Stdin Stdout Stderr"
description: "The three standard streams every process inherits: input, output, and diagnostics"
tags: ["streams", "stdio", "redirect", "pipes"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Stdin Stdout Stderr

## Summary
Every Unix process gets three open streams: stdin (input, fd 0), stdout (results, fd 1), and stderr (diagnostics, fd 2). The separation lets pipelines consume results while errors still reach the user.

## Details
- Redirect: `> file`, `< file`, `2> err`, and `2>&1` to merge; pipes connect stdout to the next stdin.
- Writing diagnostics to stderr keeps them out of pipeline data.
- RSIS3 relevance: the harness separates agent output from logs by stream discipline.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — pipelines are built on these streams
- [[wiki/os-shell/exit-codes|Exit Codes]] — streams carry output, exit code carries status
- [[wiki/os-shell/here-documents|Here Documents]] — feeding stdin from script text
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — the CLI contract is stream-shaped
- [[wiki/api-protocols/rest-apis|REST APIs]] — HTTP request/response mirrors the streams
