---
type: "concept"
title: "Data Poisoning in Practice"
description: "Attacks that corrupt training data to steer models"
tags: ["poisoning", "attacks", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Poisoning in Practice

## Summary
Data poisoning injects crafted examples into training data so the model learns attacker-chosen behavior.

## Details
- Data poisoning injects crafted examples into training data so the model learns attacker-chosen behavior.
- Backdoors are the targeted form; general poisoning degrades quality.
- Defenses: data provenance, filtering, robust aggregation, and audits.
- RSIS3 relevance: unvetted sources in the wiki would be a poisoning vector for its embeddings.

- Attack surface: training data, retrieval corpora, and feedback signals are all injection points; for a retrieval-based system the corpus is the direct vector, so curation and provenance are the defense.
- Defense layers: provenance tracking, filtering of unvetted sources, robust aggregation, and audits — each layer raises the cost of a successful injection even when no single layer is perfect.
- Detection: backdoors are hard to detect after the fact; the standing practice is to keep a clean holdout of vetted sources and test for anomalous behavior on it after each acquisition pass.
- Corpus policy: seeds and captures would enter the wiki's corpus through a review gate rather than directly, so the embedding store would only ever be built from vetted material.
- Poisoning versus noise: noise degrades quality evenly, while poisoning steers behavior in a chosen direction, which is why targeted defenses matter more than sheer data volume.
- Traceability: provenance metadata should be recorded per page so a poisoning incident can be traced to its entry point and the affected embeddings rebuilt.
- Robust aggregation: retrieval and ranking should tolerate a small fraction of bad examples — for example, majority-based link suggestions or score clipping — so one injected page cannot dominate results.
- Audit cadence: provenance and filtering rules should be re-checked on the same cadence as other corpus hygiene, because the attack surface changes as new sources are added.
## Related
- [[wiki/concepts/backdoor-attacks-llm|Backdoor Attacks on LLMs]] — the targeted form
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the delivery path
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — the defense
- [[wiki/concepts/red-teaming-ai|Red Teaming AI]] — the detection
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]] — the full treatment of this theme
