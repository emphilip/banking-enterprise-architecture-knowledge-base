---
title: Servicing - Monetary
type: capability
level: L1
capability-id: SVC-MON
parent: Servicing (SVC)
tags: [capability, servicing, monetary, pricing, apr, cli, retail-banking, cards]
aliases: [SVC-MON, Monetary Servicing, Pricing and Rate Management]
---

# Servicing — Monetary (SVC-MON)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Servicing (SVC)]]

The Monetary Servicing capability group covers the **money-affecting** servicing of a card account — rate and fee management, adjustments, payment allocation, disputes, and credit-limit changes. For the flows in this library it is the home of **pricing** (the rate/APR templates set up for products and offers) and **CLI/CLD** (credit-limit increase/decrease), which value-add offers present and servicing executes.

## L2 Capabilities

### SVC-MON-01 — Rate / APR Mgmt.

Management of interest rates and APRs at product and account level — the destination of the pricing templates configured in [[Manage Pricing Flow]] (standard/contract rate, penalty rate, promotional rate) and the rate behind promotional balance-transfer offers in [[Pricing Offer Presentment Flow]].

### SVC-MON-02 — Fee Mgmt.

Management of card fees (annual, transaction, penalty fees).

### SVC-MON-03 — Adjustments

Monetary adjustments to an account.

### SVC-MON-04 — Credit Balance Refund

Refunding credit balances.

### SVC-MON-05 — Acct. Balance Transfer

Account-level balance transfers (servicing execution of the BT feature in [[Cards|PLB-CRD-09]]).

### SVC-MON-06 — Payment Allocation

Allocation of payments across balances per regulation.

### SVC-MON-07 — Disputes

Transaction dispute handling.

### SVC-MON-08 — CLI / CLD

**Credit-Limit Increase / Decrease.** The servicing execution of a credit-limit change — presented to customers as a value-add offer in [[Value-Add Offer Presentment Flow]] and processed against the card account and the card processing platform.

### SVC-MON-09–14 — Further Monetary Servicing

Insurance Adj., Withholding Tax, Refunds / Reversals, Interest Posting, Late Charge, Statement Credit — additional money-affecting servicing functions.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Manage Pricing Flow]] | SVC-MON-01, 02 |
| [[Pricing Offer Presentment Flow]] | SVC-MON-01, 05 |
| [[Value-Add Offer Presentment Flow]] | SVC-MON-08 |

## Related

[[Cards]] · [[Offers]] · [[Manage Pricing Flow]] · [[Value-Add Offer Presentment Flow]] · [[Canadian Regulatory Context]]
