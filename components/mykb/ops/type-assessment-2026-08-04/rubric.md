---
type: "concept"
title: "MyKB Note Type-Assessment Rubric"
description: "Decision rules for auditing the type frontmatter field of MyKB wiki notes: type-named directories, entity vs concept, and conservatism"
tags: [mykb, rubric, frontmatter, curation, type-assessment]
timestamp: "2026-08-04T00:00:00Z"
status: stable
---
# MyKB Note Type-Assessment Rubric (2026-08-04)

You are one of **6 parallel agents** auditing the `type` frontmatter field of MyKB wiki notes.

- Repo root: `/data/data/com.termux/files/home/dev/cosmos`
- Wiki root: `components/mykb/wiki/` (your slice paths are relative to `components/mykb/`)
- Your slice: `ops/type-assessment-2026-08-04/slice-N.txt` — one relative path per line.
  The 6 slices are disjoint. **Touch ONLY files listed in your slice.** Other agents are
  editing other files concurrently; never run repo-wide builds or touch files outside your slice.

## Allowed type vocabulary
Use ONLY these existing bundle types (never invent a new one):
`concept`, `entity`, `source`, `synthesis`, `project`, `question`, `domain`, `log`,
`daily`, `index`, `decision`, `episode`, `experiment`, `plan`, `pulse`, `reflection`, `session`.

## Decision rules (priority order)
1. **Directory rule** — in type-named directories the type should match the directory:
   `decisions/`→decision · `questions/`→question · `pulses/`→pulse · `episodes/`→episode ·
   `experiments/`→experiment · `plans/`→plan · `projects/`→project · `reflections/`→reflection ·
   `sources/`→source · `syntheses/`→synthesis · `entities/`→entity · `daily/`→daily.
   (Note: many files in these dirs are currently mis-typed `concept` — fix them.)
2. **Entity vs concept** (domain areas such as `api-protocols/`, `data-storage/`, `ai-ml/`, …):
   - `entity` = a **named thing**: a specific spec/protocol (MCP, AsyncAPI), tool/library
     (FastAPI, SQLite), product, acronym, project, person, or organization.
   - `concept` = a general idea, principle, pattern, method, or technique
     (property-based testing, rollback plans, data deduplication).
   - A note about one specific named thing → `entity`; otherwise keep `concept`.
3. **Conservatism** — only change when clearly wrong. If genuinely ambiguous, KEEP the
   current type. A wrong change is worse than no change.

## Edit mechanics
- Read each file. Judge from `title`, `description`, and body.
- If the `type:` value is wrong per the rules, edit **only the `type:` line** inside the
  YAML frontmatter block (first `---` section). Preserve the existing quote style.
- Never add/remove other frontmatter fields; never edit body text, links, or formatting.
- Files already correct: skip, no edit.

## Reporting (final message)
- Changed count + skipped count.
- List of changed files, one per line: `path  old_type -> new_type`.
- Any files you were unsure about, with one-line reason.
