---
type: "concept"
title: "Agentic Loops"
description: "Designing the goal, tools, and loop that lets a coding agent iterate to a solution on its own"
tags: ["agentic-loops", "loop-design", "coding-agents", "yolo-mode", "verification"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://simonwillison.net/2025/Sep/30/designing-agentic-loops/"]
---

# Agentic Loops

## Summary
An agentic loop is the arrangement of goal, tools, and iteration that lets a coding agent brute-force its way to a solution. Simon Willison's framing: an LLM agent is something that runs tools in a loop to achieve a goal, and the art of using them well is designing the tools and loop rather than the prompt. Coding agents like Claude Code and Codex CLI can now exercise the code they write, correct errors, and run experiments — which turns prompt-writing into loop-designing.

## Details
- **Definition** — an agent is a tool-using loop toward a goal; the designable parts are the goal statement, the toolset, and the loop's stop and recovery rules.
- **YOLO mode** — approving every command by default is dangerous but unlocks brute-force effectiveness; three risks are destructive shell commands, exfiltration of files or secrets, and using the machine as a proxy for attacks.
- **Mitigations** — run in a sandbox (Docker or the Apple container tool), run on someone else's machine (GitHub Codespaces, Code Interpreter), or accept the risk with trusted-host network lockdown.
- **Tool selection** — expose the right commands for the loop; a shell is the most powerful tool, so the exposed surface defines blast radius.
- **Scoped credentials** — provide credentials to test/staging environments with contained damage, and set tight budget limits on anything that can spend money.
- **When to build a loop** — problems with clear success criteria that involve trial and error; signals are "ugh, I'm going to have to try a lot of variations."
- **Examples** — debugging a failing test, benchmarking SQL query performance with index experiments, bulk dependency upgrades with a solid test suite, and shrinking container sizes by iterating on base images.
- **Tests amplify value** — automated tests are the feedback signal that makes unattended iteration safe and productive; a cleanly passing suite is the precondition.

## Related
- [[wiki/llm-agents/loop-engineering|Loop Engineering]] — the systematic discipline
- [[wiki/llm-agents/loop-specification|Loop Specification]] — the formal artifact
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — what the loop feeds
- [[wiki/llm-agents/building-effective-agents|Building Effective Agents]] — workflows vs agents
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — durable loop state
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining done
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- Simon Willison, "Designing agentic loops", 2025-09-30 — https://simonwillison.net/2025/Sep/30/designing-agentic-loops/
