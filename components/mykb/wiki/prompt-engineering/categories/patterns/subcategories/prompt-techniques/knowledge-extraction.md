---
type: "entity"
title: "Knowledge Extraction Prompts"
tags: ["prompt", "wiki", "daemon", "extraction", "mykb"]
source: ["session-0c0a9b0f.md", "session-a39de5db.md"]
---

# Knowledge Extraction Prompts

The wiki daemon's prompt architecture for extracting structured knowledge from session transcripts — a self-referential prompt system.

## The Pipeline Prompts

### Post-Tool-Use Hook
Captures tool outputs as raw material:
```
At PostToolUse, save the interaction to the session buffer
with type, tool name, arguments, and result.
```

### Session-Stop Hook
Extracts entities, decisions, and facts:
```
At Stop, process the session buffer:
1. Extract entity references and definitions
2. Identify decisions made
3. Capture factual statements
4. Generate YAML frontmatter
```

### Output Format
```
---
type: "entity"
title: "[Entity Name]"
description: "[Brief description]"
tags: [tag1, tag2]
timestamp: "[ISO timestamp]"
source: ["session-[id].md"]
---

## Overview
[Entity documentation]
```

## Self-Referential Nature

The wiki daemon's prompts are themselves documented in the wiki as prompt-engineering patterns. This creates a recursive knowledge extraction loop where:

```
Prompt → Session → Extract → Wiki Page → Better Prompts → ...
```

See also: [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/system-instructions|System Instructions]], [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/iterative-refinement|Iterative Refinement]]
