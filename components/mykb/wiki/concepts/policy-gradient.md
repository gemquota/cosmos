---
type: "concept"
title: "Policy Gradient"
description: "Learning policies directly by gradient ascent on expected reward"
tags: ["policy-gradient", "reinforcement-learning", "policy", "rl"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Policy Gradient

## Summary
Policy gradient methods optimize the policy directly: estimate the gradient of expected reward with respect to policy parameters and ascend it. They matter because they handle continuous and stochastic action spaces that value methods struggle with. Modern LLM alignment uses policy-gradient-style optimization.

## Details
- The core idea: parametrize the policy π_θ(a|s) (e.g., a neural network mapping states to action distributions) and estimate ∇θ J(θ), the gradient of expected return with respect to the parameters, then update θ in the gradient direction. The policy-gradient theorem shows the gradient can be estimated as the expected value of the return times the log-gradient of the policy — "increase the probability of actions that led to good returns, decrease those that led to bad ones" — which is the intuitive heart of the method.
- REINFORCE is the simplest estimator; actor-critic reduces variance. REINFORCE collects full trajectories and uses the total return as the weighting signal; it is unbiased but high-variance because the return of an entire trajectory is a noisy estimate of an action's quality. Actor-critic methods split the model: the actor is the policy, the critic learns a value function that estimates expected return from a state, and the critic's estimate (rather than the raw trajectory return) weights the gradient — much lower variance, at the cost of introducing bias from the critic's approximation error.
- Natural gradients and PPO stabilize updates. Plain gradient steps are sensitive to learning rate and parametrization; natural gradients account for how the policy distribution changes, and proximal policy optimization (PPO) clips the update so the new policy cannot drift too far from the old one in one step. These stability mechanisms are why PPO became the default: reliable, sample-reasonable training across many domains.
- The tradeoff versus value methods: policy gradients handle continuous action spaces naturally (they sample from a distribution rather than maximizing over an action set), and they can represent stochastic policies directly, but they are sample-inefficient and sensitive to the reward scale and the baseline. Q-learning inverts the tradeoff — sample-efficient for discrete actions, but weak where the action space is continuous.
- Modern LLM alignment uses policy-gradient-style optimization: RLHF fine-tunes the policy (the language model) against a reward model with PPO, and DPO reformulates the same objective without explicit reward modeling — the reason every alignment pipeline inherits the policy-gradient vocabulary of policies, rewards, and clipped updates.
- Open question: credit assignment across long agent trajectories — the return of a 100-step agent episode is a poor per-action signal, and the field's biggest practical gap.
- RSIS3 relevance: parameter tuning from outcomes is a policy-gradient analogy — each pass is an episode, the metric deltas are rewards, and the loop's parameter updates are gradient-like adjustments toward the configurations that produced good outcomes.

## Related
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — the reward signal can be exploited
- [[wiki/concepts/q-learning|Q-Learning]] — the value-based alternative
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — critic learning
- [[wiki/concepts/utility-functions|Utility Functions]] — what is being maximized
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — the formal setting
