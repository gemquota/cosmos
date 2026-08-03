---
type: "concept"
title: "Release Trains"
description: "Shipping releases on a fixed cadence so every change rides the next scheduled departure"
tags: ["release-trains", "releases", "cadence", "devops"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Release Trains

## Summary
A release train ships on a fixed schedule — every two weeks, every month — with whatever is ready at departure. The cadence makes planning predictable, keeps small changes flowing, and converts release day from a crisis into a routine; changes that miss the train wait for the next one instead of delaying it.

## Details
- Mechanics: a cut-off point freezes what may board; integration and testing happen in the window before departure; the train departs with validated cargo; hotfixes ride an express path outside the schedule; each departure gets a version and changelog entry.
- Concrete example: a two-week train — feature freeze Friday, staging integration and regression tests through the weekend, departure Monday with a tagged release; a critical fix ships immediately as a hotfix patch, then merges back into the next train; teams plan work so the risky changes land early in the window.
- Failure modes: features merged too late, skipping integration testing and breaking the release; train anxiety — teams rush borderline changes to make the window, shipping bugs; the train departing with known-broken cargo because the gate was calendar-based; hotfix proliferation that erodes the cadence's value.
- Tradeoffs: trains give predictability and amortize release cost but introduce wait time for finished work and a discipline tax (cut-off enforcement); continuous delivery removes the wait but requires full automation and mature testing; trains suit teams where integration risk or process cost dominates; the schedule is a governance choice, not a technical necessity.
- Operational notes: enforce the cut-off, keep the gate honest (release quality, not date), and make hotfixes the documented exception.
- RSIS3 relevance: RSIS3's own artifact releases (dashboard builds, loop versions) can ride a train — predictable cadence for non-urgent changes, express path for fixes, matching the release discipline of its components.

## Related
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — how train cargo is rolled out
- [[wiki/devops-infra/release-versioning|Release Versioning]] — naming each train departure
- [[wiki/devops-infra/changelog-practices|Changelog Practices]] — documenting what a train carries
- [[wiki/devops-infra/github-actions|GitHub Actions]] — automating train departures
