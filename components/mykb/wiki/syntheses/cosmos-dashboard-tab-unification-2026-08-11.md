---
type: "synthesis"
title: "Cosmos dashboard tab unification — SPACE/MyKB/RSIS3 shell + KG lite mode"
description: "Durable patterns for converting embedded RSIS3 tabs into a standalone telemetry page, unifying three components under one swipeable four-tab shell, and keeping the knowledge graph interactive at full scale via a lite node subset"
tags: ["synthesis", "dashboard", "rsis3", "mykb", "space", "knowledge-graph", "performance", "unification", "shell"]
timestamp: "2026-08-11T00:00:00Z"
status: "growing"
---

# Cosmos dashboard tab unification — SPACE/MyKB/RSIS3 shell + KG lite mode

Patterns distilled from the 2026-08-11 unification pass: converting the RSIS3 tabs to a
standalone page, collapsing the old dashboard to a component shell, and making the
knowledge graph usable at full scale.

## Dashboard regression fixes (empty squares in RSIS3 tabs)
- **Telemetry-only page, no cross-component iframes**: `rsis3.html` owns only RSIS3
  telemetry tabs (Overview/Pulses/KG/Graphs/Constraints/Loops). Previously the wrapped
  dashboard iframed other components and served the old MyKB/SPACE tabs; those now live
  in the shell (`index.html`), so an empty component iframe can never blank an RSIS3 tab.
- **Static payloads are derived data**: `rack/pulses/dashboard-data.json`,
  `loops.json`, `roadmap.json`, `ecosystem.json`, `files.json` are rebuilt from live
  sources by `gen-static-data.py` — never hand-edit; re-run + `--check` after changes.
- **KG renderers must survive null DOM**: missing renderer IDs or a single unguarded
  throw blanks every later tab. Hoist/guard renderer failures so one tab can't kill the
  app.

## Unified shell contract (`index.html` + `?embed=cosmos`)
- One root shell with exactly four tabs: **SPACE | MyKB | RSIS3 | Fusion**; lazy iframes
  (`data-src`) so only the active pane loads.
- Navigation is multi-modal by design: top tabs, edge arrows (`#edgeL`/`#edgeR`),
  `ArrowLeft`/`ArrowRight` keyboard, and touch swipe. Any pane may post
  `{cosmos:'swipe', dir:'next'|'prev'}` or `{cosmos:'goto', tab:'space'|'mykb'|'rsis3'|'fusion'}`
  to move the shell; the shell exposes `window.go(tab)` / `window.step(dir)` for
  programmatic control.
- Deep links compose tab and pane state: `#rsis3:graphs` or `#mykb:graph` loads the
  right iframe URL and activates the right inner tab on first paint.
- Embedded pages accept `?embed=cosmos` to force the shared palette (#0f172a bg,
  #121726 panels, indigo #6366f1 / violet #a855f7 accents, #e8ecf4 text) instead of
  inheriting the parent — theme is owned by each embed, so panes stay identical when
  hosted standalone or inside the shell.

## Knowledge graph performance (lag → usable)
- **Lite mode is the default**: `okf-graph.html` and MyKB's inline graph viewer load
  `graph.lite.json` (420 nodes / 1,965 edges, hub + topic + top-degree sampling) instead
  of the full 5,510-node / 36,984-edge graph. `?full=1` opts into the full graph.
- Keep a visible, working **Switch to full/lite** toggle and report the loaded scale in
  the footer (e.g. `lite · 420 nodes, 1965 edges`) so the mode is never surprising.
- Cytoscape perf flags matter: disable label scaling/rotation, cap label visibility by
  zoom, and sample edges before layout; layout cost dominates at full scale.

## Fusion (multi-component extrapolation surface)
- Fusion mixes `rack/pulses/dashboard-data.json` (RSIS3 telemetry),
  `graph.lite.json` + `catalog.lite.json` (MyKB structure), and
  `space/web/framework-summary.json` (SPACE framework series) into one extrapolation
  view — the pattern for deeper multi-component data generation surfaces.

## Related
- [[wiki/syntheses/cosmos-dashboard-snapshot-fallback-2026-08-11|Dashboard Snapshot Fallback — never regen from an environment-dependent source]]
- [[wiki/syntheses/rsis3-dashboard-unified-embed-2026-08-10|RSIS3 unified dashboard — live-telemetry rebuild & unified embed]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]]
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]]
