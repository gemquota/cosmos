# Phase 3: Export Pipeline — Development Guide

**Spec References:** `specs/03-export-pipeline.md`
**Prerequisites:** Phase 1 complete
**Estimated Effort:** 2–3 weeks
**Sprint Count:** 1-2

**Status:** Implemented | **Tests:** ✅ | **Last Cycle:** 004 | **Coverage:** 80%+

---

## Overview

Build the multi-format export pipeline that transforms completed (or partial) session data into production-ready specification documents. Replaces the broken `consolidate-spec.sh` and original browser-only JSON download with 6 export formats.

---

## Task Table

| ID | Title | Spec | Effort | Deps | Acceptance Criteria |
|----|-------|------|:------:|------|---------------------|
| 3.T1 | Exporter interface and pipeline orchestrator | 03 §5 | M | 0.T1 | Pipeline accepts session + format, returns result |
| 3.T2 | JSON v2 exporter | 03 §4.2 | M | 3.T1 | Produces valid v2 JSON with all answers |
| 3.T3 | Markdown exporter | 03 §4.3 | L | 3.T1 | Produces valid MD with TOC and sections |
| 3.T4 | YAML exporter | 03 §4.4 | M | 3.T1 | Produces valid YAML matching JSON v2 structure |
| 3.T5 | Prompt template exporter | 03 §4.5 | M | 3.T1 | Produces single system prompt from answers |
| 3.T6 | HTML exporter (styled document) | 03 §4.6 | L | 3.T3 | Styled HTML with collapsible sections |
| 3.T7 | Diff exporter (session comparison) | 03 §4.6 | M | 3.T1 | Correct diff between two sessions |
| 3.T8 | `space export` CLI command | 04 §3.1 | M | 3.T1–3.T5 | CLI exports to file(s) |
| 3.T9 | Export tests and validation | — | M | 3.T1–3.T7 | All formats validated |

---

## Task Details

#### 3.T1: Exporter Pipeline Orchestrator

**What:**
Create the `Exporter` interface and `ExportPipeline` class that routes to format-specific exporters.

**Files:**
- `src/export/types.ts` — Exporter interface
- `src/export/pipeline.ts` — Router/orchestrator
- `src/export/formatters/` — One file per format

**Done When:**
- [ ] `pipeline.export(session, artifacts, 'json')` routes to JSON exporter
- [ ] All formats return `ExportResult` with content, filename, mime_type
- [ ] Unknown format returns clear error

---

#### 3.T3: Markdown Exporter

**What:**
Generate a complete, styled Markdown specification document with table of contents, numbered sections, and proper formatting.

**Files:**
- `src/export/formatters/markdown.ts`
- `tests/export/markdown.test.ts`

**Implementation Notes:**
- Generate TOC from series/round structure with anchor links
- Each series = H2 section; each round = H3 subsection
- Answers formatted as blockquotes
- Choices shown as bold labels
- Long answers (>500 chars) wrapped in `<details>` tags
- Include metadata header (date, completion %, time)
- Empty answers shown as `[Not answered]`

**Done When:**
- [ ] Output passes `markdownlint` with no errors
- [ ] All 326 questions present (answered or placeholder)
- [ ] TOC links work (GitHub-compatible anchors)
- [ ] Responsive when opened in any MD viewer

---

#### 3.T5: Prompt Template Exporter

**What:**
Combine all answers into a single, copy-paste-ready system prompt that an LLM can use as its development specification context.

**Files:**
- `src/export/formatters/prompt.ts`
- `tests/export/prompt.test.ts`

**Implementation Notes:**
- Use the artifact dictionary as primary data source
- Structure: Domain → Entities → Relationships → Procedures → Technical → Methodology → Operations
- Each section is self-contained (can be used independently)
- Include "instruction preamble" explaining the spec to the LLM
- Handle partial sessions gracefully (mark missing sections)
- Support `compact` mode (shorter) and `full` mode (detailed)

**Done When:**
- [ ] Output is a single, coherent text block
- [ ] Can be pasted as a system prompt into any LLM chat
- [ ] Missing sections noted but don't break the output
- [ ] Both compact and full modes produce valid output

---

## Testing

- JSON round-trip: export → import → re-export produces equivalent output
- Markdown: rendered correctly in GitHub, VS Code, and browser
- YAML: parseable by any YAML parser
- Prompt: manually tested by pasting into ChatGPT/Claude
- Diff: synthetic sessions with known changes → verify correct diff

## Risks

- Markdown edge cases with special characters in user answers — escape properly
- Prompt template length may exceed LLM context window for very detailed sessions
