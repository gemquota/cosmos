# Adversarial Review 3 — MyKB Stub Promotion Wave (slice3, 220 files)

Reviewer: adversarial reviewer #3
Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice3.txt` (220 paths)
Areas: dev-tools (21), devops-infra (166), frontend-frameworks (26), identity (7)
Method: ran `check_slice.py`, verified every flagged file by reading it, deep-read 48 files
across all four areas, spot-checked 16 link targets by opening them.

## Verdict

**Score: 79 / 100**

The promotion wave held its hard invariants: all 220 files are `status: growing`, every
body is ≥ 320 words (min observed 323), all six required frontmatter keys are present,
there are no broken wikilinks or markdown links, no missing files, and no non-UTF8 bytes.
I found **no fabrication**: the only URLs in the slice (NIST SP 800-63B, OWASP Auth Cheat
Sheet, GDPR Art. 33, RFC 5321, MITRE ATT&CK TA0006, FIDO Alliance, Wikipedia) are real,
and the technical claims I could check offline (3-2-1 math, 99.9% = 43 min/month, p99
fan-out amplification, CoreDNS `ndots:5`, CSI plugin split, PDB `minAvailable`, GDPR 72h,
Angular signals, GraphQL APQ handshake) are accurate. The score is pulled down by a
systematic template failure: 6 self-links, 16 files with orphan "takeaway" bullets, 14
devops-infra files whose Related sections contain **zero** topical links (only cluster
boilerplate), keyword-matched irrelevant links, and 5 identity files that pad their word
count by repeating the Summary sentence verbatim as the first Details bullet. These are
real defects but not fabricated knowledge; the wiki's memory value is intact.

- Checker: 12 files flagged → 6 confirmed defects (self-links), 6 false positives (all
  placeholder hits were legitimate prose or example domains).
- Per-defect-type: invariant violations 6/220 (2.7%); padding/word-stuffing 5/220
  (2.3%); structural (orphan bullets) 16/220 (7.3%); link hygiene (boilerplate-only
  Related) 14/220 (6.4%); link hygiene (keyword-matched irrelevant links) ≥6/220.

## Critical findings

1. **Self-links in Related sections — 6 files (invariant violation).**
   The cluster-link generator emitted a link to the page itself in each file, labeled
   "related coverage in the same cluster", which is impossible for a related page.
   - `frontend-frameworks/concurrent-rendering.md` (line 25):
     `- [[wiki/frontend-frameworks/concurrent-rendering|Concurrent Rendering]] — related coverage in the same cluster`
   - `frontend-frameworks/reactivity-pitfalls.md` (line 25):
     `- [[wiki/frontend-frameworks/reactivity-pitfalls|Reactivity Pitfalls]] — related coverage in the same cluster`
   - `frontend-frameworks/starttransition.md` (line 25):
     `- [[wiki/frontend-frameworks/starttransition|startTransition]] — related coverage in the same cluster`
   - `frontend-frameworks/suspense-practice.md` (line 25):
     `- [[wiki/frontend-frameworks/suspense-practice|Suspense in Practice]] — related coverage in the same cluster`
   - `frontend-frameworks/vue-composition-api.md` (line 25):
     `- [[wiki/frontend-frameworks/vue-composition-api|Vue Composition API]] — related coverage in the same cluster`
   - `frontend-frameworks/vue-reactivity.md` (line 25):
     `- [[wiki/frontend-frameworks/vue-reactivity|Vue Reactivity]] — related coverage in the same cluster`
   Why it is wrong: a self-link is dead weight, breaks graph tools that assume Related is
   a neighbor set, and shows the Related list was generated without reading it. Suggested
   fix: drop the self entry from the generator output (all six are the 5th of 7 links in
   an otherwise identical template) and re-run the checker's self-link rule on the wave.

## Major findings

1. **Related sections with zero topical links — 14 devops-infra files.**
   These files link only `kubernetes-control-plane`, `observability-pillars`, and the two
   syntheses pages, even though topically adjacent pages exist in the same slice:
   `automated-rollbacks.md`, `cosign-and-sigstore.md`, `devcontainers-revisited.md`,
   `game-days-and-failure-drills.md`, `hostpath-and-subpath.md`,
   `leader-election-and-quorum.md`, `open-tofu-forks.md`,
   `operator-sdk-and-controller-runtime.md`, `pulumi-and-crossplane.md`,
   `readiness-vs-liveness-revisited.md`, `rto-and-rpo.md`, `sbom-and-syft.md`,
   `supply-chain-attestations.md`, `vulnerability-fix-cadence.md`.
   Evidence: `devops-infra/rto-and-rpo.md` Related is only
   `kubernetes-control-plane`, `observability-pillars`, `knowledge-acquisition-workflow`,
   `mykb-acquisition-curation-and-practices` — while `disaster-recovery-tiers.md`,
   `point-in-time-recovery.md`, and `backups.md` (all in this slice) are unlinked.
   `readiness-vs-liveness-revisited.md` does not link `startup-probes-and-graceful-shutdown.md`
   or `health-endpoint-contracts.md`; `cosign-and-sigstore.md` does not link
   `image-signing-and-notary.md` or `supply-chain-attestations.md`. The Related section is
   the primary navigation surface of a knowledge graph; these pages are dead ends.

2. **Keyword-matched irrelevant links (link inflation).**
   Several Related links are topically unrelated and appear matched on a title keyword:
   - `devops-infra/custom-resource-definitions.md` links `[[wiki/os-shell/resource-utilization-analysis|Resource Utilization Analysis]]`,
     `[[wiki/cloud-infra/resource-tagging|Resource Tagging]]`,
     `[[wiki/infrastructure/t-shirt-sizing-and-resource-models|T Shirt Sizing And Resource Models]]`,
     and `[[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]]` — all
     about compute *resources*, none about Kubernetes custom resources (CRDs).
   - `devops-infra/backup-strategies-3-2-1.md` links `[[wiki/devops-infra/cache-invalidation-strategies|Cache Invalidation Strategies]]`
     — a caching page on a backup page — plus `cloud-migration-strategies` and
     `progressive-sync-strategies` (matched the word "strategies").
   - `devops-infra/disaster-recovery-tiers.md` links `[[wiki/cloud-infra/azure-blob-access-tiers|Azure Blob Access Tiers]]`
     and `[[wiki/infrastructure/pulsar-architecture-and-tiers|Pulsar Architecture And Tiers]]`
     — storage/messaging tiers, not DR tiers (matched the word "tiers").
   - `devops-infra/policy-engines-opa-kyverno.md` links `[[wiki/os-shell/regex-engines|Regex Engines]]`.
   - `devops-infra/service-meshes-istio-linkerd.md` links `[[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]`.
   All are labeled with the template phrase `related coverage in the same cluster`, which
   182/220 files use. This reads as an automated linker matching basename keywords without
   semantic checks; it inflates link counts and misdirects navigation.

3. **Orphan "takeaway" bullets appended after the Details list — 16 dev-tools files.**
   Each file ends its Details list with a `- RSIS3 relevance:` bullet, then a blank line,
   then 1–3 additional bullets that belong to no heading and duplicate advice already in
   the list:
   - `dev-tools/log-levels.md`: `- Treat the level contract as part of the code review: wrong levels are caught in review, not in production.`
   - `dev-tools/token-bucket.md`: `- Expose the effective rate and burst in documentation so callers know what the limiter allows before they hit it.`
   - `dev-tools/property-testing-libraries.md` has three stray bullets, including
     `- Combine libraries with model-based testing: ...`
   - `dev-tools/runbook-automation.md` has two stray bullets.
   Others: `log-rotation`, `package-managers`, `printf-debugging`, `profiling-tools`,
   `request-tracing`, `semver-tooling`, `slo-budgets`, `slug-changes`, `status-pages`,
   `summary-quality`, `timeout-policy`, `verbose-flag`. This is a template artifact (the
   takeaway line was appended outside the list) and renders as orphan content between
   Details and Related.

4. **Summary-sentence duplication used to reach the word floor — 5 of 7 identity files.**
   The first Details bullet repeats the Summary's opening sentence verbatim or
   near-verbatim:
   - `identity/brute-force-protection.md`: Summary `Brute-force protection throttles repeated authentication attempts through rate limiting, delays, and lockouts so that guessing a password or secret becomes economically infeasible.` → Details bullet `Brute-force protection throttles repeated authentication attempts through rate limiting, delays, and lockouts.`
   - `identity/device-fingerprinting.md`: Summary `Device fingerprinting assembles browser, OS, screen, font, and network signals into a stable device identifier without cookies.` → Details bullet starts with the identical sentence.
   - `identity/email-verification.md`: identical sentence repeated as first bullet.
   - `identity/hardware-security-keys.md`: `Hardware security keys (FIDO2/CTAP2 devices such as YubiKeys ...` repeated as `Hardware security keys (FIDO2/CTAP2 devices like YubiKey) ...`.
   - `identity/account-recovery.md`: the NIST SP 800-63B sentence appears in Summary and again as the first Details bullet.
   This is textbook padding (defect class 3/4): ~25 words per file restated with no new
   information to push the body over 320 words. These five files sit at 434–456 words,
   roughly 120 of which is duplicated lead.

5. **Universal trailing boilerplate links — 124 files.**
   Every one of these files ends its Related list with the same two syntheses links and
   identical annotation text: `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb` and
   `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to`.
   The link pair adds no per-file information; on 64 files the entire Related block is
   exactly this 4-link boilerplate (`kubernetes-control-plane` + `observability-pillars` +
   the two syntheses). It makes every page's link graph look connected to the same 4 nodes
   regardless of topic.

## Minor & nits

1. `frontend-frameworks/derived-state.md`: `Selector libraries (Redux \`createSelector\`, Zustand selectors) move the same derivation into the store layer with memoization` — Zustand selectors do not memoize by default (no built-in `createSelector`; needs `useShallow` or middleware); *likely* conflation, minor.
2. `dev-tools/property-testing-libraries.md` links both `[[wiki/dev-tools/property-based-testing|Property-Based Testing]]` and `[[wiki/testing/property-based-testing|Property-Based Testing]]` with identical display text — a basename collision resolved ambiguously; one link is redundant.
3. Boilerplate drift: `identity/account-takeover.md` uses `For RSIS3:` while the other six identity files use `For mykb:` — same slot, two labels.
4. All 220 timestamps are exactly midnight UTC (`T00:00:00Z`) on three dates (07-31, 08-01, 08-02) — templated generation times, not capture times; graph tools cannot distinguish actual edits.
5. `identity/email-verification.md` links `[[wiki/security/ldap|LDAP]] — directory identities often key on email` — LDAP is tangential to email verification; reads as keyword-matched.
6. Illustrative numbers I cannot verify offline (not confirmed defects, flagged per instructions): `dev-tools/profiling-tools.md` "py-spy attach to a slow agent process shows 60% of time in tokenization"; `devops-infra/argocd-applicationsets.md` "`argocd appset list`" (CLI subcommand); `dev-tools/token-bucket.md` "AWS and many gateway rate limits model exactly this". All appear inside `Concrete example` framing, so I treat them as hypotheticals, not fabrication.
7. Repeated sentence template `the mature pattern is ...` closes the Tradeoffs bullet in nearly every dev-tools/devops-infra file; combined with dev-tools bodies clustering at 323–344 words, the files read as minimum-quota generated, though the content itself is accurate.

## Sample audit table

| File (components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| dev-tools/lockfiles.md | 326 | PASS | Accurate; related links topical. |
| dev-tools/log-levels.md | 324 | FAIL (minor) | Orphan takeaway bullet after Details. |
| dev-tools/log-rotation.md | 325 | FAIL (minor) | Orphan takeaway bullet. |
| dev-tools/mutation-testing.md | 344 | PASS | Stryker/PIT, equivalent mutants accurate. |
| dev-tools/package-managers.md | 323 | FAIL (minor) | Orphan takeaway bullet; content accurate. |
| dev-tools/printf-debugging.md | 327 | FAIL (minor) | Orphan takeaway bullet; checker "placeholder" flag is a false positive. |
| dev-tools/profiling-tools.md | 329 | FAIL (minor) | Orphan bullet; unverifiable 60% example. |
| dev-tools/property-testing-libraries.md | 344 | FAIL (major) | 3 orphan bullets; duplicate "Property-Based Testing" display links. |
| dev-tools/request-tracing.md | 338 | FAIL (minor) | Orphan bullet; W3C traceparent claim correct. |
| dev-tools/runbook-automation.md | 335 | FAIL (minor) | 2 orphan bullets. |
| dev-tools/semver-tooling.md | 333 | FAIL (minor) | Orphan bullet; semver claims correct. |
| dev-tools/slo-budgets.md | 330 | FAIL (minor) | Orphan bullet; 43 min/month math correct. |
| dev-tools/status-pages.md | 324 | FAIL (minor) | Orphan bullet. |
| dev-tools/summary-quality.md | 327 | FAIL (minor) | Orphan bullet. |
| dev-tools/tail-latency.md | 327 | PASS | Fan-out math correct; no stray bullet. |
| dev-tools/timeout-policy.md | 328 | FAIL (minor) | Orphan bullet. |
| dev-tools/token-bucket.md | 338 | FAIL (minor) | Orphan bullet; algorithm description accurate. |
| dev-tools/verbose-flag.md | 328 | FAIL (minor) | Orphan bullet. |
| devops-infra/argocd-applicationsets.md | 351 | PASS | Generators accurate; `argocd appset list` cannot verify offline. |
| devops-infra/backup-strategies-3-2-1.md | 431 | FAIL (major) | Keyword-matched links (cache-invalidation, migration, sync strategies). |
| devops-infra/caddy-and-traefik.md | 355 | PASS | Content accurate; example.com flag is a false positive. |
| devops-infra/container-storage-interfaces.md | 369 | PASS | CSI controller/node split accurate. |
| devops-infra/cosign-and-sigstore.md | 354 | FAIL (major) | Boilerplate-only Related; no link to image-signing-and-notary. |
| devops-infra/custom-resource-definitions.md | 399 | FAIL (major) | Keyword-matched "resource" links (resource utilization/tagging/sizing/cgroups). |
| devops-infra/disaster-recovery-tiers.md | 400 | FAIL (major) | Keyword-matched "tiers" links (Azure Blob, Pulsar). |
| devops-infra/envoy-data-plane.md | 388 | PASS | xDS/listener/cluster model accurate. |
| devops-infra/error-budgets.md | 366 | PASS | 99.9%/30d = 43 min correct. |
| devops-infra/haproxy-vs-nginx.md | 380 | PASS | Tradeoffs fair; health-check claims sound. |
| devops-infra/image-signing-and-notary.md | 422 | PASS | Notary/Notation framing reasonable; topical links present. |
| devops-infra/k8s-dns-and-coredns.md | 379 | PASS | ndots/search-domain claims correct. |
| devops-infra/operator-sdk-and-controller-runtime.md | 357 | FAIL (major) | Boilerplate-only Related; envtest claim correct. |
| devops-infra/policy-engines-opa-kyverno.md | 420 | FAIL (major) | regex-engines link irrelevant; Rego/Kyverno content accurate. |
| devops-infra/readiness-vs-liveness-revisited.md | 393 | FAIL (major) | Boilerplate-only Related; probe semantics accurate. |
| devops-infra/retry-policies.md | 408 | PASS | Backoff/jitter/idempotency guidance correct. |
| devops-infra/rto-and-rpo.md | 357 | FAIL (major) | Boilerplate-only Related; content correct. |
| devops-infra/sbom-and-syft.md | 366 | FAIL (major) | Boilerplate-only Related; Syft/Grype claims correct. |
| devops-infra/secret-stores-vault-consul.md | 426 | PASS | Vault/Consul distinction correct; topical links. |
| devops-infra/service-meshes-istio-linkerd.md | 419 | FAIL (minor) | Function-as-a-Service link irrelevant; mesh content accurate. |
| devops-infra/trivy-and-image-scanning.md | 402 | PASS | Trivy Operator/gate claims plausible. |
| frontend-frameworks/angular-signals.md | 464 | PASS | signal/computed/effect/input() claims accurate. |
| frontend-frameworks/concurrent-rendering.md | 502 | FAIL (critical) | Self-link in Related; scheduler model accurate. |
| frontend-frameworks/derived-state.md | 508 | FAIL (minor) | Zustand-selector memoization claim likely conflated. |
| frontend-frameworks/persisted-queries.md | 527 | PASS | APQ handshake and manifest model accurate. |
| frontend-frameworks/react-query-practice.md | 488 | PASS | staleTime/gcTime/invalidation claims accurate. |
| frontend-frameworks/reactivity-pitfalls.md | 527 | FAIL (critical) | Self-link in Related; toRefs/observer guidance accurate. |
| frontend-frameworks/redux-practice.md | 506 | PASS | Redux Toolkit/selector claims accurate. |
| frontend-frameworks/starttransition.md | 499 | FAIL (critical) | Self-link in Related. |
| frontend-frameworks/suspense-practice.md | 510 | FAIL (critical) | Self-link in Related. |
| frontend-frameworks/vue-composition-api.md | 503 | FAIL (critical) | Self-link in Related. |
| frontend-frameworks/vue-reactivity.md | 539 | FAIL (critical) | Self-link in Related. |
| identity/account-recovery.md | 451 | FAIL (major) | NIST sentence duplicated Summary→Details. |
| identity/account-takeover.md | 442 | PASS | Accurate; "For RSIS3:" label drift (nit). |
| identity/breach-notification.md | 446 | PASS | GDPR 72h/Art. 34 claims accurate. |
| identity/brute-force-protection.md | 434 | FAIL (major) | Summary sentence duplicated in Details. |
| identity/device-fingerprinting.md | 456 | FAIL (major) | Summary sentence duplicated in Details. |
| identity/email-verification.md | 452 | FAIL (major) | Summary sentence duplicated; LDAP link tangential. |
| identity/hardware-security-keys.md | 453 | FAIL (major) | Summary sentence duplicated near-verbatim. |

## Recommendations

1. **Fix the cluster-link generator, not the files one by one.** The self-links (6), the
   zero-topical Related blocks (14), and the keyword-matched irrelevant links all come
   from one automated "related coverage in the same cluster" step. Add a self-link guard,
   require ≥1 topical link per Related block (validated against the page's own tags), and
   drop keyword-only matches; then re-run `check_slice.py` plus a semantic spot-check on
   the wave.
2. **Remove the orphan takeaway bullets** (16 dev-tools files): merge the takeaway into
   the `Operational notes` bullet or delete it, and add a lint rule that the Details list
   ends immediately before `## Related` with no dangling bullets.
3. **De-duplicate the identity leads** (5 files): delete the Summary-sentence restatement
   from the first Details bullet and replace it with a genuinely new fact; then enforce
   a similarity check (Summary sentence vs. first Details bullet) in the promotion
   pipeline to stop padding-by-repetition.
4. **Trim the universal syntheses boilerplate**: link the two curation pages from a
   shared template/footer rather than from each article's Related list (124 files), so
   Related lists carry only topical neighbors and the graph stops being a star on 4 nodes.
5. **Re-run the checker with self-links as a hard gate** and add a "no `related coverage
   in the same cluster` label on a link to the page itself" rule; then re-audit the 64
   files whose Related block is exactly the 4-link boilerplate to give each a topical link.
