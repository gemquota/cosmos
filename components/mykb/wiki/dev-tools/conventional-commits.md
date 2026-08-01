---
type: "concept"
title: "Conventional Commits"
description: "A lightweight commit message convention that encodes the type and scope of each change"
tags: ["git", "commits", "conventions", "release"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Conventional Commits

## Summary
Conventional Commits prefixes messages with types like `feat:`, `fix:`, and `docs:` so tools and humans can read intent at a glance. Changelogs, releases, and semantic version bumps can be derived automatically.

## Details
- Format: `type(scope): description`; breaking changes use `!` or a `BREAKING CHANGE:` footer.
- Pairs with semver: fixes bump patch, features bump minor, breaking changes bump major.
- RSIS3 relevance: the wiki's acquisition rounds are `feat:`-class changes to knowledge.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]] — message conventions discipline branch merging
- [[wiki/dev-tools/semver-tooling|Semver Tooling]] — conventional commits drive version numbers
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]] — docs changes are typed commits too
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — CI can lint commit messages and build changelogs
- [[wiki/data-storage/data-versioning|Data Versioning]] — typed commits are versioning events
