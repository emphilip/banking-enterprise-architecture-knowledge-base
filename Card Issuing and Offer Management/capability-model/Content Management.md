---
title: Content Management
type: capability
level: L1
capability-id: CEN-CNT
parent: Customer Engagement (CEN)
tags: [capability, content-management, cms, disclosures, publishing, retail-banking]
aliases: [CEN-CNT, Content Management Capability, CMS]
---

# Content Management (CEN-CNT)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Customer Engagement (CEN)]]

The Content Management capability group covers how the bank **authors, versions, reviews, publishes, and retires** customer-facing content across its digital and assisted channels — marketing banners, offer cards, product descriptions, rewards content, disclosures, calculators, and knowledge articles. For a card issuer it is the engine behind both the **public (sales/acquisition) site** and the **secure (authenticated) site**, and the source of truth for the legal and product text that fulfilment and offer presentment reuse.

## L2 Capabilities

### CEN-CNT-01 — Define / Publish

Authoring and publishing content through a managed workflow.

- **Editor → Publisher separation of duties:** a content *editor* drafts and submits; a content *publisher* reviews, performs final QA, confirms legal approvals, and releases to the live channel. The two roles are distinct logins with distinct permissions.
- **Channel/zone targeting:** content is placed into channel-specific zones (web, POS/branch portal, referral, retail-front) and onto specific surfaces (offers tab, rewards tab, account screens, banners, splash screens).
- **Publish now or schedule:** approved content can go live immediately or be scheduled for a future date.
- Exercised end-to-end by [[Create and Update Content Management Flow]], [[Content Management CPCMS Flow]], and [[Content Management Site Refresh Flow]].

### CEN-CNT-02 — Version History

Maintaining an auditable history of content changes.

- Submitted layouts and approved content are stored with the editor/publisher, timestamp, and sign-off retained for audit.
- Hard and soft copies of published applications/screens are archived for audit purposes (a control surfaced explicitly in the public-site publish flow).

### CEN-CNT-03 — Search

Locating content for edit or reuse by content type, campaign, zone, or source code.

### CEN-CNT-04 — FAQ

Managing frequently-asked-question and help content surfaced in self-serve channels.

### CEN-CNT-05 — Tools / Calc

Managing interactive tools and calculators (e.g., interest, balance-transfer, and rewards calculators) and the variable content that drives them.

### CEN-CNT-06 — Knowledge Base

Curating the structured knowledge articles consumed by agents and self-serve customers.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Create and Update Content Management Flow]] | CEN-CNT-01, 02 |
| [[Content Management CPCMS Flow]] | CEN-CNT-01, 02, 03 |
| [[Content Management Site Refresh Flow]] | CEN-CNT-01, 02 |
| [[Disclosure Management Flow]] | CEN-CNT-01, 02 |
| [[Value-Add Offers Flow]] | CEN-CNT-01 |

## Related

[[Offers]] · [[Contact Management]] · [[Disclosure Management Flow]] · [[Canadian Regulatory Context]] · [[Systems and Integration Reference]]
