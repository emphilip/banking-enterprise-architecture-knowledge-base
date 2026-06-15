---
id: card-personalisation
title: Card Personalisation
type: business-capability
domain: Cards
level: L4
aliases: ["Card Encoding", "EMV Personalisation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.emvco.com/specifications/"]
---

# Card Personalisation

**Definition.** Card Personalisation encodes cardholder data, chip applets and design onto the card device, supporting the BIAN Issued Device Administration service domain.
**Also known as:** Card Encoding, EMV Personalisation.

## Relationships
- Card Personalisation is defined in the Cards domain.
- Card Personalisation is derived from Card Production & Fulfilment.
- Card Personalisation depends on the Card Processing capability.

## Details
This capability writes the EMV application data and personalisation keys (per EMVCo Book 2/3 and the issuer's profile) into the chip, alongside magnetic-stripe track data and printed/embossed PAN and CVV2. Personalisation derives card-unique keys (e.g. for the Application Cryptogram) from issuer master keys, and the process is governed by PCI Card Production logical security requirements covering key management within an HSM.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [EMVCo Specifications](https://www.emvco.com/specifications/)
