---
id: emv-cryptogram-validation
title: EMV Cryptogram Validation
type: technology-capability
domain: Core Processing
level: L3
aliases: ["ARQC Validation", "Chip Cryptogram Service", "EMV Validation Service"]
status: draft
sources: ["https://network.americanexpress.com/globalnetwork/dam/jcr:7d61622d-72b8-4cd2-9a28-625ef4e2c221/EMV%20Validation%20Service%20Product%20Capability%20Guide.pdf", "https://www.cryptomathic.com/blog/a-brief-overview-of-the-challenges-involved-in-key-management-for-emv-personalization-the-main-actors-of-emv-personalization"]
---

# EMV Cryptogram Validation

**Definition.** EMV Cryptogram Validation is the technology capability that validates EMV chip cryptograms (ARQC) during authorization and generates the response cryptogram (ARPC), deriving session keys from issuer master keys to confirm card authenticity and counter cloned or skimmed cards.
**Also known as:** ARQC Validation, Chip Cryptogram Service, EMV Validation Service.

## Relationships
- EMV Cryptogram Validation is defined in the Core Processing domain.
- EMV Cryptogram Validation is derived from Card Authorization Engine.
- EMV Cryptogram Validation is related to Card Authorization.

## Details
EMV Cryptogram Validation derives the card session key from the issuer master key and the card's ATC, then verifies the Authorization Request Cryptogram (ARQC) presented in the chip data to prove the card is genuine. It returns an Authorization Response Cryptogram (ARPC) so the chip can confirm a legitimate issuer response, defeating cloned and skimmed cards. Key derivation and validation execute inside hardware security modules to protect EMV keys.

## References
- [American Express EMV Validation Service Capability Guide](https://network.americanexpress.com/globalnetwork/dam/jcr:7d61622d-72b8-4cd2-9a28-625ef4e2c221/EMV%20Validation%20Service%20Product%20Capability%20Guide.pdf)
- [Cryptomathic: Key Management for EMV Personalization](https://www.cryptomathic.com/blog/a-brief-overview-of-the-challenges-involved-in-key-management-for-emv-personalization-the-main-actors-of-emv-personalization)
