---
title: Offers
type: capability
level: L1
capability-id: CEN-OFR
parent: Customer Engagement (CEN)
tags: [capability, offers, offer-engine, presentment, cross-sell, retail-banking]
aliases: [CEN-OFR, Offers Capability, Offer Management]
---

# Offers (CEN-OFR)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Customer Engagement (CEN)]]

The Offers capability group covers how the bank **defines, manages, generates, and presents** offers to customers and prospects — across pricing offers (e.g., promotional balance-transfer rates), value-add offers (credit-limit increases, credit alerts, product changes), insurance offers, and rewards offers. It owns the **offer engine** that determines eligibility and availability, the **offer management** repository that holds offer definitions and dispositions, and the cross-channel **presentment** of offers through online, phone, IVR, direct-mail, and statement channels.

## L2 Capabilities

### CEN-OFR-01 — Offer Mgmt.

The repository and lifecycle of offer definitions and customer-level dispositions.

- Holds the catalogue of available offers (pricing, value-add, insurance, rewards) and their eligibility, content, and disclosure linkage.
- Records each customer's **offer disposition** (presented, accepted, declined, "maybe") and updates **offer history** so the same offer is not re-presented inappropriately.
- Underpins the add/remove/modify operations on [[Pricing Offer Presentment Flow]], [[Value-Add Offer Presentment Flow]], and [[Insurance Offer Presentment Flow]].

### CEN-OFR-02 — Offer Engine

Real-time determination of which offers a given customer is eligible for.

- Evaluates account entitlements and offer eligibility (often via a business rules engine) and returns the set of available offers and cross-sell offers, ranked for presentment.
- Drives the [[Online Campaign Flow]] and the available-offers lookup in the phone-channel presentment flows.

### CEN-OFR-03 — Promo Offer Generation

Generating promotional and acquisition offers, including the **source codes** that bind an offer to a product instance, pricing, channel, and reward.

- Realized by [[Manage Source Code Flow]] and the promotional content published through [[Content Management CPCMS Flow]].

### CEN-OFR-04 — Intro Offers

Introductory and acquisition offers presented to prospects and new customers (e.g., intro APR, welcome rewards). Exercised by [[Phone Campaign New Customer Flow]].

### CEN-OFR-05 — Wallet Offers

Wallet- and network-linked offers (MasterPass / digital-wallet class offers).

### CEN-OFR-06 — Offer Analytics

Measuring offer take-up, disposition, and channel effectiveness; feeds segmentation and campaign tuning.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Pricing Offer Presentment Flow]] | CEN-OFR-01 |
| [[Value-Add Offer Presentment Flow]] | CEN-OFR-01 |
| [[Insurance Offer Presentment Flow]] | CEN-OFR-01 |
| [[Online Campaign Flow]] | CEN-OFR-01, 02 |
| [[Phone Campaign Existing Customer Flow]] | CEN-OFR-01, 02 |
| [[Phone Campaign New Customer Flow]] | CEN-OFR-04 |
| [[Manage Source Code Flow]] | CEN-OFR-03 |
| [[Value-Add Offers Flow]] | CEN-OFR-01 |
| [[Apply List to Offers Flow]] | CEN-OFR-01 |

## Related

[[Content Management]] · [[Contact Management]] · [[Marketing and Sales]] · [[Rewards]] · [[Servicing - Monetary]]
