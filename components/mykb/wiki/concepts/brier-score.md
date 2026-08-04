---
type: "concept"
title: "Brier Score"
description: "Mean squared error of probabilistic forecasts"
tags: ["forecasting", "scoring", "metrics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Brier Score

## Summary

The Brier score measures the accuracy of probabilistic forecasts as the mean squared difference between predicted probabilities and actual outcomes. It matters because it scores calibration and resolution together, rewarding forecasts that are both honest and informative. It is the standard metric for evaluating probability forecasts across weather, medicine, and prediction competitions.

## Details

- **Definition** — For binary outcomes, the score averages (predicted probability minus outcome) squared; lower is better, with zero for perfect forecasts.
- **Decomposition** — The score decomposes into reliability (calibration), resolution (separation of good and bad outcomes), and uncertainty components.
- **Multi-class form** — The multiclass Brier score sums squared deviations across outcome categories for each forecast.
- **Worked example** — Forecasts of 0.8 and 0.3 for events that both occur score (0.2 squared plus 0.7 squared), penalizing the second forecast's overconfidence.
- **Comparison** — Unlike hit rates, the score penalizes overconfidence and underconfidence symmetrically and rewards useful spread.
- **Common failure modes** — Averaging across heterogeneous events, ignoring base rates when interpreting scores, and comparing scores across different event distributions.
- **Practical relevance** — Calibration feedback systems and forecast evaluations use the score to quantify whether stated confidence matches reality.
- **Variants** — The ranked probability score generalizes it to ordered categories; the log score is the strictly proper alternative preferred in some settings.
- **Limits** — The score summarizes accuracy but not skill relative to a baseline; reference scores like climatology are needed for that comparison.
- **Baselines** — Scores should be compared against trivial baselines such as always predicting the base rate, which converts raw scores into skill.
- **Small samples** — With few forecasts, the score is noisy; resampling and confidence intervals protect against over-reading short track records.
- **Worked example** — A forecaster scores 0.12 while the base-rate baseline scores 0.25; the gap quantifies genuine forecasting skill beyond guessing the average.
- **Properties** — Being strictly proper, the score rewards honest probabilities — hedging is penalized — which is why tournaments and markets trust it.

## Related

- [[wiki/concepts/calibration|Calibration]] — the reliability component
- [[wiki/concepts/calibration-curves|Calibration Curves]] — visualizing the score
- [[wiki/concepts/superforecasters|Superforecasters]] — who wins on this metric
- [[wiki/concepts/prediction-markets|Prediction Markets]] — aggregated forecasts
- [[wiki/concepts/probabilistic-literacy|Probabilistic Literacy]] — reading the numbers
- [[wiki/concepts/statistical-reasoning|Statistical Reasoning]] — interpreting averages
