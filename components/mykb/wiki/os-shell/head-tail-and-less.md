---
type: "concept"
title: "head, tail & less"
description: "Stream preview and interactive paging"
tags: ["head", "tail", "less", "pager", "logs"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html", "https://man7.org/linux/man-pages/man1/less.1.html"]
---

# head, tail & less

## Summary
head and tail slice the first or last lines of a stream, and less pages through files interactively with search and follow modes. Together they are the daily tools for previewing files and watching logs.

## Details
- head -n 10 file prints the first ten lines; -c limits bytes; head is how pipelines sample large outputs (big.log | head).
- tail -n 20 prints the last lines; tail -f follows a growing file for log watching; -F retries the open, surviving rotation — use -F for rotated logs.
- tail --pid=PID stops following when a process exits; tail -n +2 skips a header line, a common CSV idiom.
- less opens files interactively: /pattern searches forward, ? backward, n/N repeat, G end, g start, F follows like tail -f, Ctrl-C stops.
- less flags: -N line numbers, -S chop long lines, -i case-insensitive search, and LESS env var sets defaults; less file +F starts in follow mode.
- In pipes, less -R preserves ANSI colors from grep --color or journalctl; most is the minimal alternative.
- Watching patterns in logs: tail -F file | grep ERROR pipelines handle simple cases; journalctl -f covers systemd logs directly.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — where head/tail stage
- [[wiki/os-shell/systemd-journal|systemd-journal]] — journalctl's built-in paging
- [[wiki/os-shell/grep-patterns|Grep Patterns]] — filtering streams after tail
- [[wiki/os-shell/ansi-escape-sequences|ANSI Escape Sequences]] — color that less -R renders
- [[wiki/os-shell/terminal-emulators|Terminal Emulators]] — where pagers run
