# Series 7: Operational / Functional Preferences

**x = 3 rounds · y = 2 open-ended per round · z = 3 choices per open-ended**

Defines deployment, runtime behavior, monitoring, and maintenance preferences informed by tech spec and methodology. This is the final series — you should have a complete specification picture when done.

Context from Series 5 & 6: tech=`{tech_stack}`, performance=`{performance_targets}`, integrations=`{integration_contracts}`, cadence=`{development_cadence}`, quality=`{quality_practices}`

---

## Round 1: Deployment and Delivery

### Open-Ended 7.1.1
**How should the system be deployed, released, and updated in production?**

Write freely. Describe the release process, frequency, and level of automation.

**After answering, choose one:**
- a) Manual deploy — push artifacts, restart services, update on schedule
- b) Automated CI/CD — merged to main triggers build + deploy pipeline
- c) Progressive delivery — feature flags, canary releases, gradual rollout

---

### Open-Ended 7.1.2
**What environment and release management strategy should be used?**

Write freely. Consider how code flows from development to production.

**After answering, choose one:**
- a) Single environment — production only, with local dev
- b) Dev / staging / production — standard promotion pipeline
- c) Ephemeral environments — per-branch previews, review apps

---

## Round 2: Runtime Behavior and Observability

### Open-Ended 7.2.1
**What logging, monitoring, alerting, and observability infrastructure is needed?**

Write freely. Define what must be measured and what triggers human attention.

**After answering, choose one:**
- a) Minimal — basic logging to stdout, manual check-ins
- b) Standard — structured logging, metrics dashboard, alert on errors
- c) Full observability — traces, logs, metrics; SLO monitoring; on-call rotation

---

### Open-Ended 7.2.2
**What configuration and feature management approach should be used at runtime?**

Write freely. Consider how settings change after deployment.

**After answering, choose one:**
- a) Static config — environment variables, restart to change
- b) Dynamic config — runtime-reloadable config without redeploy
- c) Feature flags + config — separate toggle system with gradual rollout

---

## Round 3: Maintenance and Evolution

### Open-Ended 7.3.1
**What maintenance schedule, upgrade policy, and lifecycle management is expected?**

Write freely. Describe how the system stays healthy over time.

**After answering, choose one:**
- a) Firefighting — fix issues as they arise, no scheduled maintenance
- b) Regular maintenance — scheduled patch cycles, dependency updates
- c) Proactive — automated updates, security scanning, continuous improvement

---

### Open-Ended 7.3.2
**What is the long-term stewardship plan? Who owns the system after initial delivery?**

Write freely. Define the hand-off, ownership, or governance model.

**After answering, choose one:**
- a) Hand-off — delivered to a separate operations team
- b) Build-and-run — the same team owns development and operations
- c) Community/open-source — external contributions, governance model
