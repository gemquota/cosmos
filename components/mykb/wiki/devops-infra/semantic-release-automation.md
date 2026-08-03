---
type: "concept"
title: "Semantic Release Automation"
description: "Deriving versions and changelogs from commit conventions"
tags: ["semver", "release", "automation", "changelog"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Semantic Release Automation

## Summary
Semantic-release automates the entire release process from commit messages: it parses Conventional Commits, determines the next version (major/minor/patch), generates the changelog, creates the git tag and release notes, and publishes the artifact. The version and the release notes become derived data, not hand-written decisions.

## Details
- Mechanism: commits must follow Conventional Commits (feat, fix, BREAKING CHANGE); semantic-release analyzes commits since the last release, applies the version rules, writes CHANGELOG.md, tags the commit, creates a GitHub/GitLab release, and triggers publish; release types (pre-release channels) can gate which commits reach which channel.
- Concrete example: a repo with `feat` commits since 1.2.0 releases 1.3.0; a commit with `BREAKING CHANGE` triggers 2.0.0; the changelog groups feat/fix/breaking sections automatically; the release tag and published package version come from the same computation, so they never disagree.
- Failure modes: undisciplined commits (all fix or all feat) producing wrong or empty releases — enforce Conventional Commits with a linter and block non-conforming merges; release-triggering commits merged by automation that then cannot run (release PRs need the same CI); tag conflicts when the tool runs twice; changelog overwrites of hand-written history; breaking changes shipped as minor because the commit message did not mark them.
- Tradeoffs: automation makes releases deterministic and frequent but bakes the policy into commit discipline — the cost is process, not technology; the alternative, manual version decisions, is flexible and error-prone; semantic-release pays off when releases are frequent enough that the discipline is self-enforcing.
- Operational notes: gate merges on commit format, test the release pipeline in a dry-run mode, and keep publish credentials scoped and rotated.
- RSIS3 relevance: cosmos's artifact releases could ride the same automation — version, changelog, and publish derived from commit history, giving RSIS3 an auditable release trail.

## Related
- [[wiki/cloud-infra/storage-tiering-automation|Storage Tiering Automation]] — related coverage in the same cluster
- [[wiki/devops-infra/release-engineering-trains|Release Engineering Trains]] — related coverage in the same cluster
- [[wiki/devops-infra/changelog-automation|Changelog Automation]] — related coverage in the same cluster
- [[wiki/devops-infra/release-trains|Release Trains]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
