---
type: index
title: Workflows
status: stable
created: 2026-07-18
updated: 2026-07-18
tags: [workflow, ops]
source: []
---

# Workflows

## 1. Capture

Put anything valuable but unprocessed into `raw/inbox/`.

## 2. Ingest

Process one source at a time. Use [[ops/prompts/ingest-source|Ingest Source Prompt]]:

1. Create `wiki/sources/YYYY-MM-DD-slug.md`.
2. Write the summary, key claims, actionable insights, and questions to verify.
3. Extract or update pages in `wiki/concepts/`, `wiki/questions/`, and `wiki/projects/`.
4. Update [[wiki/index]] and [[wiki/log]].

## 3. Query

When asking a question, start from [[wiki/index]], then follow related domains, concepts, and sources. Use [[ops/prompts/query-wiki|Query Wiki Prompt]].

## 4. Synthesize

When multiple sources point to the same theme, create or update a `wiki/syntheses/` page.

## 5. Lint

Every week, use [[ops/prompts/lint-wiki|Lint Wiki Prompt]] for maintenance.

