---
title: Identity, Auth & Access
type: capability-model
level: L0
capability-id: IAA
domain: banking-and-payments
tags: [capability-model, L0, identity-auth-access]
aliases: [IAA, Identity, Auth & Access]
---

# Identity, Auth & Access (IAA)

**Parent:** [[00 - Master Capability Model]]

Identity, Auth & Access governs who a user is, how they prove it, and what they are permitted to do. It underpins every authenticated channel and origination flow and is the primary control point against account takeover and identity fraud, working closely with [[FRR Fraud & Risk|Fraud & Risk]].

## L1 Capability Groups

| ID | Capability Group | L2s | Summary |
|---|---|---|---|
| IAA-IDM | [[IAA-IDM Identity Management\|Identity Management]] | 6 | Identity Management establishes and maintains digital identities, their attributes, roles, and lifecycle across the bank |
| IAA-ATH | [[IAA-ATH Authentication\|Authentication]] | 6 | Authentication verifies that a returning user is who they claim to be at the point of access |
| IAA-AUZ | [[IAA-AUZ Authorization\|Authorization]] | 6 | Authorization decides what an authenticated user may do and enforces step-up controls for sensitive actions |
| IAA-IDF | [[IAA-IDF Identity Fraud\|Identity Fraud]] | 4 | Identity Fraud detects and prevents impersonation and fraudulent enrolment, and captures consent during onboarding |

## Related

[[00 - Master Capability Model]]
