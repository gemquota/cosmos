# Adversarial Review 1 (Pass 2) — MyKB Stub-Promotion Wave (slice1, 220 files)

Reviewer: adversarial #1 · Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice1.txt` (220 files)
Areas in slice: api-protocols (117), cloud-infra (60), ai-ml (32), agent-systems (8), android-core (3)
Method: invariant checker + manual verification of all 14 flagged files + full re-read of the 2 factually-fixed files in-slice (dp-vs-px, anr-diagnostics) + deep-read of 30 files spanning all 5 areas + 10 link-target spot checks + corpus-wide scans for the fixed defect classes.

## Verdict

**Health score: 79 / 100**

**Pass 1 fixes held in this slice — verified.** The mechanical cleanup landed completely: 0 self-links (was 33 in 30 files), 0 occurrences of the "related coverage in the same cluster"/"full treatment of this theme"/"existing graph context"/"— note"/"— see also" annotation strings (was 799 across 114 files), 0 duplicated Related lines (was 17 files), 0 truncated `[[raw/archive/…]]` links, 0 dead `README` links, and the shared non-topical networking tail shrank from 41 cloud-infra files to 10 files that are all networking articles themselves (dnssec-and-validation, quic-and-http3, etc.), so the tail is now topically defensible. The 320-word floor holds: 0 files in the slice are below it (all 14 checker placeholder flags verified false positives: 12 legitimate RFC 2606 `example.com` doc domains, 1 descriptive "no placeholder text" in article-health-scores, 1 regex artifact in hash-collision-dos). Both in-slice factual fixes are correct: `dp-vs-px.md` now says 4px/xxxhdpi consistently ("1dp is 1px on mdpi and 4px on xxxhdpi", Details "xxxhdpi = 4x"), and `anr-diagnostics.md`'s `apply()`/`commit()` conflation is corrected ("apply() whose queued disk writes drain on the main thread when the activity stops" — accurate QueuedWork behavior).

The score stays below 80 because the defect classes the cleanup deliberately did NOT touch are still pervasive and now dominate the defect surface: 74 files (33.6%) still carry unverifiable "the wiki's … does Y" operational claims (DNSSEC automated rollover, HTTP/3 edge serving, a quota registry, a cost model, tunneled lab networks, preemptible batch runners, Graviton migration records) for which I found no supporting config anywhere in the repo — these read as invented specificity stored as fact in a memory layer whose whole job is trustworthy recall. Keyword-matched irrelevant links remain confirmed in 4+ files (savings-plans → Rollback Plans; glacier-and-s3-lifecycle → three "lifecycle" pages; azure-blob-access-tiers → Remote Access Methods / Zero Trust Access Proxies; point-of-presence → Point-in-Time Recovery), and the cleanup introduced one new regression class: **3 files lost their entire Related section** (amd-epyc-and-intel-xeon, authoritative-and-recursive-resolvers, legal-hold-and-preservation) instead of retargeting to topical links. The linked-target invariant from Pass 1 also persists: promoted files link to same-title, sub-320-word `growing` pages (oauth2-authorization-code at 249 words with title identical to authorization-code-flow; retry-backoff 222; networking-fundamentals 218), and corpus-wide 1,673 `growing` files sit below 320 body words.

Technical content quality remains high — in 30 deep-reads I found no fabricated papers, models, APIs, or wrong protocol mechanics; the OAuth, JWT, HTTP, DNS, multicast, and ML content is accurate. The remaining problems are systemic generator/pipeline defects, not hallucinated prose.

Per-defect-type quantification (of 220 files): status ≠ growing **0** · body < 320 **0** · missing frontmatter keys **0** · self-links **0 (was 30)** · annotation strings **0 (was 114)** · duplicated Related lines **0 (was 17)** · placeholder flags **14, all false positives** · broken links **0 (checker); 0/10 spot-checked (all targets exist, 2 topically wrong)** · files with no `## Related` **3 (new)** · files with "the wiki's …" unverifiable claims **74 (33.6%, unchanged)** · files with confirmed keyword-matched irrelevant links **≥4 (unchanged)** · "RSIS3/mykb relevance" boilerplate **186 (84.5%, unchanged)**.

