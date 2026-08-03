# Adversarial Review #2 — MyKB Stub Promotion Wave (slice 2)

Reviewer: adversarial reviewer #2 (slice: 220 files)
Date: 2026-08-03
Method: `check_slice.py` on all 220 files; full or near-full deep-read of 44 files across
cloud-infra, concepts, data-storage, dev-tools, communities, compositions, decisions;
28 link targets spot-checked (all exist, all topically related).

## Verdict

**Score: 57 / 100**

The wave passes every mechanical invariant it was measured on: 212/220 files clean per the
checker, zero missing files, zero wrong statuses, zero body-word deficits, zero missing
frontmatter keys, zero broken wikilinks or markdown links (per the checker's resolution
rules and my own spot-checks). But the mechanical bar was the *only* bar that held, and it
was set low. The five self-links are real invariant violations and two of them carry
nonsensical labels. More damaging: the promotion wave's own stated standard — "two or more
curl-verified sources" (`concepts/promotion-checklist.md`) — is met by essentially none of
the slice: 218/220 files contain not a single URL or citation, so the many specific numeric
and infrastructure claims cannot be checked and were evidently written without provenance.
Systemic wave artifacts dominate: 93 files (42%) carry machine-generated Related-block
annotations ("the full treatment of this theme", "existing graph context") that add noise
and inflate link counts; 59 files (27%) have trailing "practice" bullets bolted on after
the RSIS3 relevance bullet (37 of them orphaned by a blank line); 76 files (35%) sit within
20 words of the 320-word floor (minimum exactly 320, median 389.5), consistent with
padding-to-threshold. Twenty files assert unverifiable specifics about "the wiki's" own
infrastructure in template-identical sentence skeletons. There is also one confirmed
semantic error (`concepts/calibration.md`, reliability-diagram direction reversed) and a
stub-naming concatenation artifact (`data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`).
The corpus is mostly *accurate* at the summary level — the best files (bayesian-networks,
forward-chaining, eval-contamination, hotfix-branches, temporal-difference-learning) are
genuinely good — but for a persistent memory store feeding an agentic loop, the systemic
boilerplate, fabricated-relevance framing, and missing provenance are a real quality cost.

## Critical findings

1. **Five confirmed self-links (invariant violation, 5/220 = 2.3%)** — all verified by reading; none are false positives.
   - `concepts/causal-interventions-ai.md` Related: `[[wiki/concepts/causal-interventions-ai|causal-interventions-ai]] — statistical basis` — links to its own page, and the anchor "statistical basis" is semantically wrong for an article about causal interventions.
   - `concepts/content-freshness-review.md` Related: `[[wiki/concepts/content-freshness-review|Content Freshness Review]]` — self-link appended as the last Related entry.
   - `concepts/dependency-attacks-ai.md` Related: `[[wiki/concepts/dependency-attacks-ai|dependency-attacks-ai]] — note` — self-link with filler annotation.
   - `concepts/expected-value-reasoning.md` Related: `[[wiki/concepts/expected-value-reasoning|Expected Value Reasoning]] — see also` — self-link with filler annotation.
   - `dev-tools/frontmatter-linting.md` Related: `[[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]` — self-link.
   - Why wrong: a self-link adds a node pointing at itself in the knowledge graph, corrupting traversal/backlink statistics, and the pattern (four of five carry filler labels like "— note" / "— see also") shows these were appended mechanically to pad the Related block. Fix: delete the self-links; replace with a real related page or drop the bullet.

