---
type: "synthesis"
title: "MyKB Guidance UI Overhaul — navigation, article tools, graph repair"
description: "Home-page routing, prominent Guidance button with Direction/Queue/Triage tabs, article toolbar (Graph/Edit/Archive/Delete), knowledge-graph load fix, and live-mode category grouping"
tags: ["guidance", "mykb-ui", "knowledge-graph", "navigation", "article-toolbar", "stub-triage"]
timestamp: "2026-08-06T00:00:00Z"
status: "growing"
---

# MyKB Guidance UI Overhaul — navigation, article tools, graph repair

## Summary
Turned the mykb single-page app into a more usable research surface:

- **Home routing**: the index (empty hash) now lands on the mykb home page
  (metrics, recent documents, quick actions) instead of auto-opening the first
  visible file. The sidebar title and "All Documents" entry both return home.
- **Prominent Guidance button**: Guide moved out of the sidebar tab row into a
  dedicated gradient promo button above the tabs; `#guidance`/`#stubs`/`#guide`
  hashes still route there. Inside, the guide is split into three sub-tabs —
  **Direction** (area health + wanted links), **Research queue** (wanted
  pages / directions / questions / feedback + drain), and **Stub triage**.
- **Article toolbar**: every open article shows Graph / Edit / Archive /
  Delete. Edit opens an in-app markdown editor; Save POSTs to the daemon
  (`/api/v2/file`); Archive git-moves to `raw/archive/stub-audit-<date>/` and
  Delete git-removes (`/api/v2/file/archive|delete`). Static-mode fallbacks
  copy the equivalent git commands. Graph switches to the knowledge graph.
- **Knowledge graph repaired**: `drawGraph` referenced an undefined `camZoom`
  (the graph never painted). Now uses `graphCam.zoom`, draws once immediately
  so the graph is visible while physics refines, and caps refinement passes
  for very large graphs (5,401 nodes) so the first render lands fast.
- **Categories fixed in live mode**: the daemon's `/files.json` returned a
  plain path list (no frontmatter), so Type grouping collapsed everything into
  "other". It now serves the enriched snapshot, restoring area/type grouping
  with counts and type chips when running under `server.py`.

## Rules / patterns
- Toolbar and editor are siblings of `#doc-body` inside `#content-doc`; content
  renders (loading, error, article, home) must target `#doc-body`, never
  overwrite `#content-doc`, or the toolbar/editor disappear.
- Article mutating endpoints live on the daemon (`/api/v2/file*`) with
  plain-filesystem fallback for untracked files; static pages show copyable
  git commands instead of failing silently.
