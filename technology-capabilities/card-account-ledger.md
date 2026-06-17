---
id: card-account-ledger
title: Card Account Ledger
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Cardholder Ledger", "Card Billing Engine", "Card Statement Ledger"]
status: draft
sources: ["https://www.lithic.com/blog/developer-first-issuer-processing", "https://www.pismo.io/"]
---

# Card Account Ledger

**Definition.** Card Account Ledger is the technology capability that maintains the cardholder account system-of-record, holding balances, holds and authorizations-in-flight, posted transactions, statement billing cycles, fees and, for credit, credit-limit and revolving-balance accounting.
**Also known as:** Cardholder Ledger, Card Billing Engine, Card Statement Ledger.

## Relationships
- Card Account Ledger is defined in the Core Processing domain.
- Card Account Ledger is derived from Card Processing.
- Card Account Ledger is related to Card Issuing.

## Details
Card Account Ledger records authorization holds at decision time and posts cleared transactions once presentments arrive, keeping available balance and open-to-buy accurate. It runs statement billing cycles, applies fees and interest, and for credit products tracks credit limits and revolving balances. Lithic emphasises precise double-entry debit and credit ledgers, while Pismo provides a high-throughput cloud-native ledger for all card product types.

## References
- [Lithic: Developer-First Issuer Processing](https://www.lithic.com/blog/developer-first-issuer-processing)
- [Pismo](https://www.pismo.io/)