2. **Fabricated-looking, unverifiable "the wiki's …" infrastructure claims (20/220 = 9%)** — the RSIS3/mykb relevance paragraphs assert specific facts about the wiki's own infrastructure in a template-identical sentence skeleton ("the wiki's X …; this note records the Y the loop checks"). I cannot verify any of these offline, and the uniformity of the skeleton across unrelated topics (VPN, spot pricing, TLS, storage, Lamport clocks) makes them read as generated filler rather than recorded reality. Examples:
   - `cloud-infra/site-to-site-vpn.md`: "the wiki's hybrid connectivity uses dual tunnels with BGP; this note records the tunnel and route policy the loop checks during network changes."
   - `cloud-infra/spot-instances.md`: "the wiki's batch layer runs spot-first with checkpointing; this note records interruption-rate telemetry so the loop tunes the spot/on-demand mix empirically."
   - `cloud-infra/tls-1-3-session-resumption.md`: "the wiki's API layer enables TLS 1.3 resumption with short-lived tickets; this note records the ticket policy the loop verifies after certificate or proxy changes."
   - `cloud-infra/snapshot-lifecycle-policies.md`: "the wiki's backup policies are recorded with their retention matrices here" — circular: the article claims it *is* the record of the policies, with no pointer to where those policies actually live.
   - Why wrong: a memory store for an agentic loop will retrieve these as premises about the system's own setup; if the claims are invented, the loop will act on false self-knowledge. Fix: either make the claims real (link to the actual config/policies) or rewrite as hedged hypotheticals ("if the wiki ran spot-first …").

3. **Provenance bar violated across the whole slice: 0 citations in 220 files.** The wiki's own `concepts/promotion-checklist.md` (in this slice) states: "two or more curl-verified sources" is a checklist item and "the source item enforces provenance (claims must trace to verifiable references)". Only 2 of 220 files contain any `http(s)` string, both documentation examples (`cloud-infra/service-discovery-dns-based.md` `http://payments.svc.internal:8080`; `dev-tools/curl-patterns.md` `https://api.example/health`), not citations. Zero sources, zero "source:" fields, zero links to a sources index were found in any file read. Consequences: every specific numeric claim in the slice is unverifiable — e.g. `data-storage/hnsw.md` "~95% recall at efSearch 64" and "memory sits around 10x vector size", `cloud-infra/spot-instances.md` "GCP preemptible fixed 24h/80% discount", `cloud-infra/storage-tiering.md` "cut storage spend 50-80%", `cloud-infra/site-to-site-vpn.md` "typically 1.25-10 Gbps on cloud gateways". Either the checklist is aspirational fiction or the wave skipped a stated promotion criterion; both are bad. Fix: add a "Sources" section with real URLs to the articles carrying numeric claims, or relax the checklist and say so explicitly.

## Major findings

1. **Machine-generated Related-block annotation boilerplate (93/220 = 42%, 215 annotations).** Phrases repeated near-verbatim across files: "the full treatment of this theme" (72 files), "existing graph context" (79 files), plus "— the category", "— the class", "— the framework", "— see also", "— note", "— related tool". Examples: `concepts/dependency-attacks-ai.md` `[[wiki/decisions/self-hosting|Self-Hosting]] — the full treatment of this theme`; `concepts/sandbagging.md` `[[wiki/testing/ai-safety-evals|Ai Safety Evals]] — existing graph context`. These labels carry no information, are identical across unrelated topics, and inflate the link count — the "irrelevant links added purely to inflate the link count" defect class. Fix: strip the annotations, keep plain links.

2. **Trailing "practice" bullets bolted on after the RSIS3 relevance bullet (59/220 = 27%).** Content that belongs in Details or a dedicated section was appended after the relevance paragraph — 37 files orphan the bullet behind a blank line (list broken), 22 keep it adjacent but still out of place. Examples:
   - `data-storage/pinecone.md`: "## Details" list ends with the RSIS3 bullet, then a blank line, then `- Keep embeddings and metadata exportable so a future self-hosted move does not require re-indexing from scratch.` (same shape in `data-storage/milvus.md`, `data-storage/simhash.md`, `data-storage/postgres-tsvector.md`, `dev-tools/fixed-window.md`, `dev-tools/leaky-bucket.md`, `dev-tools/fuzzing-tools.md`, `decisions/api-access-policies.md`, and 30 more).
   - `cloud-infra/split-horizon-dns.md`: `- Synchronization: generate internal and external views from the same source of truth; manual dual maintenance is how the two views diverge.` directly after the relevance bullet (same shape in `cloud-infra/spot-instances.md`, `cloud-infra/site-to-site-vpn.md`, `compositions/lamport-clocks.md`, etc.).
   - Why wrong: these bullets are effectively orphaned content — half of them render outside any list, and their placement (after the relevance paragraph) is arbitrary, a hallmark of word-count chasing. Fix: merge into Details in reading order or promote to a real section.

