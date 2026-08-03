# Adversarial Review — Pass 2 (Post-Cleanup), Slice 2

**Reviewer:** adversarial-reviewer-2 (PASS 2)
**Date:** 2026-08-03
**Slice:** `/data/data/com.termux/files/home/.cache/mykb-review/slice2.txt` — 220 paths, 219 existing files (1 intentionally renamed; see below)
**Scope:** cloud-infra (20), communities (1), compositions (3), concepts (~110), data-storage (~55), decisions (12), dev-tools (~40)
**Method:** automated invariant checker + 60+ deep-reads + 12 link-target spot-checks + targeted pattern scans (annotation strings, trailing orphan bullets, duplicated bullets, duplicate Related links, mislabeled links, near-duplicate shingle scan, threshold-hugging analysis).

## Verdict

**64 / 100**

The hard invariants hold and the Pass 1 fixes **mostly landed in this slice, but with new cleanup-induced regressions**. Verified held: 0 self-links, 0 annotation strings ("related coverage in the same cluster" / "the full treatment of this theme" / "existing graph context" / "— note" / "— see also"), 0 unclosed `[[raw/archive/…]]` links, 0 `sources|syntheses/README` links, 0 files under 320 body words (min exactly 320), 0 empty `## Related` sections, 0 broken wikilinks/markdown links, and the one factual fix in this slice (`concepts/calibration.md` reliability-diagram direction) is correct; the out-of-slice factual fixes (contrast-ratios, dom-clobbering, gpu-drivers-and-cuda, dp-vs-px, anr-diagnostics) also verify as correct. The `clickhouse-vs-druid-pinot-druid-architecture.md` rename landed with all 3 referrers retargeted.

However, the cleanup left the slice in a visibly unfinished state: **60 of 219 files (27.4%) contain orphaned trailing bullets after the "RSIS3 relevance" paragraph and before `## Related`**, with no header; at least 3 files contain a duplicated "Operational notes" bullet inside one file; 1 missed duplicate `Related` link; and 1 wrong-page link (`[[wiki/compositions/lease-based-locks|Fencing Tokens]]`). The deliberately-unfixed Pass 1 classes remain pervasive: 86% of files end with a templated "RSIS3 relevance" paragraph, 48 files assert unverifiable "the wiki's / the bundle's X does Y" infrastructure claims, and files cluster at the 320-word floor (4 files at exactly 320). No fabrication, no broken links, and no semantic errors were confirmed in 60+ deep reads — the content, where it is content, is accurate. The score reflects that the floor held but the bar (real, distinct, verifiable prose per file) is only partially met.

## Critical findings

1. **Orphaned trailing bullets after the "RSIS3 relevance" paragraph — 60/219 files (27.4%)** (cleanup regression / padding evidence).
   Content after the RSIS3 paragraph, before `## Related`, with no header. Examples (all paths relative to `components/mykb/wiki/`):
   - `decisions/content-policy-ai.md` (exactly 320 words):
     > - RSIS3 relevance: the wiki's curation rules are a content policy for knowledge …
     > - Include concrete examples per category so both classifiers and human reviewers interpret the rules consistently.
     > - Measure enforcement against the policy with a labeled test set so rule changes show up as measurable behavior shifts.
   - `cloud-infra/security-group-best-practices.md`:
     > - Review cadence: run an exposure scan on a schedule and treat any new 0.0.0.0/0 rule on a management port as a review event …
     > - Naming: name groups by role and environment (web-prod, db-prod) …
   - `compositions/fencing-tokens.md`: "- Token hygiene: …" and "- Lease interplay: …"; `compositions/lamport-clocks.md`: "- Counter persistence: …" and "- Choice guidance: …"; `compositions/query-plans.md`: "- Plan reviews: …" and "- Workload realism: …"; `cloud-infra/warm-storage.md`: "- Data temperature model: …" and "- Cost reporting: …"; `data-storage/simhash.md`, `data-storage/locality-sensitive-hashing.md`, `data-storage/topic-modeling.md`, `data-storage/latent-semantic-analysis.md`, `data-storage/postgres-tsvector.md`, `data-storage/lucene.md`, `dev-tools/fixed-window.md`, `dev-tools/leaky-bucket.md`, `dev-tools/fail-safe.md`, `decisions/copyright-and-ai.md`, `decisions/data-license-issues.md` (3 bullets), etc. (full list in the audit methodology: 60 files).
   Why wrong: these are orphaned bullets — either a stripped header left them stranded or a top-up editor appended them after the RSIS3 paragraph to reach 320 words. They break the article skeleton (`Details` → `RSIS3 relevance` → `Related`) that every other file follows, and several duplicate advice already present in the same file (see finding 2). They are precisely the "orphaned bullets where a header was removed / awkward joins after annotation stripping" regression class Pass 2 was asked to check for. Fix: merge into an "Operational notes"/"Practice" section or delete; do not just renumber.

