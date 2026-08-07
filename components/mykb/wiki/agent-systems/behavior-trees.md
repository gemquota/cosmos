---
type: "concept"
title: "Behavior Trees"
description: "Hierarchical control structures for composing reactive behaviors"
tags: ["behavior-trees", "control", "reactive", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)", "https://arxiv.org/abs/1709.00084"]
---

# Behavior Trees

## Summary
Behavior trees compose behaviors as a tree of nodes — sequences, selectors, conditions, and leaf actions — evaluated top-down on each tick. They make reactive control modular, debuggable, and reusable: subtrees can be recombined, and the tick discipline gives natural interruption and priority. They originated in games and apply to agent control flow.

## Details
- **Node types** — sequence nodes run children until one fails; selector nodes run children until one succeeds; decorators modify behavior (invert, retry, limit); leaves are actions or conditions returning success, failure, or running.
- **Tick discipline** — every node re-evaluates each tick, which gives reactive interruption: a high-priority branch can take over when its condition becomes true.
- **Composability** — subtrees are reusable modules, so libraries of behaviors (navigation, escalation, fallback) can be assembled per agent; this is easier to reason about than a monolithic finite-state machine.
- **Costs** — deep trees are hard to debug without visualization, and the tick discipline can waste evaluation on branches that will not run.
- **Worked example** — an agent's daily routine as a tree: a selector tries review-queue work first, falls back to stub-writing when the queue is empty, with a health-check condition at the root deciding whether to run at all.
- **LLM integration** — open design question: how tree control structures combine with LLM action selection, typically with the tree choosing policy and the model choosing the concrete action.
- **For mykb** — curation workflows branch like trees: the same checks (freshness, links, sources) run against every article batch, with conditions routing to repair or promotion paths.

- **Testing** — because trees are deterministic and visualizable, they can be unit-tested branch by branch: each subtree gets scenarios asserting success, failure, and running returns, which catches control bugs before deployment.
## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop trees control
- [[wiki/concepts/reactive-planning|Reactive Planning]] — the no-upfront-plan alternative
- [[wiki/concepts/production-rules|Production Rules]] — condition-action control
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — shared-state alternative
- [[wiki/ai-ml/article-health-scores|Article Health Scores]] — checks a curation tree runs
- [[wiki/agent-systems/agent-state-machines|Agent State Machines]] — state-based alternative