3. **Confirmed semantic error in `concepts/calibration.md`.** Details bullet: "A reliability diagram plots the two; points above the diagonal are overconfident, points below are underconfident." This is backwards. In a reliability diagram (x = predicted confidence, y = observed accuracy), a point above the diagonal means accuracy exceeds confidence — i.e. *under*confident; below the diagonal is overconfident. This is exactly the class of "subtly wrong definition" the review targets, in a page about calibration. Fix: swap "over" and "under".

4. **Stub-naming concatenation artifact: `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`.** Filename contains "druid" twice; title is "ClickHouse vs Druid vs Pinot". The slug looks like two stub titles ("clickhouse-vs-druid-pinot" + "druid-architecture") welded together at promotion. Structural/SEO defect and a red flag for the wave's rename/merge hygiene. Fix: rename to `clickhouse-vs-druid-vs-pinot.md` (with referrer updates).

5. **Word-floor clustering consistent with padding (76/220 = 35% at 320–339 words).** Minimum in slice is exactly 320; median 389.5; 25 files at 320–325. `cloud-infra/vpn-split-tunneling.md` (320), `dev-tools/correlation-ids.md` (320), `data-storage/pinecone.md` (322), `dev-tools/four-golden-signals.md` (322), `cloud-infra/site-to-site-vpn.md` (323) all sit just past the bar, and several carry the dangling-bullet filler above. Clustering at the threshold plus the appended bullets is the profile of floor-hitting, not organic expansion. Fix: require a margin above the floor (e.g. ≥380) and spot-check for append-patterns before promoting.

## Minor & nits