2. **Duplicated bullets inside a single file — confirmed in ≥3 files**.
   - `dev-tools/baggage-propagation.md` (line 20 and line 23, both bullets start "Operational notes:"):
     > - Operational notes: document the baggage schema, cap size and count, and sanitize values at the edge.
     > - Operational notes: document the baggage schema, cap its size, and treat baggage values as untrusted strings at every hop — never use them for access decisions.
   - `dev-tools/apm-tools.md` (line 20 and line 23, both "Operational notes:" bullets — "set sampling policies…" vs "sample aggressively…").
   - `dev-tools/breakpoint-debugging.md` (line 20 and line 23, both "Operational notes:" bullets).
   Why wrong: same section name twice in one file; the trailing copy sits in the orphaned zone of finding 1. The Pass 1 cleanup claimed "deduped 22 repeated bullets" — this slice shows the dedupe was incomplete.

3. **Wrong-page link: `compositions/fencing-tokens.md`**.
   > - [[wiki/compositions/lease-based-locks|Fencing Tokens]]
   The display label is "Fencing Tokens" but the target is `compositions/lease-based-locks.md` ("Lease-Based Locks"). Clicking "Fencing Tokens" lands on the lease article. This looks like a self-link that was retargeted to a sibling during cleanup without updating the label. It is the one confirmed label/target mismatch in the slice (verified by scanning all ~1,300 wikilinks for label-vs-basename mismatch; every other flagged candidate is a benign styling variant like "TF-IDF", "Q-Learning", "SIEM").

## Major findings

4. **Unverifiable "the wiki's / the bundle's X does Y" claims — 48 files** (deliberately unfixed in Pass 1; re-measured and still pervasive).
   - 32 files have "RSIS3 relevance: the wiki's …" infrastructure claims, e.g. `cloud-infra/spot-instances.md` ("the wiki's batch layer runs spot-first with checkpointing"), `cloud-infra/tcp-retransmission.md` ("the wiki's cross-region sync logs retransmit rates per link"), `cloud-infra/split-horizon-dns.md` ("the wiki's VPC uses private hosted zones with split views"), `compositions/fencing-tokens.md` ("wiki publish writes carry fencing tokens from the sync lease service"), `compositions/lamport-clocks.md` ("the wiki's sync layer linearizes event order with Lamport timestamps").
   - 16 files in `decisions/` use "RSIS3 relevance: the bundle's …", e.g. `decisions/patent-issues-ai.md` ("the bundle's novel scripts and methods have patent-adjacent disclosure choices"), `decisions/usage-policies-ai.md` ("the bundle's worker briefs are usage policies for its agents").
   - 32 files make "mykb …" claims, e.g. `data-storage/faiss.md` ("a local FAISS index over mykb embeddings"), `data-storage/named-entity-recognition.md` ("mykb's entity extraction from sessions is NER plus resolution; the results populate the entities directory").
   Why wrong: each is an assertion of fact about the wiki's or bundle's real infrastructure (tunnels, spot fleets, sync leases, entity pipelines) that cannot be verified from the wiki and, in several cases, contradicts observable reality (the wiki is an Obsidian markdown store — "publish writes carry fencing tokens" and "cross-region sync logs" have no supporting evidence anywhere in the corpus). These are not flagged as confirmed fabrication, but as unverifiable confident claims presented as fact — the exact class Pass 2 was asked to keep hunting. Fix: either attach evidence (link the pipeline/state file) or rewrite as conditional ("a sync layer *should* use …").

