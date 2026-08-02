---
type: "concept"
title: "Tree of Thought Search"
description: "Exploring multiple reasoning branches and backtracking to better answers"
tags: ["reasoning", "search", "decoding", "problem-solving"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.10601", "https://arxiv.org/abs/2201.11903"]
---

# Tree of Thought Search

## Summary
Tree of thought lets a model explore several reasoning paths, evaluate partial progress, and backtrack, instead of committing to one chain. It frames reasoning as search over a tree of thoughts. It improves hard problems at the price of many more model calls.

## Details
- **Mechanism** — generate candidate next thoughts, evaluate them, keep promising branches, and continue or backtrack; a search policy (BFS/DFS) controls the tree.
- **Components** — thought generation, state evaluation, and a search algorithm; the evaluator can be the model itself.
- **When it helps** — problems with checkable partial progress: planning, math, puzzles, and code design.
- **Cost** — each branch is a full generation; budgets cap total calls.
- **Worked example** — for a scheduling problem, the model generates three partial schedules, scores feasibility, discards one, and extends the survivors.
- **mykb relevance** — tree of thought is an existing mykb topic; its variants and Monte Carlo tree search extend the idea.

## Related
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — existing tree-of-thought concept
- [[wiki/prompt-engineering/monte-carlo-tree-search-llm|Monte Carlo Tree Search for LLMs]] — MCTS for LLMs
- [[wiki/prompt-engineering/beam-search-decoding|Beam Search Decoding]] — beam search as tree search
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — evaluating branches
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning with search
- [[wiki/prompt-engineering/tree-of-thoughts-variants|Tree of Thoughts Variants]] — related concept in this cluster
- [[wiki/ai-ml/self-attention|Self-Attention]] — attention foundation
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
