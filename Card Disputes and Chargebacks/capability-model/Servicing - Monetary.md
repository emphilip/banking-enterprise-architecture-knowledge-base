---
title: Servicing - Monetary
type: capability
level: L1
capability-id: SVC-MON
parent: Servicing (SVC)
tags: [capability, servicing, monetary, disputes, adjustments, reversals, write-off, retail-banking, cards]
aliases: [SVC-MON, Monetary Servicing, Disputes Servicing]
---

# Servicing — Monetary (SVC-MON)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Servicing (SVC)]]

The Monetary Servicing capability group covers the **money-affecting** servicing of a card account. For the disputes program its central capability is **Disputes** — the cardholder-facing claim that a transaction is unauthorized or wrong — together with the **adjustments, refunds/reversals, write-offs, and goodwill credits** that resolve a dispute on the account.

## L2 Capabilities

### SVC-MON-07 — Disputes

The **dispute** itself: the cardholder's claim against a posted transaction, logged as a claim case and worked through the chargeback lifecycle. This is the primary capability of the entire library; every flow ultimately serves the lifecycle of a dispute. Disputes are intaken in [[Initiate Dispute Flow]] and resolved across the chargeback and compliance flows.

### SVC-MON-03 — Adjustments

Monetary adjustments to the account during dispute resolution, including the **Customer Service Gesture (CSG)** goodwill credit applied when the bank elects not to pursue a chargeback. Applied in [[Dispute Workbasket Flow]].

### SVC-MON-11 — Refunds / Reversals

Refunds and reversals on the account — provisional credit at dispute initiation, and the **reversal** of that credit when a merchant credit is later received. See [[Merchant Collaboration Credit Flow]].

### SVC-MON-04 — Credit Balance Refund

Refunding a resulting credit balance.

### SVC-MON-02 — Fee Mgmt.

Fee handling associated with disputes and chargebacks.

### SVC-MON-08/09/12–14 — Further Monetary Servicing

CLI/CLD, Insurance Adj., Interest Posting, Late Charge, Statement Credit — additional money-affecting servicing functions (largely out of scope for the dispute flows, listed for model completeness).

> **Write-off (WO)** in these flows is the act of absorbing the disputed amount as a loss when a chargeback is not pursued or not won; it is governed by dispute-analyst authority limits and Performance-Auditor approval — see [[Performance Auditor Writeoff Flow]].

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Initiate Dispute Flow]] | SVC-MON-07 |
| [[Dispute Transfer to ITR Flow]] | SVC-MON-07 |
| [[Dispute Workbasket Flow]] | SVC-MON-07, 03 |
| [[Merchant Collaboration Credit Flow]] | SVC-MON-11 |
| [[Second Presentment Flow]] | SVC-MON-07 |
| [[Performance Auditor Writeoff Flow]] | SVC-MON-07 |
| [[Arbitration Flow]] | SVC-MON-07 |

## Related

[[Transaction Processing]] · [[Case Management]] · [[Fraud Management]] · [[Canadian Regulatory Context]]
