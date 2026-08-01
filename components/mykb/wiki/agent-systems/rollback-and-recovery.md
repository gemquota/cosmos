---
type: "concept"
title: "Rollback and Recovery"
description: "Returning a system to a known-good state after a failed change"
tags: ["rollback", "recovery", "git", "reliability", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://git-scm.com/docs/git-revert"]
---

# Rollback and Recovery

## Summary
Rollback and recovery is the ability to undo a change and restore the last known-good state, then resume from there. It matters because agents will make mistakes, and the cost of a mistake is determined by how fast and cleanly it can be reverted. RSIS3 treats rollback as a first-class mechanism: mutations are test-gated and git-backed, so a failed change is discarded instantly.

## Details
- **Snapshot discipline**: every change is a small, reversible unit (a patch, a commit, a checkpoint).
- **Test gates** decide when a state is known-good: a change that fails its tests is rolled back, not patched over.
- **Recovery paths**: revert the change, restore the checkpoint, and continue the session from the last good state.
- Deterministic replay complements rollback: re-run the failed sequence to learn why it failed before retrying.
- RSIS3's rule: no mutation is accepted unless all tests pass — git rollback enforces this automatically.
- Worked example: a refactor breaks the build; git revert restores the tree and the session resumes with the lesson logged.

## Related

- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — re-running failures before retrying
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioning what gets rolled back
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the record of what was changed
- [[raw/archive/session-artifacts-2026-07/topics/git-2|git — the version-control substrate
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — recovery lessons become knowledge
- [[wiki/ops/gap-report|Gap Analysis Report]] — recovery gaps identified