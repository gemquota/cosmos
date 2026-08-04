---
type: "concept"
title: "Calibration Curves"
description: "Plots of predicted probability versus observed frequency"
tags: ["calibration", "visualization", "forecasting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Calibration Curves

## Summary

A calibration curve plots predicted probabilities against observed frequencies, showing how well a forecaster's or model's confidence matches reality. It matters because it turns calibration from an abstract property into a visible shape: points on the diagonal mean perfect calibration. Curves expose both overconfidence and underconfidence and guide where recalibration is needed.

## Details

- **Definition** — Forecasts are binned by predicted probability; each bin's observed event rate is plotted against it, with the diagonal representing perfect calibration.
- **Reading the curve** — Points above the diagonal indicate overconfidence (high predictions, lower observed rates); points below indicate underconfidence.
- **Construction** — Enough predictions per bin are required for stable estimates; binning choices affect how smooth and how honest the curve looks.
- **Worked example** — A model predicts 0.8 confidence in a hundred cases; if only fifty percent actually occur, the 0.8 bin sits well above the diagonal.
- **Complements** — Calibration is only part of quality; a curve can look perfect while forecasts are uselessly uninformative, so resolution matters too.
- **Common failure modes** — Too few samples per bin, plotting reliability on tiny test sets, and treating calibration curves as interchangeable with Brier scores.
- **Practical relevance** — Model confidence displays, forecasting teams, and risk systems use curves to monitor drift and to target recalibration effort.
- **Variants** — Reliability diagrams, quantile-quantile plots for continuous predictions, and reliability-by-bucket tables serve related checks.
- **Limits** — Curves summarize aggregate behavior; individual forecasts can still be miscalibrated in ways the aggregate smooths away.
- **Drift monitoring** — Recomputing curves on rolling windows detects calibration drift after deployment, triggering recalibration before overconfidence compounds.
- **Binning trade-offs** — Few wide bins smooth noise but hide local miscalibration; many narrow bins are noisy without enough data.
- **Worked example** — A risk model's 0.7 bin historically matches observed risk; after a policy change, the curve lifts, and the team recalibrates the model to the new base rate.
- **Reporting** — Publishing the curve with sample counts per bin lets reviewers judge the reliability of the calibration evidence.

## Related

- [[wiki/concepts/calibration|Calibration]] — the underlying property
- [[wiki/concepts/brier-score|Brier Score]] — the scalar summary
- [[wiki/concepts/overconfidence-mitigation|Overconfidence Mitigation]] — fixing the shape
- [[wiki/concepts/superforecasters|Superforecasters]] — the trained benchmark
- [[wiki/concepts/prediction-markets|Prediction Markets]] — market calibration
- [[wiki/concepts/probabilistic-literacy|Probabilistic Literacy]] — reading the plot
