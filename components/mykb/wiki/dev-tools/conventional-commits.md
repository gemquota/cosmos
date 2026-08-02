---
type: "concept"
title: "Conventional Commits"
description: "A lightweight commit message convention that encodes the type and scope of each change"
tags: ["git", "commits", "conventions", "release"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.conventionalcommits.org/en/v1.0.0/", "https://github.com/conventional-changelog/commitlint"]
---

# Conventional Commits

## Summary
Conventional Commits prefixes messages with types like `feat:`, `fix:`, and `docs:` so tools and humans can read intent at a glance. Changelogs, releases, and semantic version bumps can be derived automatically.

## Details
- Format: `type(scope): description`; breaking changes use `!` or a `BREAKING CHANGE:` footer.
- Pairs with semver: fixes bump patch, features bump minor, breaking changes bump major.
- RSIS3 relevance: the wiki's acquisition rounds are `feat:`-class changes to knowledge.
- Conventional Commits is a lightweight commit-message convention: type(scope): description, with types like feat, fix, docs, and breaking-change markers.
- The convention makes history machine-readable — changelogs, version bumps, and release notes can be generated from the commits.
- The rules are deliberately small: a valid prefix, an imperative summary, and optional body and footer sections.
- Adoption costs a little message discipline and pays in automation and greppable history.
- **Worked example / comparison** — Worked example — 'fix(links): repair broken wikilink after merge-conflict resolution' triggers a patch release and lands in the changelog automatically.
- For mykb, conventional commits is the history convention the wiki's own release-days and changelog practice build on.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]]
- [[wiki/dev-tools/semver-tooling|Semver Tooling]]
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]]
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]]
- [[wiki/data-storage/data-versioning|Data Versioning]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
