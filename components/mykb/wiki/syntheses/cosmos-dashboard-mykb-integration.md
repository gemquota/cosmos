---
type: synthesis
title: "Cosmos Dashboard & MyKB Integration Patterns"
description: "Durable engineering patterns for the static-hosted dashboard↔wiki integration: lazy iframes, bounded client-side search, repo-relative snapshots, read-only validation, verification-first changes"
tags: [synthesis, dashboard, mykb, static-hosting, iframe, verification, performance]
timestamp: "2026-07-31T00:00:00Z"
status: stable
source: []
---

# Cosmos Dashboard & MyKB Integration Patterns

## Context

The unified dashboard embeds MyKB and SPACE as lazy-loaded iframes and ships on
GitHub Pages (static hosting, no wiki daemon). Derived from the xxl + 4xl
refinement sessions on the dashboard↔wiki integration; rules here are the
durable conclusions, not the session trivia.

## Patterns

1. **Bound client-side search.** Any client-side scan over `files.json`
   (~1,900 entries) runs on every keystroke on static hosting. Always debounce
   (≥150 ms) and bound the match scan (early-exit cap) so worst-case work is
   constant. Prefer path-substring + basename matching, escaped output.

2. **Repo-relative snapshot paths + read-only validation.** `files.json`
   entries are repo-relative (no `components/mykb/` prefix); the browser strips
   prefixes and the generator filters dead/missing entries. Snapshot
   generators must not rewrite files in `--check`/validation mode — compare
   in-memory instead, or every CI check churns the `generated` timestamp.

3. **Hide rules live at the level they hide.** Nested sub-tab systems need
   their own `.hide` rule (`.cst.hide`), not a rule from a sibling system
   (`.tab-body.hide`). A missing class silently makes the "second tab" appear
   dead while the first works.

4. **Parent-relative links on static hosting.** `../x.md` cannot resolve on a
   static site. Map them to a snapshot-relative path when the target exists in
   `files.json` (the daemon still handles real paths). Same idea applies to
   `#anchor` splitting: `.md` navigation must ignore raw `#...` sidebar hrefs
   or every header/file click breaks.

5. **Iframe embedding.** Use `data-src` + lazy activation (set `src` once on
   tab open), add `title` for accessibility, and keep per-component state in
   the parent so sub-tab switches hide/show the right views. Deep links
   (`#mykb:graph`) must round-trip through the same `sw`/`cs` path as clicks.

6. **Verification-first, with an external gate.** Every change is gated by a
   harness battery (embedded-server sim, probe variants, snapshot `--check`,
   syntax checks) — never let the improver grade itself. The immutable
   evaluator principle (see [[wiki/llm-agents/approval-gates|Approval Gates]])
   bounds how far self-improvement can drift.

7. **Engine-compat guards.** Lookbehind regexes are parse-time `SyntaxError`s
   on older engines; construct them via `new RegExp(...)` inside `try/catch`
   and degrade gracefully instead of crashing the viewer.

## Related

- [[wiki/index|Wiki Index]]
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]]
- [[wiki/frontend/static-site-generation|Static Site Generation]]
- [[wiki/testing/llm-evaluation|LLM Evaluation]]
- [Wiki Schema](../ops/wiki-schema.md)
