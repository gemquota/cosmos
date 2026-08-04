---
type: "entity"
title: "Execution Modes"
description: "Execution Modes: environment-selected run behavior for development, testing, and production"
tags: ["entity", "api", "ast", "auth", "bash", "bootstrap", "environments"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# Execution Modes

## Summary

Execution Modes is the bootstrap-cluster entity for run-mode configuration: development, testing, and production behaviors selected by environment. Modes gate logging, validation, caching, and feature availability. They matter because the same code must behave differently without changing source. Mode discipline keeps the codebase honest about the difference between environments.

## Details

- **Definition** — An execution mode is a named configuration of runtime behavior, usually derived from the deployment environment.
- **Common modes** — Development, test, and production modes each adjust verbosity, optimization, and safety checks.
- **Mode selection** — Environment variables or build flags select the mode; selection must be explicit and auditable.
- **Behavior deltas** — Modes change logging levels, source maps, caching, mock providers, and feature flags.
- **Danger of drift** — When modes diverge too far, tests validate code that production never runs; parity matters. A mode matrix that names each behavior delta is the reference document that keeps the modes honest.
- **Worked example** — Development mode enables hot reload and verbose logs; production disables both and enables minification.
- **Failure modes** — Production mode accidentally enabled locally, secrets exposed by dev defaults, and mode-dependent bugs.
- **Practical relevance** — Execution modes pair with decision types and global config to keep environment policy centralized.
- **Mode matrix** — A documented matrix of behaviors per mode makes deltas explicit and reviewable.
- **Parity testing** — Running the test suite in production-like mode catches mode-only failures.
- **Audit logging** — Recording the active mode in logs explains environment-specific symptoms after the fact.
- **Mode detection** — Detecting the environment from deployment metadata rather than convention avoids misclassifying containers and CI runners.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/decisiontype|DecisionType]] — typed mode selection
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/best-for|Best For]] — choosing per-mode behavior
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/functionality-audit|Functionality Audit]] — verifying each mode
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/project-overview|Project Overview]] — documenting run modes
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/project-overview|Project Overview]] — documenting modes
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/missing-complexity-slider|Missing Complexity Slider]] — mode complexity
