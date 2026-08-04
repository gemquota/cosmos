---
type: "concept"
title: "Prediction Markets"
description: "Markets whose prices aggregate forecasts about future events"
tags: ["forecasting", "markets", "aggregation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Prediction Markets

## Summary

Prediction markets are exchange platforms where participants trade contracts whose payouts depend on future events, so prices reflect aggregated forecasts. They matter because they consistently outperform polls and individual experts at forecasting, converting dispersed information into a single number. Their power comes from incentives: money concentrates attention on accuracy.

## Details

- **Definition** — A contract pays out if an event occurs; its price is interpreted as the market's probability estimate for that event.
- **Information aggregation** — Traders with superior information push prices toward their beliefs, and the mechanism rewards those who are right.
- **Accuracy** — Market prices typically beat surveys and expert panels, especially near resolution, and track benchmark forecasts well.
- **Worked example** — A market on a product launch date trades a contract; as news emerges, informed traders adjust the price, which the team reads as the consensus probability.
- **Common failure modes** — Thin liquidity, manipulation, mis-specified contracts, and regulatory barriers that kill the market or its incentives.
- **Practical relevance** — Internal prediction markets support estimation, risk assessment, and decision review inside organizations.
- **Variants** — Play-money markets, conditional markets, and combinatorial markets extend the basic design at the cost of complexity.
- **Limits** — Prices reflect what is priced and traded; neglected scenarios and event definitions that shift after listing distort the signal.
- **Contract design** — Binary contracts, conditional contracts, and question framing all affect liquidity and interpretation; precise wording is essential.
- **Liquidity** — Thin markets move on few trades and are easily manipulated; subsidies and market makers address early-stage illiquidity.
- **Worked example** — A team runs an internal market on launch date; the price reacts to schedule slips within hours, providing an early warning.
- **Limits** — Markets forecast what traders can price; unknown-unknowns and event definitions that shift after listing escape the mechanism.

## Related

- [[wiki/concepts/superforecasters|Superforecasters]] — individual forecasting skill
- [[wiki/concepts/brier-score|Brier Score]] — scoring the forecasts
- [[wiki/concepts/calibration-curves|Calibration Curves]] — checking probability accuracy
- [[wiki/concepts/probabilistic-literacy|Probabilistic Literacy]] — reading the numbers
- [[wiki/concepts/statistical-reasoning|Statistical Reasoning]] — updating on evidence
- [[wiki/concepts/ambiguity-aversion|Ambiguity Aversion]] — pricing uncertainty
