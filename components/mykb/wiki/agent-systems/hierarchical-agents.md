---
type: "concept"
title: "Hierarchical Agents"
description: "Agents organized in a tree where higher levels delegate to lower ones"
tags: ["hierarchical", "delegation", "multi-agent", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Hierarchical_control_system", "https://arxiv.org/abs/2210.03629", "https://en.wikipedia.org/wiki/Hierarchical_task_network"]
---

# Hierarchical Agents

## Summary
Hierarchical agents arrange roles in a tree: a top-level planner delegates subtasks to mid-level coordinators, which delegate further to workers. It matters because it scales coordination and matches organizational structure. RSIS3's executive planner plus sub-agents is a shallow hierarchy.

## Details
- Each level abstracts the level below: workers report outcomes, not process.
- Benefits: modular roles, bounded context, clear accountability.
- Risks: information loss and latency across layers.
- Open questions: optimal depth and span of control.
- A hierarchy works because each level abstracts the one below it: the planner issues goals, coordinators decompose them, and workers return outcomes rather than process details.
- The classic failure modes are information loss across layers (workers' context never reaches the planner) and latency from top-down serialization; hybrid designs let workers escalate exceptions directly.
- Depth should be driven by span of control: add a level only when one node genuinely cannot supervise the next tier's work.
- **Worked example / comparison** — Worked example — a three-level wiki agent: a top-level editor delegates to section coordinators, which delegate to per-topic writers; each level reports summaries, not transcripts.
- For mykb, hierarchical delegation is how the curation workforce divides its 400-article pass into per-cluster batches, with promotion-readiness as the outcome contract between levels.

## Related
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]]
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]]
- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]]
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]]
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/deep-dives|Deep Dives]]
