---
type: "concept"
title: "Unix Text Processing Tools"
description: "The grep, sed, awk, cut, sort, jq family for streaming text transformation"
tags: ["text", "grep", "sed", "awk", "unix"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Unix Text Processing Tools

## Summary
The grep, sed, awk, cut, sort, jq family for streaming text transformation. These tools process text one line at a time, so they handle files far larger than memory, and composing them with pipes turns ad-hoc inspection into repeatable, reviewable data pipelines.

## Details
- **grep** — filter lines by pattern: `grep -E` for extended regex, `-i` for case, `-r` for recursive search, `-c` for counts, and `-o` to extract only the matches; the distinction between grep (line filtering) and sed/awk (line editing) keeps pipelines readable; `rg` is the faster, cleaner modern replacement and is the default in this repo.
- **sed** — stream editor for line-oriented edits: `s/pattern/replacement/` substitutions with flags (global `g`, per-line), `-n` with `p` to print only selected lines, and address ranges (`sed -n '10,20p'`); sed is at its best for mechanical rewrites (renaming tokens, stripping headers) and at its worst when the edit needs context beyond the current line.
- **awk** — the programmable member: field splitting on whitespace or a delimiter (`-F,`), `$1`/`$NF` field access, BEGIN/END blocks for running totals, and full condition-action programming; awk handles the transformations that grep and sed cannot: column math, sums and averages over groups, multi-line joins, and conditional reformatting; for anything beyond a few lines of logic, a real script is more maintainable.
- **cut, sort, uniq** — column extraction (`cut -d: -f1`), ordering (`sort -n` numeric, `-k` keys), and deduplication with counts (`uniq -c` after `sort`, since uniq only sees adjacent lines); the trio is the standard pipeline for frequency tables: `cut | sort | uniq -c | sort -rn` turns raw logs into a ranked top-N in one line.
- **jq** — the JSON counterpart: `jq '.field'` for extraction, `jq '.[] | select(.status == "ok")'` for filtering, and `jq -r` for raw (unescaped) output; it replaces the fragile regex-and-awk approach to JSON and is the right tool whenever the data is structured; `yq` plays the same role for YAML.
- **Failure modes** — locale-dependent sorting (set `LC_ALL=C` for byte-order consistency), NUL bytes and binary input corrupting line-based tools (use `tr -d '\0'` or the tools' `-z` modes), trailing whitespace and CRLF line endings breaking field parsing (`dos2unix` or `sed 's/\r$//'`), and forgetting that `-i` sed edits in place with no backup unless `-i.bak` is given.
- **Pipeline discipline** — debug with `| head`, then `| sed -n l` to reveal invisible characters; keep each stage single-purpose so it can be tested alone; and never let a pipeline silently drop errors — add `set -o pipefail` in scripts so a failing stage is visible; the output of a pipeline is only as trustworthy as its weakest stage.
- **RSIS3 relevance** — these tools are the workhorses for mykb's data hygiene: extracting and normalizing wiki metadata, counting link health from generated JSON, and reshaping snapshots (files.json, ecosystem.json) without loading them into memory; the wiki's own build scripts could lint frontmatter with awk and grep before the graph builder runs, catching malformed notes early.

## Related
- [[wiki/devops-infra/backup-tools-restic-borg|Backup Tools: restic & Borg]] — related coverage in the same cluster
- [[wiki/devops-infra/fault-injection-tools|Fault Injection Tools]] — related coverage in the same cluster
- [[wiki/os-shell/awk-text-processing|Awk Text Processing]] — related coverage in the same cluster
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — related coverage in the same cluster
- [[wiki/shell-environment/shell-environments-and-rc-files|Shell Environments & RC Files]] — related coverage in the same cluster
- [[wiki/shell-environment/terminal-multiplexers-tmux|Terminal Multiplexers: tmux]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
