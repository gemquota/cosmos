---
type: readme
title: mykb — RSIS3 Long-Term Memory
description: Persistent, human-readable semantic knowledge database for the RSIS3 cognitive engine
tags: [readme, memory, rsis3, okf]
timestamp: "2026-07-31T00:00:00Z"
---

# mykb

mykb is **RSIS3's long-term memory**: a persistent, human-readable semantic
knowledge database built on the Open Knowledge Format (OKF) and Obsidian wiki
conventions. Every article is markdown with YAML frontmatter; links are the
graph.

Start from [[Home]] or the [[wiki/index|Wiki Index]]. New to the
knowledge base? Read the [[ops/conceptual-guide|mykb for Humans — Conceptual
Guide]] first: it explains the mental model, the layers, and how to navigate.

## Roles

- **Memory store** — pulses, decisions, sessions, reflections (see
  [[ops/rsis3-memory-bridge|RSIS3 Memory Bridge]])
- **Semantic database** — typed, tagged, timestamped articles plus an emergent
  link graph (`graph.json`)
- **Research corpus** — sources and syntheses from acquisition rounds (see
  [[ops/knowledge-acquisition|Knowledge Acquisition]])

## Layout

- `raw/`: original material and archives
- `wiki/`: processed knowledge (concepts, sources, syntheses, memory areas)
- `templates/`: note templates
- `ops/`: workflows, schema, prompts, reports
- `daily/`: daily notes
- `graph.json`: static knowledge-graph export (nodes + edges)
- `files.json`, `wiki/index.json`: static indexes for hosting without the daemon

## Operations

- `okf validate .` — OKF conformance
- `okf lint .` — curation quality
- `python3 .wiki-daemon/build_graph.py` — regenerate the link graph
- `python3 build-index.py` — regenerate `wiki/index.json`
- `python3 .wiki-daemon/build_files_index.py` — regenerate `files.json`
