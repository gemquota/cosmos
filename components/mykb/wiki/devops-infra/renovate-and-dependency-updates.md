---
type: "concept"
title: "Renovate & Dependency Updates"
description: "Automated pull requests that keep dependencies current"
tags: ["renovate", "dependencies", "updates", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Renovate & Dependency Updates

## Summary
Renovate (and Dependabot) automate dependency updates: they watch package manifests, open pull requests for new versions, and group, schedule, and merge updates according to policy. They turn dependency maintenance from a periodic chore into a continuous, reviewable stream that keeps the supply chain current.

## Details
- Mechanism: Renovate scans repositories for dependency manifests (package.json, requirements.txt, Dockerfiles, GitHub Actions, Terraform, and hundreds more); on schedule or on release, it opens PRs that bump versions, update lockfiles, and add changelogs; configuration controls grouping, scheduling, automerge, and which updates are ignored; the CI pipeline tests each PR before merge.
- Concrete example: Renovate opens a PR bumping a Python package from 2.4.1 to 2.5.0 with the changelog attached; CI runs tests; the PR auto-merges when green; a major version is grouped and held for manual review; security advisories get priority handling with expedited PRs.
- Failure modes: update spam — hundreds of PRs overwhelming reviewers (group minor/patch updates, automerge with test coverage); blind automerge shipping breaking updates when tests are weak (only automerge with real test gates); lockfile conflicts between parallel PRs; version constraints that block updates forever or jump majors unexpectedly; updates that are merged but never deployed, leaving the repo ahead of production.
- Tradeoffs: automation guarantees dependencies stay current and reduces manual chore time, but it moves review burden to triage — the team must decide what automerges and what needs eyes; the alternative, manual updates, is slower and accumulates CVE debt; the payoff is a smaller, more frequent upgrade surface instead of quarterly migration events.
- Operational notes: configure per-ecosystem policies, monitor merge success rate, and keep test coverage strong enough to trust automerge.
- RSIS3 relevance: cosmos's dependencies (python, node) should ride the same continuous-update loop — RSIS3's own patch cadence signal benefits when the underlying stack stays current.

## Related
- [[wiki/devops-infra/dependency-mapping-and-blast-radius|Dependency Mapping & Blast Radius]]
- [[wiki/devops-infra/os-updates-and-immutable-images|OS Updates & Immutable Images]]
