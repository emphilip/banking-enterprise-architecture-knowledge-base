---
id: card-blocking
title: Card Blocking
type: business-capability
domain: Cards
level: L3
aliases: ["Card Hotlisting", "Card Suspension", "Block/Unblock"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.iso.org/standard/31628.html"]
---

# Card Blocking

**Definition.** Card Blocking places temporary or permanent blocks and hotlists a device against use, recording fraud warnings and cancellations in the BIAN Issued Device Administration service domain.
**Also known as:** Card Hotlisting, Card Suspension, Block/Unblock.

## Relationships
- Card Blocking is defined in the Cards domain.
- Card Blocking is derived from Card Lifecycle Management.
- Card Blocking depends on the Card Processing capability.

## Details
The BIAN Issued Device Administration service domain sets the card status (temporary block, permanent hotlist, or cardholder freeze) that the authorization host applies on each ISO 8583 request, declining with action codes such as 04 (pickup), 41 (lost), or 43 (stolen). For permanent blocks the PAN is added to the scheme exception/warning files (Visa Card Recovery Bulletin, Mastercard ICR) distributed to acquirers for stand-in declines.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [ISO 8583 Financial transaction card messaging](https://www.iso.org/standard/31628.html)
