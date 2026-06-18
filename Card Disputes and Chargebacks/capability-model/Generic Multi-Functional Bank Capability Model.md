---
title: Generic Multi-Functional Bank — Capability Model
type: capability-model
level: L0
domain: banking-and-payments
tags: [capability-model, master-model, retail-banking, cards, disputes, chargebacks, canada, L0]
aliases: [Master Capability Model, Bank Capability Model, B&P Capability Model, Slide 4]
---

# Generic Multi-Functional Bank — Capability Model

The enterprise capability model for a **generic multi-functional bank** — the master reference that this library's process flows are mapped against. It is organized as **L0 domains → L1 capability groups → L2 capabilities**. The flows in this library are *generalized* from a real Canadian card-issuer **disputes & chargebacks** program; brand and vendor specifics have been abstracted to the generic roles described in [[Systems and Integration Reference]].

> This is the same master model (slide 4 of the Banking & Payments Accelerator) used by the companion *Card Issuing & Offer Management* and *Onboarding & Origination* libraries; capability IDs are shared across all three so cross-library references stay consistent.

## L0 Domains

The thirteen L0 functional domains: **Fraud & Risk**, **Channels**, **Interaction Management**, **Identity, Auth & Access**, **Marketing & Sales**, **Customer Engagement**, **Onboarding & Origination**, **Products & LOB**, **Card-Linked Products**, **Servicing**, **Payments & Transaction Processing**, **Enterprise Support**, and **Operations** — supported by a corporate-function band (Business Strategy, Product Mgmt., Project Mgmt., HR & Talent, Legal, Vendor/Partner/Supplier, Facilities, Comms & Investor Relations, Corporate Responsibility).

## Scope Covered by This Library

The card-disputes and chargeback flows here primarily exercise four L0 domains. The L1 capability groups documented as notes are:

| L0 Domain | L1 Capability Group | ID | Note |
|---|---|---|---|
| Payments & Transaction Processing | Transaction Processing | `PAY-TXN` | [[Transaction Processing]] |
| Payments & Transaction Processing | Settlement | `PAY-STL` | [[Settlement]] |
| Servicing | Monetary | `SVC-MON` | [[Servicing - Monetary]] |
| Fraud & Risk | Fraud Management | `FRR-FRD` | [[Fraud Management]] |
| Operations | Case Management | `OPS-CAS` | [[Case Management]] |

## Cross-Domain Dependencies

The flows also touch capabilities owned by adjacent L0 domains, referenced inline rather than given their own notes:

- **Operations — Workflow & Rules** (`OPS-WFR`) — approvals (write-off and arbitration approvals), SLA timers, and exception handling behind the resolution gates.
- **Customer Engagement — Relationship Management** (`CEN-REL`) — complaint handling and the Client Care referral path (`CEN-REL-04` Complaints).
- **Servicing — Non-Monetary** (`SVC-NON`) — card block/cancel and reissue when fraud is confirmed (`SVC-NON-06` Card Reissue, `SVC-NON-08` Card Block/Unblock).
- **Channels — Assisted** (`CHN-AS`) — the contact centre that takes the inbound dispute call.
- **Customer Engagement — Customer Info Mgmt / Enterprise Support — Books of Record** — the customer information file and transaction system of record read throughout.

## Identifier Conventions

- **Capability IDs** — `<L0>-<L1>-nn`, e.g., `PAY-TXN-04` (Payments & Txn Proc → Transaction Processing → Chargebacks).
- **Step IDs** — each process flow uses a flow-local prefix (e.g., `INIT-`, `CB1-`, `ARB-`) on `Step XX-nn` headings, addressable as `[[Flow Name#Step XX-nn — Title]]`. Where the source diagram numbered steps (e.g., `ATO05`, `PCOM001`), those numbers are preserved in the step text.
- Full traceability of flow steps to L2 capabilities lives in the [[Process-to-Capability Mapping Matrix]].

## Related

[[00 - Card Disputes and Chargebacks Index]] · [[Systems and Integration Reference]] · [[Glossary]] · [[Canadian Regulatory Context]]
