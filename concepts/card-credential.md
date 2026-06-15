---
id: card-credential
title: Card Credential
type: artifact
domain: Cards
aliases: ["Card Number Credential", "PAN Credential"]
status: draft
sources: ["https://www.zeta.tech/us/resources/blog/demystifying-tokenized-card-payments/", "https://dwaynegefferie.substack.com/p/modern-issuer-processing"]
---

# Card Credential

**Definition.** Card Credential is the PAN, expiry, CVV and EMV chip data provisioned to a payment card and its tokens. Card Credential is the artifact that lets a card authenticate itself and generate authorization requests.

**Also known as:** Card Number Credential, PAN Credential.

## Relationships
- Card Credential is related to the Cards domain.
- Card Credential mentions Card Issuance.
- Card Credential mentions Card Production & Fulfillment.

## Details
Card Credential comprises the Primary Account Number (PAN), expiry date, service code, CVV/CVC values and the EMV chip keys used to compute the ARQC cryptogram during authorization. It is generated under PCI DSS PAN-protection and HSM key controls after application approval, then personalised onto the physical/virtual card and, via network tokenisation, provisioned to digital wallets as device tokens that shield the real PAN. Card Credential underpins every Authorization Request the card emits, and is reissued or re-credentialed when a card is renewed, replaced or blocked for fraud.

## References
- https://www.zeta.tech/us/resources/blog/demystifying-tokenized-card-payments/
- https://dwaynegefferie.substack.com/p/modern-issuer-processing
