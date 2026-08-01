---
type: "concept"
title: "Tree of Thought"
description: "Exploring multiple reasoning branches with evaluation and backtracking"
tags: ["tree-of-thought", "reasoning", "search", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Tree of Thought

## Summary
Tree of thought generalizes chain of thought into a search: the model proposes multiple reasoning steps, evaluates them, and explores promising branches with backtracking. It matters because single linear traces fail on problems needing exploration. It brings classical search to LLM reasoning.

## Details
- Steps: generate candidates, evaluate, expand the best, backtrack on dead ends.
- Analogous to search in planning and MCTS.
- Cost grows quickly; budgets and pruning are essential.
- Open questions: evaluation quality of intermediate nodes.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the search paradigm it borrows
- [[wiki/concepts/monte-carlo-tree-search|Monte Carlo Tree Search]] — the search algorithm it resembles
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the linear baseline
- [[wiki/concepts/planning-as-search|Planning as Search]] — the general framework
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — another way to diversify answers
