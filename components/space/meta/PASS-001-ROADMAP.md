# SPACE — Pass 001 Improvement Roadmap

**Project:** Superb Prompt Automatic Creation Engine (SPACE)
**Based on:** `meta/PASS-001-AUDIT.md`
**Created:** 2026-07-25
**Status:** Complete (executed as Pass 002)

---

## Overview

Pass 001 was an initial exploratory and analytical audit of the `prompt-framework` codebase — the foundational knowledge-gathering phase. This roadmap captures the improvement directions identified during that audit, which were subsequently implemented in Pass 002.

## Key Findings Requiring Action

| # | Finding | Priority | Target |
|:-:|---------|:--------:|--------|
| 1 | JSON data duplicated across `json/` and embedded in web app | Critical | Deduplicate to single source of truth |
| 2 | No programmatic API — browser-only via Vite dev server | High | Build CLI + API layer |
| 3 | localStorage persistence only — no file or DB storage | High | Multi-session storage |
| 4 | No LLM integration — purely manual elicitation | High | LLM-augmented question refinement |
| 5 | Single CSS file (626 lines) — no component styling | Medium | Modular styling |
| 6 | No test suite | Critical | Jest/vitest test infrastructure |
| 7 | Bash launcher script — fragile entry point | Medium | Node.js CLI entry point |
| 8 | Template variables in questions not interpolated | Medium | Template engine |
| 9| No export pipeline beyond manual JSON download | High | Multi-format export |
| 10 | No i18n/l10n support | Low | Localization infrastructure |

## Strategic Direction

1. **Data-first architecture** — JSON specs become canonical; everything else serves them
2. **API-native design** — Every feature exposed programmatically; UI is one consumer
3. **LLM-in-the-loop** — Questions refined dynamically using accumulated context
4. **Incremental delivery** — Each phase produces shippable artifacts

## Execution Plan

The improvements were structured into 7 phases (Phase 0–6) covering foundation, execution engine, LLM integration, export pipeline, interactive UI, persistence, and intelligence — implemented in full during Pass 002.
