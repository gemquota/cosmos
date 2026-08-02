---
type: "concept"
title: "Chain of Responsibility"
description: "Passing a request along a chain until some handler processes it"
tags: ["chain", "patterns", "design", "handlers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Chain of Responsibility

## Summary
Chain of responsibility lets each handler decide whether to process a request or pass it to the next — middleware pipelines, event filters, validation chains. It decouples senders from the specific handler that will act.

## Details
- Handlers are ordered; a handler either handles, forwards, or both (filtering).
- Pipelines (HTTP middleware) are the dominant modern form of this pattern.
- Ordering is semantics: reordering handlers changes behavior, so make order explicit.
- mykb relevance: the wiki build runs processors in a chain — frontmatter, links, sources, lint.

## Related
- [[wiki/software-engineering/mediator-pattern|Mediator Pattern]]
- [[wiki/software-engineering/decorator-pattern|Decorator Pattern]]
- [[wiki/software-engineering/command-pattern|Command Pattern]]
- [[wiki/software-engineering/pipeline-architecture|Pipeline Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
