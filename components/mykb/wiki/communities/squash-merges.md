---
type: "concept"
title: "Squash Merges"
description: "Collapsing a branch's commits into one before merging to main"
tags: ["squash-merges", "git", "history", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Squash Merges

## Summary
Squash merging folds a feature branch's whole commit set into a single commit on main, trading granular history for a clean, readable log. It is the standard for PR-based workflows where branch commits are messy.

## Details
- Squashing loses per-commit granularity and bisect fidelity within the branch.
- Pair squash with a good PR title and description — that becomes the commit message.
- Use conventional commits on the squashed message for changelog automation.
- mykb relevance: the wiki's PRs would squash to one conventional commit each.

The squash commit keeps the branch's net effect, so reviewers read one coherent change instead of a trail of fixup commits, and git bisect still works across merges even though the individual branch steps are gone; the discipline is to squash at merge time rather than rewriting shared history, and to write the squashed message as if it were the only record of the change, because that is what future maintainers and release notes will actually see.

Platforms that support squash-on-merge apply the policy mechanically, removing the temptation to hand-craft commit-per-step histories that nobody reads; the remaining risks are losing the branch's intermediate reasoning, mitigated by a rich PR description and links to the tracked issue, and squashing changes that should have been split into independent commits, so a squash policy works best when paired with review conventions that keep each PR focused on one logical change and with a convention that follow-up fixes arrive as separate commits rather than amendments to the squashed message.

When squashing is the norm, the branch's per-step commit messages still matter as raw material: a good workflow writes meaningful step messages as the change happens and then composes the squash summary from them, so the squash preserves the reasoning without cluttering the mainline log.

## Related
- [[wiki/communities/rebase-vs-merge|Rebase vs Merge]]
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/communities/semantic-release|Semantic Release]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
