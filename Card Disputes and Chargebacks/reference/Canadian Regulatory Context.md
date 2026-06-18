---
title: Canadian Regulatory Context
type: reference
domain: banking-and-payments
tags: [reference, regulatory, canada, disputes, chargebacks, zero-liability, network-rules, fcac]
aliases: [Regulatory Context, Disputes Regulation, Compliance Context]
---

# Canadian Regulatory Context

The regulatory and network-rule backdrop relevant to the **card disputes & chargebacks** flows, for a generic Canadian retail card issuer. This is generalized context, not legal advice.

## Card-Network Rules

- **Network operating rules (Visa / Mastercard)** are the primary rulebook for chargebacks: they define **chargeback rights**, reason codes, **timeframes** (e.g., the 45-day acquirer-response question raised in [[Second Presentment Flow]]), the second-presentment / pre-arbitration / arbitration sequence, and the **compliance** track for rules violations. The chargeback-rights gate in [[Initiate Dispute Flow]] and the arbitration ruling in [[Arbitration Flow]] are network-rule-driven.
- **Fee collection and settlement** between issuer and acquirer follow network settlement rules — see [[Compliance Flow]] and [[Settlement]].
- **Network fraud reporting (SAFE)** obligations require reporting confirmed fraud to the network; removing a transaction from the fraud report when a cardholder is held liable is part of keeping that reporting accurate ([[Dispute Workbasket Flow]]).

## Cardholder Protection

- **Zero-liability / fraud protection.** Issuers apply zero-liability policies for unauthorized transactions; the fraud (ATO/FA) path provisionally credits the cardholder and pursues recovery via chargeback. Holding a cardholder liable (CHL) requires a documented basis (the victim commentary in [[Dispute Transfer to ITR Flow]]).
- **Billing-error / dispute rights.** Cardholders have the right to dispute transactions; the issuer must investigate and resolve within reasonable timeframes, with provisional credit pending resolution.
- **Cost-of-borrowing interplay.** Interest/fees on a disputed amount are typically suspended or reversed pending resolution per cardholder-agreement and cost-of-borrowing expectations.

## Market Conduct & Complaints

- **FCAC** (Financial Consumer Agency of Canada) oversees federal market-conduct obligations, including **complaint-handling**. The escalation to the manager and the **Client Care** referral in [[Dispute Workbasket Flow]] reflect the bank's complaint-handling obligations when a client does not accept an outcome.
- **Code of Conduct for the Credit and Debit Card Industry in Canada** governs aspects of merchant/acquirer conduct relevant to disputes.

## Privacy & Records

- **PIPEDA** governs the personal information collected and shared during a dispute/fraud investigation (transaction data, victim statements, supporting documents). Case notes, approval forms, and the fraud document repository are subject to retention and handling expectations.
- **Audit trail.** The running case notes, victim commentary, and write-off approval evidence (see [[Performance Auditor Writeoff Flow]]) provide the auditable record required to substantiate chargeback and write-off decisions.

## Related

[[Transaction Processing]] · [[Servicing - Monetary]] · [[Fraud Management]] · [[Glossary]] · [[Systems and Integration Reference]]
