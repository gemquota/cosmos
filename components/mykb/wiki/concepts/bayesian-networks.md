---
type: "concept"
title: "Bayesian Networks"
description: "Graphical models encoding conditional dependencies among variables"
tags: ["bayesian", "probabilistic-models", "graphical-models"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Bayesian Networks

## Summary
A Bayesian network is a directed acyclic graph (DAG) whose nodes are random variables and whose edges encode direct probabilistic dependencies. Each node carries a conditional probability table or distribution over its values given its parents, and the graph's structure lets the joint distribution factor into a product of local terms — the compact representation that makes reasoning tractable.

## Details
- The graph encodes conditional-independence assumptions: a node is independent of its non-descendants given its parents (the Markov condition). That property is both the network's power and its danger. Correct structure shrinks inference dramatically; a missing or spurious edge silently encodes a wrong independence assumption and the network will produce confident, incorrect beliefs.
- The joint distribution factors as the product over nodes of P(node | parents). Exact inference uses variable elimination or belief propagation: you marginalize variables by summing them out in an order that keeps intermediate factors small. The catch is that the treewidth of the graph governs cost — networks with densely connected substructures blow up, which is why exact inference is replaced by sampling methods like Gibbs sampling, likelihood weighting, or particle filters when the graph is large.
- Learning a network is two problems in one: structure learning (which edges exist) and parameter learning (the conditional probabilities). Parameters can be fitted by maximum likelihood or Bayesian estimation from data, but structure search is combinatorial — greedily adding and removing edges under a score like BIC or Bayesian Dirichlet is the practical compromise. The tradeoff is between model complexity and fit, and overfit structures encode noise as dependency.
- Failure modes include cycles (the DAG requirement forbids feedback, which is why temporal models use dynamic Bayesian networks with time slices), deterministic nodes that create zero-probability regions, and sensitivity to discretization when variables are continuous.
- RSIS3 relevance: a knowledge graph with typed links is a cousin of a Bayesian network. If the wiki's link structure carried weights or probabilities, retrieval could use belief propagation instead of keyword scoring — and network diagnostics such as unobserved confounders map directly to missing-link analysis.

## Related
- [[wiki/concepts/probabilistic-programming|Probabilistic Programming]] — building and inferring such models
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — temporal cousin
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]] — adds hidden state
- [[wiki/concepts/active-inference|Active Inference]] — Bayesian machinery applied to agents
- [[wiki/agent-systems/risk-bounded-agents|Risk Bounded Agents]]
- [[wiki/concepts/belief-states|Belief States]]
- [[wiki/concepts/abductive-reasoning|Abductive Reasoning]]
