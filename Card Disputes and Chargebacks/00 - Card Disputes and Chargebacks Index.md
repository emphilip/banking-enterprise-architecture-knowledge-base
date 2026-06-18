---
title: Card Disputes & Chargebacks — Knowledge Library Index
type: index
domain: banking-and-payments
capability-l0: [Payments & Transaction Processing, Servicing, Fraud & Risk, Operations]
tags: [disputes, chargebacks, fraud, capability-model, index, retail-banking, canada]
aliases: [Disputes Index, Chargebacks Index, Disputes Library Index]
---

# Card Disputes & Chargebacks — Knowledge Library

This library documents the **card disputes and chargebacks lifecycle** of a generic Canadian retail card issuer, paired with **generalized process flows** and mapped to the **master capability model** ([[Generic Multi-Functional Bank Capability Model|slide 4]]). Every capability has a stable ID, every flow is mapped to the L2 capabilities it exercises, and vendor/brand specifics are abstracted in the reference notes.

**Scope.** The end-to-end dispute lifecycle: intake and triage, the fraud (account-takeover) path, the fraud-claims work-basket, the first chargeback, merchant-collaboration credit recovery, second presentment, write-off approval, arbitration, and the pre-compliance / compliance rules-violation track.

**Provenance.** Process flows are generalized from a real Canadian card-issuer disputes program (CIBC; deck prepared by Capco, 2020). Vendor and brand specifics — the claims/chargeback platform, the card processing platform, the network dispute-management application, the fraud system, the merchant-collaboration network, and the bank's own brand — have been abstracted to generic roles per [[Systems and Integration Reference]]. The source contained DRAFT / TBD items, preserved as such.

> Sibling library to *Card Issuing & Offer Management* and *Onboarding & Origination*; all three share the same slide-4 capability IDs.

---

## 1. Capability Model

Mapped to the L1 capability groups of the [[Generic Multi-Functional Bank Capability Model]]:

| L1 Capability | ID | L0 Domain |
|---|---|---|
| [[Transaction Processing]] | PAY-TXN | Payments & Transaction Processing |
| [[Settlement]] | PAY-STL | Payments & Transaction Processing |
| [[Servicing - Monetary]] | SVC-MON | Servicing |
| [[Fraud Management]] | FRR-FRD | Fraud & Risk |
| [[Case Management]] | OPS-CAS | Operations |

Overview note: [[Generic Multi-Functional Bank Capability Model]]

## 2. Process Flows

10 generalized flows, grouped by lifecycle stage. Full L2 traceability in the [[Process-to-Capability Mapping Matrix]].

### Intake & Fraud

| Process Flow | Stage | Primary Capabilities |
|---|---|---|
| [[Initiate Dispute Flow]] | Intake / triage | SVC-MON, OPS-CAS, PAY-TXN, FRR-FRD |
| [[Dispute Transfer to ITR Flow]] | Fraud path | FRR-FRD, OPS-CAS, SVC-MON |
| [[Dispute Workbasket Flow]] | Fraud resolution | FRR-FRD, OPS-CAS, SVC-MON |

### Chargeback Resolution

| Process Flow | Stage | Primary Capabilities |
|---|---|---|
| [[First Chargeback Flow]] | 1st chargeback | PAY-TXN, OPS-CAS, FRR-FRD |
| [[Merchant Collaboration Credit Flow]] | Merchant credit | PAY-TXN, PAY-STL, SVC-MON |
| [[Second Presentment Flow]] | Acquirer response | PAY-TXN, OPS-CAS, OPS-WFR |
| [[Performance Auditor Writeoff Flow]] | Write-off approval | OPS-WFR, OPS-CAS, SVC-MON |
| [[Arbitration Flow]] | Network ruling | PAY-TXN, OPS-CAS, SVC-MON |

### Compliance

| Process Flow | Stage | Primary Capabilities |
|---|---|---|
| [[Pre-Compliance Flow]] | Rules-violation track | PAY-TXN, OPS-CAS, OPS-WFR |
| [[Compliance Flow]] | Compliance settlement | PAY-STL, OPS-CAS, PAY-TXN |

## 3. Reference

- [[Process-to-Capability Mapping Matrix]] — full traceability of flows to L2 capabilities
- [[Systems and Integration Reference]] — generic system roles and the source→generic genericisation mapping
- [[Glossary]] — disputes & chargebacks terminology
- [[Canadian Regulatory Context]] — network rules, zero-liability, FCAC complaint handling, dispute timeframes, privacy

---

## Identifier Conventions

- **Capability IDs** — `<L0>-<L1>-nn`, e.g., `PAY-TXN-04` (Payments & Txn Proc → Transaction Processing → Chargebacks). Defined in [[Generic Multi-Functional Bank Capability Model]].
- **Step IDs** — each flow uses a flow-local prefix on `Step XX-nn` headings (e.g., `INIT-`, `CB1-`, `ARB-`). Where the source diagram numbered steps (e.g., `ATO05`, `PCOM001`), those numbers are preserved.

## How to Query This Library

- **"What happens when a customer disputes a transaction?"** → [[Initiate Dispute Flow]]
- **"How is an account-takeover dispute handled?"** → [[Dispute Transfer to ITR Flow]] → [[Dispute Workbasket Flow]]
- **"How does the first chargeback get raised?"** → [[First Chargeback Flow]]
- **"How is a merchant credit recovered through the collaboration network?"** → [[Merchant Collaboration Credit Flow]]
- **"What happens when the acquirer re-presents?"** → [[Second Presentment Flow]] → [[Arbitration Flow]]
- **"Who approves a write-off and when?"** → [[Performance Auditor Writeoff Flow]]
- **"How is a rules-violation dispute settled?"** → [[Pre-Compliance Flow]] → [[Compliance Flow]]
