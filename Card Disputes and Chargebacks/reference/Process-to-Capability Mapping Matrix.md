---
title: Process-to-Capability Mapping Matrix
type: reference
domain: banking-and-payments
tags: [reference, mapping, traceability, capability-model, process-flow, disputes, l2-capabilities]
aliases: [Mapping Matrix, Capability Matrix, Traceability Matrix]
---

# Process-to-Capability Mapping Matrix

Full traceability between the [[00 - Card Disputes and Chargebacks Index|library's]] 10 process flows and the **L2 capabilities** of the [[Generic Multi-Functional Bank Capability Model|master capability model (slide 4)]]. Legend: **P** = primary (the flow *is* this capability in action) · **S** = supporting · **—** = not exercised.

L1 column codes: **TXN** = [[Transaction Processing|PAY-TXN]] · **STL** = [[Settlement|PAY-STL]] · **MON** = [[Servicing - Monetary|SVC-MON]] · **FRD** = [[Fraud Management|FRR-FRD]] · **CAS** = [[Case Management|OPS-CAS]]. *Adjacent* lists L0/L1 domains exercised outside the five columns (OPS-WFR = Operations Workflow & Rules / approvals; CEN-REL = Customer Engagement Relationship Mgmt / complaints; SVC-NON = Servicing Non-Monetary / card block & reissue; CHN = Channels).

## Matrix — L1 Summary

| Process Flow | TXN | STL | MON | FRD | CAS | Adjacent |
|---|:--:|:--:|:--:|:--:|:--:|---|
| [[Initiate Dispute Flow]] | **P** | — | **P** | S | **P** | SVC-NON, CHN, OPS-WFR |
| [[Dispute Transfer to ITR Flow]] | S | — | **P** | **P** | **P** | SVC-NON |
| [[Dispute Workbasket Flow]] | S | — | **P** | **P** | **P** | CEN-REL, OPS-WFR |
| [[First Chargeback Flow]] | **P** | S | — | S | **P** | — |
| [[Merchant Collaboration Credit Flow]] | **P** | **P** | S | — | S | OPS-WFR |
| [[Second Presentment Flow]] | **P** | — | S | — | **P** | OPS-WFR |
| [[Performance Auditor Writeoff Flow]] | — | — | **P** | S | **P** | **OPS-WFR** |
| [[Arbitration Flow]] | **P** | — | S | — | **P** | OPS-WFR |
| [[Pre-Compliance Flow]] | **P** | — | — | — | **P** | OPS-WFR, CEN-REL |
| [[Compliance Flow]] | S | **P** | S | — | **P** | — |

## Matrix — Flow to Primary L2 Capabilities

Step-level detail lives in each flow's *Capability Mapping* table and `Step` headings.

### Intake & Fraud

| Flow | Primary L2 capabilities |
|---|---|
| [[Initiate Dispute Flow]] | SVC-MON-07 Disputes; OPS-CAS-01/02 Create/Route Case; PAY-TXN-04 Chargebacks; FRR-FRD-03 Fraud Detection |
| [[Dispute Transfer to ITR Flow]] | FRR-FRD-04 Investigation, FRR-FRD-03 Detection; OPS-CAS-01/04; SVC-MON-07; PAY-TXN-04 |
| [[Dispute Workbasket Flow]] | FRR-FRD-04/05; OPS-CAS-02/04/05/06; SVC-MON-07/03 (CSG) |

### Chargeback Resolution

| Flow | Primary L2 capabilities |
|---|---|
| [[First Chargeback Flow]] | PAY-TXN-04 Chargebacks; OPS-CAS-01/03/04; FRR-FRD-02 SAFE; PAY-STL-02 |
| [[Merchant Collaboration Credit Flow]] | PAY-TXN-05 Reversals; PAY-STL-05/01/02; SVC-MON-11 Refunds/Reversals |
| [[Second Presentment Flow]] | PAY-TXN-04; OPS-CAS-03/05/06; OPS-WFR-02 Approvals; SVC-MON-07 |
| [[Performance Auditor Writeoff Flow]] | OPS-WFR-02 Approvals; OPS-CAS-04/05/06; SVC-MON-07 Write-off |
| [[Arbitration Flow]] | PAY-TXN-04; OPS-CAS-06 Resolution; SVC-MON-07 |

### Compliance

| Flow | Primary L2 capabilities |
|---|---|
| [[Pre-Compliance Flow]] | PAY-TXN-04; OPS-CAS-02/03/05; OPS-WFR-02 Approvals |
| [[Compliance Flow]] | PAY-STL-01 Network Settle / Fee Collection; OPS-CAS-02/05/06; PAY-TXN-04; SVC-MON-07 |

## Coverage Notes

- **Strongly evidenced by source artifacts:** PAY-TXN-04/05/06 (chargeback lifecycle), SVC-MON-07/03/11 (disputes, CSG, reversals), OPS-CAS-01–06 (case lifecycle), FRR-FRD-03/04 (fraud detection/investigation), PAY-STL-01/02/05 (fee collection, merchant credit, recon), OPS-WFR-02 (approvals).
- **Generalized from standard Canadian card-issuer practice** (thin/implicit in source): PAY-TXN-01/02/03 (the upstream authorization/clearing of the disputed transaction), FRR-FRD-01/06 (fraud-loss strategy, mass compromise), PAY-STL-03/04/06 (broader settlement). Documented at capability level in the L1 notes, with the generalization flagged.
- **Adjacent-domain dependencies** (OPS-WFR approvals/SLA, CEN-REL complaints & Client Care, SVC-NON card block/reissue, CHN contact centre, Enterprise Support customer information file) are referenced inline in the flows rather than given their own notes.
- **Open / TBD items preserved from source:** the 45-day arbitration question ([[Second Presentment Flow]]); accept-liability sub-processes ([[Pre-Compliance Flow]]); the merchant-credit month-end adjustment ([[Merchant Collaboration Credit Flow]]); the acquirer-liable close action ([[Arbitration Flow]]); and the referral work-basket ([[Compliance Flow]]).

## Related

[[Generic Multi-Functional Bank Capability Model]] · [[Systems and Integration Reference]] · [[Glossary]] · [[Canadian Regulatory Context]]
