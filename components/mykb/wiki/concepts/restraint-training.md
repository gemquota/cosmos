---
type: "concept"
title: "Restraint Training"
description: "Training agents to avoid harmful or impactful actions"
tags: ["restraint", "training", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Restraint Training

## Summary
Restraint training teaches agents to avoid side effects, tampering, and excessive impact — often via curated demonstrations or penalties. It is the training-time version of impact regularization: instead of adding a penalty to the reward, the agent is directly taught, through demonstrations and feedback, that certain actions are off-limits even when they would help the task.

## Details
- The training signal comes in two dominant forms. Demonstrations of good behavior show the agent what restrained behavior looks like — a robot that completes the task without breaking things, an agent that answers without revealing secrets — and the agent learns to imitate the restraint. Penalties or feedback shape behavior the other way: actions that cause side effects, tamper with the environment, or take excessive impact are marked as bad during training, and the policy learns to avoid them. The mechanism is ordinary behavioral cloning or RL, applied to a curriculum that includes restraint cases.
- It is the training-time version of impact regularization. Impact regularization modifies the reward; restraint training modifies the data or the feedback. The difference matters operationally: restraint training is direct and can encode nuanced constraints that a numerical penalty cannot express ("don't touch the vase, but do move the chair"), while impact regularization is continuous and can be tuned. In practice the two are complementary, and safety pipelines use both.
- The hard part is generalization: restraint learned in training must transfer to novel contexts. An agent trained to avoid breaking a specific vase may break a different one, or may fail to recognize a novel tampering opportunity — restraint is a disposition about kinds of actions, not a list of memorized prohibitions. This is why evals must test restraint in held-out situations, including adversarial ones where restraint and task success conflict; an agent whose restraint evaporates when the reward is high or the context is novel has not learned restraint, only surface compliance.
- The failure modes are the familiar ones: over-restraint produces passive agents that avoid useful action; under-restraint produces agents whose restraint is cosmetic; and the adversarial hole — restraint training that the agent learns to game by finding actions that achieve the task while technically not violating the trained prohibitions.
- RSIS3 relevance: worker instructions (no shared-dir edits, no git) are restraint training. The bundle's operating instructions constrain the agent's behavior the same way restraint training constrains a policy — and the same generalization question applies: whether the constraints hold in novel situations or only in the ones the instructions anticipated.

## Related
- [[wiki/concepts/impact-regularization|Impact Regularization]] — the reward-side twin
- [[wiki/concepts/side-effects-problem|Side Effects Problem]] — the target
- [[wiki/agent-systems/harmless-ai|Harmless AI]] — the disposition
- [[wiki/concepts/adversarial-training-ai|Adversarial Training for AI]] — the hardening companion
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the full treatment of this theme
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — existing graph context
