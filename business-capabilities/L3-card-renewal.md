---
id: card-renewal
title: Card Renewal
type: business-capability
domain: Cards
level: L3
aliases: ["Card Reissuance", "Expiry Renewal"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.emvco.com/specifications/"]
---

# Card Renewal

**Definition.** Card Renewal reissues a card on or before expiry with refreshed credentials and validity dates, updating the BIAN Issued Device Administration service domain.
**Also known as:** Card Reissuance, Expiry Renewal.

## Relationships
- Card Renewal is defined in the Cards domain.
- Card Renewal is derived from Card Lifecycle Management.
- Card Renewal depends on the Card Processing capability.

## Details
The BIAN Issued Device Administration service domain drives automatic reissue as the printed expiry date approaches, generating a new card with a fresh expiration date and CVV2 while typically retaining the PAN. Network token credentials and card-on-file mandates are refreshed via Visa/Mastercard Account Updater (VAU / Automatic Billing Updater) so merchant recurring charges continue uninterrupted, and the EMV chip is re-personalised with new card-unique keys.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [EMVCo Specifications](https://www.emvco.com/specifications/)
