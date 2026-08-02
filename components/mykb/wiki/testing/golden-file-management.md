---
type: "concept"
title: "Golden File Management"
description: "Curating canonical expected-output files and their update workflow"
tags: ["golden-files", "testing", "baselines", "cli"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://llvm.org/docs/TestingGuide.html", "https://www.llvm.org/docs/CommandGuide/FileCheck.html"]
---

# Golden File Management

## Summary
Golden files are canonical expected outputs stored on disk and compared against test results. Managing them well, naming, reviewing, and updating, decides whether they are a precise oracle or a liability that hides regressions.

## Details
- LLVM and FileCheck popularized golden-file comparison for compiler and CLI output.
- Update workflow: regenerate on intentional change, review the diff, and commit with the code change.
- Never blindly accept updates: a regenerated golden can hide a real regression.
- Keep goldens small and focused; split by feature instead of one giant file.
- Store goldens near the test; CI diff output should make failures readable.
- Version-controlled goldens give change history and reviewability.
- Combine exact match with semantic checks such as contains or parses where output is brittle.

## Related
- [[wiki/testing/snapshot-testing|Snapshot Testing]] — framework-managed golden baselines
- [[wiki/testing/golden-tests|Golden Tests]] — fixed expected outputs for LLM systems
- [[wiki/testing/approval-testing|Approval Testing]] — human sign-off on golden changes
- [[wiki/testing/regression-testing|Regression Testing]] — goldens catch output drift
- [[wiki/testing/characterization-testing|Characterization Testing]] — goldens lock existing behavior
- [[wiki/software-engineering/git-workflows|Git Workflows]] — reviewing golden file diffs in PRs
