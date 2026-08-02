---
type: "concept"
title: "Static Analysis"
description: "Analyzing code without running it to find bugs and enforce rules"
tags: ["static-analysis", "analysis", "quality", "tools"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Static_program_analysis", "https://en.wikipedia.org/wiki/Code_audit"]
---

# Static Analysis

## Summary
Static analysis inspects code without executing it — type checking, linting, dataflow and null-safety analysis, and vulnerability scanning. It finds whole classes of bugs cheaply at edit time, and its power grows the more precise the analysis.

## Details
- Levels of analysis: syntax, style (linters), types, dataflow, and interprocedural reachability.
- Sound analysis finds all real bugs (but flags false positives); unsound analysis finds many real bugs fast (and misses some).
- Integrate early and continuously: editor diagnostics, pre-commit, and CI gates keep findings fresh.
- False positives are the adoption killer — tune, suppress with reasons, and measure signal.
- Security static analysis (SAST) targets vulnerability patterns like injection and unsafe deserialization.
- For the mykb bundle, static analysis covers the tooling's code and the corpus: frontmatter, link, and structure checks.
- Worked example — a static analysis pass flags an unescaped path join in the wiki sync script; the fix lands before the bug ever reaches a user.

Worked example — a static analysis pass flags an unescaped path join in the wiki sync script; the fix lands before the bug ever reaches a user.

## Related
- [[wiki/software-engineering/linting-practice|Linting Practice]]
- [[wiki/software-engineering/type-systems-in-practice|Type Systems in Practice]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
- [[wiki/compositions/shift-left-security|Shift-Left Security]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
- [[wiki/communities/lint-staged|Lint-Staged]]
- [[wiki/communities/vulnerability-scanning-ci|Vulnerability Scanning in CI]]
- [[wiki/testing/ci-quality-gates|CI Quality Gates]]
