---
type: "concept"
title: "Code Formatters"
description: "Tools that automatically normalize source code formatting to a fixed style"
tags: ["tooling", "formatting", "style", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Code Formatters

## Summary

Code formatters (gofmt, prettier, black, rustfmt, clang-format) automatically normalize code style, ending style debates and review noise. They are a prerequisite for reliable diffs and fast review — and a source of churn when configured late or inconsistently.

## Details
- Mechanism: formatters parse source and re-emit it in canonical style; they run on save, in editors, and in CI (format-check as a gate); config files (prettierrc, pyproject/black, .editorconfig) pin rules per project; some formatters are opinionated with no config (gofmt, rustfmt defaults), which removes bikeshedding entirely.
- Concrete example: a repo adopts prettier with a single config; CI fails on unformatted files, so style never appears in review; a merge-train runs format-on-save and the diff noise disappears. The anti-pattern: formatting the whole codebase in the same commit as a feature, making history unblamable.
- Failure modes: formatter config drift between projects (files reformat when opened); formatting-only commits mixed with logic changes; formatters that cannot express a needed style (rare constructs get mangled); and language ecosystems where formatters disagree on semantics, causing cross-tool churn.
- Operational tradeoffs: formatters trade a little control for consistency and review speed — the standard is adopt early, config once, enforce in CI, and run format-on-save. Let the formatter win style arguments; reserve review energy for behavior.
- RSIS3/mykb relevance: loop-generated code passes through the repo's formatter in CI, so generated patches arrive style-clean without manual cleanup.
- Adoption sequencing: add the formatter and config first, apply it in a dedicated commit, then enforce in CI — mixing formatting with features destroys blameability.
- Edge policy: decide up front how generated code and vendored files are excluded so the formatter does not fight code generators.

## Related
- [[wiki/software-engineering/code-review|Code Review]] — formatters eliminate style noise from reviews
- [[wiki/dev-tools/markdown-authoring|Markdown Authoring]] — markdown formatters keep notes tidy
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]] — formatters and linters run together
- [[wiki/software-engineering/developer-experience|Developer Experience]] — formatting automation removes friction
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — format checks gate CI
