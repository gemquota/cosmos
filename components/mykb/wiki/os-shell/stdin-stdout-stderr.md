---
type: "concept"
title: "Stdin Stdout Stderr"
description: "The three standard streams every process inherits: input, output, and diagnostics"
tags: ["streams", "stdio", "redirect", "pipes"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Stdin Stdout Stderr

## Summary
Every Unix process inherits three open streams: stdin (fd 0) for input, stdout (fd 1) for results, and stderr (fd 2) for diagnostics. The separation is the foundation of pipelines — `cmd | next` connects stdout to the next command's stdin while errors still reach the terminal — and the discipline of writing errors to stderr is what keeps data flowing through pipes clean.

## Details
- Mechanism: the kernel gives each process three file descriptors by convention, usually pointing at the terminal. The shell redirects them: `>` writes stdout to a file, `<` reads stdin from a file, `2>` sends stderr to a file, `2>&1` merges stderr into stdout's target, `&>` (bash/zsh) redirects both, and `1>&2` sends stdout to stderr's target. Pipes (`|`) connect one process's stdout to the next's stdin; `|&` pipes both streams in bash. The key property: stdout carries the *data contract* (whatever the next stage expects), stderr carries *human diagnostics* (progress, warnings, errors) — so `find / -name x 2>/dev/null` drops noise without corrupting the result list, and `cmd > out.txt 2> err.txt` separates them.
- Concrete examples: `git log | grep -i fix` feeds one stream into another; `rsync -av /src/ /dst/ > rsync.log 2>&1` captures everything; a script that prints prompts to stderr (`echo "Enter name:" >&2`) keeps prompts out of piped output; `curl -s ... | jq .` relies on curl's errors going to stderr so the JSON stream stays clean; `3>&1`/`4>&2` juggling captures specific streams in complex scripts; `exec 2>err.log` redirects stderr for the rest of the script.
- Failure modes: the classic failures are writing diagnostics to stdout — a script's log lines then corrupt the pipeline data for every downstream consumer (the "my grep output has garbage in it" bug); closing or redirecting the wrong fd (`2>&1` order matters: `cmd 2>&1 >file` vs `cmd >file 2>&1` differ); and buffering surprises (stdout is block-buffered when redirected, line-buffered on a tty, so interleaved stdout/stderr order can appear scrambled in logs).
- Operational tradeoffs: the stream separation costs nothing and buys composability — every tool becomes a filter stage — and the tradeoff is discipline: tools must agree that stdout is data and stderr is commentary, which is why command-line contract design (like the "stdout data, stderr diagnostics" convention) matters as much as exit codes. The practice rules: write results to stdout and everything human-readable to stderr, use `2>&1` deliberately (after choosing the target), and treat stream hygiene as part of the CLI contract. RSIS3 relevance: the harness separates agent output from logs by stream discipline — tool results flow on stdout where they can be parsed, diagnostics on stderr where they can be shown without corrupting the structured output, exactly the contract RSIS3 expects from every tool.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — pipelines are built on these streams
- [[wiki/os-shell/exit-codes|Exit Codes]] — streams carry output, exit code carries status
- [[wiki/os-shell/here-documents|Here Documents]] — feeding stdin from script text
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — the CLI contract is stream-shaped
- [[wiki/api-protocols/rest-apis|REST APIs]] — HTTP request/response mirrors the streams
