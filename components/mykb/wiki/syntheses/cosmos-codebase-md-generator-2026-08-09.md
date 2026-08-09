---
type: "synthesis"
title: "CODEBASE.md — regenerable hierarchical codebase concatenation for context injection"
description: "gen-codebase-md.py produces CODEBASE.md, a single hierarchical concatenation of the COSMOS source tree (header + inclusion rules + ASCII tree + anchor TOC + per-file sections); records the durable inclusion/exclusion rules and maintenance invariants"
tags: ["tooling", "codebase", "documentation", "generator", "context-injection"]
timestamp: "2026-08-09T14:15:00Z"
status: "growing"
---

# CODEBASE.md — regenerable codebase concatenation

`gen-codebase-md.py` (repo root) renders the whole COSMOS source tree into
`CODEBASE.md` for context injection and review. Regenerate anytime with:

```bash
python3 gen-codebase-md.py   # optional: --out PATH
```

## Output shape

- Header with UTC timestamp, file count, size, and the generating script.
- `## Inclusion rules` — human-readable summary, kept in sync with the
  module docstring.
- `## Repository tree` — pruned ASCII tree of included paths.
- `## Table of contents` — one anchor link per file, sorted by full path.
- Sections grouped by top-level directory (root files first, then dirs
  alphabetically); each file is a `### \`path\`  [NNKB]` heading followed
  by a fenced code block with the language mapped from extension.

## Durable inclusion rules

- Extensions: `.py .mjs .js .cjs .ts .tsx .html .css .sh .yml .yaml .json`
  plus `.md` only from selected roots (repo, rsis3, mykb, space, contracts,
  vercel-deploy, docs) — MyKB `wiki/` content stays out (it is data).
- Extensionless executable shebang scripts are source too (`cli/cosmos`).
- `.github/` is included (root CI workflows + nested ones such as
  `components/space/.github/`), the one hidden dir allowed through.
- Excluded: `.git`, `node_modules`, `dist/`, `auto/`, `exports/`, `.rsis/`,
  telemetry/cycles/sessions, generated snapshots (`graph.json`,
  `files.json`, `catalog.json`, `dashboard-data.json`, `loops.json`,
  `package-lock.json`, `log.md`, `mykb-code.md`, `mykb-content.md`, …),
  images, zips, `docs/audit-suite`/`docs/superpowers` reports, `ops/`,
  `diagrams/`, mykb `ops/`, rsis3 `lifecycles/` archives, and the output
  file itself.
- Per-file cap 250 KB; oversized files are skipped and reported to stderr.

## Maintenance invariants

- TOC uses prefixed anchors (`file-…`) so links never collide with the
  many `### ` headings that appear inside embedded code blocks.
- TOC order (full-path sort) intentionally differs from section order
  (grouped by top level) — both derive from the same file list, so counts
  must stay equal (361 files / ~2.6 MB as of 2026-08-09).
- When editing rules, update the module docstring and the generated
  `## Inclusion rules` text together.

## Related

- [[wiki/syntheses/rsis3-phase-4-5-ops-autonomy-2026-08-08|RSIS3 Phases 4–5 — ops maturity + autonomy]]
