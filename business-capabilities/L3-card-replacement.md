---
id: card-replacement
title: Card Replacement
type: business-capability
domain: Cards
level: L3
aliases: ["Lost/Stolen Replacement", "Emergency Card Replacement"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.ecfr.gov/current/title-12/chapter-X/part-1026"]
---

# Card Replacement

**Definition.** Card Replacement issues a substitute device following loss, theft or damage, retiring the prior device in the BIAN Issued Device Administration service domain.
**Also known as:** Lost/Stolen Replacement, Emergency Card Replacement.

## Relationships
- Card Replacement is defined in the Cards domain.
- Card Replacement is derived from Card Lifecycle Management.
- Card Replacement depends on the Card Processing capability.

## Details
On a lost/stolen report the BIAN Issued Device Administration service domain blocks the old PAN and issues a replacement with a new PAN (fraud cases) or same PAN (damage), within the cardholder liability limits of Reg Z 1026.12 ($50 cap for credit cards) and Reg E for debit. Scheme Emergency Card Replacement services support travelers abroad, and network tokens are re-provisioned so digital wallets keep working after the physical card changes.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [eCFR Regulation Z, 12 CFR Part 1026](https://www.ecfr.gov/current/title-12/chapter-X/part-1026)
