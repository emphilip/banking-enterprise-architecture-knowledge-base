---
title: Loyalty
type: capability
level: L1
capability-id: CLP-LOY
parent: Card-Linked Products (CLP)
tags: [capability, loyalty, affinity, partners, tiers, retail-banking, cards]
aliases: [CLP-LOY, Loyalty Capability]
---

# Loyalty (CLP-LOY)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Card-Linked Products (CLP)]]

The Loyalty capability group covers **programs, tiers, affinity/co-brand partnerships, and member management** for card-linked loyalty. For a card issuer it is the home of **affinity partnerships** (the co-brand and partner relationships that produce affinity cards), tiered status (standard / premium / elite), program definitions, and the partner-facing administration that sets these up and maintains them.

## L2 Capabilities

### CLP-LOY-01 — Multi-Tender

Loyalty that spans multiple tender types and programs.

### CLP-LOY-02 — Tiered Status

Status tiers and the benefits attached to each (standard vs. premium/World-tier vs. elite). Configured when a premium card product is built in [[Set Up Premium Card Product Flow]].

### CLP-LOY-03 — Programs

Definition and lifecycle of loyalty programs, including the benefit sets attached to a card program — see [[Manage Card Benefits Flow]].

### CLP-LOY-04 — Affinity

**Affinity partnerships:** the co-brand/partner relationships that underpin affinity card products. Create, suspend, and modify operations are handled by [[Manage Affinity Partnership Flow]].

### CLP-LOY-05 — Analytics

Loyalty program analytics and engagement reporting.

### CLP-LOY-06 — Partners

Partner onboarding, agreements, and partner administration for affinity and co-brand programs.

### CLP-LOY-07 — Member Mgmt.

Enrolment and lifecycle management of program members.

### CLP-LOY-08 — Engagement Metrics

Member engagement measurement feeding program tuning.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Manage Affinity Partnership Flow]] | CLP-LOY-04, 06 |
| [[Manage Card Benefits Flow]] | CLP-LOY-03 |
| [[Set Up Premium Card Product Flow]] | CLP-LOY-02, 04 |

## Related

[[Rewards]] · [[Cards]] · [[Manage Affinity Partnership Flow]] · [[Set Up Premium Card Product Flow]]
