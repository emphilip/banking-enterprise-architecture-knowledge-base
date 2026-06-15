---
id: card-tokenisation
title: Card Tokenisation
type: business-capability
domain: Cards
level: L3
aliases: ["Network Tokenisation", "Wallet Provisioning", "Token Provisioning"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.emvco.com/specifications/"]
---

# Card Tokenisation

**Definition.** Card Tokenisation provisions network and device tokens for digital wallet and card-on-file use, replacing the PAN per the BIAN Issued Device Administration service domain.
**Also known as:** Network Tokenisation, Wallet Provisioning, Token Provisioning.

## Relationships
- Card Tokenisation is defined in the Cards domain.
- Card Tokenisation is derived from Card Issuing.
- Card Tokenisation depends on the Card Processing capability.

## Details
This capability implements the EMVCo Payment Tokenisation Specification, mapping the PAN to a domain-restricted token (DPAN) issued through a Token Service Provider such as Visa Token Service or Mastercard MDES. During wallet provisioning (Apple Pay, Google Pay) the issuer performs identification and verification (the ID&V / "yellow path" step) before approving the token, and a cryptogram is generated per transaction so the real PAN is never exposed at the merchant, reducing PCI DSS scope.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [EMVCo Payment Tokenisation Specifications](https://www.emvco.com/specifications/)
