---
type: prompt
title: lint-wiki
description: Agent prompt for lint wiki
tags: [prompt, ops]
---

# Prompt: Lint Wiki

Run a health check on the current wiki.

Check:

- Missing or malformed frontmatter.
- Orphaned wiki pages.
- Source pages that do not link to concepts, questions, projects, or syntheses.
- Claims without source support.
- Duplicate concepts or overlapping pages.
- Stale open questions.
- Important pages missing from `wiki/index.md`.
- Major changes missing from `wiki/log.md`.

Return:

1. Critical fixes.
2. Suggested merges.
3. Pages to update.
4. Questions worth keeping.
5. A short maintenance plan.