## Critical findings

1. **Unverifiable "the wiki's … does Y" claims remain in 74 files (33.6%) — Pass 1 Major #6, deliberately unfixed, confirmed still present.**
   These assert concrete operational facts about the wiki/deployment that no repo artifact supports. I searched `components/rsis3`, `components/space/src`, and `components/mykb/.wiki-daemon` for each claimed subsystem: no DNS/DNSSEC automation, no backup lifecycle, no HTTP/3/QUIC edge config, no quota registry, no cost model, no tunneled-lab config, no preemptible-runner config, no Graviton migration records exist outside the wiki prose itself.
   - `cloud-infra/dnssec-and-validation.md`: "RSIS3/mykb relevance: the wiki's domains are signed with automated key rollover; this note records the DS publication and rollover procedure the loop's DNS automation follows."
   - `cloud-infra/http-3-0-rtt.md`: "RSIS3/mykb relevance: the wiki's edge serving enables HTTP/3 with h2 fallback; this note records the fallback order…"
   - `cloud-infra/glacier-and-s3-lifecycle.md`: "RSIS3/mykb relevance: the wiki's backup lifecycle (30/90/365) is recorded here with its restore tests…"
   - `cloud-infra/quota-management.md`: "the wiki's quota registry tracks per-service limits and headroom…"
   - `cloud-infra/mtu-and-fragmentation.md`: "the wiki's tunneled lab networks record per-link MTUs and MSS clamps…"
   - `cloud-infra/graviton-and-aws.md`: "the wiki records per-service Graviton migration results…"
   Why it is wrong: these are specific factual assertions ("is signed with automated key rollover", "enables HTTP/3") stored as memory; an agent that inherits them will plan against infrastructure that does not exist. Unverifiable offline and unsupported by the repo. Fix: either point each claim at real config/telemetry, or convert to policy ("the standing rule is …"), or delete the sentence.