5. **Template uniformity and threshold-hugging padding**.
   - 188/219 files (86%) end with an "RSIS3 relevance" paragraph; 79 files share the full 7-part template (Summary → Details[Mechanism, Concrete example, Failure modes, Tradeoffs, Operational notes] → RSIS3 relevance → Related). The paragraph adds genuine value in good concept files (`concepts/active-inference.md`, `concepts/overfitting-llm.md`) and zero value in many infra files where it is the same claim restated ("the wiki's X does Y").
   - Word counts cluster at the floor: exactly 320 in `data-storage/sqlite-fts5.md`, `data-storage/time-travel-queries.md`, `decisions/content-policy-ai.md`, `dev-tools/correlation-ids.md`; 321 in `compositions/query-plans.md`, `data-storage/ivf.md`, `data-storage/simhash.md`, `dev-tools/latency-percentiles.md`; 322 in another 5. Four files at exactly 320 is statistically implausible for organic prose and matches the Pass 1 note that 62 files were "topped up" to the floor. In `content-policy-ai.md`, the two orphaned bullets of finding 1 are visibly the top-up. This is the "padding-to-threshold" defect class, re-measured.

6. **Near-duplicate structural clones — ~7 families, no verbatim duplication**.
   A 5-gram shingle-Jaccard scan across all 219 files found no pair above 0.30 (no copy-paste), but these families re-cover the same ground with the same template and cross-link each other:
   - DLQ family: `dead-letter-queues-and-retries.md`, `dead-letter-topics-and-dlq.md` (near-identical Summary/Mechanism/Failure-modes; both end "RSIS3's ingestion pipeline … quarantine"), plus `dead-letter-queues.md` and `dead-letter-data-and-repair-pipelines.md` (both linked from each of them).
   - Vector-search family: `faiss.md`, `ivf.md`, `hnsw.md`, `milvus.md`, `pinecone.md`, `product-quantization.md` — the first three each contain the same "the alternative, vector database …" tradeoff sentence shape.
   - Similarity-metric family: `cosine-similarity.md`, `dot-product.md`, `euclidean-distance.md` (each "normalize at write and query" advice repeated).
   - FTS family: `sqlite-fts5.md`, `postgres-tsvector.md`, `lucene.md`, `elasticsearch.md` (each: "the mature pattern is X for embedded, Y for scale").
   - LSH family: `minhash.md`, `simhash.md`, `locality-sensitive-hashing.md` ("keep exact verification mandatory" appears in all three).
   - Reward-model trio: `reward-model-error.md`, `reward-model-issues.md`, `reward-model-overfitting.md` (all in slice, all "reward model" ground).
   - Ethics family: `moral-agency/patiency/status-questions/uncertainty/weights`, `personhood-questions.md`, `rights-for-ai.md` (mutually cross-linked, overlapping criteria lists).
   Not a hard defect per file, but a redundancy tax: a reader of the DLQ family reads the same 350 words four times with different vendor nouns.

