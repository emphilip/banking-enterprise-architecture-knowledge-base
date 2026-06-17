---
id: authorization-validation-and-decisioning
title: Authorization Validation & Decisioning
type: business-process
level: sub-process
domain: Cards
aliases: ["Auth Decisioning", "Approve/Decline"]
status: draft
sources: ["https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html"]
---

# Authorization Validation & Decisioning

**Definition.** Authorization Validation & Decisioning validates the card/cryptogram and PIN and decides approve/decline against limit, funds and fraud rules.
**Also known as:** Auth Decisioning, Approve/Decline.

## Relationships
- Authorization Validation & Decisioning is derived from Card Transaction Authorization.
- Authorization Validation & Decisioning is defined in the Cards domain.
- Authorization Validation & Decisioning depends on the Card Authorization capability.

## Details
Authorization Validation & Decisioning validates the EMV ARQC cryptogram and PIN/CVM, checks the available credit limit or funds, applies velocity and fraud rules, and reaches the approve/decline decision. Actors include the Card Operations Analyst.

## References
- [ARQC validation for issuers](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html)
