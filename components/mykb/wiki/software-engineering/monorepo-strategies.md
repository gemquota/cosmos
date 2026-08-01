---
type: "concept"
title: "Monorepo Strategies"
description: "Version-control layouts that keep many projects in a single repository with shared tooling"
tags: ["monorepo", "git", "version-control", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.atlassian.com/git/tutorials/monorepos"]
---

# Monorepo Strategies

## Summary
A monorepo keeps multiple projects or packages in a single git repository with one build, one dependency graph, and atomic cross-project changes. The strategy trades independent versioning and access control for unified tooling, refactoring, and release coordination.

## Details
- Benefits: atomic commits across projects, consistent dependency versions, shared CI configuration, and easier cross-cutting refactors that touch several packages at once.
- Costs: repository size and clone times grow, CI must avoid rebuilding everything (changed-path detection), and permission granularity is coarser than per-repo access control.
- Tooling: Nx, Bazel, Turborepo, and Gradle understand workspace graphs and cache builds; most package managers support workspaces (npm/pnpm/Yarn, Cargo, Go modules).
- Variants: polyrepo (many repos), monorepo (one repo), and mono-repo-with-packages (single repo with independently versioned packages).
- Git-scale strategies include shallow clones, sparse checkouts, and partial clone filters to keep monorepos usable.
- RSIS3 relevance: cosmos keeps code, wiki, and ops together; git-for-notes discipline and atomic commits keep the wiki and code history coherent.
- Worked example: an app with a shared design system, two services, and docs all changed atomically in one pull request.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]] — branching and merging practices operate inside the chosen repo layout
- [[wiki/software-engineering/code-review|Code Review]] — reviewing large atomic changes is the monorepo's daily practice
- [[wiki/software-engineering/project-scaffolding|Project Scaffolding]] — shared templates keep monorepo packages consistent
- [[wiki/dev-tools/lockfiles|Lockfiles]] — one dependency graph per workspace demands one lockfile
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — changed-path pipelines make monorepo builds fast
- [[wiki/memory/git-for-notes|Git for Notes]] — the wiki itself lives in the cosmos monorepo
- [[wiki/concepts/project-lineage|RSIS3 Project Lineage]] — the monorepo is the lineage record for the project
