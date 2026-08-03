# Adversarial Review #3 — Pass 2 (MyKB Stub Promotion Wave, 2026-08-03)

Slice: `slice3.txt` — 220 files (`dev-tools/`, `devops-infra/`, `frontend-frameworks/`, `identity/`)
Report: `ops/reports/adversarial-reviews/review-3-pass2.md`

## Verdict

**Score: 62 / 100**

The Pass 1 mechanical fixes **held** in this slice: 0 self-links, 0 occurrences of the
stripped annotation strings, 0 unclosed `[[raw/archive/…]]` links, 0 `README` links, 0
files below the 320-body-word floor, and the invariant checker's 6 flags are all false
positives (legitimate `example.com`/`todo-app`/printf content). The 6 factually-fixed
files (contrast-ratios, dom-clobbering, gpu-drivers-and-cuda, calibration, dp-vs-px,
anr-diagnostics) are **not in this slice**, so their corrections could not be re-read;
the syntheses `type` fix is likewise N/A (no syntheses files in slice).

What did **not** hold, and what was deliberately left in place, is where the score drops:
the "fixed syntheses trailer" was not removed — 124/220 files (56%) still end with the
two-link boilerplate ("how stubs grow into full articles in mykb" / "the curation loop
this stub belongs to"); 96 files append a keyword-matched, topically irrelevant
`Kubernetes Control Plane` link and 65 append `Observability Pillars`; the cleanup
**introduced** 14 orphaned trailing bullets in `dev-tools/` (a header was stripped,
leaving a floating practice bullet glued to `## Related` with no blank line); and the
Pass 1 defect classes left intentionally untouched are pervasive — 219/220 files carry a
speculative "RSIS3 relevance"/"For mykb" section that is often padding, at least 8
`frontend-frameworks` files make confidently false claims about the real dashboard's
stack (it is vanilla JS: Tailwind + Chart.js + `config.js`; it uses no React, `useMemo`,
Zustand, or selectors), and one confirmed near-duplicate pair
(`ephemeral-environments` / `preview-environments`, ~90% identical) survives with more
partial pairs adjacent.

## Critical findings

1. **Fabricated system claims: `frontend-frameworks` files assert the dashboard is built
   on the very library each article describes.** Verified against
   `components/rsis3/dashboard/index.html` (Tailwind CDN, Chart.js 4, `config.js`, no
   React anywhere) and `components/rsis3/dashboard/config.js` (reads
   `rack/pulses/dashboard-data.json`).
   - `frontend-frameworks/use-memo.md`: "the dashboard's derived telemetry (aggregates
     over pulses) is exactly what `useMemo`-style caching protects"
   - `frontend-frameworks/memoization-practice.md`: "memoized selectors are how the
     dashboard derives graph stats and loop success rates from raw telemetry"
   - `frontend-frameworks/zustand-practice.md`: "the dashboard's shared UI state (active
     view, filters, daemon status) is a natural Zustand store"
   - `frontend-frameworks/react-query-practice.md`: "MyKB's dashboard is the textbook
     workload: search results, article lookups, and graph nodes keyed by query … TanStack
     Query's cache-and-invalidate model would replace the ad-hoc fetch state"
   - `frontend-frameworks/selector-libraries.md`: "the dashboard's telemetry views are the
     selector use case: memoized slices (success rate per loop, pulse counts per window)"
   - Same pattern in `frontend-frameworks/selectors-practice.md` and
     `frontend-frameworks/jotai-practice.md`; `frontend-frameworks/xstate-practice.md`
     adds the bolder "XState is the reference implementation of RSIS3's own loop
     semantics" (RSIS3 is a Python engine; nothing in the repo implements it in
     XState).
   Why wrong: the dashboard is a static vanilla-JS page; none of these libraries exist in
   it, so each claim misstates the knowledge base's own system — exactly the fabrication
   cost the review is meant to catch. Fix: rewrite as hypotheticals ("if the dashboard
   moved to React…") or delete; never state the system's stack as fact without checking
   it.

2. **Keyword-matched irrelevant links, mass-appended as a boilerplate trailer.**
   96/220 files link `[[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control
   Plane]]` and 65/220 link `[[wiki/devops-infra/observability-pillars|Observability
   Pillars]]`; 64 files carry the full 4-link trailer (KCP + Obs + 2 syntheses). The
   targets exist but are topically wrong for most sources:
   - `devops-infra/cosign-and-sigstore.md` (artifact signing) → "Kubernetes Control
     Plane" (kube-apiserver/scheduler/etcd)
   - `devops-infra/haproxy-vs-nginx.md` (L4/L7 proxy choice) → "Kubernetes Control Plane"
   - `devops-infra/runbooks-and-playbooks.md` (incident procedures) → "Kubernetes Control
     Plane"
   - `devops-infra/release-engineering-trains.md` → "Traffic Engineering" (network
     capacity routing) and "Chaos Engineering" — both matched on the keyword "engineering"
   - `devops-infra/ephemeral-environments.md` → "Shell Environments & RC Files" — matched
     on the keyword "environments"
   - `devops-infra/zero-trust-access-proxies.md` → "Zero-Downtime Deploys" — matched on
     the keyword "zero"
   These inflate the link counts of nearly every file and poison cross-navigation. Fix:
   bulk-remove the KCP/Obs trailer and re-link topically or not at all.

3. **The "fixed syntheses trailer" was not removed — 124/220 files (56%).** The cleanup
   claimed it "removed the fixed syntheses trailer", but in this slice the identical
   trailer survives, e.g. `devops-infra/canary-and-blue-green-revisited.md`:
   - `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] —
     how stubs grow into full articles in mykb`
   - `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation &
     Practices]] — the curation loop this stub belongs to`
   This is the same class of annotation boilerplate as the strings that were stripped,
   and it is identical across 124 files. Fix: strip these two bullets (and their
   annotations) from every file, as was done for the other annotation strings.

## Major findings

4. **Cleanup regression: 14 `dev-tools` files have orphaned trailing bullets.** A header
   was evidently stripped during annotation removal (or a top-up was inserted), leaving a
   lone bullet floating between the RSIS3 bullet and `## Related` with no blank line and
   no heading. Affected: `log-levels`, `log-rotation`, `package-managers`,
   `printf-debugging`, `profiling-tools`, `request-tracing`, `semver-tooling`,
   `slo-budgets`, `slug-changes`, `status-pages`, `summary-quality`, `timeout-policy`,
   `token-bucket`, `verbose-flag`. Evidence (`dev-tools/token-bucket.md`):
   > - RSIS3 relevance: a token bucket per tool class keeps agent bursts inside provider limits …
   >
   > - Expose the effective rate and burst in documentation so callers know what the limiter allows before they hit it.
   > ## Related
   Same shape in `dev-tools/summary-quality.md` ("Rewrite the summary from the finished
   Details…") and `dev-tools/package-managers.md` ("Prefer the package manager's own
   update flow over manual edits…"). Fix: re-attach these bullets under a real heading
   (e.g. a "Practice" subsection) or fold them into Operational notes.

5. **Confirmed near-duplicate pair: `ephemeral-environments.md` vs
   `preview-environments.md`.** A direct diff shows only the title, description, one
   example ID (`pr-123` vs `pr-42`), one added failure mode, and a few synonym swaps;
   the Mechanism/Concrete example/Tradeoffs/RSIS3 bullets are otherwise identical and
   both carry the same KCP + syntheses trailer. Two files describing the same concept
   with the same body is duplication, not coverage. The pair cross-links each other,
   which masks the duplication.

6. **Relevance-section padding signature: 219/220 files (99.5%) end with an
   "RSIS3 relevance"/"RSIS3/mykb relevance"/"For mykb" bullet, and many are content-free
   or unverifiable.** Examples: `dev-tools/semver-tooling.md` — "wiki article status
   (stub vs growing) is a semver-like signal — the same derived, verifiable progression
   discipline"; `dev-tools/slo-budgets.md` — "treat wiki-link breakage as budget spend on
   the knowledge SLO — the same numeric discipline for the wiki's reliability";
   `devops-infra/error-budgets.md` — "RSIS3's own loops have reliability targets — an
   error budget for pulse collection or dashboard generation tells the meta-loops when to
   stop shipping new behavior". None of these are grounded in any observable system
   behavior; several contradict it (see finding 1). The `dev-tools` body-word counts
   cluster 323–344, just above the 320 floor (`package-managers` 323, `lockfiles` 326,
   `printf-debugging` 327, `summary-quality` 327), consistent with padding-to-threshold
   via these bullets.

7. **`release-engineering-trains.md` contradicts its own frontmatter.** Description:
   "Fixed-cadence release trains that batch changes predictably"; body: "Release
   engineering turns software delivery into a repeatable process: versioning, changelogs,
   build reproducibility, artifact signing, promotion, and rollback…" — the body never
   discusses trains, while `release-trains.md` (in the same slice) covers the actual
   topic. Frontmatter/body mismatch plus a second overlapping article; 3 of 6 Related
   links are keyword-matched "engineering" links (Chaos, SRE, Traffic).

8. **`runbooks.md` / `runbooks-and-playbooks.md` partial duplicate.** Both are
   "step-by-step operational procedures for known incidents" with overlapping
   Summary/Details (rot, vague steps, game days). `runbooks-and-playbooks.md` adds the
   KCP + Obs + syntheses trailer and a `[[wiki/devops-infra/kubernetes-control-plane|Kubernetes
   Control Plane]]` link; `runbooks.md` has genuinely topical links (incident-response,
   on-call-rotations, escalation-policies). One should be merged into the other.

## Minor & nits

9. `devops-infra/haproxy-vs-nginx.md`: "config is text-based and reloadable without
   dropping connections (exclusive mode)" — "exclusive mode" is not standard HAProxy
   terminology (cannot verify; likely invented). HAProxy's seamless reload uses socket
   transfer/SO_REUSEPORT, not an "exclusive mode".
10. `identity/breach-notification.md`: "state laws such as the California Consumer
    Privacy Act … impose similar duties with varying timelines and thresholds" — CCPA's
    breach duty is a private right of action for unencrypted personal information
    (Civil Code 1798.150), not a notification statute with timelines; California's
    notification rule lives in Civil Code 1798.82. Misleading framing of a real regime.
11. `use-memo.md` and `use-callback.md` share 6 of 7 Related links and near-identical
    RSIS3/mykb relevance claims ("derived metric re-runs because its input function
    reference changed") — acceptable topical overlap, but the duplicated Related lists
    and identical system claims read as batch boilerplate.
12. Seven "revisited" files in the slice (`canary-and-blue-green-revisited`,
    `devcontainers-revisited`, `feature-flag-systems-revisited`,
    `kubernetes-operators-revisited`, `patch-management-revisited`,
    `readiness-vs-liveness-revisited`, `zero-trust-networking-revisited`) duplicate
    existing articles across namespaces (e.g. the pair links
    `infrastructure/canary-deployments` and `infrastructure/blue-green-deployments`);
    the "revisited" suffix hides the duplication.
13. `dev-tools/printf-debugging.md`: checker flag on "insert prints at function entry" is
    a false positive (legitimate mechanism text); but the RSIS3 bullet ("when a generated
    article looks wrong, printf the template variables") states agent behavior that
    cannot be verified.
14. `identity/hardware-security-keys.md`, `identity/account-recovery.md`,
    `identity/device-fingerprinting.md`: on-topic content is accurate (WebAuthn origin
    binding, NIST recovery-as-auth, fingerprint-as-risk-signal); the "For mykb:" bullets
    ("hardware keys should be mandatory for admin and agent-owner identities") are
    unverifiable policy claims, not recorded facts.
15. `devops-infra/zero-trust-networking-revisited.md` → "Multicast Networking" link is
    keyword-matched ("networking") and topically irrelevant to zero-trust access.
16. `devops-infra/canary-and-blue-green-revisited.md`: content (Argo Rollouts, Flagger +
    Prometheus canary analysis) is correct, but 4 of 6 Related links are the boilerplate
    trailer (KCP + Obs + 2 syntheses).

## Sample audit table

| File | Words | Verdict | Notes |
|---|---|---|---|
| dev-tools/printf-debugging.md | 327 | OK-with-nits | Checker flag false positive; unverifiable RSIS3 bullet |
| dev-tools/lockfiles.md | 326 | OK-with-nits | Sound; 326w just above floor; "the wiki's generated JSON indexes" unverifiable |
| dev-tools/mutation-testing.md | 344 | OK | Accurate; related links topical |
| dev-tools/property-based-testing.md | 344 | OK | Accurate; 6 topical links |
| dev-tools/token-bucket.md | 338 | FAIL | Orphaned trailing bullet; RSIS3 bullet speculative |
| dev-tools/slo-budgets.md | 330 | FAIL | Orphaned trailing bullet; fabricated "knowledge SLO" claim |
| dev-tools/semver-tooling.md | 333 | FAIL | Orphaned trailing bullet; "stub vs growing is semver-like" padding |
| dev-tools/package-managers.md | 323 | FAIL | Orphaned trailing bullet; 323w = floor-adjacent padding |
| dev-tools/summary-quality.md | 327 | FAIL | Orphaned trailing bullet; "wiki's" unverifiable claim |
| devops-infra/release-trains.md | 340 | OK | Correct on-topic article; good links |
| devops-infra/release-engineering-trains.md | 329 | FAIL | Description contradicts body; 3 keyword-matched "engineering" links; syntheses trailer |
| devops-infra/runbooks.md | 342 | OK | Good topical links; no trailer |
| devops-infra/runbooks-and-playbooks.md | 347 | FAIL | Near-duplicate of runbooks.md; KCP + Obs + syntheses trailer |
| devops-infra/compression-and-brotli.md | 356 | FAIL | Correct content; KCP link irrelevant; syntheses trailer |
| devops-infra/cosign-and-sigstore.md | 340 | FAIL | Correct content; KCP + Obs + syntheses trailer (all irrelevant) |
| devops-infra/haproxy-vs-nginx.md | 352 | FAIL | "exclusive mode" unverifiable term; KCP link irrelevant; trailer |
| devops-infra/canary-and-blue-green-revisited.md | 358 | FAIL | Content correct; 4/6 links are boilerplate trailer |
| devops-infra/ephemeral-environments.md | 343 | FAIL | Near-duplicate of preview-environments; Shell-Env link keyword-matched; trailer |
| devops-infra/preview-environments.md | 349 | FAIL | Near-duplicate of ephemeral-environments; trailer |
| devops-infra/error-budgets.md | 366 | OK-with-nits | 43-min figure correct; RSIS3 bullet speculative |
| devops-infra/zero-trust-access-proxies.md | 350 | FAIL | "Zero-Downtime Deploys" keyword link; KCP link; unverifiable RSIS3 claim |
| devops-infra/zero-trust-networking-revisited.md | 349 | FAIL | Multicast link keyword-matched; overlaps access-proxies article |
| frontend-frameworks/use-memo.md | 435 | FAIL | Fabricated "dashboard uses useMemo" claim; dup Related w/ use-callback |
| frontend-frameworks/use-callback.md | 421 | FAIL | Fabricated "dashboard" claim; dup Related w/ use-memo |
| frontend-frameworks/zustand-practice.md | 447 | FAIL | Fabricated "dashboard is a natural Zustand store" claim |
| frontend-frameworks/memoization-practice.md | 454 | FAIL | Fabricated "memoized selectors are how the dashboard derives graph stats" claim |
| frontend-frameworks/xstate-practice.md | 482 | FAIL | Fabricated "XState is the reference implementation of RSIS3's own loop semantics" claim |
| frontend-frameworks/react-query-practice.md | 439 | FAIL | Fabricated "MyKB's dashboard is the textbook workload" claim |
| frontend-frameworks/selector-libraries.md | 477 | FAIL | Fabricated "dashboard's telemetry views are the selector use case" claim |
| frontend-frameworks/jotai-practice.md | 471 | FAIL | Fabricated "dashboard's filter, search, and selection state fits this model" claim |
| identity/account-recovery.md | 451 | OK | NIST 800-63B framing accurate; "For mykb" unverifiable |
| identity/breach-notification.md | 446 | OK-with-nits | GDPR 72h correct; CCPA framed as notification law (minor error) |
| identity/hardware-security-keys.md | 453 | OK | Accurate (origin binding, AAL3); "For mykb" policy claim unverifiable |
| identity/device-fingerprinting.md | 456 | OK | Accurate; topical links; "For mykb" claim unverifiable |

## Recommendations (top 5)

1. **Strip the syntheses trailer and KCP/Obs boilerplate links** (124 + 96 + 65 files).
   Remove the two syntheses bullets and the keyword-matched `Kubernetes Control Plane` /
   `Observability Pillars` links where the source is not about k8s/observability; keep
   topically justified links only. This is a scriptable, mechanical fix.
2. **Correct or delete the fabricated dashboard-stack claims** in `frontend-frameworks/`
   (at least use-memo, use-callback, memoization-practice, zustand-practice,
   react-query-practice, selector-libraries, selectors-practice, jotai-practice).
   The dashboard is vanilla JS; rewrite the relevance bullets as explicit hypotheticals
   or remove them.
3. **Repair the 14 orphaned trailing bullets** in `dev-tools/` — restore a heading
   (e.g. `## Practice`) or fold each bullet into Operational notes so nothing floats
   unheaded above `## Related`.
4. **Merge confirmed near-duplicates**: fold `preview-environments` into
   `ephemeral-environments` (or delete one); merge `runbooks-and-playbooks` into
   `runbooks`; resolve the `release-engineering-trains` frontmatter/body mismatch and its
   overlap with `release-trains`; audit the 7 "revisited" files against their originals
   (cross-namespace duplicates).
5. **Re-audit the relevance sections against the 320-word floor.** With 219/220 files
   carrying a speculative relevance bullet and `dev-tools` files clustered at 323–344
   words, require each relevance bullet to be verifiable or delete it, then re-measure
   body words — and treat any file that drops below 320 after removal as failing, rather
   than topping up with new boilerplate.

### Pass 2 verification summary (this slice)

- Checker: 214/220 clean; 6 flagged — all false positives (verified by reading).
- Pass 1 fixes held: self-links 0, annotation strings 0, unclosed raw/archive links 0,
  README links 0, files < 320 words 0. ✔
- Pass 1 fixes NOT verified: 6 factual-fix files and syntheses `type` fix are outside
  this slice (N/A here).
- Cleanup regressions introduced: 14 orphaned trailing bullets (dev-tools).
- Deliberately-unfixed classes still present: syntheses trailer 124 files, KCP link 96,
  Obs-Pillars link 65, relevance-section padding 219, fabricated dashboard claims 8,
  near-duplicates ≥4 pairs, unverifiable "the wiki's…" claims 8 files.
