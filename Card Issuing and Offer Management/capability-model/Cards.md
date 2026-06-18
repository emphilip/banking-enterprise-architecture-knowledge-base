---
title: Cards
type: capability
level: L1
capability-id: PLB-CRD
parent: Products & LOB (PLB)
tags: [capability, cards, credit-card, product-setup, balance-transfer, retail-banking]
aliases: [PLB-CRD, Cards Capability, Card Products]
---

# Cards (PLB-CRD)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Products & LOB (PLB)]]

The Cards capability group covers the **card products** a bank offers and their **product-level configuration** — personal and corporate credit, co-brand/private-label (PLCC), debit, pre-paid, digital wallet, and the product features that ride on them (limits, balance transfers, installments). For a card issuer this is the home of **product setup**: defining product instances, attaching benefits, pricing, rewards, and affinity, and maintaining the product through its lifecycle. The product-setup flows in this library write to the **product catalogue** (the product book of record) and propagate to the card processing platform.

## L2 Capabilities

### PLB-CRD-01 — Personal Credit

Personal credit-card products and their configuration — product-instance creation, suspension, and update via [[Manage Product Instance Flow]], and premium-tier products via [[Set Up Premium Card Product Flow]].

### PLB-CRD-02 — Corporate Credit

Corporate/commercial credit-card products.

### PLB-CRD-03 — Co-Brand / PLCC

Co-branded and private-label credit-card products, produced from affinity partnerships — see [[Manage Affinity Partnership Flow]].

### PLB-CRD-04 — BNPL

Buy-now-pay-later products.

### PLB-CRD-05 — Debit Cards

Debit-card products.

### PLB-CRD-06 — Pre-Paid

Pre-paid card products.

### PLB-CRD-07 — Digital Wallet

Digital-wallet provisioning of card credentials.

### PLB-CRD-08 — Card Limits

Credit-limit configuration and limit-change products — the target of credit-limit-increase (CLI) value-add offers in [[Value-Add Offer Presentment Flow]] (servicing execution sits in [[Servicing - Monetary]]).

### PLB-CRD-09 — Card Balance Transfers

Balance-transfer (BT) features and the promotional pricing attached to them — presented as pricing offers in [[Pricing Offer Presentment Flow]].

### PLB-CRD-10 — Card Installments

Installment-plan features on card balances.

### PLB-CRD-11 — Convenience Cheques

Convenience-cheque features.

## Card-Product Configuration Constructs

Product setup composes several constructs maintained by the flows in this library: **benefits** ([[Manage Card Benefits Flow]]), **rewards** ([[Create Reward Flow]]), **affinity** ([[Manage Affinity Partnership Flow]]), **pricing** ([[Manage Pricing Flow]]), and the **product instance** itself ([[Manage Product Instance Flow]] / [[Set Up Premium Card Product Flow]]). Changes that must reach the card processing platform are dispatched as an **Options Maintenance Request** ([[Submit Options Maintenance Request Flow]]).

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Manage Product Instance Flow]] | PLB-CRD-01 |
| [[Set Up Premium Card Product Flow]] | PLB-CRD-01 |
| [[Manage Card Benefits Flow]] | PLB-CRD-01 |
| [[Manage Affinity Partnership Flow]] | PLB-CRD-03 |
| [[Pricing Offer Presentment Flow]] | PLB-CRD-09 |
| [[Value-Add Offer Presentment Flow]] | PLB-CRD-08 |

## Related

[[Insurance]] · [[Loyalty]] · [[Rewards]] · [[Servicing - Monetary]] · [[Submit Options Maintenance Request Flow]]
