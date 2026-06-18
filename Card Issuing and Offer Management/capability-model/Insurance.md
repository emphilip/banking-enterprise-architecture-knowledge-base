---
title: Insurance
type: capability
level: L1
capability-id: PLB-INS
parent: Products & LOB (PLB)
tags: [capability, insurance, creditor-insurance, balance-protection, policy, retail-banking]
aliases: [PLB-INS, Insurance Capability]
---

# Insurance (PLB-INS)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Products & LOB (PLB)]]

The Insurance capability group covers the bank's insurance products and policy lifecycle. In a card-issuing context the relevant products are **creditor / credit-protection insurance** (balance protection, payment protection) and related coverages cross-sold to cardholders. The group spans product setup (defining an insurance product the bank can offer), quoting and issuance, certificate production, and the policy-maintenance lifecycle. Insurance offers cross-sold during card servicing reference both this group and [[Offers]].

## L2 Capabilities

### PLB-INS-01 — Life

Life coverage components of creditor insurance.

### PLB-INS-02 — Property & Casualty

Property & casualty products (out of card scope but part of the master model).

### PLB-INS-03 — Auto

Auto products.

### PLB-INS-04 — Travel

Travel insurance (commonly a premium-card benefit).

### PLB-INS-05 — Health

Health/disability components of creditor insurance.

### PLB-INS-06 — Insurance Quotes

Quoting an insurance offer for a customer — exercised at presentment in [[Insurance Offer Presentment Flow]] and [[Add Insurance Product Phone Channel Flow]].

### PLB-INS-07 — Policy Issuance

Enrolling a customer in a policy / issuing coverage, including the fulfilment hand-off after acceptance. Insurance product **setup** (defining the product so it can be issued) is [[Manage Insurance Product Setup Flow]].

### PLB-INS-08 — Policy Renewal

Renewing coverage.

### PLB-INS-09 — Policy Maintenance

Maintaining in-force policies, including changes to a product's availability — the remove/retire path of [[Manage Insurance Product Setup Flow]].

### PLB-INS-10 — Policy Cancellation

Cancelling coverage at customer or bank instruction.

### PLB-INS-11 — Certificates

Producing certificates of insurance / coverage confirmations.

### PLB-INS-12–16 — Claims & Payments

Claim Opening, Claim Mgmt., Claim Adjudication, Claim Settlement, and Insurance Payments — the downstream claims lifecycle (out of scope for these origination/offer flows).

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Manage Insurance Product Setup Flow]] | PLB-INS-07, 09 |
| [[Insurance Offer Presentment Flow]] | PLB-INS-06, 07 |
| [[Add Insurance Product Phone Channel Flow]] | PLB-INS-06, 07 |
| [[Value-Add Offers Flow]] | PLB-INS-06, 07 |

## Related

[[Cards]] · [[Offers]] · [[Insurance Offer Presentment Flow]] · [[Canadian Regulatory Context]]
