---
title: Settlement
type: capability
level: L1
capability-id: PAY-STL
parent: Payments & Transaction Processing (PAY)
tags: [capability, settlement, fee-collection, network-settle, reconciliation, disputes, retail-banking]
aliases: [PAY-STL, Settlement Capability]
---

# Settlement (PAY-STL)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Payments & Transaction Processing (PAY)]]

The Settlement capability group covers the **movement and reconciliation of funds** between the issuer, the card network, and the acquirer. In the disputes context it is exercised when a dispute resolves with a financial movement — the network's **fee-collection** mechanism debiting/crediting the issuer's and acquirer's accounts on a disputed transaction, the end-of-month network credit/debit when a merchant credit is owed, and the reconciliation files that track outstanding items.

## L2 Capabilities

### PAY-STL-01 — Network Settle

Settlement with the card network, including the **fee-collection** entries that move funds between the issuer (fraud/cardholder account) and the acquirer's account on a disputed transaction — the financial close of a [[Compliance Flow|compliance]] ruling.

### PAY-STL-02 — Direct Merchant

Direct merchant settlement (e.g., a merchant processing a refund directly to the cardholder account, as in the merchant-collaboration path).

### PAY-STL-03 — Payout Alloc.

Allocation of settlement payouts.

### PAY-STL-04 — Customer Pmt

Customer payment settlement.

### PAY-STL-05 — Recon. Files

Reconciliation files — e.g., the weekly outstanding-items file and the merchant-credit tracker used to chase network credits in [[Merchant Collaboration Credit Flow]].

### PAY-STL-06 — Settlement Reporting

Reporting on settlement and dispute-related fund movements.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Compliance Flow]] | PAY-STL-01 |
| [[Merchant Collaboration Credit Flow]] | PAY-STL-02, 05 |
| [[First Chargeback Flow]] | PAY-STL-02 |

## Related

[[Transaction Processing]] · [[Servicing - Monetary]] · [[Systems and Integration Reference]]
