---
type: "concept"
title: "Git for Notes"
description: "Using git version control for note repositories to get history, diffs, and rollback"
tags: ["git", "versioning", "notes", "history"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Git for Notes

## Summary
Git for notes means keeping a markdown knowledge base in a git repository so every change has history, authorship, and rollback. It gives a wiki the safety net that databases get from transactions: nothing is ever truly lost, every edit can be diffed and reviewed, and mistakes can be reverted to the last good state.

## Details
- **What you get** — full history, `git diff` for review, rollback on mistakes, and branching for experiments. A wiki with git can treat each curation pass as a commit, so the question "what did last week's consolidation change?" has a precise answer rather than a memory.
- **Costs** — merge conflicts on concurrent edits and binary blobs; text markdown minimizes both. Conflicts happen when two processes edit the same note at once — the classic case being an agent and a human working the same file — and resolving them requires a merge strategy, not just `git pull`.
- **Concrete example** — a botched batch edit renames a concept's title and breaks twenty wikilinks; with git, the diff shows exactly which files changed, the broken links are visible in the diff, and a single revert restores the prior state instead of requiring manual repair.
- **Failure modes** — committing generated artifacts (indexes, graphs) that change on every run, producing noisy histories; large binary attachments that bloat the repository; force-pushes and history rewrites that destroy the provenance value; and the trap of treating git as a backup — a local repository is one disk failure away from losing everything, so remote mirrors matter.
- **Tradeoffs** — git is the highest-fidelity, lowest-friction versioning for plain text, but it has no built-in conflict UI for non-technical users and no per-note ACLs; teams needing fine-grained permissions or web editing often layer a sync service on top. For a text-only knowledge base, those costs are usually acceptable.
- **Agent relevance** — RSIS3 already rolls back failed code changes via git; the same discipline applies to wiki edits made by the agent. Committing wiki changes separately from code changes keeps each history reviewable on its own.
- **RSIS3/mykb relevance** — git history doubles as provenance: every claim in the wiki can be traced to the commit that introduced it, which is exactly the audit trail the L3 consolidation practice wants for durable conclusions.

## Related
- [[wiki/data-storage/data-versioning|Data Versioning]] — the general practice git realizes
- [[wiki/memory/provenance|Provenance]] — git history doubles as provenance
- [[wiki/memory/org-mode|Org Mode]] — plain-text systems version cleanly
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — versioned PKM survives mistakes
- [[wiki/sources/index|Sources]] — the namespace whose history matters most
