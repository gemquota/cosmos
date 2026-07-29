---
type: "entity"
title: "Iterative Prompt Refinement"
tags: ["prompt", "iteration", "refinement", "optimization"]
source: ["session-89e039d9.md", "session-b006376d.md", "session-a39de5db.md"]
---

# Iterative Prompt Refinement

The process of evolving prompts through multiple iterations, clearly visible across the session logs.

## The Refinement Cycle

1. **Initial broad instruction** — "Do X"
2. **Observe output** — Too broad, misses context
3. **Narrow scope** — "Do X with Y constraint"
4. **Add examples** — "Like A, B, C but not D"
5. **Define output format** — "Return as JSON with fields:"
6. **Set quality criteria** — "Ensure X, avoid Y"

## Real Patterns from Sessions

### Renaming/Refactoring Pattern
```
Iteration 1: "Rename X to Y"
Iteration 2: "Rename X to Y throughout the codebase, update all references"
Iteration 3: "Rename X to Y in all files, update imports, verify no stale references"
```

### Technical Cleanup Pattern
```
Iteration 1: "Replace sci-fi terms with formal terms"
Iteration 2: "Replace [list of specific terms] with [formal equivalents]"
Iteration 3: "Replace terms, update UI labels, and fix any broken references"
```

## Principles

- **Start broad, narrow fast** — First iteration discovers scope
- **Add constraints progressively** — Each iteration handles one failure mode
- **Include negative examples** — "Don't do X" prevents regression
- **Verify after each iteration** — Run tests, check output

See also: [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/tool-use-prompts|Tool Use Prompts]], [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/knowledge-extraction|Knowledge Extraction]]
