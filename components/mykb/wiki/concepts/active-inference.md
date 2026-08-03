---
type: "concept"
title: "Active Inference"
description: "Perception and action unified as minimizing expected free energy"
tags: ["active-inference", "perception", "action", "bayesian"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Active Inference

## Summary
Active inference treats perception and action as two sides of one process: agents minimize variational free energy by updating beliefs (perception) and by choosing actions that fulfill prior expectations (action). It matters because it offers a unified, principled account of goal-directed behavior. It connects neuroscience, Bayesian inference, and control.

## Details
- The agent maintains a generative model of how hidden states produce observations. Perception is approximate Bayesian inference: after each observation, the agent updates its posterior over hidden states, and the mismatch between predicted and actual sensory input — the prediction error — is the quantity that drives both learning and action.
- Action is selected by evaluating the expected free energy of candidate policies. Expected free energy balances two terms: pragmatic value (does the policy lead to preferred outcomes?) and epistemic value (does it resolve uncertainty?). That decomposition gives a principled account of curiosity: an agent will seek out observations that reduce uncertainty even when they have no immediate utility, which resolves the classic exploration-exploitation dilemma without a separate exploration bonus.
- Preferences are priors over outcomes, encoded in the generative model rather than in an external reward function. This reframing is philosophically significant: goals are not utilities to be maximized but expectations to be realized, and behavior emerges from the imperative to make the world conform to the model.
- Practical implementations approximate the full scheme with Monte Carlo rollouts, variational message passing, or deep-learning parametrizations of the generative model. The main operational tradeoff is fidelity versus tractability: richer generative models capture more real-world structure but make the free-energy minimization expensive, so deployed agents typically bound the planning horizon and prune policy sets.
- Failure modes include overconfident priors that suppress learning (the agent persists in wrong beliefs because it acts to confirm them), misspecified generative models that mistake proxies for true preferences, and computational blowup when the policy space grows combinatorially.
- RSIS3 relevance: self-improvement loops can be read as active inference. The system holds a prior over what a good improvement looks like, performs epistemic actions (experiments, retrievals) to reduce uncertainty, and updates its synthesis beliefs when evidence contradicts its predictions.

## Related
- [[wiki/agent-systems/planning-systems|Planning Systems]] — planning as expected-outcome selection
- [[wiki/concepts/free-energy-principle|Free Energy Principle]] — the theoretical umbrella
- [[wiki/concepts/belief-states|Belief States]] — what perception updates
- [[wiki/concepts/world-models|World Models]] — the generative model it assumes
- [[wiki/concepts/partially-observable-mdp|Partially Observable MDP]] — the formal cousin
