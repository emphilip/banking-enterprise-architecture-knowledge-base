---
title: Card Issuing & Offer Management — Knowledge Library Index
type: index
domain: banking-and-payments
capability-l0: [Customer Engagement, Card-Linked Products, Products & LOB, Marketing & Sales, Servicing]
tags: [cards, content-management, rewards, offers, product-setup, capability-model, index, retail-banking, canada]
aliases: [Card Issuing Index, Offer Management Index, Cards Library Index]
---

# Card Issuing & Offer Management — Knowledge Library

This library documents the **content, rewards, product-setup, and offer-management** processes of a generic Canadian retail bank's **credit-card issuing business**, paired with **generalized process flows** and mapped to the **master capability model** ([[Generic Multi-Functional Bank Capability Model|slide 4]]). It is structured for use as a queryable knowledge base: every capability has a stable ID, every process flow is mapped to the L2 capabilities it exercises, and the vendor/brand abstractions are recorded in dedicated reference notes.

**Scope.** Three process pillars from the source program — **Content Management**, **Product Setup**, and **Sales / Value-Add / Offer Management** — exercised across five L0 domains of the master model: Customer Engagement, Card-Linked Products, Products & LOB, Marketing & Sales, and Servicing.

**Provenance.** Process flows are generalized from a real Canadian card-issuer integration program (the "MBNA Day 1 / BAT-SIT" workshop process flows). Vendor and brand specifics — the card processing platform, loyalty platform, offer/order management system, workflow/BPM platform, content and disclosure systems, and the bank's own brand — have been abstracted to generic roles so the content applies to the average Canadian retail bank. See [[Systems and Integration Reference]] for the role mapping. The source material was DRAFT workshop content.

---

## 1. Capability Model

Mapped to the L1 capability groups of the [[Generic Multi-Functional Bank Capability Model]] (slide 4 of the Banking & Payments Accelerator):

| L1 Capability | ID | L0 Domain |
|---|---|---|
| [[Content Management]] | CEN-CNT | Customer Engagement |
| [[Offers]] | CEN-OFR | Customer Engagement |
| [[Contact Management]] | CEN-CON | Customer Engagement |
| [[Rewards]] | CLP-RWD | Card-Linked Products |
| [[Loyalty]] | CLP-LOY | Card-Linked Products |
| [[Cards]] | PLB-CRD | Products & LOB |
| [[Insurance]] | PLB-INS | Products & LOB |
| [[Marketing and Sales]] | MKS-MKT · MKS-CRM | Marketing & Sales |
| [[Servicing - Monetary]] | SVC-MON | Servicing |

Overview note: [[Generic Multi-Functional Bank Capability Model]]

## 2. Process Flows

26 generalized flows, grouped by source pillar. Full L2 traceability in the [[Process-to-Capability Mapping Matrix]].

### Content Management

| Process Flow | Channel | Primary Capabilities |
|---|---|---|
| [[Create and Update Content Management Flow]] | Secure site | CEN-CNT, CEN-OFR, CLP-RWD |
| [[Value-Add Offers Flow]] | Secure site | CEN-OFR, PLB-INS |
| [[Content Management CPCMS Flow]] | Public site | CEN-CNT, CEN-OFR, MKS, SVC-MON |
| [[Disclosure Management Flow]] | Public site | CEN-CNT, ONB-CCC |
| [[Content Management Site Refresh Flow]] | Public site | CEN-CNT |

### Rewards

| Process Flow | Channel | Primary Capabilities |
|---|---|---|
| [[Publish Rewards Flow]] | Omni-channel | CLP-RWD, MKS, CEN-CON |
| [[Create Reward Flow]] | Back office | CLP-RWD, PLB-CRD |

### Product Setup

