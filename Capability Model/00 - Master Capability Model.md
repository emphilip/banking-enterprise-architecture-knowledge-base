---
title: Generic Multi-Functional Bank — Master Capability Model
type: index
domain: banking-and-payments
tags: [capability-model, master-model, index, retail-banking, canada, L0, slide-4]
aliases: [Master Capability Model, Bank Capability Model, B&P Capability Model, Slide 4, Capability Framework]
---

# Generic Multi-Functional Bank — Master Capability Model

The enterprise capability framework for a **generic multi-functional bank**, transcribed from **Slide 4** of the *Banking & Payments Accelerator*. It is organised as a four-level hierarchy:

> **L0 domain → L1 capability group → L2 capability → L3 process flow**

This vault holds **L0, L1, and L2** as one note each — every L2 is its own atomic note so it can be queried directly and so its **L3 process flows** can be hung off it as they are mapped. Three companion libraries already contain L3 process flows; where they exercise an L2, they are linked from that L2's *Process Flows (L3)* section.

## How to navigate

- Each **L0** note lists its **L1** groups; each **L1** note lists its **L2** capabilities; each **L2** note describes the capability and links the **L3** flows that exercise it.
- Capability IDs follow `<L0>-<L1>-<nn>` (e.g. `FRR-FRD-01`). Notes are filename-prefixed with their ID, so search/sort follows the model.
- L3 process flows live in the companion libraries: [[00 - Onboarding and Origination Index|Origination & Onboarding]], [[00 - Card Disputes and Chargebacks Index|Card Disputes & Chargebacks]], [[00 - Card Issuing and Offer Management Index|Card Issuing & Offer Management]].

## L0 Domains

| # | L0 Domain | ID | L1 Groups | Note |
|---|---|---|---|---|
| 1 | Fraud & Risk | FRR | Fraud Mgmt., Credit Risk, Market & Op Risk, Compliance, Audit & Security | [[FRR Fraud & Risk]] |
| 2 | Channels | CHN | Self-Serve, Assisted | [[CHN Channels]] |
| 3 | Interaction Mgmt. | INT | Routing, Queue Mgmt., Conversation Tools, Collab. & Co-Browse, Transfers & Handoff, Notifications & Alerts | [[INT Interaction Mgmt.]] |
| 4 | Identity, Auth & Access | IAA | Identity Mgmt., Authentication, Authorization, Identity Fraud | [[IAA Identity, Auth & Access]] |
| 5 | Marketing & Sales | MKS | Marketing, Sales & CRM | [[MKS Marketing & Sales]] |
| 6 | Customer Engagement | CEN | Customer Info Mgmt., Relationship Mgmt., Contact Mgmt., Offers, Content Mgmt., Customer Experience, Accessibility & Language | [[CEN Customer Engagement]] |
| 7 | Onboarding & Origination | ONB | Application, Adjudication & Underwriting, AML/KYC/Compliance, Account Setup & Fulfillment, Collateral & Comms, Activation & Enrolment | [[ONB Onboarding & Origination]] |
| 8 | Products & LOB | PLB | Deposits, Cards, Lending & Mortgages, Insurance | [[PLB Products & LOB]] |
| 9 | Card-Linked Products | CLP | PIN Mgmt., Loyalty, Rewards | [[CLP Card-Linked Products]] |
| 10 | Servicing | SVC | Non-Monetary, Monetary | [[SVC Servicing]] |
| 11 | Payments & Txn Proc. | PAY | Money Movement, Txn Processing, Settlement, Payment Servicing, Merchant Acquisition, Internal Movement, Collections | [[PAY Payments & Txn Proc.]] |
| 12 | Enterprise Support | ENT | Books of Record, Data & Analytics, AI/ML/NLU, Reporting, Finance & Accounting, DevSecOps/Infra, Docs & Integrations | [[ENT Enterprise Support]] |
| 13 | Operations | OPS | Workflow & Rules, Workforce Mgmt., Agent Experience, Quality Control, Case Mgmt. | [[OPS Operations]] |

## Corporate Functions (supporting band)

A horizontal band on the slide supports all 13 domains and is not decomposed to L2: **Business Strategy · Product Mgmt. · Project Mgmt. · HR & Talent · Legal · Vendor / Partner / Supplier · Facilities · Comms & Investor Rel. · Corporate Responsibility (CRA)**. See [[Corporate Functions]].

## Companion L3 libraries

| Library | Domains it primarily exercises |
|---|---|
| [[00 - Onboarding and Origination Index\|Origination & Onboarding]] | ONB (+ IAA, FRR, CHN, CEN, PAY) |
| [[00 - Card Disputes and Chargebacks Index\|Card Disputes & Chargebacks]] | PAY-TXN, PAY-STL, SVC-MON, FRR-FRD, OPS-CAS |
| [[00 - Card Issuing and Offer Management Index\|Card Issuing & Offer Management]] | PLB-CRD, PLB-INS, CLP-LOY, CLP-RWD, SVC-MON, CEN, MKS |

---

*Provenance: Slide 4, Banking & Payments Accelerator. Capability IDs are shared with the three companion libraries so cross-references stay consistent. L3 process flows are filled in per L2 as they are mapped.*
