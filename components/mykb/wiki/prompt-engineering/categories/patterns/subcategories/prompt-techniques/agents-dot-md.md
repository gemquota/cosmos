---
type: "entity"
title: "AGENTS.md as a Prompt Pattern"
tags: ["prompt", "agents.md", "system-instruction", "codex"]
source: ["session-4b35bd59.md", "session-0c0a9b0f.md", "session-a39de5db.md"]
---

# AGENTS.md as a Prompt Pattern

A foundational prompt engineering pattern in the Codex ecosystem. The AGENTS.md file serves as a persistent system instruction that shapes agent behavior across sessions.

## Structure

Every project in the ecosystem has an AGENTS.md that defines:
- **Constitutional rules** — Core invariants the agent must follow
- **Operating procedures** — How to interact with the codebase
- **Code conventions** — Style, testing, and architecture guidelines
- **Quick-start instructions** — How to begin working with the project

## Examples from the Ecosystem

| Project | AGENTS.md Focus |
|---------|----------------|
| `ww/` | Bridge agent operations, testing absolutes |
| `rsis3/` | Constitution v2.0.0, identity invariants |
| `2b/` | Gemma 2B harness specifications |
| `mykb/` | Knowledge extraction pipeline |
| `vepa2/` | Emergent physics system rules |

## Design Principles

1. **Persistent context** — Survives across sessions, unlike ephemeral instructions
2. **Machine-readable** — Parsed by both human and AI readers
3. **Executable constraints** — Rules that the agent can self-enforce
4. **Version controlled** — Changes tracked in git alongside code
5. **Composable** — Multiple AGENTS.md files at different directory levels

See also: [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/system-instructions|System Instructions]], [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/tool-use-prompts|Tool Use Prompts]]
