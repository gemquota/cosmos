---
type: "concept"
title: "Forward Models"
description: "Internal models that predict the next state from current state and action"
tags: ["models", "prediction", "motor-control"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Forward Models

## Summary

Forward models are internal models that predict the next state of a system — often the body or environment — from the current state and an action. They matter because prediction lets agents compensate for delays, anticipate consequences, and learn from prediction error. Forward models are central to motor control, active perception, and predictive processing accounts of the brain.

## Details

- **Definition** — A forward model computes an expected next state and sensory outcome given the current state and a candidate action.
- **Motor control** — The brain uses forward predictions to compensate for transmission delays, so movements feel immediate despite slow feedback loops.
- **Learning** — Prediction error — the difference between expected and actual outcome — drives adaptation of both the model and the controller.
- **Worked example** — Reaching for a cup, the motor system predicts where the hand will be and corrects mid-flight; the prediction, not the delayed sensation, steers the movement.
- **Common failure modes** — Stale models that predict old dynamics, overconfident predictions that ignore noise, and error signals that are too weak to update.
- **Practical relevance** — Robotics, agent simulation, and adaptive control systems build explicit forward models for the same reasons.
- **Variants** — Inverse models map desired outcomes to actions; paired forward-inverse architectures support both prediction and control.
- **Limits** — Forward models approximate the real system; their validity degrades outside the states and actions they were trained on.
- **Sensory attenuation** — Predicted self-generated sensations are attenuated, explaining why tickling yourself feels weaker than being tickled.
- **Prediction and agency** — Matching predictions to outcomes supports the sense of agency: you experience actions you predicted as your own.
- **Worked example** — A robot arm learns a forward model of its payload; the model predicts trajectories, and corrections use the prediction error to adapt to load changes.
- **Computational role** — Forward models also support planning by simulating candidate actions without executing them.

## Related

- [[wiki/concepts/active-inference|Active Inference]] — prediction-driven action
- [[wiki/concepts/predictive-processing|Predictive Processing]] — the general account
- [[wiki/concepts/bayesian-brain|Bayesian Brain]] — probabilistic prediction
- [[wiki/concepts/event-segmentation|Event Segmentation]] — boundaries from error
- [[wiki/concepts/episodic-memory|Episodic Memory]] — storing predicted outcomes
- [[wiki/concepts/working-memory|Working Memory]] — holding state online
