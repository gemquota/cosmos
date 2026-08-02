---
type: "concept"
title: "xargs"
description: "Building command lines, -0, -n, -I, and batching"
tags: ["xargs", "command-line", "batching", "pipes"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/xargs.1.html"]
---

# xargs

## Summary
xargs reads items from stdin and builds command lines from them, solving the problem that shell pipelines cannot pass arguments through pipes. It batches items to respect ARG_MAX and can parallelize work across multiple invocations.

## Details
- Plain xargs rm splits stdin on blanks and newlines; the GNU default also honors quotes, which surprises people with filenames containing spaces.
- -0 switches to NUL-delimited input, matching find -print0; this is the safe mode for arbitrary filenames.
- -n N limits items per invocation, -I {} replaces a placeholder (one item per command), and -L N groups by input lines.
- -P N runs up to N commands in parallel — a quick map-reduce for image resizing, downloads, or hashing.
- -r suppresses running the command when input is empty; without it, xargs runs the command once with no arguments.
- Exit status 123 means some invocation failed; with -P the overall behavior needs care, so scripts should check it.
- Delimiter pitfalls: use -d '
' (GNU) to split strictly on newlines, or prefer -0 when the producer supports it.

## Related
- [[wiki/os-shell/find-command|find]] — the primary -print0 producer
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — the pipeline context xargs lives in
- [[wiki/os-shell/quoting-rules|Quoting Rules]] — why spaces break naive xargs
- [[wiki/devops-infra/worker-pools|Worker Pools]] — parallel runners for heavy jobs
- [[wiki/os-shell/exit-codes|Exit Codes]] — decoding xargs status 123
