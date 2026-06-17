---
id: balance-and-funds-verification
title: Balance & Funds Verification
type: business-capability
domain: Cards
level: L4
aliases: ["Available Balance Check", "Open-to-Buy Check"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.iso.org/standard/31628.html"]
---

# Balance & Funds Verification

**Definition.** Balance & Funds Verification confirms available credit or funds and places holds during authorization, supporting the BIAN Card Authorization service domain.
**Also known as:** Available Balance Check, Open-to-Buy Check.

## Relationships
- Balance & Funds Verification is defined in the Cards domain.
- Balance & Funds Verification is derived from Authorization Decisioning.
- Balance & Funds Verification depends on the Card Processing capability.

## Details
Within the BIAN Card Authorization flow this capability computes open-to-buy for credit cards (credit limit minus posted balance, pending authorizations and accrued fees) or available balance for debit/prepaid, then earmarks the authorized amount as a hold. ISO 8583 partial-approval (field 39 / DE 90) and pre-auth completion handling let it release or adjust holds; failing this check yields a 51 "insufficient funds" decline.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [ISO 8583 Financial transaction card messaging](https://www.iso.org/standard/31628.html)
