---
type: "concept"
title: "Microsoft Entra ID"
description: "Microsoft's cloud identity and access management service (formerly Azure AD)"
tags: ["azure", "entra", "iam", "identity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/entra/identity/", "https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis"]
---

# Microsoft Entra ID

## Summary


## Details
- Azure Active Directory (now Microsoft Entra ID) is the identity and access service for Microsoft cloud: directory, authentication, and authorization in one platform.
- It provides single sign-on, MFA, conditional access policies, and app registrations that issue tokens for APIs.
- Conditional access evaluates signals (user, device, location, risk) to allow or block access, which is its core security differentiator.
- Governance features — access reviews, PIM, and audit logs — make it the administrative backbone of an Entra tenant.
- **Worked example / comparison** — Worked example — a conditional access policy requires a compliant device and MFA for wiki-administration roles while allowing basic read access from any registered device.
- For mykb, Entra ID is documented as the third leg of the cloud-identity cluster, alongside AWS IAM and GCP IAM.

## Related
- [[wiki/identity/identity-providers|Identity Providers]]
- [[wiki/identity/openid-connect|OpenID Connect]]
- [[wiki/identity/single-sign-on|Single Sign-On]]
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
