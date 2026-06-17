---
id: card-issuance
title: Card Issuance
type: business-process
domain: Cards
aliases: ["Card Issuance Process"]
status: draft
---

# Card Issuance

**Definition.** Card Issuance is the process of provisioning, producing, and delivering payment cards to customers, including physical and virtual cards, activation, and credential setup.
**Also known as:** Card Issuance Process.

## Relationships
- Card Issuance is defined in the Cards domain.
- Card Issuance depends on the Card Issuing capability.
- Card Issuance depends on the Card Processing capability.

## Details
Card Issuance creates the card account, generates the card profile and PAN, instructs personalization and fulfillment, and manages activation and digital wallet provisioning. Actors include customers, card operations staff, and fulfillment vendors. Systems involved include a card processing platform, tokenization services, and notification services.

## Flow
- Capture Card Application causes Decision Card Application.
- Decision Card Application causes Generate Card Credential.
- Generate Card Credential causes Personalize Card.
- Personalize Card causes Fulfill Card.
- Fulfill Card causes Activate Card.
- Activate Card causes Provision Wallet Token.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
