---
type: "concept"
title: "Tag Strategies"
description: "How releases are marked in git and what tags point to"
tags: ["tags", "git", "releases", "conventions"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tag Strategies

## Summary
Tag strategies decide what a tag means — vX.Y.Z on release commits, environment tags, per-artifact tags — and how tags relate to branches. Good tagging makes any release findable and reproducible.

## Details
- Annotated tags carry messages and signatures; lightweight tags are just pointers.
- Tag the artifact-producing commit so builds are reproducible from the tag.
- Signed tags (and cosign on images) tie releases to identity for supply-chain trust.
- mykb relevance: the wiki tags vX.Y.Z on release commits and signs them.

## Related
- [[wiki/communities/version-bumping|Version Bumping]]
- [[wiki/communities/release-branches|Release Branches]]
- [[wiki/dev-tools/release-management|Release Management]]
- [[wiki/communities/image-tagging|Image Tagging]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
