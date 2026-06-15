---
id: card-transaction-authorization
title: Card Transaction Authorization
type: business-process
domain: Cards
aliases: ["Authorization Process", "Card Auth"]
status: draft
sources: ["https://dpogroup.com/blog/a-step-by-step-guide-to-the-emv-and-online-card-transaction-journey/", "https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html", "https://www.aciworldwide.com/emv-payments-transactions"]
---

# Card Transaction Authorization

**Definition.** Card Transaction Authorization is the real-time decisioning of a card authorization request at the issuer: EMV/cryptogram and PIN validation, credit-limit/funds and velocity/fraud checks, and approve/decline with an authorization hold, including stand-in (STIP) when the issuer is unavailable.
**Also known as:** Authorization Process, Card Auth.

## Relationships
- Card Transaction Authorization is defined in the Cards domain.
- Card Transaction Authorization depends on the Card Authorization capability.

## Details
Card Transaction Authorization receives the Authorization Request routed from the acquirer through the card scheme, validates the EMV ARQC cryptogram and PIN/CVM, checks the available credit limit or funds against the requested amount, applies velocity and fraud-scoring rules, and decides approve or decline. An approval places an authorization hold and returns an ARPC response; stand-in processing (STIP) applies the issuer's fallback rules when the host is unavailable. PCI DSS protects the PAN throughout. Actors include the Card Operations Analyst. The cleared presentment is later matched to the hold and posted to the cardholder account.

## Flow
- Receive Authorization Request causes Validate Card Cryptogram.
- Validate Card Cryptogram causes Check Available Limit.
- Check Available Limit causes Apply Velocity Rules.
- Apply Velocity Rules causes Authorize Transaction.
- Authorize Transaction causes Return Authorization Response.
- Return Authorization Response causes Post Cleared Transaction.

## References
- [EMV and online card transaction journey](https://dpogroup.com/blog/a-step-by-step-guide-to-the-emv-and-online-card-transaction-journey/)
- [ARQC validation for issuers](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html)
- [EMV payments transactions](https://www.aciworldwide.com/emv-payments-transactions)
