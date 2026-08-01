---
type: "concept"
title: "Code Formatters"
description: "Tools that automatically normalize source code formatting to a fixed style"
tags: ["tooling", "formatting", "style", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Code Formatters

## Summary
Code formatters rewrite source to a canonical style — indentation, quoting, line length — removing formatting from human judgment. Prettier, gofmt, Black, and rustfmt are the archetypes.

## Details
- Format-on-save and a CI format check keep diffs clean and reviews focused on logic.
- Formatting is not a preference debate once adopted: the tool decides.
- RSIS3 relevance: consistent formatting extends to markdown, where linters normalize tables and headings.

## Related
- [[wiki/software-engineering/code-review|Code Review]] — formatters eliminate style noise from reviews
- [[wiki/dev-tools/markdown-authoring|Markdown Authoring]] — markdown formatters keep notes tidy
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]] — formatters and linters run together
- [[wiki/software-engineering/developer-experience|Developer Experience]] — formatting automation removes friction
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — format checks gate CI
