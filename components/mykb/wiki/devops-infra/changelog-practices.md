---
type: "concept"
title: "Changelog Practices"
description: "Maintaining readable, structured records of what changed in each release"
tags: ["changelog", "documentation", "releases", "communication"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Changelog Practices

## Summary
Changelogs record what changed in each release — added, changed, fixed, removed — in language humans can act on.

## Details
- Group by type (Added/Changed/Fixed/Removed) and reference issue/PR numbers.
- Keep the top entry for the unreleased version; move it at release time.
- Write for humans: behavioral changes matter more than internal refactors.
- Open question: how changelogs should be generated vs hand-curated.

## Related
- [[wiki/devops-infra/release-versioning|Release Versioning]] — changelogs map to versions
- [[wiki/devops-infra/release-trains|Release Trains]] — changelogs ship with each train
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — changelogs explain canary behavior
- [[wiki/api-protocols/api-versioning|API Versioning]] — documenting API changes