1. **Duplicate links to the same target within one file** (4 files): `compositions/fencing-tokens.md` links `wiki/compositions/lease-based-locks` twice; `concepts/activation-patching.md` links `wiki/concepts/causal-interventions-ai` twice; `concepts/causal-interventions-ai.md` links `wiki/concepts/activation-patching` twice; `decisions/data-license-issues.md` links `wiki/syntheses/evidence-and-provenance` twice. Related blocks should have one link per target.
2. **Blank line directly after the "## Related" heading** (20 files), e.g. `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`, `data-storage/scd-type-2-slowly-changing-dimensions.md`, `data-storage/backpressure-and-flow-control.md` — formatting drift from the template.
3. `concepts/sandbagging.md` Related label `Ai Safety Evals` — inconsistent capitalization ("AI Safety Evals").
4. `concepts/early-stopping.md` Related label `eval-splits` — lowercase slug used as display text.
5. `concepts/causal-interventions-ai.md` — self-link mislabeled "statistical basis" (see Critical #1); also double-links `activation-patching` ("the main method" + "the framing").
6. Unverifiable numeric specifics (cannot verify offline; none sourced): `data-storage/hnsw.md` "~95% recall at efSearch 64" / "memory sits around 10x vector size"; `cloud-infra/storage-tiering.md` "cut storage spend 50-80%" and "costs 5-10x"; `cloud-infra/site-to-site-vpn.md` "typically 1.25-10 Gbps on cloud gateways" (mixes AWS's ~1.25 Gbps-per-tunnel with Azure's top-SKU ~10 Gbps without attribution).
7. `cloud-infra/spot-instances.md` — "GCP preemptible fixed 24h/80% discount": discount varies by machine type (60–91%), and GCP preemptible VMs were superseded by GCP Spot in 2021; wording is outdated and the 80% figure is not universal.
8. `dev-tools/flame-graphs.md` — "a wiki build that takes 40 seconds — a flame graph shows 25 seconds in markdown parsing and 10 in link resolution": invented-specific example figures presented as concrete fact; harmless but fabricated precision.
9. Checker false positives (all three placeholder flags are legitimate usage, confirmed by reading): `cloud-infra/split-horizon-dns.md` "example.com" (RFC 2606 documentation domain), `concepts/stub-criteria.md` "placeholder" (defining what a stub is), `data-storage/postgres-tsvector.md` "insert and query" (analyzer-mismatch explanation).

## Sample audit table

| File (relative to components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| concepts/causal-interventions-ai.md | 404 | FAIL | self-link "statistical basis"; duplicate link to activation-patching |
| concepts/content-freshness-review.md | 386 | FAIL | self-link in Related |
| concepts/dependency-attacks-ai.md | 386 | FAIL | self-link "— note"; boilerplate annotations |
| concepts/expected-value-reasoning.md | 447 | FAIL | self-link "— see also" |
| dev-tools/frontmatter-linting.md | 340 | FAIL | self-link; dangling bullet after RSIS3 relevance |
| concepts/calibration.md | 409 | FAIL | reliability diagram: above-diagonal = underconfident, not overconfident |
| data-storage/clickhouse-vs-druid-pinot-druid-architecture.md | 378 | FAIL | filename duplicates "druid"; blank line after ## Related |
| cloud-infra/split-horizon-dns.md | 325 | PASS w/ issues | example.com false positive; trailing "Synchronization" bullet after relevance |
| cloud-infra/site-to-site-vpn.md | 323 | PASS w/ issues | unverifiable "the wiki's hybrid connectivity" claim; trailing bullet; unsourced Gbps range |
| cloud-infra/spot-instances.md | 339 | PASS w/ issues | unverifiable "the wiki's batch layer" claim; outdated GCP preemptible wording; trailing bullets |
| cloud-infra/tcp-retransmission.md | 341 | PASS w/ issues | sound mechanics; trailing "Diagnosis order"/"Baseline first" bullets |
| cloud-infra/tls-1-3-session-resumption.md | 321 | PASS w/ issues | accurate; unverifiable "the wiki's API layer" claim |
| cloud-infra/vpn-split-tunneling.md | 320 | PASS (at floor) | exactly 320; trailing bullet |
| cloud-infra/storage-tiering.md | 346 | PASS w/ issues | unsourced "50-80%"/"5-10x"; trailing bullets |
| cloud-infra/snapshot-lifecycle-policies.md | 331 | PASS w/ issues | circular "recorded with their retention matrices here"; trailing bullets |
| cloud-infra/sovereignty-and-compliance-storage.md | 336 | PASS w/ issues | unverifiable "the wiki's data-classification matrix" claim; trailing bullets |
| concepts/stub-criteria.md | 428 | PASS | "placeholder" false positive; good content |
| concepts/activation-patching.md | 404 | PASS w/ issues | duplicate link to causal-interventions-ai; boilerplate annotations |
| concepts/bayesian-networks.md | 396 | PASS | clean; correctly hedged relevance |
| concepts/induction-heads.md | 440 | PASS | accurate; good |
| concepts/polysemanticity.md | 433 | PASS | accurate; boilerplate annotations in Related |
| concepts/sandbagging.md | 470 | PASS w/ issues | "Ai Safety Evals" label; solid body |
| concepts/early-stopping.md | 445 | PASS w/ issues | "eval-splits" lowercase label |
| concepts/forward-chaining.md | 433 | PASS | accurate (XCON example fine); good |
| concepts/temporal-difference-learning.md | 529 | PASS | accurate; good |
| concepts/eval-contamination.md | 406 | PASS | accurate; good |
| data-storage/postgres-tsvector.md | 336 | PASS w/ issues | "insert and query" false positive; dangling bullet |
| data-storage/faiss.md | 366 | PASS | accurate; boilerplate annotations |
| data-storage/hnsw.md | 332 | PASS w/ issues | unsourced "~95% recall"/"10x vector size" |
| data-storage/milvus.md | 337 | PASS w/ issues | dangling bullet |
| data-storage/pinecone.md | 322 | PASS w/ issues | dangling bullet |
| data-storage/simhash.md | 321 | PASS w/ issues | dangling bullet |
| data-storage/scd-type-2-slowly-changing-dimensions.md | 371 | PASS | good; blank line after ## Related |
| dev-tools/correlation-ids.md | 320 | PASS (at floor) | exactly 320; content sound |
| dev-tools/fixed-window.md | 324 | PASS w/ issues | dangling bullet |
| dev-tools/leaky-bucket.md | 329 | PASS w/ issues | dangling bullet |
| dev-tools/fuzzing-tools.md | 325 | PASS w/ issues | dangling bullet |
| dev-tools/link-fix-automation.md | 335 | PASS w/ issues | dangling bullet |
| dev-tools/four-golden-signals.md | 322 | PASS | sound |
| dev-tools/flame-graphs.md | 325 | PASS w/ issues | invented "40-second build" example numbers |
| communities/hotfix-branches.md | 540 | PASS | clean, different (better) template |
| compositions/fencing-tokens.md | 350 | PASS w/ issues | duplicate link to lease-based-locks |
| compositions/lamport-clocks.md | 327 | PASS w/ issues | trailing bullets; unverifiable "the wiki's sync layer" claim |
| decisions/api-access-policies.md | 329 | PASS w/ issues | dangling bullet |

Quantification across the 220-file slice: status failures 0/220 (0%); word-count failures 0/220 (0%); missing/invalid frontmatter 0/220 (0%); broken wikilinks/mdlinks per checker 0/220 (0%); self-links 5/220 (2.3%); real placeholders 0/220 (3 false positives); Related-block annotation boilerplate 93/220 (42%); trailing-bullet defect 59/220 (27%); blank line after "## Related" 20/220 (9%); unverifiable "the wiki's …" relevance claims 20/220 (9%); files at 320–339 words 76/220 (35%); files with any citation URL 0/220.

## Recommendations

1. **Add a provenance gate before the next promotion wave.** The wave's own checklist requires "two or more curl-verified sources"; 0/220 files carry one. Require a `Sources` section (real URLs) for any article containing numeric, vendor, or infrastructure claims, and make the promotion checker fail without it. This is the single highest-impact fix: it turns the "cannot verify" findings into "verified" or "removed".
2. **Remove the machine-generated Related annotations and self-links.** Strip "— the full treatment of this theme" / "— existing graph context" / "— note" / "— see also" labels (215 instances, 93 files), delete the 5 self-links, and deduplicate same-target links (4 files). Enforce in the linter: no self-links, max one link per target.
3. **Re-merge or re-place the 59 trailing "practice" bullets.** Move them back into the Details list in reading order (or promote them to a real section) and restore single-list structure; fix the 37 blank-line-orphaned bullets and the 20 blank lines after "## Related". A structural lint pass can make this mechanical.
4. **Fix the two content defects now**: swap over/under in `concepts/calibration.md` (reliability-diagram paragraph) and rename `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md` to a non-duplicated slug, updating referrers. These are cheap and immediately improve correctness.
5. **Raise the effective promotion floor and require a margin.** With the median at 389.5 and 76 files within 20 words of 320, the threshold invites append-padding (which is visible in the trailing bullets). Set the promotion bar to ~400 body words with a rule that bullets after the RSIS3 relevance paragraph require explicit review, so floor-hitting stops producing the current artifact profile.