7. **Duplicate `Related` link: `decisions/data-license-issues.md`**.
   > - [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]]
   > - [[wiki/decisions/model-license-risks|Model License Risks]] — the model side
   > - [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — the wiki practice
   The same target+label appears twice in one Related block (a missed dedupe; Pass 1 claimed 22 deduped bullets).

## Minor & nits

- **Stale display labels after the ClickHouse rename** (fix landed but labels not refreshed): `data-storage/pinot-real-time-analytics.md` and `data-storage/clickhouse-and-columnar-oltp.md` both link `[[wiki/data-storage/clickhouse-vs-druid-vs-pinot|Clickhouse Vs Druid Pinot Druid Architecture]]` — target is the new file, label still the old slug-title.
- The slice file itself lists the pre-rename slug `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`; the checker's "MISSING FILE" flag is a false positive against an intentional rename (documented in `syntheses/adversarial-review-pass-1-2026-08.md`).
- Remaining 3 checker flags verified as false positives: `cloud-infra/split-horizon-dns.md` "example.com" (RFC 2606 reserved domain, legitimate DNS example), `concepts/stub-criteria.md` "placeholder" (prose defining the stub concept), `data-storage/postgres-tsvector.md` "insert and query" (technical phrase "analyzer mismatches between insert and query").
- `compositions/fencing-tokens.md`, `lamport-clocks.md`, `query-plans.md` (and all 3 compositions files) have no blank line between the frontmatter close (`---`) and the `# Title` — cosmetic but inconsistent with the rest of the slice.
- `data-storage/time-travel-queries.md` has a stray blank line before `## Related`.
- `cloud-infra/tls-1-3-session-resumption.md` links to both `wiki/cloud-infra/https-and-tls` and `wiki/os-shell/tls-and-https` — two links to near-same-topic targets in one Related block.
- `concepts/lottery-ticket-hypothesis.md` has a bare `[[wiki/concepts/sae-research|sae-research]]` link with no descriptor, while every sibling link carries a "—" annotation.
- Inconsistent RSIS3 line forms across the slice: "RSIS3 relevance:", "RSIS3/mykb relevance:", "mykb relevance:" — same template, three spellings.
- `concepts/named-entity-recognition.md`'s "entities directory" claim is at least consistent with the wiki (an `entities/` directory exists), so it is plausible; still unverified that "mykb's entity extraction from sessions" populates it.
- `dev-tools/four-golden-signals.md` "the golden signals map to article latency, read traffic, curation errors, and storage saturation" — a hypothetical mapping stated as fact; borderline instance of finding 4.

## Sample audit table

Word counts = body words, frontmatter excluded. Verdicts: OK = accurate, well-formed; WEAK = structural/regression defect; PASS = checked clean; FAIL = confirmed defect.

| File (relative to components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| cloud-infra/security-group-best-practices.md | 329 | WEAK | 2 orphaned trailing bullets after RSIS3 paragraph; content otherwise accurate |
| cloud-infra/service-discovery-dns-based.md | 322 | WEAK | 1 orphaned trailing bullet; "the wiki's services resolve through an internal DNS" unverifiable |
| cloud-infra/site-to-site-vpn.md | 337 | WEAK | 1 orphaned trailing bullet; "the wiki's hybrid connectivity uses dual tunnels with BGP" unverifiable |
| cloud-infra/split-horizon-dns.md | 328 | OK | checker "example.com" flag is a false positive (RFC 2606); orphaned trailing bullet "Synchronization:" |
| cloud-infra/spot-instances.md | 339 | WEAK | "the wiki's batch layer runs spot-first with checkpointing" — unverifiable; 2 orphaned trailing bullets |
| cloud-infra/tcp-retransmission.md | 332 | WEAK | technically sound (RTO, fast retransmit, SACK, DSACK); 2 orphaned trailing bullets; unverifiable cross-region sync claim |
| cloud-infra/tls-1-3-session-resumption.md | 334 | OK | accurate (0-RTT, tickets, anti-replay); duplicate topical TLS links in Related |
| cloud-infra/warm-storage.md | 341 | WEAK | 2 orphaned trailing bullets; IA/Glacier claims plausible |
| communities/hotfix-branches.md | 540 | OK | best file in slice: substantive, distinct, well-structured; dual-merge logic correct |
| compositions/fencing-tokens.md | 350 | FAIL | wrong-page link `[[wiki/compositions/lease-based-locks\|Fencing Tokens]]`; 2 orphaned bullets; unverifiable "publish writes carry fencing tokens" |
| compositions/lamport-clocks.md | 327 | WEAK | correct (counter ticks, max+1); 2 orphaned bullets; unverifiable sync-layer claim |
| compositions/query-plans.md | 321 | WEAK | correct EXPLAIN/plan mechanics; 2 orphaned bullets; exactly-321 threshold-hugging |
| concepts/active-inference.md | 403 | OK | accurate FEP/active-inference account; interpretive RSIS3 line acceptable |
| concepts/calibration.md | 414 | PASS | factual fix verified: reliability diagram direction correct (above diagonal = underconfident) |
| concepts/induction-heads.md | 433 | OK | accurate; Olsson et al. paper correctly attributed |
| concepts/lottery-ticket-hypothesis.md | 446 | OK | accurate; Frankle & Carbin correctly described; bare sae-research link (nit) |
| concepts/moral-status-questions.md | 456 | OK | fair survey; "AI systems raise novel status questions" appropriately hedged |
| concepts/overfitting-llm.md | 457 | OK | accurate; contamination/memorization framing correct; meta RSIS3 line is apt |
| concepts/polysemanticity.md | 422 | OK | accurate superposition/dictionary-learning account |
| concepts/sandbagging.md | 459 | OK | accurate; incentive-invariance detection correctly described |
| concepts/spec-gaming-examples.md | 435 | OK | canonical DeepMind catalogue correctly cited; examples accurate |
| concepts/utilitarian-calculus.md | 446 | OK | Bentham/Mill correct; interpersonal-comparison objection correctly stated |
| data-storage/cosine-similarity.md | 347 | WEAK | mathematically correct; "wiki retrieval by cosine … is the core of semantic search in mykb" unverifiable; template clone of dot-product/euclidean |
| data-storage/dead-letter-queues-and-retries.md | 377 | WEAK | correct DLQ mechanics; near-clone of dead-letter-topics-and-dlq.md (same failure modes/tradeoffs, both "RSIS3's ingestion pipeline … quarantine") |
| data-storage/dead-letter-topics-and-dlq.md | 351 | WEAK | correct Kafka DLQ details; near-clone of sibling; "a Kafka consumer of wiki events" is a wiki claim |
| data-storage/faiss.md | 366 | WEAK | correct library facts; "a local FAISS index over mykb embeddings … the right scale for the wiki today" unverifiable |
| data-storage/ivf.md | 321 | WEAK | nlist/nprobe math plausible (8/4096 cells ≈ 2k scans); template clone; threshold-hugging |
| data-storage/hnsw.md | 332 | WEAK | M/efSearch ranges plausible; template clone of faiss/ivf |
| data-storage/latent-semantic-analysis.md | 335 | WEAK | correct SVD/TF-IDF account; orphaned trailing bullet duplicates "weight with TF-IDF" |
| data-storage/locality-sensitive-hashing.md | 332 | WEAK | correct LSH families; orphaned trailing bullet duplicates "keep exact verification" |
| data-storage/named-entity-recognition.md | 365 | OK | correct NER approaches; "entities directory" claim plausible (dir exists) but unverified |
| data-storage/postgres-tsvector.md | 336 | WEAK | correct tsvector/tsquery; checker "insert and query" flag is a false positive; orphaned trailing bullet duplicates generated-column advice |
| data-storage/simhash.md | 321 | WEAK | correct SimHash mechanism; orphaned trailing bullet; threshold-hugging |
| data-storage/sqlite-fts5.md | 320 | WEAK | correct FTS5 facts; "mykb's data layer favors SQLite" claimed twice; exactly 320 words |
| data-storage/time-travel-queries.md | 320 | OK | correct Delta/Iceberg/Snowflake snapshot claims; exactly 320; stray blank line nit |
| data-storage/topic-modeling.md | 331 | WEAK | correct LDA/LSA/BERTopic; orphaned trailing bullet |
| decisions/api-access-policies.md | 332 | WEAK | sensible policy taxonomy; orphaned trailing bullet; "the wiki daemon and dashboard should document … access tiers" speculative |
| decisions/content-policy-ai.md | 320 | FAIL | 2 orphaned trailing bullets (visible top-up to exactly 320); "the wiki's curation rules are a content policy" unverifiable |
| decisions/copyright-and-ai.md | 328 | WEAK | accurate fair-use framing; 2 orphaned trailing bullets, first duplicates "keep provenance records" |
| decisions/data-license-issues.md | 328 | FAIL | 3 orphaned trailing bullets; duplicate `evidence-and-provenance` Related link |
| decisions/test-set-discipline.md | 331 | OK | accurate holdout/contamination discipline |
| dev-tools/apm-tools.md | 336 | FAIL | duplicated "Operational notes:" bullet (lines 20 & 23) |
| dev-tools/baggage-propagation.md | 337 | FAIL | duplicated "Operational notes:" bullet (lines 20 & 23) |
| dev-tools/breakpoint-debugging.md | 339 | FAIL | duplicated "Operational notes:" bullet (lines 20 & 23) |
| dev-tools/burn-rate-alerts.md | 336 | OK | 14.4x/1h and 1x/24h window math matches SRE workbook conventions |
| dev-tools/correlation-ids.md | 320 | OK | accurate; exactly 320 words |
| dev-tools/fail-fast.md | 339 | OK | accurate; boundary-validation framing correct |
| dev-tools/fail-safe.md | 335 | WEAK | accurate deny-by-default; orphaned trailing bullet |
| dev-tools/fixed-window.md | 324 | WEAK | correct 2x boundary-burst analysis; orphaned trailing bullet |
| dev-tools/four-golden-signals.md | 322 | OK | accurate SRE signals; "map to article latency …" is a hypothetical stated as fact |
| dev-tools/leaky-bucket.md | 329 | WEAK | correct; orphaned trailing bullet "Apply it where downstream capacity is genuinely fixed …" |

## Recommendations (top 5)

1. **Repair the 60 orphaned trailing bullets.** Mechanical, high-impact: move each trailing block into the file's existing structure (append to a proper "Operational notes" section or fold into Related-free prose) or delete it. This is the single largest quality defect in the slice and is directly attributable to the cleanup/top-up pass. Include a checker rule that no bullet may exist between the last "RSIS3 relevance" line and `## Related`.
2. **Add an intra-file duplication check to the cleanup tooling.** Pass 1 deduped 22 bullets but missed the three duplicated "Operational notes" bullets (apm-tools, breakpoint-debugging, baggage-propagation) and the duplicated `evidence-and-provenance` Related link in `decisions/data-license-issues.md`. A per-file duplicate-line detector (normalized) would have caught all four.
3. **Retire the "the wiki's / the bundle's X does Y" claim template in 48 files.** Either attach a resolvable link to the claimed artifact (pipeline, lease service, sync layer) or rewrite as a recommendation ("a sync layer *should* linearize with Lamport timestamps"). As written, these read as facts about infrastructure the wiki does not document anywhere else — the highest-risk fabrication-adjacent class remaining.
4. **Fix and audit link labels.** Correct `compositions/fencing-tokens.md` (`[[wiki/compositions/lease-based-locks|Fencing Tokens]]` → label "Lease-Based Locks" or target `fencing-tokens`), refresh the two stale "Clickhouse Vs Druid Pinot Druid Architecture" display labels, and add a label-vs-target consistency check (label contains none of the target's basename words → flag for review).
5. **Stop threshold-hugging and shrink the clone families.** Raise the effective floor by requiring ≥2 sections beyond the template (or a verifiable citation) for `growing`, so a file at exactly 320 words cannot pass on template padding alone; and consolidate the DLQ, similarity-metric, FTS, vector-search, and LSH families by cross-linking one canonical treatment per family instead of four parallel articles with identical skeletons.

**Pass 1 fix verification (explicit):** self-links (0), annotation strings (0), unclosed `[[raw/archive/…]]` links (0), `sources|syntheses/README` links (0), sub-320 files (0), empty Related sections (0) — **held in this slice**. The `calibration.md` factual fix is correct and the ClickHouse rename landed with referrers retargeted. What did **not** hold cleanly is the claim that the cleanup left no structural residue: 60 orphaned trailing bullets, 3 duplicated in-file bullets, 1 duplicate Related link, and 1 wrong-page link are all cleanup-adjacent regressions present after the pass.
