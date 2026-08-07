---
type: "concept"
title: "Monte Carlo Tree Search"
description: "Search that builds a tree by simulating random rollouts and backing up results"
tags: ["mcts", "search", "planning", "games"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Monte Carlo Tree Search

## Summary
Monte Carlo tree search (MCTS) grows a search tree by repeated cycles of selection, expansion, simulation, and backpropagation, guided by bandit-style selection (UCT). It matters because it searches huge spaces with limited compute. It powered AlphaGo and remains the standard for planning in games.

## Details
- Phases: select promising node → expand → simulate rollout → backpropagate outcome. Each iteration starts at the root, walks down the tree by repeatedly choosing the most promising child, expands a new node when it reaches a leaf, plays a rollout (a fast, usually random simulation) from that node to a terminal state, then backpropagates the outcome up the path, updating each visited node's visit count and average value. Repeating this millions of times concentrates the tree's growth on the branches that look best while still exploring uncertain ones.
- Balances exploration and exploitation via UCB scores. The selection rule is a multi-armed bandit algorithm — Upper Confidence Bounds — scoring each child as its average value plus an exploration bonus that shrinks as the child is visited more. The formula is: score = mean reward + c × sqrt(ln(parent visits) / child visits). The constant c trades exploration against exploitation: too high, the search wastes time on bad branches; too low, it locks onto a locally good line and misses a better one.
- Why it works: the tree is asymmetric — it grows deep and wide exactly where outcomes are promising — and the rollouts provide an unbiased (if noisy) value estimate that improves with search. It needs only a simulator, no domain heuristics, which is why it generalized from Go (where the branching factor defeated alpha-beta search) to games, robotics, and planning. AlphaGo's historic achievement was combining MCTS with learned value and policy networks, replacing random rollouts with learned guidance and beating the world champion.
- Applicable to agent planning where outcomes are simulatable: if an agent can simulate the effect of a candidate action (a tool call, a plan step), MCTS can allocate search effort to the most promising sequences. The open frontier is MCTS over LLM-generated branches — treating language-model continuations as actions and using MCTS-style search to plan multi-step reasoning, as in tree-of-thought and reasoning-search hybrids.
- The costs: MCTS needs a good simulator or learned model, a terminal or value signal, and enough budget for the exploration-exploitation tradeoff to work — with too little compute it behaves like shallow random sampling.
- RSIS3 relevance: an improvement pass that simulates candidate changes before committing them is MCTS-style planning over the space of possible passes — the tree is the set of change sequences, and the value is the predicted metric outcome.

## Related
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — search-based planning family
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — LLM analog of tree search
- [[wiki/concepts/multi-armed-bandit|Multi-Armed Bandit]] — the selection mechanism
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — the balance it implements
- [[wiki/concepts/planning-as-search|Planning as Search]] — the general framework
