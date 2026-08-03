---
type: "concept"
title: "Tree of Thought"
description: "Exploring multiple reasoning branches with evaluation and backtracking"
tags: ["tree-of-thought", "reasoning", "search", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Tree of Thought

## Summary

Tree-of-thought (ToT) extends chain-of-thought by exploring multiple reasoning branches — generating candidate steps, evaluating them, and searching (BFS/DFS) the tree of possibilities before committing to an answer. It trades heavy inference for deeper exploration on hard problems.

## Details
- Mechanism: at each reasoning step the agent generates K candidate continuations, evaluates them (self-score, verifier, or test), keeps the promising branches, and explores further; search policies (breadth/depth, beam width) bound the tree; the final answer comes from the best-completed path. It is reasoning as search rather than a single greedy trace.
- Concrete example: a constraint puzzle (24 game, Sudoku-like logic) generates candidate equations at each step, prunes by correctness, and explores the survivors; a planning task generates action sequences and evaluates each branch against the goal before choosing; a debugging task explores fix hypotheses in parallel and tests them.
- Failure modes: combinatorial explosion without pruning (evaluation must be cheap and discriminative); evaluators that misjudge branches (pruning the correct path); cost — ToT multiplies tokens per problem; and overkill — simple problems waste budget where single-path reasoning suffices.
- Operational tradeoffs: ToT buys depth and robustness on hard, verifiable problems at multiplied inference cost; the discipline is using it where steps are verifiable and branches diverge, bounding the tree, and falling back to cheaper methods for routine tasks.
- RSIS3/mykb relevance: the wiki's planning passes use bounded tree search for hard design choices, with the explored branches logged so the loop's reasoning is auditable.
- Evaluation design: the branch evaluator must be fast and discriminative; a slow or noisy evaluator makes the search worse than single-path reasoning.
- Result reporting: log the tree (branches explored, pruned, chosen) so reviewers can see why the agent committed to its path — search is only auditable with its trace.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — the search paradigm it borrows
- [[wiki/concepts/monte-carlo-tree-search|Monte Carlo Tree Search]] — the search algorithm it resembles
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the linear baseline
- [[wiki/concepts/planning-as-search|Planning as Search]] — the general framework
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — another way to diversify answers
