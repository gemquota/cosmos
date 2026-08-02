---
type: "index"
title: "Concepts Index"
description: "Listing of the concepts/ folder (74 pages)."
tags: ["index"]
timestamp: "2026-08-02T00:00:00Z"
---

# Concepts

Part of [[wiki/index|Wiki Index]]. 74 pages.

- [[wiki/concepts/abductive-reasoning|Abductive Reasoning]] — Inference to the best explanation for observed evidence
- [[wiki/concepts/active-inference|Active Inference]] — Perception and action unified as minimizing expected free energy
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — Standardized task suites for comparing agent performance
- [[wiki/concepts/analogical-reasoning|Analogical Reasoning]] — Transferring structure from a known situation to a new one
- [[wiki/concepts/answer-set-programming|Answer Set Programming]] — Declarative programming where solutions are stable models of logic programs
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]] — Selection processes that decide what information an agent focuses on
- [[wiki/concepts/backward-chaining|Backward Chaining]] — Reasoning from a goal backward to known facts
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — Directed graphical models of probabilistic dependencies
- [[wiki/concepts/belief-states|Belief States]] — The agent's internal model of the world, updated by observations
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — Decision making under limited time, information, and computation
- [[wiki/concepts/calibration|Calibration]] — The match between an agent's stated confidence and its actual accuracy
- [[wiki/concepts/case-based-reasoning|Case-Based Reasoning]] — Solving new problems by retrieving and adapting similar past cases
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — Git-based snapshots taken before every mutation so any change can be reverted — the self-improvement safety net
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]] — The fixed structure of memory, perception, and control that shapes an agent's cognition
- [[wiki/concepts/cognitive-load|Cognitive Load]] — The demand placed on working memory by a task or context
- [[wiki/concepts/confabulation|Confabulation]] — Producing plausible but fabricated explanations without intent to deceive
- [[wiki/concepts/constraint-logic-programming|Constraint Logic Programming]] — Logic programming extended with constraint solving over domains
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — Finding solutions that meet a set of hard requirements
- [[wiki/concepts/deadband-control|Deadband Control]] — Hysteresis thresholds that keep a controller silent inside a target band and reactive outside it
- [[wiki/concepts/declarative-memory|Declarative Memory]] — Memory of facts and events that can be consciously stated
- [[wiki/concepts/defeasible-reasoning|Defeasible Reasoning]] — Reasoning with conclusions that can be withdrawn given new evidence
- [[wiki/concepts/deployment-context|Deployment Context]] — RSIS3 runs on Android Termux and Codex web app — dual-environment deployment
- [[wiki/concepts/dual-process-theory|Dual Process Theory]] — Fast intuitive System 1 and slow deliberate System 2 reasoning
- [[wiki/concepts/episodic-memory|Episodic Memory]] — Records of specific events and sessions an agent has experienced
- [[wiki/concepts/executive-function|Executive Function]] — The cognitive control layer that plans, prioritizes, and inhibits actions
- [[wiki/concepts/expert-systems|Expert Systems]] — Classical rule-based systems encoding human expertise in a domain
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — The trade-off between trying new options and using known good ones
- [[wiki/concepts/fitness-stagnation|Fitness Stagnation]] — The plateau signal: generations stop improving, and the meta-tuner responds by raising mutation
- [[wiki/concepts/forward-chaining|Forward Chaining]] — Reasoning from known facts toward a goal by applying rules
- [[wiki/concepts/free-energy-principle|Free Energy Principle]] — A theory that self-organizing systems minimize surprise about their world
- [[wiki/concepts/goal-regression|Goal Regression]] — Planning backward from the goal to the initial state
- [[wiki/concepts/hierarchical-task-network|Hierarchical Task Network]] — Planning by decomposing abstract tasks into concrete subtask networks
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — Self-model with genesis hash, layer scores, crisis detection, and value reinforcement
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — The frozen, read-only judge that gates every proposed change — never in-scope for self-improvement
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — Two nested optimization loops — a fast inner learner and a slow outer updater — the shape of RSIS3's stack
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — The semantic memory tier: typed nodes (improvements, insights, strategies) and edges queried by the loops
- [[wiki/concepts/learning-to-learn|Learning to Learn]] — Meta-learning: improving the learner itself across tasks, so each task gets faster — the goal of the loop stack
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — The formal framework for sequential decisions under uncertainty
- [[wiki/concepts/means-ends-analysis|Means-Ends Analysis]] — Reducing the difference between current state and goal step by step
- [[wiki/concepts/memory-hierarchy|Memory Hierarchy]] — Three tiers with different guarantees — git (truth), knowledge graph (insight), vectors (retrieval)
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — Bounded, registry-driven adjustment of a loop's own parameters by a higher loop — the +3 diagonal in practice
- [[wiki/concepts/metacognition|Metacognition]] — Thinking about and regulating one's own cognitive processes
- [[wiki/concepts/monte-carlo-tree-search|Monte Carlo Tree Search]] — Search that builds a tree by simulating random rollouts and backing up results
- [[wiki/concepts/multi-armed-bandit|Multi-Armed Bandit]] — The problem of choosing among options with unknown rewards
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Comprehensive analysis of the mykb personalized knowledge wiki system, its architecture, extraction pipeline, and strategies for active curation.
- [[wiki/concepts/mykb-implementation-report|mykb Implementation Report: 6-Phase Buildout — Actual State, Architecture, and Results]] — Post-implementation report documenting all 6 phases of the mykb intelligence buildout — architecture decisions, metrics, API surface, and future roadmap.
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Comprehensive research report analyzing personal knowledge database systems, LLM-native wikis, graph-based RAG, and related methodologies — with an implementation blueprint for mykb.
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — RSIS3's original nine nested self-improvement loops — L1–L9 all implemented as bounded, evaluator-gated cycles
- [[wiki/concepts/non-monotonic-logic|Non-Monotonic Logic]] — Logics where adding premises can invalidate earlier conclusions
- [[wiki/concepts/operator-subgoaling|Operator Subgoaling]] — Creating subgoals to satisfy the preconditions of a desired operator
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]] — Sequential decision making when the true state is hidden
- [[wiki/concepts/perception-loop|Perception Loop]] — Feeding raw observations into an agent's state before reasoning and action
- [[wiki/concepts/planning-as-search|Planning as Search]] — Treating planning as a search problem over states and actions
- [[wiki/concepts/policy-gradient|Policy Gradient]] — Learning policies directly by gradient ascent on expected reward
- [[wiki/concepts/population-based-evolution|Population-Based Evolution]] — Elitism, mutation, and recombination over a persistent population of strategy variants — L5's engine
- [[wiki/concepts/probabilistic-programming|Probabilistic Programming]] — Writing programs with random variables and performing inference over them
- [[wiki/concepts/procedural-memory|Procedural Memory]] — Memory of how to do things — skills, routines, and tool usage
- [[wiki/concepts/production-rules|Production Rules]] — Condition-action rules that fire when their conditions match state
- [[wiki/concepts/project-lineage|RSIS3 Project Lineage]] — Full evolutionary history from iterative agent swarm attempts through RRP, rsirrp, rsis, rsirrp2, rsirrpb, rsis2, to rsis3
- [[wiki/concepts/pulse-cycle|Pulse Cycle]] — 9-phase evaluation protocol — the core cognitive loop of RSIS3
- [[wiki/concepts/q-learning|Q-Learning]] — Off-policy TD learning of action values for optimal policies
- [[wiki/concepts/reactive-planning|Reactive Planning]] — Deciding actions from current state without maintaining a plan
- [[wiki/concepts/recursion-guard|Recursion Guard]] — Untuned fixed points: the top three loops tune others but are never tuned themselves, capping self-modification depth
- [[wiki/concepts/satisficing|Satisficing]] — Accepting the first option that meets an aspiration level
- [[wiki/concepts/semantic-memory|Semantic Memory]] — General facts and abstractions, independent of the episode that produced them
- [[wiki/concepts/telemetry|Workspace Telemetry]] — Structured, append-only event records of every loop action — the audit trail that makes self-improvement observable
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — Learning from the difference between successive value estimates
- [[wiki/concepts/triad-architecture|Triad Architecture]] — Three-project architecture: RSIS3 (cognitive engine) + mykb (knowledge OS) + myrsikb (memory bridge)
- [[wiki/concepts/tuning-oscillation|Tuning Oscillation]] — The thrash signal: a tuned loop flips its adjustments back and forth, and the meta-tuner widens the deadband
- [[wiki/concepts/tuning-ownership-diagonal|Tuning Ownership Diagonal]] — The +3 rule: loop k+3 tunes loop k, so every parameter has exactly one writer
- [[wiki/concepts/utility-functions|Utility Functions]] — Numerical objectives agents maximize when choosing actions
- [[wiki/concepts/vector-memory|Vector Memory]] — Dense-embedding retrieval over past improvements — semantic recall for similar-pattern reuse
- [[wiki/concepts/working-memory|Working Memory]] — The small, active set of information an agent holds while reasoning
- [[wiki/concepts/world-models|World Models]] — Internal representations that let agents simulate and predict their environment
