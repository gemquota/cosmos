---
type: "concept"
title: "Code-Generation Agents"
description: "Agents that write, test, and patch code in real repositories"
tags: ["code-generation", "agents", "software-engineering", "patches", "testing"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2310.06770"]
---

# Code-Generation Agents

## Summary
Code-generation agents operate inside a repository: they read context, produce patches, run tests, and iterate until the change is correct. This matters because it turns coding from a completion exercise into an engineering loop — and SWE-bench showed the gap between generating code and resolving real issues. RSIS3's own code generation is AST-aware and test-gated, applying the same discipline to itself.

## Details
- **Repository context**: the agent must locate relevant files and understand build/test conventions before editing.
- **Patch discipline**: changes are surgical diffs (apply_patch), not full-file rewrites, so review and rollback stay easy.
- **Test loop**: run tests, observe failures, fix, re-run; the loop exits only on green or budget exhaustion.
- **Gating**: no mutation is accepted without passing tests — RSIS3 rolls back via git when tests fail.
- Evaluation uses issue-resolution benchmarks (SWE-bench style) plus diff-quality review.
- Worked example: an agent fixes a failing test by searching the codebase, patching one function, running the suite, and verifying.

## Related

- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — the broader workflow this agent executes
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — re-running the edit-test cycle for debugging
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioning the agent's own code and config
- [[raw/archive/session-artifacts-2026-07/tools/apply-patch-1-10|apply_patch — the surgical edit tool RSIS3 uses
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — an example of agent-built systems
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — knowledge captured from coding sessions