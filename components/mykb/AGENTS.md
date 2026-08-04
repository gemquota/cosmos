---
type: config
title: Agent Instructions
description: Agent configuration and working principles for the mykb bundle
tags: [meta, config]
---

# AGENTS.md

This vault is a personal wiki knowledge iteration system for daily learning,
formatted as an **Open Knowledge Format (OKF) bundle**. Use `$okf` for
knowledge work.

## OKF Bundle

This project is registered as an OKF bundle. The `okf` CLI is installed and
available. Main verbs:

- `okf validate <dir>` — check OKF v0.1 conformance
- `okf lint <dir>` — curation-quality report
- `okf search <dir> <term>` — find concepts
- `okf produce` — create new concepts
- `okf maintain` — keep in sync
- `okf server <dir>` — serve as interactive graph

This vault also follows the **Obsidian Wiki System** pattern.
Use `$obsidian-wiki-system` for maintenance workflows, or `$okf` for OKF operations.

## Core Layers

- `raw/`: Original material (links, PDFs, screenshots, transcripts, clippings).
  Store here without rewriting source facts.
- `wiki/`: Processed knowledge. Digested, linked, rewritten notes.
  Each file has YAML frontmatter with `type`, `title`, `tags`, `timestamp`.
- `templates/`: OKF note templates (from the installed skill).
- `ops/`: Operating layer — workflows, schema, prompts, maintenance rules.
- `daily/`: Daily notes.

## Working Principles

- Read `index.md` (OKF bundle root) and `wiki/index.md` before editing.
- Preserve the `raw -> wiki -> index/log` iteration loop.
- One concept = one file. Links are the graph.
- New pages must include YAML frontmatter with at minimum a `type` field.
- Use `[[wikilinks]]` for internal vault pages alongside markdown links.
- Update `log.md` after meaningful structural changes.
- Run `okf validate` and `okf lint` after major edits.

## Wiki Frontmatter (compatible with OKF)

```yaml
---
type: concept    # Required by OKF §9.2
title: ""        # Display name
description: ""  # One-sentence summary
tags: []         # Cross-cutting labels
timestamp: ""    # ISO 8601
```

Extended frontmatter (obsidian wiki compatible):

```yaml
---
status: seed      # seed | growing | stable | archive
source: []        # Links to source materials
```

Valid `type` values: `source`, `concept`, `domain`, `project`, `question`,
`synthesis`, `daily`, `index`, `log`.

## Common Actions

- **Ingest material**: put original in `raw/inbox/`, then use `$okf produce` to create wiki concept pages.
- **Process source**: use `ops/prompts/ingest-source.md` to create a `wiki/sources/` page from inbox material.
- **Synthesize**: after collecting related sources, create a synthesis page in `wiki/syntheses/` that cross-links concepts.
- **Weekly review**: update `wiki/syntheses/weekly-review.md`, merge duplicate notes, check isolated pages.
- **Query knowledge**: use `okf search` from the CLI, or `$okf search`
  from the agent.
- **Health check**: `okf validate .` for conformance, `okf lint .` for curation.
- **Serve graph**: `okf server .` to browse as an interactive knowledge graph.

## Web Dashboard

The wiki is served via `server.py` (Python HTTP server) on port 8826.

```bash
# Start dashboard
bash start.sh
# Or from anywhere (after sourcing ~/.bashrc):
mykb
```

Dashboard URL: `http://127.0.0.1:8826`

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serves `index.html` (SPA viewer) |
| `/files.json` | GET | Enriched index of all `.md` files: `{path, type, title, tags}` |
| `/api/file?path=<rel>` | GET | Serves raw markdown content |
| `/api/stats` | GET | System statistics |
| `/api/v2/search/hybrid?q=` | GET | Hybrid search (BM25 + TF-IDF) |
| `/api/v2/search/build` | GET | Rebuild search index |
| `/api/v2/graph/topology?root=&depth=` | GET | Subgraph filtering |
| `/api/v2/history/log/<path>` | GET | Git commit history for a file |
| `/api/v2/history/snapshot?path=&ts=` | GET | File content at a point in time |
| `/api/v2/health/lint` | GET | Wikilink integrity report |
| `/graph.json` | GET | Full knowledge graph (nodes + edges) |
| `/search?q=` | GET | Basic TF-IDF search |

### Viewer Features

- **Docs tab**: Browse all markdown files in a sidebar, type-grouped or directory-grouped
- **Graph tab** (Ctrl+G): Force-directed knowledge graph with topology filtering
- **Actions tab** (Ctrl+H): System stats, linter, search index rebuild
- **Search** (Ctrl+K): Full-text search across all documents
- **Theme toggle** (T): Cycles light → dark → AMOLED ultra-black

## Session Capture Hooks

Python hooks capture agent turns and buffer them for knowledge extraction.

### Architecture

```
Agent turn → PostToolUse hook → buffer (.ndjson)
Session end → Stop hook → signal file
```

### Components

- `hooks/post-tool-use.py` — captures each turn to `.wiki-daemon/buffers/<session>.ndjson`
- `hooks/session-stop.py` — writes session-end signal to `.wiki-daemon/buffers/signals/`

### Usage

Hooks are configured in the Codex settings and run automatically.
No manual start/stop required.

## Active .wiki-daemon Scripts

These scripts are referenced by `server.py` and actively used:

- `search_fusion.py` — hybrid search engine (BM25 + TF-IDF + RRF)
- `kb_linter.py` — wikilink integrity, orphan detection
- `temporal_engine.py` — Git-backed history, auto-commit, time-travel retrieval

Standalone utility scripts (run manually) are archived in `.wiki-daemon/archive/unused-scripts/`.

## File Inventory

### Top-level

| File | Purpose |
|------|---------|
| `server.py` | HTTP server with API endpoints |
| `index.html` | SPA viewer (Docs/Graph/Actions tabs) |
| `start.sh` | Server launcher (run from any directory) |
| `build-export.py` | Concatenate project into two markdown files |
| `build-index.py` | Build enriched index.json from wiki frontmatter |
| `AGENTS.md` | This file — agent instructions |
| `index.md` | OKF bundle root |
| `Home.md` | Daily knowledge entry point |
| `log.md` | Iteration log |
| `README.md` | Project overview |

### Backup/Archive

- `.wiki-daemon/archive/` — archived scripts, dead files, old viewers
- `mykb-code.md` / `mykb-content.md` — full project export (generated by `build-export.py`)