2. **`growing`-status pages below the 320-word floor and title collisions persist (Pass 1 Critical #2, unfixed), and promoted files link to them.**
   Confirmed still present in-slice links:
   - `api-protocols/oauth2-authorization-code.md` — 249 body words, `status: growing`, title `"Authorization Code Flow"` — byte-identical title to the promoted `api-protocols/authorization-code-flow.md`, which links to it in Related: `- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]`.
   - `api-protocols/oauth2-client-credentials.md` — 240 words, growing; `api-protocols/oauth2-refresh-tokens.md` — 256 words, growing; also `oauth2-pkce.md` (256), `oauth2-scopes.md` (230), `oauth2.md` (235).
   - `api-protocols/retry-backoff.md` — 222 words, growing (linked from 429-handling, webhook-signatures, webhook-retries); `cloud-infra/networking-fundamentals.md` — 218 words, growing (linked from 10 files).
   Corpus-wide scan: **1,673 files carry `status: growing` below 320 body words**, so "growing" does not denote the wave's quality bar anywhere except the 1,098 promoted files. Fix: merge the oauth2-* siblings into the promoted articles, and re-audit corpus-wide statuses against the word floor.

## Major findings

1. **Cleanup regression: 3 files lost their entire `## Related` section — orphaned links removed without replacement.**
   - `cloud-infra/amd-epyc-and-intel-xeon.md` (Pass 1 documented its "Irrelevant Related tail"; the tail is now gone but so is the whole section — the file ends at the last Details bullet).
   - `cloud-infra/authoritative-and-recursive-resolvers.md`
   - `cloud-infra/legal-hold-and-preservation.md` — a compliance topic with zero links to object-lock/immutability/retention pages, which exist in the corpus.
   This is the "orphaned/empty Related" regression class the cleanup was supposed to check: removing bad links is right, but these articles are now link-isolated in a knowledge graph whose own metrics (`ai-ml/graph-density-metrics.md`: "two related articles that never link are a discovery failure") treat that as a defect. Fix: retarget to topical pages (e.g., amd-epyc → cloud-providers-aws-azure-gcp, legal-hold → object-lock-and-worm).

2. **Keyword-matched irrelevant links remain (Pass 1 Major #3, deliberately unfixed) — confirmed in 4 files, likely more.**
   - `cloud-infra/savings-plans.md` Related still opens with `- [[wiki/devops-infra/rollback-plans|Rollback Plans]]` — a deployment-rollback page matched on the word "plans".
   - `cloud-infra/glacier-and-s3-lifecycle.md` Related still lists `[[wiki/cloud-infra/function-execution-lifecycle|Function Execution Lifecycle]]`, `[[wiki/os-shell/process-signals-and-lifecycle|Process Signals & Lifecycle]]`, `[[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]]` — a pure "lifecycle" keyword match; serverless cold starts and pod states have nothing to do with S3 archive tiering. (The cleanup did add the topical `snapshot-lifecycle-policies` link, making the mismatch starker.)
   - `cloud-infra/azure-blob-access-tiers.md` Related contains `[[wiki/cloud-infra/remote-access-methods|Remote Access Methods]]` and `[[wiki/devops-infra/zero-trust-access-proxies|Zero Trust Access Proxies]]` — matched on the word "access".
   - `cloud-infra/point-of-presence.md` Related contains exactly one link: `- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]]` — matched on "point", and now the article's only outbound edge.
   These are defect class 6 ("irrelevant links added purely to inflate the link count") in the wiki's own `ai-ml/link-diversity.md` taxonomy. Fix: rerun the Related generator with topic filtering (Jaccard over article bodies, or curated per-area link sets).

3. **The 320-word floor is met by structure, not content, in the bottom tier — padding-to-threshold persists in mechanism, if not in the body prose.**
   25 files sit at 320–329 words. The bodies themselves are technically dense (multicast-networking, cost-of-bandwidth, point-of-presence read substantively), but each file carries 1–3 formulaic closing bullets ("Broker alternative:", "Group hygiene:", "Latency verification:", "Failover rehearsal:", "Hold audit:", "Release authority:", "Egress budget:") that read as threshold-fillers, plus the mandatory "RSIS3/mykb relevance" paragraph (~30–35 words). At exactly 320 words (`multicast-networking.md`, `preemptible-vm-workloads.md`), removing the boilerplate sections drops the file below the promoted tier. Fix: measure body words excluding the "RSIS3/mykb relevance" section and the trailing one-line bullets, or raise the bar and re-expand.

## Minor & nits

- **All 14 checker placeholder flags are false positives** (verified file-by-file): 12 files use RFC 2606 `example.com` doc domains correctly (cookie-prefixes, cookie-scoping, device-flow, domain-cookies, header-injection, issuer-validation, jku-attacks, samesite-lax-strict, uri-vs-url, url-structure, certificate-transparency, dnssec-and-validation); `ai-ml/article-health-scores.md` uses "no placeholder text" descriptively; `api-protocols/hash-collision-dos.md` flags are regex artifacts ("every insert and lookup degenerates into a linked-list scan"). No action needed.
- **`cloud-infra/coldline-and-archive-storage-classes.md` pricing claim unchanged** (Pass 1 minor): "5TB of legal holds in Archive at ~$0.004/GB-month … a 5x saving" — GCP Archive list is ~$0.0012/GB-month in us-central1; $0.004 is Coldline pricing, and the 5x arithmetic uses the wrong base. Likely conflation, still present.
- **`cloud-infra/preemptible-vm-workloads.md`**: "GCP preemptibles run max 24h and stop with a 30s warning (A3-style preemptibles differ)" — the parenthetical remains vague with no detail or citation (Pass 1 minor, unfixed).
- **`android-core/anr-diagnostics.md`** still uses a hyphen where the wiki uses em-dashes ("blocked too long - input dispatch"), still carries empty `source: []` frontmatter, and still has no `## Summary` heading (intro paragraph + bullets instead) — all three Pass 1 minors persist. Same `source: []` / missing-Summary pattern in `app-threading.md` and `dp-vs-px.md`.
- **"RSIS3/mykb relevance" boilerplate**: 186/220 files (84.5%) end with this section; many are generic ("storing the decision rule here keeps loop-generated incident reviews consistent across sessions" — `api-protocols/401-vs-403.md`). House style, but it is the vehicle for the unverifiable claims in Critical #1.
- **`api-protocols/authorization-code-flow.md`** Related lists both `[[wiki/api-protocols/oauth2|OAuth 2.0]]` and the sub-320 same-title `[[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]` — two edges whose link text overlaps the article's own title (basename-collision ambiguity, defect class 6, persists from Pass 1).
- **`api-protocols/401-vs-403.md`** "a revoked token must stay rejected even after re-login flows" remains a policy statement phrased as spec behavior (Pass 1 minor, unfixed).
- **Facts in the fixed android files check out** — `dp-vs-px.md` bucket factors (1x/1.5x/2x/3x/4x) correct; `anr-diagnostics.md` timeout figures (5s input, 10/60s broadcast, 20/200s service) match platform documentation.

## Sample audit table

Deep-read files (words = body words; verdict reflects content quality + remaining wave defects).

| File (relative to components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| ai-ml/article-health-scores.md | 478 | Pass | "placeholder" flag false positive; meta-article documents the wave's own remaining defects. |
| ai-ml/graph-density-metrics.md | 371 | Pass | Accurate; self-link exclusion stated and now honored by the corpus. |
| ai-ml/link-diversity.md | 345 | Pass | Sound; keyword-matched links (Major #2) still violate its own advice. |
| ai-ml/dpo.md | 385 | Pass | DPO/RLHF tradeoffs accurate; real link descriptors. |
| ai-ml/model-stealing.md | 348 | Pass | Attack taxonomy accurate; no invented specifics. |
| ai-ml/sparse-autoencoders.md | 354 | Pass | Training/interpretability caveats honest. |
| ai-ml/probing.md | 334 | Pass | Linear-probe framing and control baselines correct. |
| agent-systems/accountability-ai.md | 347 | Pass | Sound; "wiki's pass reports make the loop accountable" partially verifiable (OKF practice), mild. |
| agent-systems/ai-act.md | 363 | Pass | Tiering accurate; "2025-2027+" timeline cannot fully verify; "wiki maintains a compliance checklist" unverifiable. |
| agent-systems/ai-regulation.md | 353 | Pass | Layered-regulation framing sound. |
| agent-systems/deception-research-ai.md | 331 | Pass | Measured tone; no overclaiming. |
| android-core/dp-vs-px.md | 530 | Pass (fixed) | Factual fix correct: xxxhdpi = 4x everywhere; `source: []` and missing `## Summary` persist. |
| android-core/anr-diagnostics.md | 567 | Pass (fixed) | `apply()`/`commit()` fix correct; hyphen style + `source: []` persist. |
| api-protocols/hash-collision-dos.md | 431 | Pass | Regex flags false positives; SipHash/random-seed defense accurate. |
| api-protocols/authorization-code-flow.md | 418 | Major #2-persist | Accurate; Related links to same-title sub-320 sibling (oauth2-authorization-code). |
| api-protocols/refresh-token-rotation.md | 442 | Pass | RFC 9700 + reuse-detection accurate; self-link ×3 gone. |
| api-protocols/samesite-lax-strict.md | 439 | Pass | Lax/Strict/None rules correct; Related topical. |
| api-protocols/uri-vs-url.md | 424 | Pass | RFC 3986/URN/WHATWG distinction accurate. |
| api-protocols/401-vs-403.md | 452 | Pass | Retry semantics correct; revoked-token sentence is policy-as-spec. |
| api-protocols/jku-attacks.md | 454 | Pass | jku/jwk/x5u + SSRF framing excellent and accurate. |
| api-protocols/tcp-vs-udp.md | 448 | Pass | Transport tradeoffs accurate; self-link gone. |
| api-protocols/webhook-retries.md | 441 | Pass | Retry classification + dead-letter guidance correct. |
| cloud-infra/dnssec-and-validation.md | 332 | Critical #1 | "wiki's domains are signed with automated key rollover" — cannot verify, no repo config; tail now topical. |
| cloud-infra/glacier-and-s3-lifecycle.md | 333 | Major #2 | Three keyword-matched "lifecycle" links remain; 30/90/365 claim unverifiable. |
| cloud-infra/preemptible-vm-workloads.md | 320 | Critical #1 (mild) | "wiki's batch experiments run on preemptible capacity" unverifiable; "A3-style preemptibles differ" vague. |
| cloud-infra/http-3-0-rtt.md | 326 | Critical #1 | "wiki's edge serving enables HTTP/3" unverifiable; body accurate. |
| cloud-infra/graviton-and-aws.md | 328 | Critical #1 (mild) | "wiki records per-service Graviton migration results" unverifiable. |
| cloud-infra/multicast-networking.md | 320 | Pass (floor) | Accurate IGMP/PIM/VXLAN; "wiki's distributed-cache experiments" unverifiable; exactly 320 words. |
| cloud-infra/cost-of-bandwidth.md | 324 | Pass | Pricing figures accurate; "wiki's deployment monitors egress per service" unverifiable. |
| cloud-infra/point-of-presence.md | 325 | Major #2 | Only Related link is keyword-matched Point-in-Time Recovery. |
| cloud-infra/legal-hold-and-preservation.md | 325 | Major #1 (new) | No Related section at all; content accurate. |
| cloud-infra/savings-plans.md | 341 | Major #2 | Related opens with Rollback Plans (keyword match); Compute SP scope correct. |
| cloud-infra/amd-epyc-and-intel-xeon.md | 338 | Major #1 (new) | Related section removed entirely; body accurate. |
| cloud-infra/authoritative-and-recursive-resolvers.md | 339 | Major #1 (new) | No Related section; body accurate. |
| cloud-infra/azure-blob-access-tiers.md | 330 | Major #2 | "access"-keyword links (Remote Access Methods, Zero Trust Access Proxies) remain. |
| cloud-infra/coldline-and-archive-storage-classes.md | 334 | Minor | ~$0.004/GB-month likely Coldline not Archive pricing; otherwise tier rules correct. |

## Recommendations

1. **Remove or ground every "the wiki's … does Y" claim (74 files).** Grep the corpus for `the wiki's`/`wiki records`/`wiki maintains` and either link each to real config/telemetry, convert to policy wording, or delete. This is the highest-impact remaining defect because the wiki's purpose is reliable agent memory and these are confident assertions about infrastructure that does not exist.
2. **Restore topical Related sections to the 3 files left linkless by the cleanup** (amd-epyc-and-intel-xeon, authoritative-and-recursive-resolvers, legal-hold-and-preservation), then add a promotion invariant: "Related must contain ≥1 link and every link must be topical (no keyword-basename-only matches)."
3. **Replace the confirmed keyword-matched links** (savings-plans → Rollback Plans; glacier-and-s3-lifecycle → the three "lifecycle" pages; azure-blob-access-tiers → the two "access" pages; point-of-presence → Point-in-Time Recovery) using the same topic-filter the cleanup used to fix the 41-file networking tail — the mechanism exists, it was just not run on non-tail links.
4. **Resolve the OAuth near-duplicate cluster**: merge `oauth2-authorization-code.md`, `oauth2-client-credentials.md`, `oauth2-refresh-tokens.md` into the promoted `authorization-code-flow.md`, `client-credentials-flow.md`, `refresh-token-rotation.md` (same topics, same titles, 240–256 words vs 418–442), then run a corpus-wide status audit — 1,673 `growing` files below 320 words contradict the wave's own bar.
5. **Re-base the word-count floor on true content**: exclude the "RSIS3/mykb relevance" paragraph and the trailing one-line filler bullets from the ≥320 measurement, so files at exactly 320 words (multicast-networking, preemptible-vm-workloads) are promoted on substance rather than boilerplate. Re-verify the 62 topped-up files after re-measuring.
