---
id: 3-d-secure-service
title: 3-D Secure Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["3DS Service", "EMV 3DS ACS", "Cardholder Authentication Service"]
status: draft
sources: ["https://www.emvco.com/emv-technologies/3-d-secure/", "https://www.mastercard.com/content/dam/public/mastercardcom/globalrisk/pdf/Top-10-Things-to-Know-About-3DS.pdf"]
---

# 3-D Secure Service

**Definition.** 3-D Secure Service is the technology capability that performs EMV 3-D Secure cardholder authentication for e-commerce, operating or integrating the issuer Access Control Server, risk-based authentication and challenge flows to confirm the legitimate cardholder.
**Also known as:** 3DS Service, EMV 3DS ACS, Cardholder Authentication Service.

## Relationships
- 3-D Secure Service is defined in the Core Processing domain.
- 3-D Secure Service is derived from Card Tokenization Service.
- 3-D Secure Service depends on Customer Authentication.
- 3-D Secure Service is related to Card Authorization.

## Details
3-D Secure Service runs the issuer Access Control Server in the EMVCo 3-D Secure protocol, scoring each e-commerce authentication request and applying frictionless risk-based approval or a step-up challenge. It supports the liability shift for card-not-present transactions and aligns with regulatory strong customer authentication. EMVCo defines the 3DS message flow and Mastercard's guidance describes risk-based and challenge authentication for issuers.

## References
- [EMVCo 3-D Secure](https://www.emvco.com/emv-technologies/3-d-secure/)
- [Mastercard: Top 10 Things to Know About 3DS](https://www.mastercard.com/content/dam/public/mastercardcom/globalrisk/pdf/Top-10-Things-to-Know-About-3DS.pdf)
