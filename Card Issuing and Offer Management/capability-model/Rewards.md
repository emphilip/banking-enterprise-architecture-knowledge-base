---
title: Rewards
type: capability
level: L1
capability-id: CLP-RWD
parent: Card-Linked Products (CLP)
tags: [capability, rewards, loyalty, points, redemption, retail-banking, cards]
aliases: [CLP-RWD, Rewards Capability]
---

# Rewards (CLP-RWD)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Card-Linked Products (CLP)]]

The Rewards capability group covers the **earning, calculating, tracking, redeeming, and presentment** of card rewards (points, cash-back, miles, merchant offers) attached to card products. For a card issuer it spans the back-office definition of reward constructs (reward codes and their attributes), the cross-platform creation of a reward across the product catalogue, the card processing platform, and the loyalty platform, and the campaign that presents rewards to existing customers.

## L2 Capabilities

### CLP-RWD-01 — Earn

Defining and applying the earn rules by which transactions accrue rewards. A **reward code** (an `ARQ`-class reward identifier) and its attributes are created in the product catalogue and propagated to the card processing platform and loyalty platform — see [[Create Reward Flow]].

### CLP-RWD-02 — Calculate

Calculating accrued reward value from earn rules and transaction data.

### CLP-RWD-03 — Track

Tracking reward balances and accrual against the cardholder account and the loyalty platform.

### CLP-RWD-04 — Redeem

Redeeming accrued rewards for value (statement credit, merchandise, travel, transfers).

### CLP-RWD-05 — Presentment

Presenting rewards content and reward offers to customers across channels. The cross-functional campaign that takes a reward to existing customers via direct mail, email, and phone is [[Publish Rewards Flow]]; rewards content placed on the secure site is published by [[Create and Update Content Management Flow]].

### CLP-RWD-06 — Consolidate

Consolidating reward balances across products or programs.

### CLP-RWD-07 — Merchant Offers

Merchant-funded and card-linked merchant offers.

### CLP-RWD-08 — Tiered Rewards

Tier-dependent earn/redeem (e.g., premium card tiers earn at higher rates) — exercised when a premium card product is configured in [[Set Up Premium Card Product Flow]].

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Create Reward Flow]] | CLP-RWD-01, 02, 03 |
| [[Publish Rewards Flow]] | CLP-RWD-05 |
| [[Create and Update Content Management Flow]] | CLP-RWD-05 |
| [[Set Up Premium Card Product Flow]] | CLP-RWD-01, 08 |

## Related

[[Loyalty]] · [[Cards]] · [[Offers]] · [[Create Reward Flow]] · [[Systems and Integration Reference]]
