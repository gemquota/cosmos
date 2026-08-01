---
type: "concept"
title: "Release Trains"
description: "Shipping releases on a fixed cadence so every change rides the next scheduled departure"
tags: ["release-trains", "releases", "cadence", "devops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Release Trains

## Summary
A release train ships on a fixed schedule — every two weeks, every month — with whatever is ready at departure. The cadence makes planning predictable and small changes safe.

## Details
- Late features miss the train instead of delaying it, protecting the schedule.
- Trains reduce release anxiety by making deployment routine.
- Coupling risk: changes must merge early enough for integration testing before departure.
- Open question: how fixed a train should be when hotfixes are needed.

## Related
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — how train cargo is rolled out
- [[wiki/devops-infra/release-versioning|Release Versioning]] — naming each train departure
- [[wiki/devops-infra/changelog-practices|Changelog Practices]] — documenting what a train carries
- [[wiki/devops-infra/github-actions|GitHub Actions]] — automating train departures
