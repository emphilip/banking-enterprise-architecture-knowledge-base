---
title: Transaction Processing
type: capability
level: L1
capability-id: PAY-TXN
parent: Payments & Transaction Processing (PAY)
tags: [capability, transaction-processing, chargebacks, reversals, exception-handling, disputes, retail-banking]
aliases: [PAY-TXN, Transaction Processing Capability, Chargebacks]
---

# Transaction Processing (PAY-TXN)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Payments & Transaction Processing (PAY)]]

The Transaction Processing capability group covers the processing lifecycle of card transactions — authorization, clearing, and the **exception lifecycle** of **chargebacks, reversals, and exception handling**. For a card issuer's disputes program this is the home of the **chargeback lifecycle**: raising a first chargeback against the card network, handling the acquirer's second presentment, pre-arbitration/arbitration, and the reversals that unwind a chargeback when a merchant credit arrives.

## L2 Capabilities

### PAY-TXN-01 — Authorization

Real-time approval/decline of card transactions. (Upstream of disputes; in scope only as the transaction being disputed.)

### PAY-TXN-02 — Pre-Auth

Pre-authorization holds.

### PAY-TXN-03 — Clearing

Clearing of authorized transactions into posted transactions.

### PAY-TXN-04 — Chargebacks

The **issuer chargeback lifecycle** against the card network and acquirer:

- **First chargeback** — raised in the card processing platform and the network dispute-management application, then sent to the merchant/acquirer. See [[First Chargeback Flow]].
- **Second presentment** — the acquirer's response; reviewed and either accepted or escalated. See [[Second Presentment Flow]].
- **Pre-arbitration and arbitration** — escalation when the second presentment is not accepted. See [[Arbitration Flow]].
- **Pre-compliance and compliance** — the rules-violation track when a merchant did not comply with network rules. See [[Pre-Compliance Flow]] and [[Compliance Flow]].

### PAY-TXN-05 — Reversals

Reversing a chargeback or transaction — e.g., reversing the provisional credit / chargeback once a **merchant credit** is received through the merchant-collaboration network. See [[Merchant Collaboration Credit Flow]].

### PAY-TXN-06 — Exception Handling

The exception queues and work-baskets that route disputed items for specialist handling (challenge, write-off, escalation).

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[First Chargeback Flow]] | PAY-TXN-04 |
| [[Merchant Collaboration Credit Flow]] | PAY-TXN-05, 04 |
| [[Second Presentment Flow]] | PAY-TXN-04 |
| [[Arbitration Flow]] | PAY-TXN-04 |
| [[Pre-Compliance Flow]] | PAY-TXN-04, 06 |
| [[Compliance Flow]] | PAY-TXN-04 |
| [[Initiate Dispute Flow]] | PAY-TXN-04, 06 |

## Related

[[Settlement]] · [[Servicing - Monetary]] · [[Fraud Management]] · [[Case Management]] · [[Systems and Integration Reference]]
