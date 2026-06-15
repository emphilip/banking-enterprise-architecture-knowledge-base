---
id: card-issuing-and-personalisation
title: Card Issuing & Personalisation
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Card Issuance Engine", "Personalisation Service", "Card Provisioning"]
status: draft
sources: ["https://www.payhuddle.com/post/emv-card-personalization-validation-process", "https://enfuce.com/blog/card-issuing-api/"]
---

# Card Issuing & Personalisation

**Definition.** Card Issuing & Personalisation is the technology capability that manufactures and provisions physical and virtual cards, performing PAN and BIN allocation, EMV chip personalisation and key injection, instant and bureau issuance, and digital card-credential creation under PCI Card Production controls.
**Also known as:** Card Issuance Engine, Personalisation Service, Card Provisioning.

## Relationships
- Card Issuing & Personalisation is defined in the Core Processing domain.
- Card Issuing & Personalisation is derived from Card Processing.
- Card Issuing & Personalisation depends on Card Tokenization Service.
- Card Issuing & Personalisation is related to Card Issuing.

## Details
Card Issuing & Personalisation allocates PANs from issuer BIN ranges and personalises EMV chips with cardholder data and cryptographic keys, deriving card master keys under PCI Card Production security requirements. It supports instant in-branch issuance, bureau-based mass production and virtual card credential creation, then triggers wallet provisioning through the tokenization service. EMV personalisation prepares the chip to generate valid ARQC cryptograms during later authorization.

## References
- [EMV Card Personalization & Validation Process](https://www.payhuddle.com/post/emv-card-personalization-validation-process)
- [Enfuce Card Issuing API](https://enfuce.com/blog/card-issuing-api/)
