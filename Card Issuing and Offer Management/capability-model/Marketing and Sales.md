---
title: Marketing and Sales
type: capability
level: L1
capability-id: MKS-MKT, MKS-CRM
parent: Marketing & Sales (MKS)
tags: [capability, marketing, sales, campaign, crm, lead-gen, retail-banking]
aliases: [MKS, Marketing and Sales Capability, Marketing Strategy, CRM]
---

# Marketing & Sales (MKS)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Marketing & Sales (MKS)]] — this note covers the two L1 groups this library exercises: **Marketing Strategy (`MKS-MKT`)** and **CRM (`MKS-CRM`)**.

The Marketing & Sales domain owns **campaign strategy, segmentation, lead/prospect management, and the sales/CRM motion** that converts marketing into booked product. For a card issuer it is where acquisition and cross-sell campaigns are defined (offer-marketing criteria, channel-specific criteria, target segments), where prospect lists originate, and where the sales pipeline and cross/upsell motions are managed.

## L2 Capabilities — Marketing Strategy (MKS-MKT)

### MKS-MKT-01 — Brand Mgmt.

Brand standards and creative governance applied to campaign content.

### MKS-MKT-02 — Campaign Mgmt.

Defining and running marketing campaigns: setting **offer-marketing criteria** and **channel-specific criteria**, enriching the target population, and dispatching to channels. The backbone of [[Direct Marketing Campaign Flow]] and the campaign initiation behind [[Publish Rewards Flow]] and [[Content Management CPCMS Flow]].

### MKS-MKT-03 — Segment Mgmt.

Building and maintaining customer/prospect segments and the lists derived from them — see [[Apply List to Offers Flow]] (list creation and scrubbing).

### MKS-MKT-04 — Lead / Prospect

Sourcing and managing prospects for acquisition campaigns — the prospect list that drives [[Phone Campaign New Customer Flow]] and the acquisition offers built in [[Manage Source Code Flow]].

## L2 Capabilities — CRM (MKS-CRM)

### MKS-CRM-01 — Sales Mgmt.

Managing the sales motion across channels.

### MKS-CRM-02 — Sales Tracking

Tracking sales outcomes and attribution back to campaigns and source codes.

### MKS-CRM-03 — Cross / Upsell

Cross-sell and upsell of additional products to existing customers — the commercial intent behind value-add and insurance offer presentment ([[Value-Add Offer Presentment Flow]], [[Phone Campaign Existing Customer Flow]]).

### MKS-CRM-04 — Sales Pipeline

Pipeline management for in-progress sales.

### MKS-CRM-05 — Referrals

Referral programs and partner referrals.

### MKS-CRM-06 — Lead Gen.

Generating qualified leads for acquisition — exercised by [[Phone Campaign New Customer Flow]] and acquisition-offer source codes.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Direct Marketing Campaign Flow]] | MKS-MKT-02 |
| [[Apply List to Offers Flow]] | MKS-MKT-03 |
| [[Publish Rewards Flow]] | MKS-MKT-02 |
| [[Phone Campaign New Customer Flow]] | MKS-MKT-04, MKS-CRM-06 |
| [[Phone Campaign Existing Customer Flow]] | MKS-CRM-03 |
| [[Manage Source Code Flow]] | MKS-MKT-04, MKS-CRM-06 |
| [[Value-Add Offer Presentment Flow]] | MKS-CRM-03 |

## Related

[[Offers]] · [[Contact Management]] · [[Cards]] · [[Canadian Regulatory Context]]
