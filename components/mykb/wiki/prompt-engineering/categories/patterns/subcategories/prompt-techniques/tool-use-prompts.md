---
type: "entity"
title: "Tool Use Prompt Patterns"
tags: ["prompt", "tools", "codex", "function-calling"]
source: ["session-89e039d9.md", "session-c88fb179.md"]
---

# Tool Use Prompt Patterns

Patterns for writing prompts that effectively drive tool-using agents in the Codex environment.

## The Tool Loop Pattern

```
Reception → Plan → Execute Tool → Observe → Plan Next → ...
```

Each turn consists of:
1. **user** provides a goal or instruction
2. **assistant** plans steps using available tools
3. **exec_command / read_file / apply_patch** — tool executions
4. **Observation** — tool output feeds back into reasoning
5. **Repeat** until goal complete

## Effective Tool Instructions

### Instruction with Context
```
{"instruction": "Update X to do Y", "file_path": "src/file.py", "old_string": "...", "new_string": "..."}
```

### Batch Operations
```
{"instruction": "Apply transformation to all files in directory/", "pattern": "*.py"}
```

### Verification Steps
```
{"instruction": "After making changes, run tests to verify", "command": "pytest"}
```

## Key Insights

- **Specific instructions** outperform vague goals
- **File paths** should always be absolute or project-relative
- **Old/new string pairs** are more reliable than line numbers
- **Verification steps** reduce error cascades
- **Wait for previous** prevents race conditions in batch operations

See also: [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/system-instructions|System Instructions]], [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/iterative-refinement|Iterative Refinement]]
