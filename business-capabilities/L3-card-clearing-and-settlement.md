---
id: card-clearing-and-settlement
title: Card Clearing & Settlement
type: business-capability
domain: Cards
level: L3
aliases: ["Card Clearing", "Card Settlement", "Interchange Settlement"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://usa.visa.com/support/consumer/visa-rules.html"]
---

# Card Clearing & Settlement

**Definition.** Card Clearing & Settlement captures cleared transactions, reconciles interchange and settles network positions, realising the BIAN Card Clearing and Card Financial Settlement service domains.
**Also known as:** Card Clearing, Card Settlement, Interchange Settlement.

## Relationships
- Card Clearing & Settlement is defined in the Cards domain.
- Card Clearing & Settlement is derived from Card Authorization.
- Card Clearing & Settlement depends on the Core Banking Processing capability.

## Details
The BIAN Card Clearing and Card Financial Settlement service domains match each cleared presentment to its prior authorization, apply scheme interchange fees set by Visa/Mastercard interchange rate tables, and compute the issuer's net settlement position. Clearing files arrive via Visa BASE II / Mastercard GCMS, and the resulting net position is settled through the scheme settlement bank; posted amounts are written to the cardholder ledger in core banking. This Cards capability is distinct from the Payments domain's Payment Clearing & Settlement.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Visa Core Rules and Visa Product and Service Rules](https://usa.visa.com/support/consumer/visa-rules.html)