| Process Flow | Channel | Primary Capabilities |
|---|---|---|
| [[Manage Affinity Partnership Flow]] | Back office | CLP-LOY, PLB-CRD |
| [[Manage Card Benefits Flow]] | Back office | PLB-CRD, CLP-LOY |
| [[Set Up Premium Card Product Flow]] | Back office | PLB-CRD, CLP-LOY, CLP-RWD |
| [[Manage Insurance Product Setup Flow]] | Back office | PLB-INS, CEN-OFR |
| [[Submit Options Maintenance Request Flow]] | Back office | OPS-WFR, ENT-BOR, PLB-CRD |
| [[Operator Security Administration Flow]] | Back office | IAA-IDM, IAA-AUTHZ |
| [[Manage Pricing Flow]] | Back office | SVC-MON, PLB-CRD |
| [[Manage Product Instance Flow]] | Back office | PLB-CRD, CLP-LOY, CLP-RWD |

### Sales / Value-Add / Offer Management

| Process Flow | Channel | Primary Capabilities |
|---|---|---|
| [[Manage Source Code Flow]] | Back office | CEN-OFR, MKS |
| [[Direct Marketing Campaign Flow]] | Omni-channel | MKS, CEN-OFR, CEN-CON |
| [[Online Campaign Flow]] | Online | CEN-OFR, CEN-CON |
| [[Phone Campaign Existing Customer Flow]] | Phone | CEN-OFR, MKS, CEN-CON |
| [[Phone Campaign New Customer Flow]] | Phone | MKS, CEN-OFR, ONB-APP, ONB-ADJ |
| [[Pricing Offer Presentment Flow]] | Phone | CEN-OFR, SVC-MON, PLB-CRD |
| [[Value-Add Offer Presentment Flow]] | Phone | CEN-OFR, SVC-MON, MKS |
| [[Insurance Offer Presentment Flow]] | Phone | CEN-OFR, PLB-INS |
| [[Apply List to Offers Flow]] | Omni-channel | MKS, CEN-CON, CEN-OFR |
| [[Add Insurance Product Phone Channel Flow]] | Phone | PLB-INS, CEN-OFR |
| [[Phone Channel Outbound Flow]] | Phone | CEN-CON, CEN-OFR, MKS |

## 3. Reference

- [[Process-to-Capability Mapping Matrix]] — full traceability of flows to L2 capabilities
- [[Systems and Integration Reference]] — generic system roles and the source→generic genericisation mapping
- [[Glossary]] — terminology used across the library
- [[Canadian Regulatory Context]] — cost-of-borrowing disclosure, CASL consent, creditor insurance, privacy, bilingual obligations

---

## Identifier Conventions

- **Capability IDs** — `<L0>-<L1>-nn`, e.g., `CEN-OFR-01` (Customer Engagement → Offers → Offer Mgmt.). L0/L1 codes are defined in [[Generic Multi-Functional Bank Capability Model]].
- **Step IDs** — each flow uses a flow-local prefix on `Step XX-nn` headings (e.g., `CPM-`, `BEN-A`, `POP-`, `OMR-`), addressable as `[[Flow Name#Step XX-nn — Title]]`. Every step section carries a context line stating its capability, actor, preconditions, inputs, and exits so it can be reasoned about in isolation.

## How to Query This Library

- **"How is public-site campaign content published?"** → [[Content Management CPCMS Flow]]
- **"How does a customer enrol in balance protection online?"** → [[Value-Add Offers Flow]]
- **"How is a credit-limit increase offered on the phone?"** → [[Value-Add Offer Presentment Flow]] → [[Servicing - Monetary|CLI/CLD]]
- **"How does a reward get created across the card and loyalty platforms?"** → [[Create Reward Flow]]
- **"How do product changes reach the card processing platform?"** → [[Submit Options Maintenance Request Flow]]
- **"Which flows touch the offer & order management system?"** → [[Systems and Integration Reference]] and [[Process-to-Capability Mapping Matrix]]
- **"What disclosures are required before presenting an offer?"** → [[Disclosure Management Flow]] and [[Canadian Regulatory Context]]
