---
type: synthesis
title: "Nested-Loop Graph & Zoom Direction Fix"
description: "Durable patterns for the interactive Ω graphs: viewBox-width zoom inversion (f>1 zooms in), re-projecting only the loop family onto concentric rings at the semantic centroid, and keeping generator scripts + index cards in sync"
tags: [synthesis, diagrams, rsis3, loops, visualization, interaction, verification]
timestamp: "2026-08-01T00:00:00Z"
status: stable
source: []
---

# Nested-Loop Graph & Zoom Direction Fix

## Context

Two changes to the interactive Ω diagrams: (1) the zoom controls were
inverted — scrolling up / pinching out zoomed *out*; (2) a second graph was
added that renders the full 52-node / 64-link ecosystem with the L1–L9 stack
as nine concentric rings. Derived from the fix + build pass; rules here are
the durable conclusions.

## Patterns

1. **Zoom is viewBox-width inversion, not scaling.** `zoomAt(f)` computes
   `nw = clamp(vb.w / f)` — `f > 1` shrinks the viewBox width and zooms in.
   Wheel maps scroll-up to `f = exp(-deltaY * k) > 1`; pinch maps finger-spread
   to `f = d / pinch.d > 1`. Both interactive graphs share this single
   interaction contract, and the generator source (`omega.py`) is the
   authority — regenerated HTML must match it.

2. **A nested-loop graph re-projects only the loop family.** Keep every
   non-loop node at its canonical semantic position from the flat graph
   (they stay comparable across both views); take the *semantic centroid* of
   the L-nodes as the bullseye and place each loop on its own ring
   (`r = 48 + (k-1) * 36` for L1..L9). Bearings are min-separated (~0.24 rad)
   to avoid ring-label collisions; loop discs are immovable during the
   relaxation passes so the stack never drifts.

3. **Shared model, two views.** The nested graph imports the same
   52-node / 64-link model from `omega.py` instead of duplicating it — a
   single source of truth for nodes, edges, and λ-visibility, so the two
   interactive views cannot drift apart.

4. **Index wiring is declarative cards + in-sync generators.**
   `_index_update.py` defines `OMEGA_CARD` / `NESTED_CARD` tuples rendered by
   the `card()` helper; `_rebuild_index.py` re-derives the same panels from a
   pristine base. Adding a graph means: one card tuple, include it in the
   X++ panel list, bump the tab count, and update both scripts' header text
   together (tier count = 24 + 26 + 24 + 12 + #X++).

5. **Verification gates before shipping a graph.** The smoke script checks
   label overlap at every λ level, edge completeness (64/64), ring membership
   of every L-node, and node/edge counts — plus an rsvg snapshot at λ1 and λ4
   that is visually inspected. A graph that passes these gates is safe to
   wire into the index and commit.

## Related

- [[wiki/syntheses/nine-loop-stack-implementation|Nine-Loop Stack Implementation & Dashboard Wiring]]
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]]
- [[wiki/concepts/tuning-ownership-diagonal|Tuning Ownership Diagonal]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Dashboard & MyKB Integration Patterns]]
- [[wiki/index|Wiki Index]]
