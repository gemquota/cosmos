---
type: "concept"
title: "Static Analysis Tools"
description: "Programs that analyze source code without running it to find bugs, smells, and policy violations"
tags: ["tooling", "quality", "analysis", "linting"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Static Analysis Tools

## Summary
Static analysis inspects code without executing it, using type checking, dataflow, and heuristics to flag defects and style issues. Linters and type checkers are the everyday form; deep analyzers find security and correctness bugs.

## Details
- Categories: type checkers, linters, security scanners (SAST), and complexity analyzers.
- Run in CI and in editors; rules must be tuned to avoid noise fatigue.
- RSIS3 relevance: the wiki's link validator is a static analysis tool for notes.

## Related
- [[wiki/software-engineering/code-review|Code Review]] — automation handles the mechanical part of review
- [[wiki/software-engineering/type-systems|Type Systems]] — type checking is the deepest static analysis
- [[wiki/software-engineering/code-formatters|Code Formatters]] — formatting rules complement lint rules
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — SAST guards dependencies and code
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — analysis gates run in CI
