---
type: "concept"
title: "Monte Carlo Tree Search"
description: "Search that builds a tree by simulating random rollouts and backing up results"
tags: ["mcts", "search", "planning", "games"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Monte Carlo Tree Search

## Summary
Monte Carlo tree search (MCTS) grows a search tree by repeated cycles of selection, expansion, simulation, and backpropagation, guided by bandit-style selection (UCT). It matters because it searches huge spaces with limited compute. It powered AlphaGo and remains the standard for planning in games.

## Details
- Phases: select promising node → expand → simulate rollout → backpropagate outcome.
- Balances exploration and exploitation via UCB scores.
- Applicable to agent planning where outcomes are simulatable.
- Open questions: MCTS over LLM-generated branches.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — search-based planning family
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — LLM analog of tree search
- [[wiki/concepts/multi-armed-bandit|Multi-Armed Bandit]] — the selection mechanism
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — the balance it implements
- [[wiki/concepts/planning-as-search|Planning as Search]] — the general framework
