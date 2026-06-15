---
id: card-dispatch-and-delivery
title: Card Dispatch & Delivery
type: business-capability
domain: Cards
level: L4
aliases: ["Card Distribution", "Card Mailing"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.pcisecuritystandards.org/document_library/"]
---

# Card Dispatch & Delivery

**Definition.** Card Dispatch & Delivery tracks distribution of the produced card and PIN mailer to the cardholder, supporting BIAN Issued Device Administration status reporting.
**Also known as:** Card Distribution, Card Mailing.

## Relationships
- Card Dispatch & Delivery is defined in the Cards domain.
- Card Dispatch & Delivery is derived from Card Production & Fulfilment.
- Card Dispatch & Delivery depends on the Notification Services capability.

## Details
The BIAN Issued Device Administration service domain records dispatch and in-transit status of the card and the separately mailed PIN. PCI Card Production fulfilment requirements mandate secure mailing, separation of card and PIN, and chain-of-custody tracking to prevent interception. Delivery confirmation typically triggers a cardholder notification prompting activation before the device can transact.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [PCI SSC Document Library (Card Production)](https://www.pcisecuritystandards.org/document_library/)
