---
title: Glossary
type: reference
domain: banking-and-payments
tags: [reference, glossary, terminology, disputes, chargebacks, cards, retail-banking, canada]
aliases: [Glossary, Disputes Terms, Definitions]
---

# Glossary

Terminology used across the [[00 - Card Disputes and Chargebacks Index|Card Disputes & Chargebacks]] library. System names and their generic equivalents are in [[Systems and Integration Reference]]; regulatory terms are expanded in [[Canadian Regulatory Context]].

## Dispute & Chargeback Lifecycle

| Term | Definition |
|---|---|
| **Dispute** | A cardholder's claim that a posted transaction is unauthorized, incorrect, or otherwise improper. Logged as a claim case. See [[Initiate Dispute Flow]]. |
| **Chargeback** | The mechanism by which an issuer reverses a transaction back to the acquirer/merchant under card-network rules. |
| **First Chargeback** | The issuer's initial chargeback against the acquirer. See [[First Chargeback Flow]]. |
| **Second Presentment** | The acquirer's (merchant's bank) response to the first chargeback, re-presenting the transaction with supporting documents. See [[Second Presentment Flow]]. |
| **Pre-Arbitration (Pre-Arb)** | A step before arbitration where the issuer challenges the second presentment; the acquirer may accept or decline. |
| **Arbitration** | The card network's binding ruling on a disputed chargeback when the parties do not agree. See [[Arbitration Flow]]. |
| **Pre-Compliance / Compliance** | The rules-violation track (used when the dispute rests on a merchant breaking network rules rather than standard chargeback rights). See [[Pre-Compliance Flow]] and [[Compliance Flow]]. |
| **Representment** | General term for the acquirer re-presenting a charged-back transaction (the second presentment). |

## Fraud & Resolution

| Term | Definition |
|---|---|
| **ATO — Account Takeover** | Fraud where a third party takes over a legitimate cardholder's account. Routes to the fraud investigations team. |
| **FA — Fraudulent Application** | Fraud where the account itself was opened fraudulently. |
| **CSG — Customer Service Gesture** | A goodwill credit applied to the account in lieu of pursuing a chargeback (CSG purchase / CSG cash). |
| **CHL — Cardholder Liable** | A resolution holding the cardholder responsible for the transaction. |
| **WO — Write-Off** | Absorbing the disputed amount as a loss; gated by authority limits and approvals. See [[Performance Auditor Writeoff Flow]]. |
| **Multiprong** | A multi-part close action applied when resolving a case (combination of resolution actions). |
| **Provisional Credit** | A temporary credit to the cardholder at dispute initiation, reversed if the dispute is lost or a merchant credit arrives. |
| **SAFE Reporting** | Network fraud reporting (the network's system to report fraudulent transactions). |
| **Ruling — Acquirer / Issuer / Split Liability** | The arbitration/compliance outcome assigning liability to the acquirer, the issuer, or split between them. |

## Parties & Roles

| Term | Definition |
|---|---|
| **Issuer** | The bank that issued the card (the perspective of these flows). |
| **Acquirer** | The merchant's bank, which presents and re-presents transactions. |
| **Merchant** | The seller whose transaction is disputed. |
| **Dispute Analyst (DA)** | The disputes-operations analyst who works chargebacks; has a write-off **authority** limit. |
| **Fraud Claims Specialist** | The fraud investigations team member who works fraud (ATO/FA) disputes. |
| **Performance Auditor (PA)** | The role that reviews/approves write-offs and arbitration escalations. |
| **Fraud Operations (FO)** | The approver for higher-value fraud write-offs. |
| **Client Care** | The client care / complaints team to which unresolved client disputes are referred. |

## Operational Terms

| Term | Definition |
|---|---|
| **Work-basket** | A queue of cases for a team/role — dispute, challenge, compliance, and network acquirer baskets. |
| **Fee Collection** | The card-network mechanism that moves funds between issuer and acquirer accounts on a disputed transaction (the financial close of a compliance ruling). |
| **Merchant-Collaboration Network** | A third-party network (source: Ethoca) enabling issuer–merchant credit resolution before formal chargeback processing. See [[Merchant Collaboration Credit Flow]]. |
| **Chargeback Rights** | Whether a transaction is eligible for chargeback under network rules (a gating decision at intake). |
| **Chargeback Timeframe** | The network-defined window within which a chargeback must be raised/resubmitted (e.g., the 45-day question on acquirer responses). |
| **Claim / Claim Case** | The case grouping all disputed transactions for a cardholder, resolved and closed together. |

## Related

[[Systems and Integration Reference]] · [[Canadian Regulatory Context]] · [[Generic Multi-Functional Bank Capability Model]] · [[Process-to-Capability Mapping Matrix]]
