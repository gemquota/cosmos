---
status: "growing"
type: "entity"
title: "Hard Rules"
description: "Bash — shell scripting language, Frontend — client-side UI, IDE — code editor environment"
tags: ["entity", "ast", "bash", "bug", "frontend", "ide"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---


## Hard Rules

Hard Rules appears in 1 session(s) categorized as Debugging, Frontend, Shell. Related topics: bash, frontend, ide.

**Domain:** OS & Shell › [[wiki/web-platforms/00-index|Shell Environment]] › [[wiki/web-platforms/00-index|Dev Tools]]

## Overview

Hard rules are constraints that cannot be bent: lint and style rules, type invariants, contract requirements, or process gates. They are called hard because enforcement is automatic and failures are visible, rather than relying on reviewers or good intentions. Debugging sessions often trace bugs to rules that were bypassed, so hard rules are placed where violations are caught early.

## Applying Hard Rules

- Enforce in CI: linters, type checks, and format checks run on every change and block merges when they fail.
- Assert invariants at runtime where a broken assumption is worse than a crash.
- Document exceptions explicitly — a rule with an unmanaged escape hatch is not hard.

## Choosing What to Make Hard

Hard rules work best for cheap, deterministic checks with a clear failure mode. Formatting, linting, type checking, and dependency-audit gates all qualify: they run in seconds and catch whole classes of defects before review. Rules that need human judgment — architecture taste, naming, or large refactor approvals — do not. Making those hard tends to produce either a veto process that slows everyone down or a rule that gets bypassed and loses credibility.

## When Hard Rules Fail

Teams hit trouble when hard rules block legitimate work or when they are added without a migration path. A lint rule that rejects an entire code style forces noisy suppressions; a type invariant added mid-project can stall an otherwise safe change. The fix is to keep rules narrow, add them with a migration window, and treat the rule set as a product that gets pruned. Escalations should be visible: when an exception is granted, it should be recorded next to the rule so the next reviewer sees the history.

## Related Concepts

## Related Concepts

- [[wiki/dev-tools/conventional-commits|Conventional Commits]] — enforced commit conventions
- [[wiki/software-engineering/00-index|Software Engineering]] — process gates and standards

## Related Entities

- [[wiki/shell-environment/categories/dev-tools/bootstrap|Bootstrap]]
- [[wiki/shell-environment/categories/dev-tools/claude-code|Claude Code]]
- [[wiki/shell-environment/categories/dev-tools/claude|Claude]]
- [[wiki/shell-environment/categories/dev-tools/core-standard-the|Core Standard The]]
- [[wiki/shell-environment/categories/dev-tools/evolver|Evolver]]
- [[wiki/shell-environment/categories/dev-tools/frontend-app-builder-use|Frontend App Builder Use]]
- [[wiki/shell-environment/categories/dev-tools/image-gen|Image Gen]]
- Jul
