---
type: "entity"
title: "DecisionType"
description: "DecisionType: explicit typed models for decisions and branching logic"
tags: ["entity", "api", "ast", "backend", "bash", "bootstrap", "decisions"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# DecisionType

## Summary

DecisionType is the bootstrap-cluster entity for typed decisions: modeling choices as explicit, validated types rather than ad-hoc values. Typed decisions make branching logic readable and data-driven. They matter because untyped decisions are where bugs and miscommunication breed. The same typing discipline that protects data protects the logic that branches on it.

## Details

- **Definition** — A decision type enumerates the choices a branch can take, often with metadata about consequences and preconditions.
- **Enums and unions** — Closed sets of options are modeled as enums or discriminated unions so invalid values are unrepresentable.
- **Data-driven branching** — Tables or maps keyed by decision type replace sprawling if-else chains with configurable behavior.
- **Validation** — Types carry validation rules, so decisions are checked at their point of origin, not deep in consumers.
- **Auditability** — Typed decisions serialize cleanly, making them loggable and replayable.
- **Worked example** — A workflow engine routes tasks by decision type: approve, reject, or escalate, each with distinct handlers.
- **Failure modes** — Stringly-typed decisions, hidden fallback branches, and types that outgrow their meaning cause drift.
- **Practical relevance** — Decision types appear throughout this wiki: status fields, verdicts, and action types are all decision types.
- **Serialization** — Typed decisions serialize to stable strings or codes, so logs and storage remain meaningful.
- **Exhaustiveness** — Compile-time exhaustiveness checks force new cases to be handled, preventing silent defaults.
- **Migration** — Renaming or adding decision values is a schema change with a migration path, not a search-and-replace.
- **Documentation** — Documenting each decision type's meaning and consequences keeps the vocabulary shared across code and conversations.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/execution-modes|Execution Modes]] — mode-based branching
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/best-for|Best For]] — choosing among options
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/depth-levels|Depth Levels]] — nested decision structure
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/functionality-audit|Functionality Audit]] — checking all branches
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/presetsystem-2|PresetSystem]] — presets as decision bundles
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/probmap-2|ProbMap]] — probabilistic decisions
