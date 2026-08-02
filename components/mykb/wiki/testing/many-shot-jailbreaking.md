---
type: "concept"
title: "Many-Shot Jailbreaking"
description: "Exploiting long contexts packed with harmful examples to overwhelm safety behavior"
tags: ["security", "jailbreak", "context"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Many-Shot Jailbreaking

## Summary
Exploiting long contexts packed with harmful examples to overwhelm safety behavior

## Details
- Models increasingly imitate patterns found deep in long contexts.
- Attack scales with context length and example count.
- Defenses: context filtering, safety prompts near the end, and anomaly flags.
- Shows how context-window growth expands attack surface.

## Related
- [[wiki/testing/jailbreak-techniques|Jailbreak Techniques]] — attack family
- [[wiki/ml-frameworks/long-context-techniques|Long-Context Techniques]] — enabling technology
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — defensive placement
- [[wiki/ai-ml/content-moderation-pipelines|Content Moderation Pipelines]] — output filtering
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — discovery method
