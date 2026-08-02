---
type: "concept"
title: "Git Submodules"
description: "Embedding one git repository inside another at a pinned commit"
tags: ["git", "dependencies", "repos", "pinning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://git-scm.com/docs/git-submodule", "https://git-scm.com/book/en/v2/Git-Tools-Submodules"]
---

# Git Submodules

## Summary
Git submodules let a repository reference another repository at a specific commit. They keep nested projects versioned independently but add workflow friction: submodule state must be updated and committed deliberately.

## Details
- Operations like clone and branch-switch need `--recurse-submodules`; forgetting them leaves empty directories.
- Alternatives: vendoring, package managers, or workspace monorepos usually cause less pain.
- RSIS3 relevance: any embedded dependency of cosmos should weigh submodules against lockfiles.
- Git submodules embed another repository at a pinned commit inside the current repository, keeping the two histories separate.
- The submodule records a commit reference, not the content, so the parent repo stays small and each repo retains its own history.
- The costs are operational: clone must be recursive, and a submodule can drift or break when its upstream changes.
- Alternatives like vendoring or package managers trade the same isolation for different maintenance burdens.
- **Worked example / comparison** — Worked example — the wiki bundle pins the rsis3 repository as a submodule at a known commit; a bundle release records exactly which rsis3 version it was built against.
- For mykb, git-submodules is documented as the pin-and-embed pattern, with reproducible-builds as its quality goal.

## Related
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/security/supply-chain-security|Software Supply Chain Security]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
- [[wiki/security/sbom|SBOM]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
