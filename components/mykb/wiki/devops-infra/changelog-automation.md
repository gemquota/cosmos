---
type: "concept"
title: "Changelog Automation"
description: "Generating human-readable change logs from merged changes"
tags: ["changelog", "releases", "automation", "docs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Changelog Automation

## Summary
Changelog automation derives release notes from commit history, PR titles, or issue labels instead of hand-writing them. Conventional Commits parse commit types into Keep a Changelog sections; tools like git-cliff, semantic-release, and release-please generate and commit the changelog as part of the release pipeline.

## Details
- Mechanism: parse commits for conventional-commit prefixes (feat, fix, chore, docs, breaking change); group entries into Added/Changed/Fixed sections; the version bump derives from the highest-impact change; tools diff from the last tag so each release entry appears exactly once.
- Concrete example: a PR merged as `feat(api): add cursor pagination` becomes an Added entry and bumps the minor version; `fix(db): handle null timestamps` becomes a Fixed entry and bumps the patch. Release-please opens a release PR that updates the changelog and version files, and merging it publishes.
- Failure modes: undisciplined commit messages (all `fix` or all `chore`) produce a useless changelog — enforce Conventional Commits with a lint rule; squash merges that discard the original message lose the type; duplicate entries when multiple tags match the same range; generated changelogs that overwrite hand-written historical notes unless a template preserves them.
- Tradeoffs: automation guarantees the changelog exists and is timely but reflects commit hygiene rather than user-facing narrative; many teams add a short human "Notable changes" summary on top of the automated list. The alternative, a fully manual changelog, decays quickly under daily merge pressure.
- Operational notes: generate at release time rather than per commit, keep a single source of truth (CHANGELOG.md or a release-notes API), and link entries to PRs and issues so readers can dig into detail.
- RSIS3 relevance: RSIS3 versions its own protocols and parameters — automated changelogs make loop-evolution history auditable, so a regression can be traced to the exact change that introduced it.

## Related
- [[wiki/cloud-infra/storage-tiering-automation|Storage Tiering Automation]]
- [[wiki/devops-infra/semantic-release-automation|Semantic Release Automation]]
- [[wiki/devops-infra/database-failover-automation|Database Failover Automation]]
- [[wiki/devops-infra/changelog-practices|Changelog Practices]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
