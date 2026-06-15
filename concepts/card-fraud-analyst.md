---
id: card-fraud-analyst
title: Card Fraud Analyst
type: role
domain: Cards
aliases: ["Card Fraud Investigator", "Card Fraud Operations Analyst"]
status: draft
sources: ["https://www.sardine.ai/issuing-fraud", "https://www.checkout.com/blog/velocity-check"]
---

# Card Fraud Analyst

**Definition.** Card Fraud Analyst is the role that detects and operationally handles suspected card fraud: triaging fraud alerts from scoring and velocity rules, verifying cardholders, blocking and reissuing compromised cards, adjudicating fraud claims and referring confirmed cases for SAR consideration. Card Fraud Analyst contains card-fraud loss while preserving genuine cardholder activity.

**Also known as:** Card Fraud Investigator, Card Fraud Operations Analyst.

## Relationships
- Card Fraud Analyst is related to the Cards domain.
- Card Fraud Analyst mentions Card Fraud Handling.
- Card Fraud Analyst mentions Triage Fraud Alert.
- Card Fraud Analyst mentions Block Compromised Card.

## Details
Card Fraud Analyst triages and prioritises a Fraud Alert raised by real-time scoring and velocity rules, then contacts the cardholder to confirm whether flagged transactions are genuine. Where fraud is confirmed, the role blocks the compromised card/credential to stop further authorizations, instructs reissue and wallet-token re-provisioning, and adjudicates the fraud claim applying Reg E unauthorized-EFT liability limits. Card Fraud Analyst maintains an audit trail and refers confirmed fraud for SAR filing against regulatory thresholds, feeding intelligence back into fraud-scoring models.

## References
- https://www.sardine.ai/issuing-fraud
- https://www.checkout.com/blog/velocity-check
