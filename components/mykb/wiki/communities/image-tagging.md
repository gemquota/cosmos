---
type: "concept"
title: "Image Tagging"
description: "Naming container image versions so they are immutable and traceable"
tags: ["image-tagging", "containers", "releases", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Image Tagging

## Summary
Image tagging conventions decide how builds are named — immutable commit-short tags plus aliases like latest and env tags. Mutable tags break reproducibility; immutable tags make every deployment traceable to a build.

## Details
- Tag with commit SHA or build ID for immutability; add semver and env aliases on top.
- Re-tagging is a smell: publish a new tag rather than mutating an old one.
- Moveable aliases (latest, prod) are conveniences, not versions — keep an immutable audit trail.
- mykb relevance: wiki images tag by SHA with a v-prefixed release alias.

## Related
- [[wiki/communities/registry-practice|Registry Practice]]
- [[wiki/dev-tools/release-management|Release Management]]
- [[wiki/communities/version-bumping|Version Bumping]]
- [[wiki/communities/multi-stage-builds|Multi-Stage Builds]]
- [[wiki/communities/image-scanning|Image Scanning]]
