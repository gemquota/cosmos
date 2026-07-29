---
type: prompt
title: query-wiki
description: Agent prompt for query wiki
tags: [prompt, ops]
---

# Prompt: Query Wiki

Answer my question using the current wiki.

Rules:

1. Start from `wiki/index.md`.
2. Follow relevant wikilinks before answering.
3. Distinguish sourced notes, synthesis, and inference.
4. If evidence is weak, say what is missing.
5. Suggest which page should be updated after the answer.

Output:

- Short answer.
- Evidence from relevant pages.
- Uncertainties or gaps.
- Suggested wiki updates.
