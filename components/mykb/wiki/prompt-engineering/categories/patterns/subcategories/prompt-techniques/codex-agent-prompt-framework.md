---
type: "entity"
title: "Codex Agent Prompt Framework"
tags: ["prompt", "codex", "agent", "framework", "constitution"]
source: ["session-4b35bd59.md", "session-0c0a9b0f.md", "session-c88fb179.md"]
---

# Codex Agent Prompt Framework

The overall prompt architecture that governs Codex CLI agents in this ecosystem — combining AGENTS.md, GEM_INSTRUCTIONS.md, and real-time instructions.

## Three-Layer Prompt Architecture

### Layer 1: System Constitution (AGENTS.md)
Persistent project-level instructions versioned in git:
- Project architecture overview
- Core invariants and rules
- Testing requirements
- Code conventions

### Layer 2: Integration Protocol (GEM_INSTRUCTIONS.md)
Cross-project integration rules:
- Bridge protocol definitions
- Memory sync requirements
- API contracts between projects

### Layer 3: Session Instructions (Real-time)
Per-session task context:
- Current goal definition
- Specific constraints
- Priority adjustments

## How Layers Compose

```
Layer 1 (AGENTS.md) → Layer 2 (GEM_INSTRUCTIONS.md) → Layer 3 (User prompt)
```

Each layer narrows and specializes the previous. Layer 1 is stable and versioned. Layer 3 is ephemeral and task-specific.

## Why This Works

1. **Separation of concerns** — Each layer handles different scope/timeline
2. **Version control** — Layers 1-2 are git-tracked
3. **Progressive disclosure** — Agent sees relevant detail at each level
4. **Composability** — Projects can share Layer 1 while customizing Layer 2/3

See also: [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/agents-dot-md|AGENTS.md Pattern]], [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/system-instructions|System Instructions]]
