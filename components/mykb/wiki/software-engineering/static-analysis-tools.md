---
type: "concept"
title: "Static Analysis Tools"
description: "Programs that analyze source code without running it to find bugs, smells, and policy violations"
tags: ["tooling", "quality", "analysis", "linting"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Static Analysis Tools

## Summary

Static analysis tools inspect code without running it — linters, type checkers, security scanners, and complexity analyzers — catching whole bug classes before tests or production. They are the cheapest quality layer: rules encoded once, enforced on every change.

## Details
- Mechanism: tools parse/analyze source: linters (ESLint, Ruff, golangci-lint) enforce style and known anti-patterns; type checkers (mypy, TypeScript) verify contracts statically; security scanners (Semgrep, CodeQL, bandit) detect vulnerability patterns (injection, insecure crypto); complexity and dead-code analyzers flag maintainability risk. CI runs them as gates with pre-commit for fast feedback.
- Concrete example: a Python repo gates on Ruff + mypy + bandit; a new dependency flagged by the security scanner fails CI before merge; a type-checking fix catches a None-handling bug that tests missed; a complexity rule stops a function from growing past maintainable size.
- Failure modes: tool sprawl — overlapping rulesets with conflicting opinions; false positives that teach teams to suppress everything (review suppressions); slow gates that get bypassed; and rules that encode taste rather than risk, generating noise.
- Operational tradeoffs: static analysis trades a little setup and false-positive triage for early, cheap bug detection; the pattern is a small, maintained rule set, severity tiers (block vs warn), suppressions reviewed, and results visible in the PR flow.
- RSIS3/mykb relevance: the wiki's generated code would be gated by the repo's static-analysis set, so loop output arrives with lint, types, and security checks already applied.
- Rule stewardship: assign an owner per tool and review rule additions quarterly; rulesets grow until they enforce taste unless pruned.
- Suppression audit: count suppressions in CI and trend them; a rising suppression count means the tool is being trained to ignore real issues.

## Related
- [[wiki/software-engineering/code-review|Code Review]] — automation handles the mechanical part of review
- [[wiki/software-engineering/type-systems|Type Systems]] — type checking is the deepest static analysis
- [[wiki/software-engineering/code-formatters|Code Formatters]] — formatting rules complement lint rules
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — SAST guards dependencies and code
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — analysis gates run in CI
